import time

from selenium.webdriver.support import expected_conditions as EC
from data import const
from page_objects.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLocators as APL



class AuthorizationPage(BasePage):

    def entry_data_to_field(self, target, data):
        self.wait.until(EC.element_to_be_clickable(target))
        self.driver.find_element(*target).send_keys(data)

    def authorization_in_first_window(self, name, last_name, address, telephone):
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_NAME, name)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_LAST_NAME, last_name)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_ADDRESS, address)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_TELEPHONE, telephone)
        self.find_and_click(APL.FIELD_FOR_ENTRY_METRO_STATION)
        self.find_and_click(APL.METRO_STATION_1)
        self.find_and_click(APL.BUTTON_NEXT_AND_PLACE_ORDER)

    def authorization_in_second_window(self, day_at_week, rent_time, comment):
        print("")
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_RENTAL_COMMENT, comment)
        self.find_and_click(APL.FIELD_FOR_ENTRY_DATE)
        self.find_and_click(day_at_week)
        self.find_and_click(APL.FIELD_FOR_ENTRY_RENTAL_PERIOD)
        self.find_and_click(rent_time)





        #time.sleep(5)
        self.find_and_click(APL.BUTTON_NEXT_AND_PLACE_ORDER)
        assert 1 == 1
