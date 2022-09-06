import random


class TestBase:
    @staticmethod
    def random_id(start, finish):
        return random.randint(start, finish)

    @staticmethod
    def check_status_code(response, code):
        assert response.status_code == code, f'{response.status_code} != {code}'



