import random
import allure


class Help:
    @staticmethod
    @allure.step('Создаем случайный email пользователя')
    def generated_email():
        return f"Ivan{random.randint(1000, 9999)}@yandex.ru"

    @staticmethod
    @allure.step('Создаем случайный пароль пользователя')
    def generated_password():
        return f"UserPrakticum!*{random.randint(100, 9999)}"

    @staticmethod
    @allure.step('Создаем случайное имя пользователя')
    def generated_name():
        return f"Ivan{random.randint(1000, 9999)}"
