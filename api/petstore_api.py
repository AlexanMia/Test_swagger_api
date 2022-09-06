import requests


# перенести все реквесты


class PetstoreApi:
    BASE_URL = 'https://petstore.swagger.io/v2'
    end_point_pet_url = BASE_URL + '/pet'

    def create_pet(self, json):
        end_point_url = '/pet'
        # make request POST with json file
        return requests.post(f'{self.BASE_URL}{end_point_url}', json=json)

    def find_pet_by_id(self, id_pet):
        end_point_url = '/pet'

        # make request get with end point id_pet
        return requests.get(f'{self.BASE_URL}{end_point_url}/{id_pet}')

    def change_pets_name(self, id_pet, param):
        end_point_url = '/pet'
        # make request POST with data
        return requests.post(f'{self.BASE_URL}{end_point_url}/{id_pet}', data=param)

    def place_an_order(self, json):
        # POST
        end_point_url = '/store/order'
        return requests.post(f'{self.BASE_URL}{end_point_url}', json=json)

    def find_making_order(self, id_order):
        # GET
        end_point_url = '/store/order'

        # make request get with end point id_pet
        return requests.get(f'{self.BASE_URL}{end_point_url}/{id_order}')

    def update_status_of_pet(self, id_pet, param):
        # POST
        end_point_url = '/pet'
        return requests.post(f'{self.BASE_URL}{end_point_url}/{id_pet}', data=param)

    def inventory_status(self):
        # GET
        end_point_url = '/store/inventory'
        return requests.get(f'{self.BASE_URL}{end_point_url}')

    def delete_order(self, id_order):
        # DELETE
        end_point_url = '/store/order'
        return requests.delete(f'{self.BASE_URL}{end_point_url}/{id_order}')

    def delete_pet(self, id_pet):
        # DELETE
        end_point_url = '/pet'
        return requests.delete(f'{self.BASE_URL}{end_point_url}/{id_pet}')







