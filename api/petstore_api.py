import requests


class PetStoreApi:
    BASE_URL = 'https://petstore.swagger.io/v2'
    END_POINT_PET_URL = BASE_URL + '/pet/'
    END_POINT_STORE_ORDER_URL = BASE_URL + '/store/order/'
    END_POINT_STORE_INVENTORY_URL = BASE_URL + '/store/inventory'

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
        return self.post_with_body(self.END_POINT_PET_URL, body)

    def find_pet_by_id(self, id_pet):
        # make request GET with end point id_pet
        return self.get(f'{self.END_POINT_PET_URL}{id_pet}')

    def change_pet_name(self, id_pet, param):
        # make request POST with data
        return self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param)

    def place_an_order(self, body):
        # make request POST with json file
        return self.post_with_body(f'{self.END_POINT_STORE_ORDER_URL}', body)

    def find_order(self, id_order):
        # make request GET with end point id_order
        return self.get(f'{self.END_POINT_STORE_ORDER_URL}{id_order}')

    def update_pet_status(self, id_pet, param):
        # make request POST with data, id_pet
        return self.post_with_param(f'{self.END_POINT_PET_URL}{id_pet}', param)

    def get_inventory_statuses(self):
        # GET
        return self.get(f'{self.END_POINT_STORE_INVENTORY_URL}')

    def delete_order(self, id_order):
        # DELETE with id_order
        return self.delete(f'{self.END_POINT_STORE_ORDER_URL}{id_order}')

    def delete_pet(self, id_pet):
        # DELETE with id_pet
        return self.delete(f'{self.END_POINT_PET_URL}{id_pet}')
