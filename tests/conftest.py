import pytest
from allure import step
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils import authorization_header
from selenium import webdriver
import requests
from routes.routes import Routes
from data.user_data import UserRegistrationModel, UserLoginModel
from pages.login_page import LoginPageActions
from pathlib import Path
from pages.main_page import MainPageActions
from data.data_for_asserts import DataForAsserts
from settings import Settings


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Драйвер для запуска тестов. "
                                                            "Доступные драйверы: chrome, firefox"
    )


@step('Запуск веб-драйвера')
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver_path = Path(__file__).parent.parent / "driver"
    if browser_name == "chrome":
        service = ChromeService(executable_path=str(driver_path / "chromedriver.exe"))
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path=str(driver_path / "geckodriver.exe"))
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
    yield driver
    driver.quit()


@step('Подготовка маршрутов StellarBurgers')
@pytest.fixture
def routes():
    return Routes()


@step('Подготовка тестовых пароля и почты')
@pytest.fixture
def user_data():
    user = UserRegistrationModel().dict()
    return user['email'], user['password']


@step('Создание пользователя для теста и удаление после теста')
@pytest.fixture
def create_and_delete_user_for_test(routes):
    requests.post(url=f'{Settings().base_url}{routes.api_register_user}', json=UserRegistrationModel().dict())
    token = requests.post(url=f'{Settings().base_url}{routes.api_login}', json=UserLoginModel().dict()).json()["accessToken"]
    yield
    requests.delete(url=f'{Settings().base_url}{routes.api_user}', headers=authorization_header(token))


@step('Создание заказа для теста')
@pytest.fixture
def create_order_for_test(browser):
    main_page_step = MainPageActions(browser)
    main_page_step.drag_and_drop_ingredient_to_place_that_take_ingredients()
    main_page_step.click_to_make_an_order_button()
    main_page_step.click_to_close_window_after_make_an_order()


@step('Подготовка текстовок нужны для ассертов')
@pytest.fixture
def text_for_asserts():
    return DataForAsserts()


@step('Авторизация на UI')
@pytest.fixture()
def user_authorization(user_data, browser, create_and_delete_user_for_test):
    email, password = user_data
    login_page_step = LoginPageActions(browser)
    login_page_step.go_to_site()
    login_page_step.click_to_personal_account()
    login_page_step.get_field_for_input_mail().send_keys(email)
    login_page_step.get_field_for_input_password().send_keys(password)
    login_page_step.click_to_accept_button()
    login_page_step.click_to_personal_account()
