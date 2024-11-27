import allure
import requests
import urls
from data import Data
from stellar_burgers_api import StellarBurgersApi


class TestGetUsersOrders:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_with_auth(self, create_random_user):
        access_token = create_random_user.json()['accessToken']
        headers = {'Authorization': access_token}
        get_orders = requests.get(f'{urls.BASE_URL + urls.GET_USERS_ORDERS}', headers=headers)
        success = True
        assert get_orders.status_code == 200 and get_orders.json()['success'] == success

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_without_auth(self):
        get_orders = StellarBurgersApi.create_order_without_auth()
        assert get_orders.status_code == 401 and get_orders.text == Data.RESPONSE_GET_ORDERS_WITHOUT_AUTH



