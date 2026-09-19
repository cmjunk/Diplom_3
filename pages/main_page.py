import allure

from locators import MainPageLocators
from pages.base_page import BasePage
from urls import Links


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(Links.MAIN_URL)

    @allure.step("Перейти в раздел «Конструктор»")
    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в раздел «Лента заказов»")
    def go_to_feed(self):
        self.click(MainPageLocators.ORDERS_FEED)

    @allure.step("Перейти в личный кабинет")
    def go_to_profile(self):
        self.click(MainPageLocators.PROFILE_BUTTON)

    @allure.step("Открыть вкладку «Булки»")
    def open_buns_tab(self):
        self.click(MainPageLocators.BUNS_TAB)

    @allure.step("Открыть вкладку «Соусы»")
    def open_sauces_tab(self):
        self.click(MainPageLocators.SAUCES_TAB)

    @allure.step("Открыть вкладку «Начинки»")
    def open_fillings_tab(self):
        self.click(MainPageLocators.FILLINGS_TAB)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Проверить, что открылось окно с деталями ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_visible(MainPageLocators.POPUP_DETAILS)

    @allure.step("Закрыть окно с деталями ингредиента по крестику")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.POPUP_X)

    @allure.step("Проверить, что окно с деталями ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return self.is_invisible(MainPageLocators.POPUP_DETAILS)

    @allure.step("Перетащить ингредиент «{name}» в конструктор")
    def add_ingredient_to_basket(self, name):
        self.drag_and_drop(
            MainPageLocators.ingredient_by_name(name),
            MainPageLocators.BASKET,
        )

    @allure.step("Получить значение счётчика ингредиента «{name}»")
    def get_ingredient_counter_by_name(self, name):
        return self.get_text(MainPageLocators.ingredient_counter_by_name(name))
