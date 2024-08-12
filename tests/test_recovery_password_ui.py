import allure
from pages.login_page import LoginPageActions


class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления')
    def test_go_to_restore_password_page_afet_click_to_restore_password_button(self, browser, routes):

        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        login_page_step.click_to_personal_account()
        with allure.step('Переход на страницу восстановление пароля после нажатия на кнопку "Восстановить пароль"'):
            login_page_step.click_to_password_recovery_button()
        with allure.step('Проверка, что url страницы соответствует странице восстановления пароля '):
            assert routes.recovery_password in browser.current_url

    @allure.title('Проверка перехода на дальнейшую страницу восстановления после нажатия на кнопку восстановления')
    def test_input_email_to_recovery_password_and_click_to_recovery_btn(self, user_data, browser,
                                                                        text_for_asserts, routes):
        email, _ = user_data
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        login_page_step.click_to_personal_account()
        login_page_step.click_to_password_recovery_button()
        with allure.step('Ввод почты в поле и проверка, что действительно тестовый email был введен'):
            get_mail_field = login_page_step.get_field_for_input_mail()
            get_mail_field.send_keys(email)
            assert login_page_step.get_field_for_input_mail().get_attribute('value') == email
        with allure.step('Нажатие на кнопку восстановления пароля и проверка, что мы  на странице восстановления'):
            login_page_step.click_to_recovery_button()
            login_page_step.wait_for_url(routes.reset_password)
            assert routes.reset_password in browser.current_url

    @allure.title('Проверка фокусировки поля ввода пароля при нажатии на поле ввода пароля')
    def test_check_password_input_is_focused_if_click_on_him(self, user_data, browser, text_for_asserts, routes):
        email, _ = user_data
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        login_page_step.click_to_personal_account()
        login_page_step.click_to_password_recovery_button()
        get_mail_field = login_page_step.get_field_for_input_mail()
        get_mail_field.send_keys(email)
        login_page_step.click_to_recovery_button()
        with allure.step('Нажатие на кнопку поле ввода пароля и проверка, что поле было подсвечено'):
            login_page_step.get_field_for_input_password().click()
            assert text_for_asserts.active_status_element in login_page_step.get_active_field().get_attribute('class')

