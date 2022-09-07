from util.constants import Constants


class TestBase:
    @staticmethod
    def check_status_code(response, code):
        assert response.status_code == code, f'{response.status_code} != {code}'

    def check_status_code_is_ok(self, response):
        self.check_status_code(response, Constants.CODE_SUCCESS)

    def check_status_code_is_not_found(self, response):
        self.check_status_code(response, Constants.CODE_IS_NOT_FOUND)
