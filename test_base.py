from util.util import Util


class TestBase:
    @staticmethod
    def check_status_code(response, code):
        assert response.status_code == code, f'{response.status_code} != {code}'

    @staticmethod
    def check_value_key_is_equal_expected_value(response, key, expected_value_key):
        assert Util.extract_json_field_value(response, key)[0] == expected_value_key, \
            f'{Util.extract_json_field_value(response, key)[0]} != {expected_value_key}'

    @staticmethod
    def check_values_id_and_name_is_equal_expected(response, key_id, expected_id, key_name, expected_name):
        assert Util.extract_json_field_value(response, key_id)[0] == expected_id, \
            f'{Util.extract_json_field_value(response, key_id)[0]} != {expected_id}'
        assert Util.extract_json_field_value(response, key_name)[0] == expected_name, \
            f'{Util.extract_json_field_value(response, key_name)[0]} != {expected_name}'

    @staticmethod
    def check_int_value_key_is_equal_expected(response, key, expected_value):
        assert int(Util.extract_json_field_value(response, key)[0]) == expected_value, \
            f'{Util.extract_json_field_value(response, key)[0]} != {expected_value}'
