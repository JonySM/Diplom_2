import allure
from data import Data
from stellar_burgers_api import StellarBurgersApi


class TestCreateUser:
    @allure.title('Проверка создания пользователя')
    def test_successful_creation_user(self, create_random_user):
        success = True
        assert create_random_user.status_code == 200 and create_random_user.json()['success'] == success

    @allure.title('Проверка создания пользователя, если пользователь создан')
    def test_creating_a_registered_user(self, create_user):
        access_token = create_user.json()['accessToken']
        create_the_same_user = StellarBurgersApi.create_new_user()
        assert (create_the_same_user.status_code == 403 and create_the_same_user.text ==
                Data.CREATING_A_REGISTERED_USER_RESPONSE)
        deleting_user = StellarBurgersApi.delete_user(access_token)
        assert deleting_user.status_code == 202 and deleting_user.text == Data.DELETE_USER_RESPONSE

    @allure.title('Проверка создания пользователя, без пароля')
    def test_create_without_password_user_body(self):
        create_request = StellarBurgersApi.create_without_password_user_body()
        assert create_request.status_code == 403 and create_request.text == Data.RESPONSE_WITHOUT_USER_DATA

    @allure.title('Проверка создания пользователя, без email')
    def test_create_without_email_user_body(self):
        create_request = StellarBurgersApi.create_without_email_user_body()
        assert create_request.status_code == 403 and create_request.text == Data.RESPONSE_WITHOUT_USER_DATA

    @allure.title('Проверка создания пользователя, без имени')
    def test_create_without_name_user_body(self):
        create_request = StellarBurgersApi.create_without_name_user_body()
        assert (create_request.status_code == 403 and create_request.text == Data.RESPONSE_WITHOUT_USER_DATA)







