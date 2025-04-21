from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL
import allure


class MainPage(BasePage):

    @allure.step('Ищем веб элемент {target}, нажимаем на него и проверяет текст в выпадающем дочернем окне на совпадение с {expected_value}')
    def check_drop_down_lists(self, target, expected_value):
        self.find_and_click_by_script(target)
        parent_of_testing_element = self.driver.find_element(By.XPATH,f"//div[@aria-labelledby='{self.driver.find_element(*target).get_attribute('id')}']")
        actually_value = parent_of_testing_element.find_element(*MPL.TEXT_FIELD_OF_ELEMENT)
        WDW(parent_of_testing_element, self.wait_timer).until(EC.visibility_of_element_located(MPL.TEXT_FIELD_OF_ELEMENT))
        assert actually_value.text == expected_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value.text}"'

    @allure.step('Ищем и нажимаем кнопку "Заказать" на главной странице (в середине)')
    def push_button_place_an_order(self):
        self.find_and_focus_by_script(MPL.FIELD_HOW_IT_WORKS)
        self.find_and_click_by_script(MPL.BUTTON_PLACE_AN_ORDER)
