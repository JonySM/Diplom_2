import data
from stellar_burgers_api import StellarBurgersApi


class TestCreateUser:
    def test_successful_creation_user(self):
        create_request = StellarBurgersApi.create_new_random_user()
        access_token = create_request.json()['accessToken']
        success = create_request.json()['success']
        refresh_token = create_request.json()['refreshToken']
        user = create_request.json()['user']
        assert create_request.status_code == 200 and create_request.json()['success'] == success
        assert create_request.json()['accessToken'] == access_token
        assert create_request.json()['refreshToken'] == refresh_token
        assert create_request.json()['user'] == user
        deleting_user = StellarBurgersApi.delete_user(access_token)
        assert deleting_user.status_code == 202 and deleting_user.text == data.Data.DELETE_USER_RESPONSE

    def test_creating_a_registered_user(self, create_user):
        access_token = create_user.json()['accessToken']
        create_the_same_user = StellarBurgersApi.create_new_user()
        assert (create_the_same_user.status_code == 403 and create_the_same_user.text ==
                data.Data.CREATING_A_REGISTERED_USER_RESPONSE)
        deleting_user = StellarBurgersApi.delete_user(access_token)
        assert deleting_user.status_code == 202 and deleting_user.text == data.Data.DELETE_USER_RESPONSE

    def test_create_without_password_user_body(self):
        create_request = StellarBurgersApi.create_without_password_user_body()
        assert create_request.status_code == 403 and create_request.text == data.Data.RESPONSE_WITHOUT_USER_DATA

    def test_create_without_email_user_body(self):
        create_request = StellarBurgersApi.create_without_email_user_body()
        assert create_request.status_code == 403 and create_request.text == data.Data.RESPONSE_WITHOUT_USER_DATA

    def test_create_without_name_user_body(self):
        create_request = StellarBurgersApi.create_without_name_user_body()
        assert create_request.status_code == 403 and create_request.text == data.Data.RESPONSE_WITHOUT_USER_DATA






