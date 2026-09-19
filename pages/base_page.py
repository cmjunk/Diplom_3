import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def _wait_until(self, condition, timeout):
        wait = WebDriverWait(
            self.driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        )
        return wait.until(condition)

    @allure.step("Открыть URL")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Найти видимый элемент")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Получить тексты всех элементов (пустой список, если их нет)")
    def get_texts(self, locator):
        elements = self.driver.find_elements(*locator)
        return [(el.get_attribute("textContent") or "").strip() for el in elements]

    @allure.step("Проверить, что элемент виден")
    def is_visible(self, locator, timeout=None):
        try:
            self._wait_until(EC.visibility_of_element_located(locator), timeout or self.timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить, что элемент не виден")
    def is_invisible(self, locator, timeout=None):
        return self._wait_until(EC.invisibility_of_element_located(locator), timeout or self.timeout)

    @allure.step("Дождаться URL")
    def wait_for_url(self, url, timeout=20):
        return self._wait_until(EC.url_to_be(url), timeout)

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator, timeout=None):
        return self._wait_until(EC.visibility_of_element_located(locator), timeout or self.timeout)

    @allure.step("Дождаться, пока число в элементе станет больше {value}")
    def wait_for_number_greater(self, locator, value, timeout=20):
        def condition(driver):
            elements = driver.find_elements(*locator)
            if not elements:
                return False
            text = elements[0].text.strip()
            return text.isdigit() and int(text) > value

        try:
            return self._wait_until(condition, timeout)
        except TimeoutException:
            return False

    @allure.step("Дождаться номера {number} среди элементов")
    def wait_for_number_in_elements(self, locator, number, timeout=30):
        expected = str(number).lstrip("0")

        def condition(driver):
            elements = driver.find_elements(*locator)
            texts = [(el.get_attribute("textContent") or "").strip().lstrip("0") for el in elements]
            return expected in texts

        try:
            return self._wait_until(condition, timeout)
        except TimeoutException:
            return False

    @allure.step("Дождаться, пока текст элемента станет отличным от {excluded}")
    def wait_for_text_not_in(self, locator, excluded, timeout=60):
        def condition(driver):
            elements = driver.find_elements(*locator)
            if not elements:
                return False
            return (elements[0].get_attribute("textContent") or "").strip() not in excluded

        return self._wait_until(condition, timeout)  # при таймауте бросает TimeoutException

    @allure.step("Перетащить элемент в целевую область")
    def drag_and_drop(self, source_locator, target_locator):
        element_from = self.find_element_with_wait(source_locator)
        element_to = self.find_element_with_wait(target_locator)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)