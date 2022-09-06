# # PLAN
# создать пета (айди 4 цифры) добавила дополнительно рандомные имена
# найти пета по айди
# изменить имя пета
# проверить что имя изменено по айди найти его

# разместить заказ (номер от 1 до 10 вкл, рандомное количество)
# найти заказ, проверить айди пета и количество

# обновить статус пета в сторе (рандомный test_status_рандомные цифры)
# получить inventory
# удалить заказ
# удалить пета
# TODO переместить парсинг джейсонов и рандомайзер в папку утиль в файл утиль

import json
import jsonpath

import pytest
from api.petstore_api import PetstoreApi
from test_base import TestBase


class TestApi(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_prep(self):
        global petstore_api
        petstore_api = PetstoreApi()
        # random ID
        global id_pet
        id_pet = super().random_id(1000, 9999)
        global id_order
        id_order = super().random_id(1, 10)
        global quantity
        quantity = super().random_id(1, 7)
        # add name
        global name_pet
        name_pet = 'Richie'
        global random_status
        random_status = 'test_status_' + str(super().random_id(100, 200))



    def test_create_pet(self):
        # POST

        # read and add data in json
        # TODO в отдельный класс утилитный
        with open('add_new_pet.json', 'r') as f:
            file_content = f.read()
            request_json = json.loads(file_content)
            request_json['id'] = id_pet
            request_json['name'] = name_pet

        print(request_json)

        # make request POST with json file
        response = petstore_api.create_pet(request_json)
        #TODO 200 в константы
        super().check_status_code(response, 200)
        #assert response.status_code == 200, f'{response.status_code} != 200'
        #TODO убрать в утилитный класс как return jsonpath.jsonpath(json.loads(response.text), key)
        response_json = json.loads(response.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_name = jsonpath.jsonpath(response_json, 'name')
        response_status = jsonpath.jsonpath(response_json, 'status')

        # checking id_pet, name, status
        assert response_id[0] == id_pet, f'{response_id[0]} != {id_pet}'
        assert response_name[0] == name_pet, f'{response_name[0]} != {name_pet}'
        assert response_status[0] == "available", f'{response_status[0]} != "available"'


    def test_find_pet_by_id(self):
        response = petstore_api.find_pet_by_id(id_pet)
        print(response.content)
        print(response.status_code)

        super().check_status_code(response, 200)
        #assert response.status_code == 200

        response_json = json.loads(response.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_name = jsonpath.jsonpath(response_json, 'name')
        response_status = jsonpath.jsonpath(response_json, 'status')

        # checking id_pet, name, status
        assert response_id[0] == id_pet, f'{response_id[0]} != {id_pet}'
        assert response_name[0] == name_pet, f'{response_name[0]} != {name_pet}'
        assert response_status[0] == "available", f'{response_status[0]} != "available"'

    def test_change_pets_name(self):
        change_name = {'name': 'Crispy'}
        response = petstore_api.change_pets_name(id_pet, change_name)
        # print(response.content)
        # print(response.status_code)
        super().check_status_code(response, 200)
        #assert response.status_code == 200

        response_json = json.loads(response.text)
        response_message = jsonpath.jsonpath(response_json, 'message')
        # checking id_pet
        assert int(response_message[0]) == id_pet, f'{response_message[0]} != {id_pet}'

        # check changing name
        response_get = petstore_api.find_pet_by_id(id_pet)
        # print(response_get.content)
        # print(response_get.status_code)
        super().check_status_code(response_get, 200)
        #assert response_get.status_code == 200
        response_json = json.loads(response_get.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_name = jsonpath.jsonpath(response_json, 'name')

        # checking id_pet and name
        assert response_id[0] == id_pet, f'{response_id[0]} != {id_pet}'
        assert response_name[0] == change_name["name"], f'{response_name[0]} != {change_name["name"]}'

    def test_place_an_order(self):
        # read and add data in json
        with open('place_an_order.json', 'r') as f:
            file_content = f.read()
            order_json = json.loads(file_content)
            order_json['id'] = id_order
            order_json['petId'] = id_pet
            order_json['quantity'] = quantity

        print(order_json)
        response = petstore_api.place_an_order(order_json)
        super().check_status_code(response, 200)

        response_json = json.loads(response.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_pet_id = jsonpath.jsonpath(response_json, 'petId')
        response_quantity = jsonpath.jsonpath(response_json, 'quantity')

        # checking id_pet, name, status
        assert response_id[0] == id_order, f'{response_id[0]} != {id_order}'
        assert response_pet_id[0] == id_pet, f'{response_pet_id[0]} != {id_pet}'
        assert response_quantity[0] == quantity, f'{response_quantity[0]} != {quantity}'


    def test_find_making_order(self):
        response = petstore_api.find_making_order(id_order)
        print(response.content)
        print(response.status_code)

        super().check_status_code(response, 200)
        # assert response.status_code == 200

        response_json = json.loads(response.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_pet_id = jsonpath.jsonpath(response_json, 'petId')
        response_quantity = jsonpath.jsonpath(response_json, 'quantity')
        response_status = jsonpath.jsonpath(response_json, 'status')

        # checking id_pet, name, status
        assert response_id[0] == id_order, f'{response_id[0]} != {id_order}'
        assert response_pet_id[0] == id_pet, f'{response_pet_id[0]} != {id_pet}'
        assert response_quantity[0] == quantity, f'{response_quantity[0]} != {quantity}'
        assert response_status[0] == "placed", f'{response_status[0]} != "placed"'


    def test_update_status_of_pet(self):
        status = {'status': random_status}
        print(status['status'])
        response = petstore_api.update_status_of_pet(id_pet, status)
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 200)

        response_json = json.loads(response.text)
        response_message = jsonpath.jsonpath(response_json, 'message')
        # checking id_pet
        assert int(response_message[0]) == id_pet, f'{response_message[0]} != {id_pet}'

        # check changing name
        response_get = petstore_api.find_pet_by_id(id_pet)
        # print(response_get.content)
        # print(response_get.status_code)
        super().check_status_code(response_get, 200)
        # assert response_get.status_code == 200
        response_json = json.loads(response_get.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        response_status = jsonpath.jsonpath(response_json, 'status')

        # checking id_pet and name
        assert response_id[0] == id_pet, f'{response_id[0]} != {id_pet}'
        assert response_status[0] == random_status, f'{response_status[0]} != {random_status}'

    def test_inventory_status(self):
        response = petstore_api.inventory_status()
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 200)

        response_json = json.loads(response.text)
        assert random_status in response_json
        response_quantity = jsonpath.jsonpath(response_json, random_status)
        assert response_quantity[0] == 1, f'{response_quantity} != 1'

    def test_delete_order(self):
        response = petstore_api.delete_order(id_order)
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 200)
        # find order with id_order
        response = petstore_api.find_making_order(id_order)
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 404)

    def test_delete_pet(self):
        response = petstore_api.delete_pet(id_pet)
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 200)
        # find order with id_order
        response = petstore_api.find_pet_by_id(id_pet)
        print(response.content)
        print(response.status_code)
        super().check_status_code(response, 404)

        response_json = json.loads(response.text)
        response_message = jsonpath.jsonpath(response_json, 'message')
        # checking message
        assert response_message[0] == 'Pet not found', f'{response_message[0]} != Pet not found'



