import time

from .base_app import BasePage
from allure import step
from locators.locators import MainPageLocators


class MainPageActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = MainPageLocators

    @step('Поиск элемента, содержащего текст: Лента заказов')
    def get_orders_feed_element(self):
        return self.find_element(self.elements.ORDER_FEED_ELEMENT)

    @step('Нажатие на кнопку страницы конструктора')
    def click_to_constructor_button(self):
        return self.find_element(self.elements.CONSTRUCTOR_BUTTON).click()

    @step('Поиска ингредиента: Краторная булка')
    def get_ingredient_element(self):
        return self.find_elements(self.elements.INGREDIENT_BUTTON)[1]

    @step('Поиск текста в модальном окне ингредиента')
    def get_text_in_modal_ingredient_window(self):
        return self.find_element(self.elements.TEXT_IN_MODAL_INGREDIENT_WINDOW)

    @step('Нажатие на крестик для закрытия модального окна ингредиента')
    def click_to_close_modal_window(self):
        return self.find_element(self.elements.CLOSING_MODAL_WINDOW_BUTTON).click()

    @step('Получение элемента, куда можно перенести ингредиент')
    def get_element_that_take_ingredient(self):
        return self.find_element(self.elements.PLACE_TO_DRAG_AND_DROP)

    @step('Перенос ингредиента в поле приема ингредиентов')
    def drag_and_drop_ingredient_to_place_that_take_ingredients(self):
        return self.elements_drag_and_drop(self.get_ingredient_element(), self.get_element_that_take_ingredient())

    @step('Поиск количества добавленного ингредиента')
    def get_quantity_of_selected_ingredient(self):
        return self.find_element(self.elements.NUMBER_OF_SELECTED_INGREDIENT)

    @step('Нажатие на кнопку создания заказа')
    def click_to_make_an_order_button(self):
        element = self.find_element(self.elements.MAKE_AN_ORDER_BUTTON).click()
        return element

    @step('Поиск текста в модальном окне после создания заказа')
    def get_text_about_creating_order_in_window(self):
        return self.find_element(self.elements.TEXT_IN_WINDOW_OF_CREATED_ORDER)

    @step('Проверка активности стр конструктора')
    def assert_constructor_page_active(self):
        return self.focus_on_element(MainPageLocators.CONSTRUCTOR_BUTTON, MainPageLocators.FOCUSED_TEXT)

    @step('Проверка, что модальное окно сможет закрыться')
    def assert_modal_window_can_be_closing(self):
        return self.element_is_clickable(self.elements.CLOSING_MODAL_WINDOW_AFTER_MAKE_AN_ORDER)

    @step('Закрытие модального окна после создания заказа')
    def click_to_close_window_after_make_an_order(self):
        # Здесь убеждаеся , что элемент кликабелен, перед попыткой кликнуть на него !
        self.assert_modal_window_can_be_closing()
        return self.find_element(self.elements.CLOSING_MODAL_WINDOW_AFTER_MAKE_AN_ORDER).click()

    @step('Проверка, что модальное окно открыто')
    def assert_modal_window_is_visible(self):
        return self.modal_window_is_open(MainPageLocators.MODAL_WINDOW)
