from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL


import time

class BasePage:

    def __init__(self, driver, wait_timer):
        self.driver = driver
        self.wait_timer = wait_timer
        self.wait = WDW(self.driver, wait_timer)

    def find_and_click(self, element):
        self.wait.until(EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def find_and_click_by_script(self, element):
        self.wait.until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))

    def push_logo_scooter(self):
        #self.wait.until(EC.element_to_be_clickable(BPL.button_scooter))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_SCOOTER))

    def push_logo_yandex(self):
        #self.wait.until(EC.element_to_be_clickable(BPL.button_yandex))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_YANDEX))

    def push_button_place_an_order(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_PLACE_AN_ORDER))

        #self.wait.until(EC.visibility_of_element_located(BPL.BasePageLocators.accept_cookie_button))
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