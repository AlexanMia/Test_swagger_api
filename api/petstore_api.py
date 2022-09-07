import requests


class PetstoreApi:
    BASE_URL = 'https://petstore.swagger.io/v2'
    end_point_pet_url = BASE_URL + '/pet'
    end_point_store_order_url = BASE_URL + '/store/order'
    end_point_store_inventory_url = BASE_URL + '/store/inventory'

    def create_pet(self, json):
        # make request POST with json file
        return requests.post(f'{self.end_point_pet_url}', json=json)

    def find_pet_by_id(self, id_pet):
        # make request GET with end point id_pet
        return requests.get(f'{self.end_point_pet_url}/{id_pet}')

    def change_pets_name(self, id_pet, param):
        # make request POST with data
        return requests.post(f'{self.end_point_pet_url}/{id_pet}', data=param)

    def place_an_order(self, json):
        # make request POST with json file
        return requests.post(f'{self.end_point_store_order_url}', json=json)

    def find_making_order(self, id_order):
        # make request GET with end point id_order
        return requests.get(f'{self.end_point_store_order_url}/{id_order}')

    def update_status_of_pet(self, id_pet, param):
        # make request POST with data, id_pet
        return requests.post(f'{self.end_point_pet_url}/{id_pet}', data=param)

    def inventory_status(self):
        # GET
        return requests.get(f'{self.end_point_store_inventory_url}')

    def delete_order(self, id_order):
        # DELETE with id_order
        return requests.delete(f'{self.end_point_store_order_url}/{id_order}')

    def delete_pet(self, id_pet):
        # DELETE with id_pet
        return requests.delete(f'{self.end_point_pet_url}/{id_pet}')
