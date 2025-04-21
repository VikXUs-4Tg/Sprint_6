from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLocators as APL


class AuthorizationPage(BasePage):

    def authorization_in_first_window(self, name, last_name, address, telephone, station):
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_NAME, name)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_LAST_NAME, last_name)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_ADDRESS, address)
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_TELEPHONE, telephone)
        self.find_and_click(APL.FIELD_FOR_ENTRY_METRO_STATION)
        self.find_and_click(station)
        self.find_and_click(APL.BUTTON_NEXT_AND_PLACE_ORDER)

    def authorization_in_second_window(self, day_at_week, rent_time, color, comment):
        print("")
        self.entry_data_to_field(APL.FIELD_FOR_ENTRY_RENTAL_COMMENT, comment)
        self.find_and_click(APL.FIELD_FOR_ENTRY_DATE)
        self.find_and_click(day_at_week)
        self.find_and_click(APL.FIELD_FOR_ENTRY_RENTAL_PERIOD)
        self.find_and_click(rent_time)
        self.find_and_click(color)
        self.find_and_click(APL.BUTTON_NEXT_AND_PLACE_ORDER)

    def accept_window_yes(self):
        self.find_and_click(APL.BUTTON_YES)

    def check_order_window(self, expected_value):
        self.wait.until(EC.visibility_of_element_located(APL.TITLE_OF_ORDER_WINDOW))
        actually_value = self.driver.find_element(*APL.TITLE_OF_ORDER_WINDOW)
        assert expected_value in actually_value.text, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value.text}"'
