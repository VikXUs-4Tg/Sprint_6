from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL
from data import const
import allure


class MainPage(BasePage):

    @allure.step('Ищем веб элемент {target}, нажимаем на него и проверяет текст в выпадающем дочернем окне на совпадение с {expected_value}')
    def check_drop_down_lists(self, target, expected_value):
        self.find_and_click_by_script(target)
        parent_of_testing_element=self.find_by_attribute_of_another_element(initial_locator=MPL.EMPTY_LOCATOR_BY_ID, element=target, attribute=const['DROP_DOWN_LISTS_ATTRIBUTE_TO_ID'])
        actually_value=self.find_in_parent(parent_of_testing_element,MPL.TEXT_FIELD_OF_ELEMENT)
        self.wait_visibility_of_element_by_parent(self.wait_timer, parent_of_testing_element, MPL.TEXT_FIELD_OF_ELEMENT)
        assert actually_value.text == expected_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value.text}"'

    @allure.step('Ищем и нажимаем кнопку "Заказать" на главной странице (в середине)')
    def push_button_place_an_order(self):
        self.find_and_focus_by_script(MPL.FIELD_HOW_IT_WORKS)
        self.find_and_click_by_script(MPL.BUTTON_PLACE_AN_ORDER)
