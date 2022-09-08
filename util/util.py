import json
import random

import jsonpath


class Util:
    @staticmethod
    def generate_random_int(start, end):
        return random.randint(start, end)

    @staticmethod
    def read_json_from_file(path):
        with open(path, 'r') as f:
            return json.loads(f.read())

    @staticmethod
    def extract_json_field_value(response, key):
        return jsonpath.jsonpath(json.loads(response.text), key)[0]
