from random import randint
from faker import Faker


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


class Psychic:

    def __init__(self):
        self.name = Faker().name()
        self.answer = randint(10, 99)
        self.history_answer = []
        self.trust_psychic = 0

    def get_data(self):
        return self.__dict__


class PsychicAnaUserLists:

    def __init__(self, psychic_list=None, numbers_user=None):
        if psychic_list is None:
            self.psychic_list = [Psychic().get_data() for _ in range(1, randint(2, 10))]
        elif psychic_list is not None:
            self.psychic_list = psychic_list
        if numbers_user is None:
            self.numbers_user = []
        elif numbers_user is not None:
            self.numbers_user = numbers_user

    def create_list_psychics(self):
        return self.__dict__

    def update_data(self, number):
        for psychic in self.psychic_list:
            if int(number) == psychic['answer']:
                psychic['trust_psychic'] += 1
            else:
                psychic['trust_psychic'] -= 1
            psychic['history_answer'].append(psychic['answer'])
            psychic['answer'] = randint(10, 100)
        self.numbers_user.append(int(number))
        return self.__dict__
