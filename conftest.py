import pytest
import helpers
from selenium import webdriver
from data import firefox_options, const
from page_objects.main_page import MainPage
from page_objects.make_order_page import MakeOrderPage
from locators.make_order_page_locators import MakeOrderPageLocators as MOPL


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver, wait_timer=const['WAIT_TIMER'], start_page=const['WEBPAGE'])
    main_page.open_start_page()
    return main_page

@pytest.fixture(scope='function')
def make_order_page(driver):
    make_order_page = MakeOrderPage(driver, wait_timer=const['WAIT_TIMER'], start_page=const['WEBPAGE'])
    make_order_page.open_start_page()
    return make_order_page

@pytest.fixture(scope='function')
def random_name():
    return helpers.generate_random_name()

@pytest.fixture(scope='function')
def random_last_name():
    return helpers.generate_random_last_name()

@pytest.fixture(scope='function')
def random_address():
    return helpers.generate_random_address()

@pytest.fixture(scope='function')
def random_telephone():
    return helpers.generate_random_telephone()

@pytest.fixture(scope='function')
def random_comment():
    return helpers.generate_random_comment()

@pytest.fixture(scope='function')
def random_day_at_week():
    return helpers.generate_random_day_at_week(MOPL.BILLET_FOR_DAY_AT_WEEK)

@pytest.fixture(scope='function')
def random_rent_time():
    return helpers.generate_random_rent_time(MOPL.BILLET_FOR_RENT_TIME)

@pytest.fixture(scope='function')
def random_color():
    return helpers.generate_random_color(MOPL.BILLET_FOR_COLOR)

@pytest.fixture(scope='function')
def random_metro_station():
    return helpers.generate_random_metro_station(MOPL.BILLET_FOR_METRO_STATION)
