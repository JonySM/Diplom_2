import allure
from data import Data
from stellar_burgers_api import StellarBurgersApi


class TestUpdateUser:
    @allure.title('Обновление авторизованного пользователя')
    def test_user_update(self, create_random_user):
        access_token = create_random_user.json()['accessToken']
        update_user = StellarBurgersApi.update_user(access_token)
        success = True
        assert update_user.status_code == 200 and update_user.json()['success'] == success

    @allure.title('Обновление неавторизованного пользователя')
    def test_update_user_without_auth(self, create_random_user):
        update_user_without_token = StellarBurgersApi.update_user_without_auth()
        assert (update_user_without_token.status_code == 401 and update_user_without_token.text ==
                Data.RESPONSE_INVALID_UPDATE_USER_DATA)

    @allure.title('Обновление email пользователя, которая уже используется ')
    def test_user_with_an_existing_mail(self, create_random_user):
        access_token = create_random_user.json()['accessToken']
        update_user_with_an_existing_mail = StellarBurgersApi.update_user_with_the_same_data(access_token)
        assert (update_user_with_an_existing_mail.status_code == 403 and update_user_with_an_existing_mail.text ==
                Data.RESPONSE_REGISTERED_UPDATE_USER)







