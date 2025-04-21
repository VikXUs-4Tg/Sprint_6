import pytest
from selenium import webdriver
from conftest import random_name, random_last_name, random_address, random_telephone, random_comment, random_day_at_week, random_rent_time, random_color, random_metro_station
from data import  firefox_options, const, drop_down_lists_test_data
from page_objects.main_page import BasePage
from page_objects.main_page import MainPage
from page_objects.authorization_page import AuthorizationPage
from locators.main_page_locators import MainPageLocators as MPL
from locators.authorization_page_locators import AuthorizationPageLocators as APL

import time

class TestClass:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox(options=firefox_options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestDropDownLists(TestClass):

    @pytest.mark.parametrize('pointer_of_object,result', drop_down_lists_test_data)
    def test_drop_down_lists(self, pointer_of_object,result):
        self.driver.get(const['WEBPAGE'])
        main_page = MainPage(self.driver, const['WAIT_TIMER'])
        main_page.check_drop_down_lists(target=pointer_of_object, expected_value=result)

class TestPlaceAnOrder(TestClass):

    #entry_point
    #@pytest.mark.parametrize('pointer_of_object,result', drop_down_lists_test_data)
    def test_place_an_order(self, random_name, random_last_name, random_address, random_telephone, random_day_at_week, random_comment, random_rent_time, random_color, random_metro_station):
        self.driver.get(const['WEBPAGE'])
        base_page = BasePage(self.driver, const['WAIT_TIMER'])
        base_page.push_button_place_an_order()
        #main_page = MainPage(self.driver)
        #main_page.find_and_click(MPL.BUTTON_PLACE_AN_ORDER)
        authorization_page = AuthorizationPage(self.driver, const['WAIT_TIMER'])
        authorization_page.authorization_in_first_window(name=random_name,last_name=random_last_name,address=random_address,telephone=random_telephone, station=random_metro_station)
        authorization_page.authorization_in_second_window(day_at_week=random_day_at_week, rent_time=random_rent_time, color=random_color, comment=random_comment)
        authorization_page.accept_window_yes()
        authorization_page.check_order_window(expected_value=const['MADE_ORDER_TITLE_WINDOW'])
        base_page.push_logo_scooter()
        base_page.push_logo_yandex()
        time.sleep(5)
        #assert 0 == 1