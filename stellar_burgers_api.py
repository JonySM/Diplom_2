import allure
import requests
import urls
from data import Data


class StellarBurgersApi:
    @staticmethod
    @allure.step('Метод создания случайного пользователя')
    def create_new_random_user():
        body = Data.CREATE_RANDOM_USER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Метод удаления пользователя')
    def delete_user(accesstoken):
        headers = {'Authorization': accesstoken}
        response_delete = requests.delete(f'{urls.BASE_URL + urls.DELETE_USER}', headers=headers)
        return response_delete

    @staticmethod
    @allure.step('Метод создания пользователя по заданным данным')
    def create_new_user():
        body = Data.CREATE_USER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Метод создания пользователя без пароля')
    def create_without_password_user_body():
        body = Data.CREATE_WITHOUT_PASSWORD_USER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Метод создание пользователя без email')
    def create_without_email_user_body():
        body = Data.CREATE_WITHOUT_PASSWORD_USER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Метод создание пользователя без имени')
    def create_without_name_user_body():
        body = Data.CREATE_WITHOUT_PASSWORD_USER_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Метод авторизации пользователя')
    def login_user():
        body = Data.LOGIN_USER_BODY
        return requests.post(urls.BASE_URL + urls.LOGIN_USER, json=body)

    @staticmethod
    @allure.step('Метод авторизации с неверной парой логин и пароль')
    def login_invalid_user_data():
        body = Data.INVALID_LOGIN_USER_DATA
        return requests.post(urls.BASE_URL + urls.LOGIN_USER, json=body)

    @staticmethod
    @allure.step('Метод обновления пользователя')
    def update_user(accesstoken):
        headers = {'Authorization': accesstoken}
        body = Data.UPDATE_NEW_USER_DATA
        return requests.patch(f'{urls.BASE_URL + urls.UPDATE_USER}', headers=headers, json=body)

    @staticmethod
    @allure.step('Метод обновления пользователя без авторизации')
    def update_user_without_auth():
        body = Data.UPDATE_NEW_USER_DATA
        return requests.patch(f'{urls.BASE_URL + urls.UPDATE_USER}', json=body)

    @staticmethod
    @allure.step('Метод обновления email пользователя которая уже используется')
    def update_user_with_the_same_data(accesstoken):
        headers = {'Authorization': accesstoken}
        body = Data.REGISTERED_USER
        return requests.patch(f'{urls.BASE_URL + urls.UPDATE_USER}', headers=headers, json=body)

    @staticmethod
    @allure.step('Метод получения заказов')
    def get_ingredients():
        return requests.get(urls.BASE_URL + urls.GET_INGREDIENTS)

    @staticmethod
    @allure.step('Метод создания заказа без ингредиентов')
    def create_order_without_ingredient():
        body = Data.EMPTY_INGREDIENT_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_INGREDIENT, json=body)

    @staticmethod
    @allure.step('Метод создания заказа с неверным хешем ингредиентов')
    def create_order_with_invalid_hash_ingredient():
        body = Data.INVALID_HASH_INGREDIENT_BODY
        return requests.post(urls.BASE_URL + urls.CREATE_INGREDIENT, json=body)

    @staticmethod
    @allure.step('Метод создания заказа с без авторизации')
    def create_order_without_auth():
        return requests.get(urls.BASE_URL + urls.GET_USERS_ORDERS)










