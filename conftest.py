import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from api_client import StellarBurgersAPI
from data import TestUser
from generators import generate_login, generate_password
from pages.main_page import MainPage
from urls import Links


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service, options=options)
    else:
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service, options=options)

    allure.dynamic.parameter("browser", browser_name)

    web_driver.maximize_window()
    web_driver.get(Links.MAIN_URL)

    yield web_driver

    web_driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def registered_user():
    email = generate_login()
    password = generate_password()
    name = TestUser.NAME

    response = StellarBurgersAPI.register_user(email, password, name)
    body = response.json()
    access_token = body.get("accessToken")

    user_data = {"email": email, "password": password, "name": name}

    yield user_data

    if access_token:
        StellarBurgersAPI.delete_user(access_token)