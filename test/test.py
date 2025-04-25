import pytest
from data import const, drop_down_lists_test_data
import allure

# УДАЛИТЬ
from conftest import driver, main_page, make_order_page, random_name, random_last_name, random_address, random_telephone, random_comment, random_day_at_week, random_rent_time, random_color, random_metro_station

class TestSuit1:

    @pytest.mark.parametrize('pointer_of_object,result', drop_down_lists_test_data)
    @allure.title('Проверка ответов на "Вопросы о важном"')
    @allure.description('На главной странице ищет веб элемент содержащий искомый "вопрос", нажимает на него и проверяет "ответ" в открывающимся снизу под ним окне (дочернем элементе)')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_drop_down_lists(self, main_page, pointer_of_object, result):
        main_page.check_drop_down_lists(target=pointer_of_object, expected_value=result)

class TestSuit2:

    @allure.title("Проверяем возможность сделать заказ с случайными валидными данными через кнопку 'Заказать' в хедере")
    @allure.description("Открываем главную страницу и нажимаем кнопку 'Заказать' в хедере.\nЗаполняем первое и второе окно данных о заказе.\nПодтверждаем создание заказа и проверяем сообщение, что заказ создан.")
    @allure.story("Тестовый сценарий № 2")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_place_an_order_by_header_button(self, make_order_page, random_name, random_last_name, random_address, random_telephone, random_day_at_week, random_comment, random_rent_time, random_color, random_metro_station):
        make_order_page.push_button_place_an_order_in_header()
        make_order_page.make_order_in_first_window(name=random_name,last_name=random_last_name,address=random_address,telephone=random_telephone, station=random_metro_station)
        make_order_page.make_order_in_second_window(day_at_week=random_day_at_week, rent_time=random_rent_time, color=random_color, comment=random_comment)
        make_order_page.accept_window_yes()
        make_order_page.check_order_window(expected_value=const['MADE_ORDER_TITLE_WINDOW'])

    @allure.title("Проверяем возможность сделать заказ с случайными валидными данными через кнопку 'Заказать' на главной странице (в середине)")
    @allure.description("Открываем главную страницу и нажимаем кнопку 'Заказать' на главной странице (в середине).\nЗаполняем первое и второе окно данных о заказе.\nПодтверждаем создание заказа и проверяем сообщение, что заказ создан.")
    @allure.story("Тестовый сценарий № 2")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_place_an_order_by_main_page_button(self, make_order_page, main_page, random_name, random_last_name, random_address, random_telephone, random_day_at_week, random_comment, random_rent_time, random_color, random_metro_station):
        main_page.push_button_place_an_order()
        make_order_page.make_order_in_first_window(name=random_name,last_name=random_last_name,address=random_address,telephone=random_telephone, station=random_metro_station)
        make_order_page.make_order_in_second_window(day_at_week=random_day_at_week, rent_time=random_rent_time, color=random_color, comment=random_comment)
        make_order_page.accept_window_yes()
        make_order_page.check_order_window(expected_value=const['MADE_ORDER_TITLE_WINDOW'])

    @allure.title("Проверяем переход на главную страницу по нажатию на логотип «Самокат»")
    @allure.description("Открываем главную страницу и нажимаем кнопку 'Заказать' для перехода на страницу осуществления заказа.\nЗатем нажимаем на логотип «Самокат» и проверяем, что оказываемся на главной странице.")
    @allure.story("Тестовый сценарий № 2")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_push_logo_scooter(self, main_page):
        main_page.push_button_place_an_order_in_header()
        main_page.push_logo_scooter()
        main_page.check_push_logo_scooter()

    @allure.title("Проверяем переход на страницу Дзен по нажатию на логотип «Яндекс»")
    @allure.description("Открываем главную страницу.\nЗатем нажимаем на логотип «Яндекс» и проверяем, что оказываемся на странице Дзен.")
    @allure.story("Тестовый сценарий № 2")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_push_logo_yandex(self, main_page):
        main_page.push_logo_yandex()
        main_page.check_push_logo_yandex()
