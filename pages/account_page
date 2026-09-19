import allure

from locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
