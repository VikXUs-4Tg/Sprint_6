from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from data import const
from locators.base_page_locators import BasePageLocators as BPL

class BasePage:
    #logo_scooter = BPL.button_scooter
    #logo_yandex = BPL.button_yandex

    def __init__(self, driver):
        self.driver = driver

    def find_and_click(self, element):
        WDW(self.driver, const['wait_timer']).until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))

    def push_logo_scooter(self):
        #WDW(self.driver, const['wait_timer']).until(EC.element_to_be_clickable(BPL.button_scooter))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.button_scooter))

    def push_logo_yandex(self):
        #WDW(self.driver, const['wait_timer']).until(EC.element_to_be_clickable(BPL.button_yandex))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.button_yandex))

        #WDW(self.driver, const['wait_timer']).until(EC.visibility_of_element_located(BPL.BasePageLocators.accept_cookie_button))
        #self.driver.find_element(*BPL.BasePageLocators.accept_cookie_button).click()

    #def authorization(driver, login, password, login_field, password_field, button):
    #    WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(button))
    #    driver.find_element(*login_field).send_keys(login)
    #    driver.find_element(*password_field).send_keys(password)
    #    driver.find_element(*button).click()

    #def registration(driver, login, password, login_field, password_field, button):
    #    WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(button))
    #    names = driver.find_elements(*login_field)
    #    names[0].send_keys(login[:login.find('@')])
    #    names[1].send_keys(login)
    #    driver.find_element(*password_field).send_keys(password)
    #    driver.find_element(*button).click()