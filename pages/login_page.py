import allure

from locators import MainPageLocators, RegisterPageLocators
from pages.base_page import BasePage
from urls import Links


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(Links.LOGIN_URL)

    @allure.step("Перейти на страницу входа с главной страницы")
    def go_to_login_from_main(self):
        self.click(MainPageLocators.LOGIN_BUTTON_MAIN)

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        self.find(RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(RegisterPageLocators.SUBMIT_BUTTON)
