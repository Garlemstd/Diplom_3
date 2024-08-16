import allure
from pages.login_page import LoginPageActions
from pages.main_page import MainPageActions
from pages.orders_feed_page import OrderFeedPageActions


class TestOrdersFeed:

    @allure.title('Проверка появления модального окна при нажатии на ингредиент')
    def test_existing_modal_window_if_click_on_ingredient(self, browser, user_authorization):
        main_page_step = MainPageActions(browser)
        order_feed_steps = OrderFeedPageActions(browser)
        main_page_step.get_orders_feed_element().click()
        order_feed_steps.get_order_in_order_page().click()
        assert main_page_step.assert_modal_window_is_visible()

    @allure.title('Проверка, что заказ отображается в истории заказов в личном кабинете')
    def test_orders_from_order_history_visible_in_orders(self, browser, user_authorization):
        main_page_step = MainPageActions(browser)
        order_feed_steps = OrderFeedPageActions(browser)
        login_page_step = LoginPageActions(browser)
        main_page_step.drag_and_drop_ingredient_to_place_that_take_ingredients()
        main_page_step.click_to_make_an_order_button()
        order_number_when_creating = order_feed_steps.get_number_of_order_in_modal_window().text
        main_page_step.click_to_close_window_after_make_an_order()
        login_page_step.click_to_personal_account()
        login_page_step.click_to_orders_history()
        order_number_in_order_list = order_feed_steps.get_number_of_order_in_order_list_in_personal_account().text
        assert order_number_when_creating in order_number_in_order_list

    @allure.title('Количество заказов увеличивается после создания заказа')
    def test_quantity_of_all_orders_increased_after_create_order(self, browser, user_authorization):
        main_page_step = MainPageActions(browser)
        order_feed_steps = OrderFeedPageActions(browser)
        main_page_step.get_orders_feed_element().click()
        orders_order_quantity_for_all_time, orders_quantity_for_today = order_feed_steps.get_quantity_of_orders()
        main_page_step.click_to_constructor_button()

        main_page_step.drag_and_drop_ingredient_to_place_that_take_ingredients()
        main_page_step.click_to_make_an_order_button()
        main_page_step.assert_modal_window_can_be_closing()
        main_page_step.click_to_close_window_after_make_an_order()
        main_page_step.get_orders_feed_element().click()

        new_order_quantity_for_all_time, new_order_quantity_for_today = order_feed_steps.get_quantity_of_orders()
        assert orders_order_quantity_for_all_time != new_order_quantity_for_all_time
        assert orders_quantity_for_today != new_order_quantity_for_today

