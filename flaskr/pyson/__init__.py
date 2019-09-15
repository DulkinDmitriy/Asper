from bson.json_util import dumps
from json import loads


def convert_to_json(value):
        return loads(dumps(value))

def validate_fields(json, fields):
    for field in fields:
        if field not in json:
            return ValidationFieldsResult(False, field)
    return ValidationFieldsResult(True)

def bad_request(error, **kwargs):
        b_request = {
            "error": error
        }

        for key, value in kwargs.items():
            b_request[key] = value

        return b_request


class ValidationFieldsResult:

    def __init__(self, result, field = ""):
        self.result = result
        self.field = field   
