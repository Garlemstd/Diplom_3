import allure
from pages.login_page import LoginPageActions
from routes.routes import Routes


class TestCheckPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    def test_go_to_personal_account(self, browser, routes):
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        login_page_step.click_to_personal_account()
        assert routes.authorization_page_url in login_page_step.get_url_page()

    @allure.title('Проверка перехода в историю заказов')
    def test_go_to_orders_history(self, browser, routes, user_authorization):
        login_page_step = LoginPageActions(browser)
        login_page_step.click_to_personal_account()
        login_page_step.click_to_orders_history()
        current_order_history_url = login_page_step.get_url_page()
        assert routes.order_history in current_order_history_url

    @allure.title('Проверка выхода из аккаунта')
    def test_user_can_exit_account(self, browser, user_authorization):
        login_page_step = LoginPageActions(browser)
        login_page_step.click_to_personal_account()
        login_page_step.click_to_account_exit()
        assert login_page_step.assert_text_in_current_url(Routes().authorization_page_url)


