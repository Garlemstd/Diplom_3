from locators.locators import OrdersFeedLocators
from pages.base_app import BasePage
from allure import step


class OrderFeedPageActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.elements = OrdersFeedLocators

    @step('Поиск заказа в ленте заказов')
    def get_order_in_order_page(self):
        return self.find_element(self.elements.FIRST_OF_50_ORDER_BUTTON)

    @step('Закрытие модального окна заказа')
    def click_to_close_order_modal_window(self):
        return self.find_elements(self.elements.CLOSING_MODAL_WINDOW_BUTTON)[1].click()

    @step('Поиск текста в созданном заказе в истории заказов личного кабинета')
    def get_text_in_created_order_in_personal_account(self):
        return self.find_element(self.elements.TEXT_IN_CREATED_ORDER_IN_PERSONAL_ACCOUNT)

    @step('Поиск элементов с общим количеством заказов (за сегодня и за все время)')
    def get_quantity_of_orders(self):
        orders_for_all_time = self.find_elements(self.elements.ORDERS_QUANTITY_TEXT)[0]
        orders_for_today = self.find_elements(self.elements.ORDERS_QUANTITY_TEXT)[1]
        return orders_for_all_time, orders_for_today

    @step('Поиск номера заказа в модальном окне при создании заказа')
    def get_number_of_order_in_modal_window(self):
        return self.find_element(self.elements.ORDER_NUMBER_IN_MODAL_WINDOWS)

    @step('Поиск номера заказа в списке заказов в личном кабинете')
    def get_number_of_order_in_order_list_in_personal_account(self):
        return self.find_element(self.elements.ORDER_NUMBER_IN_ORDER_LIST_IN_PERSONAL_ACCOUNT)