import requests
from jsonschema import validate

from schemas.schemas import Schemas
from util.constants import Constants


class PetStoreApi:
    BASE_URL = 'https://petstore.swagger.io/v2'
    END_POINT_PET_URL = BASE_URL + '/pet/'
    END_POINT_STORE_ORDER_URL = BASE_URL + '/store/order/'
    END_POINT_STORE_INVENTORY_URL = BASE_URL + '/store/inventory'

    @staticmethod
    def validate_schema_json(response, success_schema, failure_schema=None):
        if success_schema is not None and response.status_code == Constants.CODE_SUCCESS:
            validate(response.json(), success_schema)
        elif failure_schema is not None and response.status_code == Constants.CODE_IS_NOT_FOUND:
            validate(response.json(), failure_schema)

    @staticmethod
    def post_with_body(endpoint, json, schema):
        response = requests.post(endpoint, json=json)
        PetStoreApi.validate_schema_json(response, schema)
        return response

    @staticmethod
    def post_with_param(endpoint, param, schema=None):
        response = requests.post(endpoint, data=param)
        PetStoreApi.validate_schema_json(response, schema)
        return response

    @staticmethod
    def get(endpoint, success_schema, failure_schema=None):
        response = requests.get(endpoint)
        PetStoreApi.validate_schema_json(response, success_schema, failure_schema)
        return requests.get(endpoint)

    @staticmethod
    def delete(endpoint, schema):
        response = requests.delete(endpoint)
        PetStoreApi.validate_schema_json(response, schema)
        return response

    def create_pet(self, body):
        # make request POST with json file

        return self.post_with_body(self.END_POINT_PET_URL, body, Schemas.CREATED_PET_SCHEMA)

    def find_pet_by_id(self, id_pet):
        # make request GET with end point id_pet
        return self.get(f'{self.END_POINT_PET_URL}{id_pet}', Schemas.CREATED_PET_SCHEMA,
                        Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)

    def change_pet_name(self, id_pet, param):
        # make request POST with data
        return self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param,
                                    Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)

    def place_an_order(self, body):
        # make request POST with json file
        return self.post_with_body(f'{self.END_POINT_STORE_ORDER_URL}', body, Schemas.PLACE_AN_ORDER_SCHEMA)

    def find_order(self, id_order):
        # make request GET with end point id_order
        return self.get(f'{self.END_POINT_STORE_ORDER_URL}{id_order}', Schemas.PLACE_AN_ORDER_SCHEMA,
                        Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)

    def update_pet_status(self, id_pet, param):
        # make request POST with data, id_pet
        return self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param)

    def get_inventory_statuses(self):
        # GET
        return self.get(f'{self.END_POINT_STORE_INVENTORY_URL}', Schemas.AVAILABLE_STATUS_SCHEMA)

    def delete_order(self, id_order):
        # DELETE with id_order
        return self.delete(f'{self.END_POINT_STORE_ORDER_URL}{id_order}', Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)

    def delete_pet(self, id_pet):
        # DELETE with id_pet
        return self.delete(f'{self.END_POINT_PET_URL}{id_pet}', Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
