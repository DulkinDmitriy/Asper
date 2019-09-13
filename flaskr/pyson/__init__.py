from bson.json_util import dumps
from json import loads


def convert_to_json(value):
        return loads(dumps(value))
