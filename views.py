from flask import request, session, url_for, redirect, render_template, Flask
from flask.views import View

from helper_classes import PsychicAnaUserLists

app = Flask(__name__)
app.secret_key = 'asuhaobsfavfb58568k'


class StartGame(View):
    """Стартовая страница для начала загадывания числа"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            if session.get('psychics') is None:
                session['psychics'] = PsychicAnaUserLists().create_list_psychics()
            return redirect(url_for('answer'))
        return render_template('index.html')


class AnswerOptions(View):
    """Страница с вводом загаданного пользователем числа и вариантами ответов экстрасетсов"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            session['psychics'] = PsychicAnaUserLists(psychic_list=session['psychics']['psychic_list'],
                                                      numbers_user=session['psychics']['numbers_user']). \
                update_data(number=request.form['number'])
            return redirect(url_for('history'))
        if session.get('psychics') is None:
            return redirect(url_for('index'))

        answers = session.get('psychics')
        return render_template('answer.html', answers=answers)


class AnswerHistory(View):
    """История всех ответов и предложение загадать новое число"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            return redirect(url_for('answer'))
        if session.get('psychics') is None:
            return redirect(url_for('index'))
        return render_template('history.html')


class ClearSession(View):
    """Просто функция для очисти чтоб не приходилось закрывать браузер для прерывания сессии"""
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            session.clear()
            return redirect(url_for('index'))
