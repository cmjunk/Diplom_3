import allure

from locators import RegisterPageLocators
from pages.base_page import BasePage
from urls import Links


class RegisterPage(BasePage):
    @allure.step("Открыть страницу регистрации")
    def open_register_page(self):
        self.open(Links.REGISTER_URL)

    @allure.step("Заполнить и отправить форму регистрации")
    def register(self, name, email, password):
        self.find(RegisterPageLocators.NAME_INPUT).send_keys(name)
        self.find(RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(RegisterPageLocators.REGISTER_FINAL)

    @allure.step("Получить текст ошибки под полем пароля")
    def get_password_error_text(self):
        return self.get_text(RegisterPageLocators.PASSWORD_ERROR)