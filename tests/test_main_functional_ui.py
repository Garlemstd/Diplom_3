import allure
from pages.login_page import LoginPageActions
from pages.main_page import MainPageActions


class TestMainFunctional:

    @allure.title('Переход на страницу конструктора')
    def test_go_to_constructor_page(self, browser):
        main_page_step = MainPageActions(browser)
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        main_page_step.click_to_constructor_button()
        assert main_page_step.assert_constructor_page_active()

    @allure.title('Переход на страницу заказов')
    def test_go_to_order_feed_page(self, browser, routes):
        main_page_step = MainPageActions(browser)
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        main_page_step.get_orders_feed_element().click()
        assert routes.orders_feed in main_page_step.get_url_page()

    @allure.title('Появляется модальное окно при нажатии на ингредиент')
    def test_check_modal_window_if_click_on_ingredient(self, browser):
        main_page_step = MainPageActions(browser)
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        main_page_step.get_ingredient_element().click()
        assert main_page_step.assert_modal_window_is_visible()

    @allure.title('Модальное окно закрывается при нажатии на крестик')
    def test_modal_window_closing_if_click_to_cross(self, browser):
        main_page_step = MainPageActions(browser)
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        main_page_step.get_ingredient_element().click()
        main_page_step.click_to_close_modal_window()

    @allure.title('Количество ингредиентов увеличивается после добавления ингредиента')
    def test_increase_ingredient_quantity_after_add_ingredient(self, browser, text_for_asserts):
        main_page_step = MainPageActions(browser)
        login_page_step = LoginPageActions(browser)
        login_page_step.go_to_site()
        with allure.step('Проверка количества булок до переноса их в конструктор'):
            quantity_of_buns_before_add_to_cart = main_page_step.get_quantity_of_selected_ingredient().text
            assert text_for_asserts.bun_numbers_before_add_to_constructor == quantity_of_buns_before_add_to_cart
        main_page_step.drag_and_drop_ingredient_to_place_that_take_ingredients()
        with allure.step('Проверка количества булок после переноса их в конструктор'):
            quantity_of_selected_buns = main_page_step.get_quantity_of_selected_ingredient().text
            assert quantity_of_selected_buns == text_for_asserts.bun_numbers_after_add_to_constructor

    @allure.title('Авторизванный юзер может сделать заказ')
    def test_created_user_can_make_an_order(self, browser, text_for_asserts, create_and_delete_user_for_test, user_data):
        with allure.step('Авторизация'):
            email, password = user_data
            main_page_step = MainPageActions(browser)
            login_page_step = LoginPageActions(browser)
            login_page_step.go_to_site()
            login_page_step.click_to_personal_account()
            login_page_step.get_field_for_input_mail().send_keys(email)
            login_page_step.get_field_for_input_password().send_keys(password)
            login_page_step.click_to_accept_button()
        with allure.step('Создание заказа'):
            main_page_step.click_to_make_an_order_button()
            assert main_page_step.assert_modal_window_is_visible()



