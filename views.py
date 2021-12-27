import json
from flask import request, session, url_for, redirect, render_template, Flask
from flask.views import View

import serializer
import models

app = Flask(__name__)
app.secret_key = 'asuhaobsfavfb58568k'


class StartGame(View):
    """Стартовая страница для начала загадывания числа"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            if (session.get('psychic_list') and session.get('numbers_user')) is None:
                work_object = models.PsychicAndUserLists()
                work_object.object_filling()
                session.update(json.loads(work_object.to_json()))
            return redirect(url_for('answer'))
        return render_template('index.html')


class AnswerOptions(View):
    """Страница с вводом загаданного пользователем числа и вариантами ответов экстрасетсов"""
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            work_object = json.loads(json.dumps(dict(session)), object_hook=serializer.custom_decoder)
            work_object.processing_entered_number(request.form['number'])
            session.update(json.loads(work_object.to_json()))
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
