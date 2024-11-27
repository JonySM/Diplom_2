import helper


class Data:

    CREATE_RANDOM_USER_BODY = {
                "email": helper.Help.generated_email(),
                "password": helper.Help.generated_password(),
                "name": helper.Help.generated_name()
                              }

    DELETE_USER_RESPONSE = '{"success":true,"message":"User successfully removed"}'

    CREATE_USER_BODY = {
               "email": "JohnSmith224@yandex.ru",
               "password": "JohnSmith!",
                "name": "John"
                               }

    CREATING_A_REGISTERED_USER_RESPONSE = '{"success":false,"message":"User already exists"}'

    CREATE_WITHOUT_PASSWORD_USER_BODY = {
                 "email": "JohnSmith219@yandex.ru",
                 "name": "John"
                               }

    CREATE_WITHOUT_EMAIL_USER_BODY = {
                 "password": "JohnSmith!",
                 "name": "John"
                                }

    CREATE_WITHOUT_NAME_USER_BODY = {
                 "email": "JohnSmith219@yandex.ru",
                 "password": "JohnSmith!",
                                 }

    RESPONSE_WITHOUT_USER_DATA = '{"success":false,"message":"Email, password and name are required fields"}'

    LOGIN_USER_BODY = {
            "email": "JohnSmith300@yandex.ru",
            "password": "JohnSmith!"
                                    }

    INVALID_LOGIN_USER_DATA = {
        "email": "JohnSmith301@yandex.ru",
        "password": "JohnSmith!1"
                                  }

    RESPONSE_INVALID_LOGIN_USER_DATA = '{"success":false,"message":"email or password are incorrect"}'

    RESPONSE_INVALID_UPDATE_USER_DATA = '{"success":false,"message":"You should be authorised"}'

    UPDATE_NEW_USER_DATA = {
        "email": helper.Help.generated_email(),
        "password": helper.Help.generated_password(),
        "name": helper.Help.generated_name()
                       }

    REGISTERED_USER = {"email": "JohnSmith545@yandex.ru"}

    RESPONSE_REGISTERED_UPDATE_USER = '{"success":false,"message":"User with such email already exists"}'

    EMPTY_INGREDIENT_BODY = {"ingredients": []}

    RESPONSE_EMPTY_INGREDIENT = '{"success":false,"message":"Ingredient ids must be provided"}'

    INVALID_HASH_INGREDIENT_BODY = {"ingredients": ["61c0c5a71d1f82001bda7a7a6dsa"]}

    RESPONSE_GET_ORDERS_WITHOUT_AUTH = '{"success":false,"message":"You should be authorised"}'










