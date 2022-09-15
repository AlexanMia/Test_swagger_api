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
    def validate_schema_json(response, schema):
        return validate(response.json(), schema)

    @staticmethod
    def post_with_body(endpoint, json):
        return requests.post(endpoint, json=json)

    @staticmethod
    def post_with_param(endpoint, param):
        return requests.post(endpoint, data=param)

    @staticmethod
    def get(endpoint):
        return requests.get(endpoint)

    @staticmethod
    def delete(endpoint):
        return requests.delete(endpoint)

    def create_pet(self, body):
        # make request POST with json file
        response = self.post_with_body(self.END_POINT_PET_URL, body)
        self.validate_schema_json(response, Schemas.CREATED_PET_SCHEMA)
        return response

    def find_pet_by_id(self, id_pet):
        # make request GET with end point id_pet
        response = self.get(f'{self.END_POINT_PET_URL}{id_pet}')
        if response.status_code == Constants.CODE_SUCCESS:
            self.validate_schema_json(response, Schemas.CREATED_PET_SCHEMA)
        elif response.status_code == Constants.CODE_IS_NOT_FOUND:
            self.validate_schema_json(response, Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
        return response

    def change_pet_name(self, id_pet, param):
        # make request POST with data
        response = self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param)
        self.validate_schema_json(response, Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
        return response

    def place_an_order(self, body):
        # make request POST with json file
        response = self.post_with_body(f'{self.END_POINT_STORE_ORDER_URL}', body)
        self.validate_schema_json(response, Schemas.PLACE_AN_ORDER_SCHEMA)
        return response

    def find_order(self, id_order):
        # make request GET with end point id_order
        response = self.get(f'{self.END_POINT_STORE_ORDER_URL}{id_order}')
        if response.status_code == Constants.CODE_SUCCESS:
            self.validate_schema_json(response, Schemas.PLACE_AN_ORDER_SCHEMA)
        elif response.status_code == Constants.CODE_IS_NOT_FOUND:
            self.validate_schema_json(response, Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
        return response

    def update_pet_status(self, id_pet, param):
        # make request POST with data, id_pet
        return self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param)

    def get_inventory_statuses(self):
        # GET
        response = self.get(f'{self.END_POINT_STORE_INVENTORY_URL}')
        self.validate_schema_json(response, Schemas.AVAILABLE_STATUS_SCHEMA)
        return response

    def delete_order(self, id_order):
        # DELETE with id_order
        response = self.delete(f'{self.END_POINT_STORE_ORDER_URL}{id_order}')
        self.validate_schema_json(response, Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
        return response

    def delete_pet(self, id_pet):
        # DELETE with id_pet
        response = self.delete(f'{self.END_POINT_PET_URL}{id_pet}')
        self.validate_schema_json(response, Schemas.COMMON_INFO_ABOUT_ACTIONS_SCHEMA)
        return response
