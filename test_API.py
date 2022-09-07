import pytest
from api.petstore_api import PetstoreApi
from test_base import TestBase
from util.constants import Constants
from util.util import Util


class TestApi(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_prep(self):
        global petstore_api
        petstore_api = PetstoreApi()
        # random ID
        global id_pet
        id_pet = Util.generate_random_int(1000, 9999)
        global id_order
        id_order = Util.generate_random_int(1, 10)
        global quantity
        quantity = Util.generate_random_int(1, 7)
        # add name
        global name_pet
        name_pet = 'Richie'
        global random_status
        random_status = 'test_status_' + str(Util.generate_random_int(100, 200))

    def test_create_pet(self):
        # POST
        open_json = Util.read_json_from_file(Constants.PATH_TO_FILE_ADD_PET)
        open_json[Constants.KEY_ID] = id_pet
        open_json[Constants.KEY_NAME] = name_pet
        response = petstore_api.create_pet(open_json)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_values_id_and_name_is_equal_expected(response, Constants.KEY_ID, id_pet, Constants.KEY_NAME,
                                                           name_pet)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_STATUS, Constants.VALUE_KEY_AVAILABLE)

    def test_find_pet_by_id(self):
        response = petstore_api.find_pet_by_id(id_pet)
        print(response.content)
        print(response.status_code)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_values_id_and_name_is_equal_expected(response, Constants.KEY_ID, id_pet, Constants.KEY_NAME,
                                                           name_pet)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_STATUS, Constants.VALUE_KEY_AVAILABLE)

    def test_change_pets_name(self):
        change_name = {Constants.KEY_NAME: Constants.VALUE_NAME}
        # POST
        response = petstore_api.change_pets_name(id_pet, change_name)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_int_value_key_is_equal_expected(response, Constants.KEY_MESSAGE, id_pet)

        # GET check changing name
        response_get = petstore_api.find_pet_by_id(id_pet)

        super().check_status_code(response_get, Constants.CODE_SUCCESS)

        super().check_values_id_and_name_is_equal_expected(response_get, Constants.KEY_ID, id_pet, Constants.KEY_NAME,
                                                           change_name[Constants.KEY_NAME])

    def test_place_an_order(self):
        open_json = Util.read_json_from_file(Constants.PATH_TO_FILE_PLACE_ORDER)
        open_json[Constants.KEY_ID] = id_order
        open_json[Constants.KEY_PET_ID] = id_pet
        open_json[Constants.KEY_QUANTITY] = quantity
        # POST
        response = petstore_api.place_an_order(open_json)
        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_ID, id_order)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_PET_ID, id_pet)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_QUANTITY, quantity)

    def test_find_making_order(self):
        # GET
        response = petstore_api.find_making_order(id_order)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_ID, id_order)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_PET_ID, id_pet)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_QUANTITY, quantity)

        super().check_value_key_is_equal_expected_value(response, Constants.KEY_STATUS,
                                                        Constants.VALUE_KEY_STATUS_PLACED)

    def test_update_status_of_pet(self):
        status = {Constants.KEY_STATUS: random_status}
        # POST
        response = petstore_api.update_status_of_pet(id_pet, status)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_int_value_key_is_equal_expected(response, Constants.KEY_MESSAGE, id_pet)

        # GET check changing name
        response_get = petstore_api.find_pet_by_id(id_pet)

        super().check_status_code(response_get, Constants.CODE_SUCCESS)

        super().check_value_key_is_equal_expected_value(response_get, Constants.KEY_ID, id_pet)

        super().check_value_key_is_equal_expected_value(response_get, Constants.KEY_STATUS, random_status)

    def test_inventory_status(self):
        # GET
        response = petstore_api.inventory_status()

        super().check_status_code(response, Constants.CODE_SUCCESS)

        super().check_value_key_is_equal_expected_value(response, random_status, Constants.QUANTITY_RANDOM_STATUS)

    def test_delete_order(self):
        # DELETE
        response = petstore_api.delete_order(id_order)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        # GET find order with id_order
        response_get = petstore_api.find_making_order(id_order)

        super().check_status_code(response_get, Constants.CODE_ERROR)

    def test_delete_pet(self):
        # GET
        response = petstore_api.delete_pet(id_pet)

        super().check_status_code(response, Constants.CODE_SUCCESS)

        # GET find pet with id
        response_get = petstore_api.find_pet_by_id(id_pet)

        super().check_status_code(response_get, Constants.CODE_ERROR)

        super().check_value_key_is_equal_expected_value(response_get, Constants.KEY_MESSAGE,
                                                        Constants.VALUE_KEY_PET_NOT_FOUND)
