import pytest
from selenium import webdriver
from data import  firefox_options, const, drop_down_lists_test_data
from page_objects.main_page import MainPage
from page_objects.make_order_page import MakeOrderPage
import allure
from conftest import random_name, random_last_name, random_address, random_telephone, random_comment, random_day_at_week, random_rent_time, random_color, random_metro_station


class TestClass:
    driver = None
    wait_timer = const['WAIT_TIMER']

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(options=firefox_options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

class TestDropDownLists(TestClass):

    @pytest.mark.parametrize('pointer_of_object,result', drop_down_lists_test_data)
    @allure.title('Проверка ответов на "Вопросы о важном"')
    @allure.description('На главной странице ищет веб элемент содержащий искомый "вопрос", нажимает на него и проверяет "ответ" в открывающимся снизу под ним окне (дочернем элементе)')
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_drop_down_lists(self, pointer_of_object,result):
        main_page=MainPage(self.driver, self.wait_timer)
        main_page.open_main_page()
        main_page.check_drop_down_lists(target=pointer_of_object, expected_value=result)

class TestPlaceAnOrder(TestClass):

    @pytest.mark.parametrize('entry_point', const['ENTRY_POINTS_LIST'])
    @allure.title("Проверяем возможность сделать заказ с случайными валидными данными, переход по нажатию на логотип «Самокат» и переход по нажатию на логотип «Яндекс» ")
    @allure.description("Нажимаем кнопку 'Заказать' и оформляем заказ с валидными данными.\nЗаполняем первое и второе окно данных о заказе.\nПодтверждаем создание заказа и проверяем сообщение, что заказ создан.\nЗатем нажимаем на логотип «Самокат» и проверяем, что оказываемся на главной странице.\nПотом нажимаем на логотип «Яндекс» и проверяем, что во второй вкладке открывается страница Дзен")
    @allure.link(const['WEBPAGE'], name='Учебный сервиса «Яндекс.Самокат» (стенд)')
    def test_place_an_order(self, entry_point, random_name, random_last_name, random_address, random_telephone, random_day_at_week, random_comment, random_rent_time, random_color, random_metro_station):
        make_order_page = MakeOrderPage(self.driver, self.wait_timer)
        make_order_page.open_main_page()
        match entry_point:
            case 1:
                make_order_page.push_button_place_an_order_in_header()
            case 2:
                MainPage(self.driver, self.wait_timer).push_button_place_an_order()
        make_order_page.make_order_in_first_window(name=random_name,last_name=random_last_name,address=random_address,telephone=random_telephone, station=random_metro_station)
        make_order_page.make_order_in_second_window(day_at_week=random_day_at_week, rent_time=random_rent_time, color=random_color, comment=random_comment)
        make_order_page.accept_window_yes()
        make_order_page.check_order_window(expected_value=const['MADE_ORDER_TITLE_WINDOW'])
        make_order_page.push_logo_scooter()
        make_order_page.check_push_logo_scooter()
        make_order_page.push_logo_yandex()
        make_order_page.check_push_logo_yandex()
