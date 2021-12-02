from flask import Flask, render_template, request, redirect, url_for, session
from random import randint
from faker import Faker

app = Flask(__name__)
app.secret_key = 'asuhaobsfavfb58568k'


def psychics(dict_values_session=None, number_user=None) -> dict:
    """
    Может принимать словарь.
    Исли значения аргиментов будут None создает новый словарь
    Если нет. Обрабатывает полученый словарь и возвращает обработынный словарь
    :param dict_values_session:
    :param number_user:
    :return:
    """
    if dict_values_session is None and number_user is None:
        fake = Faker()
        dict_values_session = {}
        [dict_values_session.update(
            {f'{fake.name()}':
                {
                    'history_guesswork': list(),
                    'credibility_psychic': 0,
                    'current_answer': randint(10, 100)
                }}
        ) for _ in range(randint(2, 5))
        ]
        return dict_values_session

    for name, values in dict_values_session.items():
        if number_user == values['current_answer']:
            values['credibility_psychic'] += 1
        else:
            values['credibility_psychic'] -= 1
        values['history_guesswork'].append(values['current_answer'])
        values['current_answer'] = randint(10, 100)
    return dict_values_session


@app.route("/", methods=['post', 'get'])
def index():
    """Стартовая страница для начала загадывания числа"""
    if request.method == 'POST':
        if session.get('psychics') is None:
            session['psychics'] = psychics()
        return redirect(url_for('answer'))
    return render_template('index.html')


@app.route('/answer', methods=['post', 'get'])
def answer():
    """Страница с вводом загаданного пользователем числа и вариантами ответов экстрасетсов"""
    if request.method == 'POST':
        session['psychics'] = psychics(dict_values_session=session.get('psychics'),
                                       number_user=int(request.form['number']))
        return redirect(url_for('history'))
    if session.get('psychics') is None:
        return redirect(url_for('index'))
    answers = session.get('psychics')
    return render_template('answer.html', answers=answers)


@app.route('/history', methods=['post', 'get'])
def history():
    """История всех ответов и предложение загадать новое число"""
    if request.method == 'POST':
        return redirect(url_for('answer'))
    if session.get('psychics') is None:
        return redirect(url_for('index'))
    return render_template('history.html', answers=session.get('psychics'))


@app.route('/clear_session', methods=['get'])
def clear_session():
    """Просто функция для очисти чтоб не приходилось закрывать браузер для прерывания сессии"""
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
