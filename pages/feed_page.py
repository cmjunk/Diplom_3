import allure

from locators import FeedPageLocators
from pages.base_page import BasePage
from urls import Links


class FeedPage(BasePage):
    @allure.step("Открыть страницу «Лента заказов»")
    def open_feed_page(self):
        self.open(Links.FEED_URL)

    @allure.step("Получить количество заказов «Выполнено за всё время»")
    def get_total_orders_count(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS_COUNT))

    @allure.step("Получить количество заказов «Выполнено за сегодня»")
    def get_today_orders_count(self):
        return int(self.get_text(FeedPageLocators.TODAY_ORDERS_COUNT))

    @allure.step("Получить список номеров заказов из раздела «В работе»")
    def get_orders_in_progress_numbers(self):
        return self.get_texts(FeedPageLocators.ORDERS_IN_PROGRESS_NUMBERS)

    @allure.step("Дождаться, пока счётчик «Выполнено за всё время» увеличится")
    def wait_for_total_orders_count_increase(self, count_before, timeout=20):
        self.wait_for_number_greater(FeedPageLocators.TOTAL_ORDERS_COUNT, count_before, timeout)
        return self.get_total_orders_count()

    @allure.step("Дождаться, пока счётчик «Выполнено за сегодня» увеличится")
    def wait_for_today_orders_count_increase(self, count_before, timeout=20):
        self.wait_for_number_greater(FeedPageLocators.TODAY_ORDERS_COUNT, count_before, timeout)
        return self.get_today_orders_count()

    @allure.step("Дождаться появления номера заказа в разделе «В работе»")
    def wait_for_order_number_in_progress(self, order_number, timeout=30):
        found = self.wait_for_number_in_elements(
            FeedPageLocators.ORDERS_IN_PROGRESS_NUMBERS, order_number, timeout
        )
        if not found:
            allure.attach(
                f"Ожидали: {order_number}; в списке: {self.get_orders_in_progress_numbers()}",
                name="Номера в «В работе»",
                attachment_type=allure.attachment_type.TEXT,
            )
        return found