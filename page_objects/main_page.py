from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):

    def check_drop_down_lists(self, target, expected_value):
        self.find_and_click_by_script(target)
        parent_of_testing_element = self.driver.find_element(By.XPATH,f"//div[@aria-labelledby='{self.driver.find_element(*target).get_attribute('id')}']")
        actually_value = parent_of_testing_element.find_element(*MPL.TEXT_FIELD_OF_ELEMENT)
        WDW(parent_of_testing_element, self.wait_timer).until(EC.visibility_of_element_located(MPL.TEXT_FIELD_OF_ELEMENT))
        assert actually_value.text == expected_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value.text}"'

    def push_button_place_an_order(self):
        self.find_and_click(MPL.BUTTON_PLACE_AN_ORDER)
