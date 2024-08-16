import time

from .base_app import BasePage
from allure import step
from locators.locators import StellarBurgersLocators


class LoginPageActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = StellarBurgersLocators

    @step('Переход на страницу входа')
    def click_to_personal_account(self):
        return self.find_element(self.elements.PERSONAL_ACCOUNT_BUTTON).click()

    @step('Нажатие кнопки "Восстановить пароль"')
    def click_to_password_recovery_button(self):
        return self.find_element(self.elements.PASSWORD_RECOVERY_BUTTON).click()

    @step('Ввод почты')
    def get_field_for_input_mail(self):
        return self.find_element(self.elements.MAIL_INPUT_FIELD)

    @step('Нажатие кнопки входа')
    def click_to_accept_button(self):
        return self.find_element(self.elements.ACCEPT_BUTTON).click()

    @step('Нажатие кнопка восстановления пароля')
    def click_to_recovery_button(self):
        return self.find_element(self.elements.RECOVERY_BUTTON).click()

    @step('Нажатие на поле ввода пароля')
    def get_field_for_input_password(self):
        return self.find_element(self.elements.PASSWORD_INPUT_FIELD)

    @step('Поиск поля ввода с активным подсвеченным состоянием')
    def get_active_field(self):
        return self.find_element(self.elements.FOCUSED_PASSWORD_INPUT_FIELD)

    @step('Поиск элемента с заполненным полем email')
    def search_filled_email_input_field(self):
        return self.find_element(self.elements.FILLED_MAIL_EDIT_INPUT_FIELD)

    @step('Нажатие на кнопку История Заказов')
    def click_to_orders_history(self):
        return self.find_element(self.elements.ORDER_HISTORY_BUTTON).click()

    @step('Нажитие на кнопку Выхода из аккаунта')
    def click_to_account_exit(self):
        element = self.find_element(self.elements.EXIT_ACCOUNT_BUTTON).click()
        return element




