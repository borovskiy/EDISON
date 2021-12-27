import json
from random import randint
from faker import Faker

import serializer


class Psychic:

    def __init__(self, name=None, answer=None, history_answer=None, trust_psychic=None):
        self.name = name
        self.answer = answer
        self.history_answer = history_answer
        self.trust_psychic = trust_psychic

    def create_psychic(self):
        self.name = Faker().name()
        self.answer = randint(10, 99)
        self.history_answer = []
        self.trust_psychic = 0
        return self

    def get_answer(self) -> int:
        return self.answer

    def calculating_coefficient_reliability_psychics(self, number) -> None:
        if int(number) == self.get_answer():
            self.adding_trust_psychic()
        else:
            self.decrease_trust()
        self.add_answer_in_history()
        self.creating_variant_number()

    def adding_trust_psychic(self) -> None:
        self.trust_psychic += 1

    def decrease_trust(self) -> None:
        self.trust_psychic -= 1

    def add_answer_in_history(self) -> None:
        self.history_answer.append(self.get_answer())

    def creating_variant_number(self) -> None:
        self.answer = randint(10, 100)


class PsychicAndUserLists(object):

    def __init__(self, psychic_list=None, numbers_user=None):
        self.psychic_list = psychic_list
        self.numbers_user = numbers_user

    def object_filling(self):
        self.psychic_list = [Psychic().create_psychic() for _ in range(1, randint(3, 10))]
        self.numbers_user = []

    def adding_number_to_list_numbers(self, number):
        self.numbers_user.append(int(number))

    def processing_entered_number(self, number):
        for psychic in self.psychic_list:
            psychic.calculating_coefficient_reliability_psychics(number)
        self.adding_number_to_list_numbers(number)

    def to_json(self):
        return json.dumps(self, cls=serializer.CustomEncoder)
