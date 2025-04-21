from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL


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

    def entry_data_to_field(self, target, data):
        self.wait.until(EC.element_to_be_clickable(target))
        self.driver.find_element(*target).send_keys(data)

    def push_logo_scooter(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_SCOOTER))

    def push_logo_yandex(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_YANDEX))

    def push_button_place_an_order(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_PLACE_AN_ORDER))
