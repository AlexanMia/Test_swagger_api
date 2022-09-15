import pytest

from api.petstore_api import PetStoreApi
from test_base import TestBase
from util.constants import Constants
from util.util import Util


class TestApi(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_prep(self):
        global pet_store_api
        pet_store_api = PetStoreApi()
        global pet_id
        pet_id = Util.generate_random_int(1000, 9999)
        global order_id
        order_id = Util.generate_random_int(1, 10)
        global pet_quantity
        pet_quantity = Util.generate_random_int(1, 7)
        global random_status
        random_status = 'test_status_' + str(Util.generate_random_int(100, 200))

    def test_create_pet(self):
        # POST
        body_json = Util.read_json_from_file(Constants.PATH_TO_FILE_ADD_PET)
        body_json[Constants.KEY_ID] = pet_id
        body_json[Constants.KEY_NAME] = Constants.PET_NAME
        response = pet_store_api.create_pet(body_json)

        super().check_status_code_is_ok(response)

        assert Util.extract_json_field_value(response, Constants.KEY_ID) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_NAME) == Constants.PET_NAME, \
            f'{Util.extract_json_field_value(response, Constants.KEY_NAME)} != {Constants.PET_NAME}'

        assert Util.extract_json_field_value(response, Constants.KEY_STATUS) == Constants.VALUE_KEY_AVAILABLE, \
            f'{Util.extract_json_field_value(response, Constants.KEY_STATUS)} != {Constants.VALUE_KEY_AVAILABLE}'

    def test_find_pet_by_id(self):
        response = pet_store_api.find_pet_by_id(pet_id)

        super().check_status_code_is_ok(response)

        assert Util.extract_json_field_value(response, Constants.KEY_ID) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_NAME) == Constants.PET_NAME, \
            f'{Util.extract_json_field_value(response, Constants.KEY_NAME)} != {Constants.PET_NAME}'

        assert Util.extract_json_field_value(response, Constants.KEY_STATUS) == Constants.VALUE_KEY_AVAILABLE, \
            f'{Util.extract_json_field_value(response, Constants.KEY_STATUS)} != {Constants.VALUE_KEY_AVAILABLE}'

    def test_change_pets_name(self):
        change_name = {Constants.KEY_NAME: Constants.CHANGED_PET_NAME}
        # POST
        response = pet_store_api.change_pet_name(pet_id, change_name)

        super().check_status_code_is_ok(response)

        assert int(Util.extract_json_field_value(response, Constants.KEY_MESSAGE)) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_MESSAGE)} != {pet_id}'

        # GET check changing name
        response_get = pet_store_api.find_pet_by_id(pet_id)

        super().check_status_code_is_ok(response_get)

        assert Util.extract_json_field_value(response_get, Constants.KEY_ID) == pet_id, \
            f'{Util.extract_json_field_value(response_get, Constants.KEY_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response_get, Constants.KEY_NAME) == Constants.CHANGED_PET_NAME, \
            f'{Util.extract_json_field_value(response_get, Constants.KEY_NAME)} != {Constants.CHANGED_PET_NAME}'

    def test_place_an_order(self):
        body_json = Util.read_json_from_file(Constants.PATH_TO_FILE_PLACE_ORDER)
        body_json[Constants.KEY_ID] = order_id
        body_json[Constants.KEY_PET_ID] = pet_id
        body_json[Constants.KEY_QUANTITY] = pet_quantity

        # POST
        response = pet_store_api.place_an_order(body_json)
        super().check_status_code_is_ok(response)

        assert Util.extract_json_field_value(response, Constants.KEY_ID) == order_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_ID)} != {order_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_PET_ID) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_PET_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_QUANTITY) == pet_quantity, \
            f'{Util.extract_json_field_value(response, Constants.KEY_QUANTITY)} != {pet_quantity}'

    def test_find_making_order(self):
        # GET
        response = pet_store_api.find_order(order_id)

        super().check_status_code_is_ok(response)

        assert Util.extract_json_field_value(response, Constants.KEY_ID) == order_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_ID)} != {order_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_PET_ID) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_PET_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response, Constants.KEY_QUANTITY) == pet_quantity, \
            f'{Util.extract_json_field_value(response, Constants.KEY_QUANTITY)} != {pet_quantity}'

        assert Util.extract_json_field_value(response, Constants.KEY_STATUS) == Constants.VALUE_KEY_STATUS_PLACED, \
            f'{Util.extract_json_field_value(response, Constants.KEY_STATUS)} != {Constants.VALUE_KEY_STATUS_PLACED}'

    def test_update_status_of_pet(self):
        status = {Constants.KEY_STATUS: random_status}
        # POST
        response = pet_store_api.update_pet_status(pet_id, status)

        super().check_status_code_is_ok(response)

        assert int(Util.extract_json_field_value(response, Constants.KEY_MESSAGE)) == pet_id, \
            f'{Util.extract_json_field_value(response, Constants.KEY_MESSAGE)} != {pet_id}'

        # GET check changing name
        response_get = pet_store_api.find_pet_by_id(pet_id)

        super().check_status_code_is_ok(response_get)

        assert Util.extract_json_field_value(response_get, Constants.KEY_ID) == pet_id, \
            f'{Util.extract_json_field_value(response_get, Constants.KEY_ID)} != {pet_id}'

        assert Util.extract_json_field_value(response_get, Constants.KEY_STATUS) == random_status, \
            f'{Util.extract_json_field_value(response_get, Constants.KEY_STATUS)} != {random_status}'

    def test_inventory_status(self):
        # GET
        response = pet_store_api.get_inventory_statuses()

        super().check_status_code_is_ok(response)

        assert Util.extract_json_field_value(response, random_status) == Constants.QUANTITY_OF_RANDOM_STATUS, \
            f'{Util.extract_json_field_value(response, random_status)} != {Constants.QUANTITY_OF_RANDOM_STATUS}'

    def test_delete_order(self):
        # DELETE
        response = pet_store_api.delete_order(order_id)

        super().check_status_code_is_ok(response)

        # GET find order with id_order
        response_get = pet_store_api.find_order(order_id)

        super().check_status_code_is_not_found(response_get)

    def test_delete_pet(self):
        # DELETE
        response = pet_store_api.delete_pet(pet_id)

        super().check_status_code_is_ok(response)

        # GET find pet with id
        response_get = pet_store_api.find_pet_by_id(pet_id)

        super().check_status_code_is_not_found(response_get)

        assert Util.extract_json_field_value(response_get, Constants.KEY_MESSAGE) == Constants.VALUE_KEY_PET_NOT_FOUND, \
            f'{Util.extract_json_field_value(response_get, Constants.KEY_MESSAGE)} != {Constants.VALUE_KEY_PET_NOT_FOUND}'
