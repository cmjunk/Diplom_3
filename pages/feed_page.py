import time

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
        elements = self.find_all(FeedPageLocators.ORDERS_IN_PROGRESS_NUMBERS)
        return [el.text for el in elements]

    @allure.step("Дождаться, пока счётчик «Выполнено за всё время» увеличится")
    def wait_for_total_orders_count_increase(self, count_before, timeout=15):
        end_time = time.time() + timeout
        current = count_before
        while time.time() < end_time:
            current = self.get_total_orders_count()
            if current > count_before:
                return current
            time.sleep(0.5)
        return current

    @allure.step("Дождаться, пока счётчик «Выполнено за сегодня» увеличится")
    def wait_for_today_orders_count_increase(self, count_before, timeout=15):
        end_time = time.time() + timeout
        current = count_before
        while time.time() < end_time:
            current = self.get_today_orders_count()
            if current > count_before:
                return current
            time.sleep(0.5)
        return current

    @allure.step("Дождаться появления номера заказа в разделе «В работе»")
    def wait_for_order_number_in_progress(self, order_number, timeout=15):
        end_time = time.time() + timeout
        while time.time() < end_time:
            numbers = self.get_orders_in_progress_numbers()
            if any(order_number.endswith(n) or n in order_number for n in numbers):
                return True
            time.sleep(0.5)
        return False