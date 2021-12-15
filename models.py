from random import randint
from faker import Faker


def psychic_any_user_lists(psychic_list, numbers_user):
    return PsychicAndUserLists(psychic_list=psychic_list, numbers_user=numbers_user)


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

    def serializer_in_dict(self):
        return self.__dict__

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


class PsychicAndUserLists:

    def __init__(self, psychic_list=None, numbers_user=None):
        self.psychic_list = psychic_list
        self.numbers_user = numbers_user

    def create_lists_psychics_and_numbers_user(self) -> object:
        self.psychic_list = [Psychic().create_psychic().serializer_in_dict() for _ in range(1, randint(3, 10))]
        self.numbers_user = []
        return self

    def serializer_objects_psychic_list_in_dict(self) -> None:
        for i in range(0, len(self.psychic_list)):
            self.psychic_list[i] = self.psychic_list[i].__dict__

    def serializer_objects_psychic_list_in_class(self) -> None:
        for i in range(0, len(self.psychic_list)):
            self.psychic_list[i] = self.psychic_decoder(self.psychic_list[i])

    @classmethod
    def psychic_decoder(cls, obj: dict) -> object:
        return Psychic(obj['name'], obj['answer'], obj['history_answer'], obj['trust_psychic'])

    def get_attrs_in_dict(self) -> dict:
        return self.__dict__

    def adding_number_to_list_numbers(self, number):
        self.numbers_user.append(int(number))

    def processing_entered_number(self, number):
        for psychic in self.psychic_list:
            psychic.calculating_coefficient_reliability_psychics(number)
        self.adding_number_to_list_numbers(number)
