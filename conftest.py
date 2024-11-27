import allure
import pytest
from stellar_burgers_api import StellarBurgersApi


@allure.step('Фикстура создания пользователя по заданным данным')
@pytest.fixture(scope='function')
def create_user():
    create_user = StellarBurgersApi.create_new_user()
    return create_user


@allure.step('Фикстура создания случайного пользователя и последующее его удаление')
@pytest.fixture(scope='function')
def create_random_user():
    create_random_user = StellarBurgersApi.create_new_random_user()

    yield create_random_user
    accesstoken = create_random_user.json()['accessToken']
    StellarBurgersApi.delete_user(accesstoken)


@allure.step('Фикстура получения всех ингредиентов')
@pytest.fixture(scope='function')
def get_ingredients():
    get_ingredients = StellarBurgersApi.get_ingredients()
    return get_ingredients



