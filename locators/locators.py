from selenium.webdriver.common.by import By
from data.user_data import UserRegistrationModel


class StellarBurgersLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[text()='Личный Кабинет']")
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//*[text()='Восстановить пароль']")
    MAIL_INPUT_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//form//input[@type='password']")
    PASSWORD_DISPLAY_BUTTON = (By.CSS_SELECTOR, ".input__icon.input__icon-action > svg")
    ACCEPT_BUTTON = (By.XPATH, ".//form//button[contains(text(), 'Войти')]")
    FILLED_MAIL_EDIT_INPUT_FIELD = (By.CSS_SELECTOR, f'[value="{UserRegistrationModel().dict()["email"]}"]')
    ORDER_HISTORY_BUTTON = (By.XPATH, "//*[text()='История заказов']")
    EXIT_ACCOUNT_BUTTON = (By.XPATH, "//*[text()='Выход']")
    RECOVERY_BUTTON = (By.XPATH, ".//form//button[contains(text(), 'Восстановить')]")
    FOCUSED_PASSWORD_INPUT_FIELD = (By.XPATH, "//*[text()='Пароль']")


class MainPageLocators:
    ORDER_FEED_ELEMENT = (By.CSS_SELECTOR, '[href="/feed"]')
    FOCUSED_TEXT = 'link_active'
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/"]')
    INGREDIENT_BUTTON = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6")
    TEXT_IN_MODAL_INGREDIENT_WINDOW = (By.XPATH, "//*[text()='Детали ингредиента']")
    CLOSING_MODAL_WINDOW_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_ > button")
    PLACE_TO_DRAG_AND_DROP = (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")
    NUMBER_OF_SELECTED_INGREDIENT = (By.CSS_SELECTOR,
                                     '[href="/ingredient/61c0c5a71d1f82001bdaaa6c"] > .counter_counter__ZNLkj')
    #  NUMBER_OF_SELECTED_INGREDIENT - Ищет количество именно краторной булки! Он завязан на ID товара!
    MAKE_AN_ORDER_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0")
    MODAL_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")  # Элемент открытого модального окна
    TEXT_IN_WINDOW_OF_CREATED_ORDER = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    CLOSING_MODAL_WINDOW_AFTER_MAKE_AN_ORDER = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS')


class OrdersFeedLocators:
    FIRST_OF_50_ORDER_BUTTON = (By.CSS_SELECTOR, ".OrderHistory_dataBox__1mkxK")
    CLOSING_MODAL_WINDOW_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_ > button")
    TEXT_IN_CREATED_ORDER_IN_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, ".OrderHistory_visible__19YMB")
    ORDERS_QUANTITY_TEXT = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ")
    ORDER_NUMBER_IN_MODAL_WINDOWS = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq")
    ORDER_NUMBER_IN_ORDER_LIST_IN_PERSONAL_ACCOUNT = (By.CSS_SELECTOR,
                                                      ".OrderHistory_textBox__3lgbs > .text_type_digits-default")



