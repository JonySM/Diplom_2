import allure
import requests
import urls
from data import Data
from stellar_burgers_api import StellarBurgersApi


class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией и с ингредиентами')
    def test_create_order_with_auth_and_ingredients(self, get_ingredients, create_random_user):
        first_ingredient = get_ingredients.json()['data'][0]['_id']
        second_ingredient = get_ingredients.json()['data'][1]['_id']
        access_token = create_random_user.json()['accessToken']
        headers = {'Authorization': access_token}
        body = {"ingredients": [first_ingredient, second_ingredient]}
        order_burger = requests.post(f'{urls.BASE_URL + urls.CREATE_INGREDIENT}', headers=headers, json=body)
        success = True
        assert order_burger.status_code == 200 and order_burger.json()['success'] == success

    @allure.title('Проверка создания заказа без авторизации и с ингредиентами')
    def test_create_order_without_auth_and_ingredients(self, get_ingredients):
        first_ingredient = get_ingredients.json()['data'][0]['_id']
        second_ingredient = get_ingredients.json()['data'][1]['_id']
        body = {"ingredients": [first_ingredient, second_ingredient]}
        order_burger = requests.post(f'{urls.BASE_URL + urls.CREATE_INGREDIENT}',  json=body)
        success = True
        assert order_burger.status_code == 200 and order_burger.json()['success'] == success

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredient(self):
        order_burger = StellarBurgersApi.create_order_without_ingredient()
        assert order_burger.status_code == 400 and order_burger.text == Data.RESPONSE_EMPTY_INGREDIENT

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_invalid_hash(self):
        order_burger = StellarBurgersApi.create_order_with_invalid_hash_ingredient()
        assert order_burger.status_code == 500









