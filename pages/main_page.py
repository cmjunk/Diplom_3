import allure

from locators import MainPageLocators, OrderLocators
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
        self.click(MainPageLocators.FEED_BUTTON)

    @allure.step("Открыть вкладку «Булки»")
    def open_buns_tab(self):
        self.click(MainPageLocators.BUNS_TAB)

    @allure.step("Открыть вкладку «Соусы»")
    def open_sauces_tab(self):
        self.click(MainPageLocators.SAUCES_TAB)

    @allure.step("Открыть вкладку «Начинки»")
    def open_fillings_tab(self):
        self.click(MainPageLocators.FILLINGS_TAB)

    @allure.step("Получить список карточек ингредиентов на экране")
    def get_ingredients(self):
        return self.find_all(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Кликнуть на карточку ингредиента")
    def click_ingredient(self, ingredient_element):
        ingredient_element.click()

    @allure.step("Проверить, что открылось модальное окно с деталями ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_visible(MainPageLocators.MODAL)

    @allure.step("Закрыть модальное окно по крестику")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        return self.is_invisible(MainPageLocators.MODAL)

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_ingredient_counter(self, ingredient_element):
        try:
            counter = ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except Exception:
            # счётчик не отрисован, пока ингредиент ни разу не добавляли — это 0
            return 0

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient_element):
        ingredient_element.find_element(*OrderLocators.ADD_TO_ORDER_BUTTON).click()

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(OrderLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        return self.get_text(OrderLocators.ORDER_NUMBER_MODAL)

    @allure.step("Закрыть модальное окно с номером заказа")
    def close_order_modal(self):
        self.click(OrderLocators.ORDER_MODAL_CLOSE_BUTTON)
