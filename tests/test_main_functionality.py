import allure

from urls import Links


class TestMainFunctionality:
    @allure.title('Клик по «Конструктор» на главной странице ничего не меняет')
    def test_click_constructor_from_main_page_does_nothing(self, main_page):
        main_page.go_to_constructor()

        assert main_page.get_current_url() == Links.MAIN_URL

    @allure.title('Клик по «Конструктор» из личного кабинета открывает главную страницу')
    def test_click_constructor_from_profile_takes_to_main_page(self, main_page):
        main_page.go_to_profile()
        main_page.go_to_constructor()

        assert main_page.wait_for_url(Links.MAIN_URL)

    @allure.title('Клик по «Конструктор» из ленты заказов открывает главную страницу')
    def test_click_constructor_from_orders_feed_takes_to_main_page(self, main_page):
        main_page.go_to_feed()
        main_page.go_to_constructor()

        assert main_page.wait_for_url(Links.MAIN_URL)

    @allure.title('Клик по «Лента заказов» открывает ленту заказов')
    def test_click_orders_feed_takes_to_orders_feed(self, main_page):
        main_page.go_to_feed()

        assert main_page.wait_for_url(Links.FEED_URL)

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_click_ingredient_opens_popup_window(self, main_page):
        main_page.click_first_ingredient()

        assert main_page.is_ingredient_modal_open()

    @allure.title('Клик по крестику закрывает окно с деталями ингредиента')
    def test_click_x_closes_popup_window(self, main_page):
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()

    @allure.title('При добавлении ингредиента в заказ его счётчик увеличивается')
    def test_ingredient_counter_increases(self, main_page):
        name = "Флюоресцентная булка R2-D3"

        main_page.add_ingredient_to_basket(name)

        assert main_page.get_ingredient_counter_by_name(name) == "2"