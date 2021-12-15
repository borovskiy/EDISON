from flask import request, session, url_for, redirect, render_template, Flask
from flask.views import View
from models import PsychicAndUserLists

app = Flask(__name__)
app.secret_key = 'asuhaobsfavfb58568k'


class StartGame(View):
    """Стартовая страница для начала загадывания числа"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            if (session.get('psychic_list') and session.get('numbers_user')) is None:
                object_psychic_any_user_lists = PsychicAndUserLists()
                object_psychic_any_user_lists.create_lists_psychics_and_numbers_user()
                session.update(object_psychic_any_user_lists.get_attrs_in_dict())
            return redirect(url_for('answer'))
        return render_template('index.html')


class AnswerOptions(View):
    """Страница с вводом загаданного пользователем числа и вариантами ответов экстрасетсов"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            psychic_any_user_lists = PsychicAndUserLists(session['psychic_list'], session['numbers_user'])
            psychic_any_user_lists.serializer_objects_psychic_list_in_class()
            psychic_any_user_lists.processing_entered_number(request.form['number'])
            psychic_any_user_lists.serializer_objects_psychic_list_in_dict()
            session.update(psychic_any_user_lists.get_attrs_in_dict())
            return redirect(url_for('history'))
        if session.get('psychic_list') is None:
            return redirect(url_for('index'))
        return render_template('answer.html')


class AnswerHistory(View):
    """История всех ответов и предложение загадать новое число"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            return redirect(url_for('answer'))
        if session.get('psychic_list') is None:
            return redirect(url_for('index'))
        return render_template('history.html')


class ClearSession(View):
    """Просто функция для очисти чтоб не приходилось закрывать браузер для прерывания сессии"""
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            session.clear()
            return redirect(url_for('index'))
