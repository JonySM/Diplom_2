import pytest
from stellar_burgers_api import StellarBurgersApi


@pytest.fixture(scope='function')
def create_user():
    create_user = StellarBurgersApi.create_new_user()
    return create_user



