import json
import models


def custom_decoder(obj):
    if obj.keys() == models.PsychicAndUserLists().__dict__.keys():
        return models.PsychicAndUserLists(**obj)
    if obj.keys() == models.Psychic().__dict__.keys():
        return models.Psychic(**obj)
    return obj


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Psychic):
            return obj.__dict__
        if isinstance(obj, models.PsychicAndUserLists):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
