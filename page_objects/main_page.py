from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from data import const


class MainPage(BasePage):

    def check_drop_down_lists(self, target, expected_value):
        self.find_and_click(target)
        parent_of_testing_element = self.driver.find_element(By.XPATH,f"//div[@aria-labelledby='{self.driver.find_element(*target).get_attribute('id')}']")
        actually_value = parent_of_testing_element.find_element(By.XPATH, "./p")
        WDW(parent_of_testing_element, const['wait_timer']).until(EC.visibility_of_element_located((By.XPATH, "./p")))
        assert actually_value.text == expected_value, f'Ожидалось значение содержимого раскрывающегося списка: "{expected_value}", получено "{actually_value.text}"'
