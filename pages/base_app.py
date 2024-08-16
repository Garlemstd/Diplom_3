from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from routes.routes import Routes
from allure import step
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Routes().main_route

    @step('Поиск элемента')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Элемент не был найден: {locator}")

    @step('Поиск нескольких элементов')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Элементы не были найдены {locator}")

    @step('Элемент виден на странице')
    def element_is_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @step('Проверка, что URL хранит ожидаемый текст')
    def assert_text_in_current_url(self, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(text))

    @step('Ожидание изменения URL')
    def wait_for_url(self, url_fragment, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url_fragment),
                                                      message=f"URL не содержит фрагмент: {url_fragment}")

    @step('На элементе установлена фокусировка')
    def focus_on_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element_attribute(locator, 'class', text))

    @step('Элемент кликабельный')
    def element_is_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @step('Проверка открытости модального окна')
    def modal_window_is_open(self, locator):
        return self.element_is_visible(locator)

    @step('Переход на главную страницу')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @step('drag and drop одного элемента на другой')
    def elements_drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

    @step('Запрос URL страницы')
    def get_url_page(self):
        return self.driver.current_url


