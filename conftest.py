import pytest
import helpers
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import firefox_options, const
from page_objects.main_page import MainPage
from page_objects.make_order_page import MakeOrderPage


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
    random_choice = helpers.generate_random_day_at_week()
    return By.XPATH, random_choice

@pytest.fixture(scope='function')
def random_rent_time():
    random_choice = helpers.generate_random_rent_time_xpath()
    return By.XPATH, random_choice

@pytest.fixture(scope='function')
def random_color():
    random_choice = helpers.generate_random_color_xpath()
    return By.XPATH, random_choice

@pytest.fixture(scope='function')
def random_metro_station():
    random_choice = helpers.generate_random_metro_station_xpath()
    return By.XPATH, random_choice
