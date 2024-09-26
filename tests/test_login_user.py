import allure

from data import Data
from stellar_burgers_api import StellarBurgersApi


class TestLogin:
    @allure.title('Успешная авторизация')
    def test_successful_login(self):
        login_request = StellarBurgersApi.login_user()
        success = True
        assert login_request.status_code == 200 and login_request.json()['success'] == success

    @allure.title('Авторизация с неверным логином и паролем')
    def test_invalid_user_data(self):
        login_request = StellarBurgersApi.login_invalid_user_data()
        assert login_request.status_code == 401 and login_request.text == Data.RESPONSE_INVALID_LOGIN_USER_DATA



