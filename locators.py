from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//div[label[text()='Имя']]/input") # Поле "Имя"
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")  # Поле «Пароль» 
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")  # Поле «Email» 
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']") # Кнопка "Зарегистрироваться" на странице входа
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"
    REGISTER_FINAL=(By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться" после ввода данных
    PASSWORD_ERROR=(By.XPATH, "//div[p][text()='Некорректный пароль']]/p") # Ошибка "Некорректный пароль"
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']") # Кнопка в строке "Уже зарегистрированы?"


class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка «Войти в аккаунт»
    PROFILE_BUTTON = (By.CSS_SELECTOR, "a[href='/account']") # Кнопка «Личный кабинет»
    LOGO_LINK = (By.CSS_SELECTOR, "[class^='AppHeader_header__logo'] a") # Логотип Stellar Burgers 
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']") # Вкладка "Булка"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']") # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']") # Вкладка "Начинки"
    ORDERS_FEED = (By.XPATH, "//p[text()='Лента Заказов']") # Кнопка "Лента заказов"
    INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/')]") # Любой ингредиент
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]") # Корзина
    INGREDIENT_BY_NAME = "//a[.//p[text()='{name}']]" 
    COUNTER_BY_NAME = "//a[.//p[text()='{name}']]//div[contains(@class, 'counter_counter__')]"
    POPUP_DETAILS = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//h2[text()='Детали ингредиента']") # Попап при нажатии на ингридиент
    POPUP_X = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//button[@type='button']") # Крестик для закрытия попапа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ»
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//h2[contains(@class, 'Modal_modal__title_shadow__')]")  # Номер заказа в окне

    @staticmethod
    def ingredient_by_name(name):
        return (By.XPATH, f"//a[.//p[text()='{name}']]")

    @staticmethod
    def ingredient_counter_by_name(name):
        return (By.XPATH, f"//a[.//p[text()='{name}']]//div[contains(@class, 'counter_counter__')]")

class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.CSS_SELECTOR, "a[href='/forgot-password']") # Кнопка Восстановить пароль

class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход"    


class FeedPageLocators:
    TOTAL_ORDERS_READY = (By.XPATH, "//p[contains(text(), 'Готовы')]") # Готовые заказы
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[contains(text(), 'В работе')]") # Заголовок "Заказы в работе"
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p") # Заказы, выполненные за все время
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p") # Заказы, выполненные за сегодня
    ORDERS_IN_PROGRESS_NUMBERS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul/li") # Количество заказов "В работе"
