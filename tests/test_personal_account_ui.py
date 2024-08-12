import allure
from pages.login_page import LoginPageActions


class TestCheckPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    def test_go_to_personal_account(self, browser, routes):
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        login_page_step.click_to_personal_account()
        assert routes.authorization_page_url in browser.current_url

    @allure.title('Проверка перехода в историю заказов')
    def test_go_to_orders_history(self, browser, routes, user_authorization):
        login_page_step = LoginPageActions(browser)
        login_page_step.click_to_personal_account()
        login_page_step.click_to_orders_history()
        current_order_history_url = browser.current_url
        assert routes.order_history in current_order_history_url

    @allure.title('Проверка выхода из аккунта')
    def test_user_can_exit_account(self, browser, user_authorization):
        login_page_step = LoginPageActions(browser)
        login_page_step.click_to_personal_account()
        login_page_step.click_to_account_exit()


