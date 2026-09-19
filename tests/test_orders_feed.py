import allure


class TestOrderFeed:
    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании заказа')
    def test_total_orders_counter_increases(self, main_page, login, order_feed_page):
        main_page.go_to_feed()
        previous_count = order_feed_page.get_total_orders_count()
        main_page.go_to_constructor()
        main_page.create_order()
        main_page.go_to_feed()
        current_count = order_feed_page.wait_for_total_orders_count_increase(previous_count)

        assert current_count > previous_count

    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании заказа')
    def test_today_orders_counter_increases(self, main_page, login, order_feed_page):
        main_page.go_to_feed()
        previous_count = order_feed_page.get_today_orders_count()
        main_page.go_to_constructor()
        main_page.create_order()
        main_page.go_to_feed()
        current_count = order_feed_page.wait_for_today_orders_count_increase(previous_count)

        assert current_count > previous_count

    @allure.title('Появление номера заказа в разделе "В работе"')
    def test_order_number_in_progress(self, main_page, login, order_feed_page):
        order_number = main_page.create_order()
        main_page.go_to_feed()

        assert order_feed_page.wait_for_order_number_in_progress(order_number)