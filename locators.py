from selenium.webdriver.common.by import By

# ВАЖНО: приложение собрано на create-react-app с CSS-модулями, поэтому классы
# вида "BurgerIngredient_counter__abc123" содержат случайный суффикс.
# Локаторы ниже используют "^=" (начинается с...), чтобы не зависеть от суффикса.
# Названия блоков (BurgerIngredient_, Modal_, FeedInfo_ и т.д.) стоит свериться
# через DevTools перед первым запуском — на разных версиях фронтенда они могут
# немного отличаться.


class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
    PROFILE_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  # Кнопка «Личный кабинет»
    LOGO_LINK = (By.CSS_SELECTOR, "[class^='AppHeader_header__logo'] a")  # Логотип Stellar Burgers
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, "a[href='/']")  # Ссылка «Конструктор» в шапке
    FEED_LINK = (By.CSS_SELECTOR, "a[href='/feed']")  # Ссылка «Лента заказов» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Пункт меню "Конструктор"
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")  # Пункт меню "Лента заказов"

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"

    # Карточка ингредиента в списке
    INGREDIENT_ITEM = (By.CSS_SELECTOR, "[class^='BurgerIngredient_ingredient__']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class^='counter_counter__'] p")

    # Модальное окно с деталями ингредиента
    MODAL = (By.CSS_SELECTOR, "[class^='Modal_modal__']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class^='Modal_modal__close']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class^='Modal_modal_overlay__']")


class OrderLocators:
    # Кнопка "Добавить" появляется на карточке ингредиента при наведении/фокусе
    ADD_TO_ORDER_BUTTON = (By.XPATH, ".//button[text()='Добавить']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.CSS_SELECTOR, "[class^='OrderDetails_orderNumber__']")
    ORDER_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class^='Modal_modal__close']")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//div[label[text()='Имя']]/input")  # Поле "Имя"
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")  # Поле «Пароль»
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")  # Поле «Email»
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")  # Кнопка "Зарегистрироваться" на странице входа
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    REGISTER_FINAL = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться" после ввода данных
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")  # Кнопка в строке "Уже зарегистрированы?"


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.CSS_SELECTOR, "a[href='/forgot-password']")  # Кнопка "Восстановить пароль"


class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"


class FeedPageLocators:
    TOTAL_ORDERS_COUNT = (By.CSS_SELECTOR, "[class^='FeedInfo_total__'] p")  # "Выполнено за всё время"
    TODAY_ORDERS_COUNT = (By.CSS_SELECTOR, "[class^='FeedInfo_todayOrders__'] p")  # "Выполнено за сегодня"
    ORDERS_IN_PROGRESS_NUMBERS = (By.XPATH, "//h3[text()='В работе']/following-sibling::ul/li")
