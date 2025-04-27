from page_objects.base_page import BasePage
from locators.make_order_page_locators import MakeOrderPageLocators as MOPL
import allure


class MakeOrderPage(BasePage):

    @allure.step('Заполняем поля заказа в первом окне')
    def make_order_in_first_window(self, name, last_name, address, telephone, station):
        self.entry_data_to_field(MOPL.FIELD_FOR_ENTRY_NAME, name)
        self.entry_data_to_field(MOPL.FIELD_FOR_ENTRY_LAST_NAME, last_name)
        self.entry_data_to_field(MOPL.FIELD_FOR_ENTRY_ADDRESS, address)
        self.entry_data_to_field(MOPL.FIELD_FOR_ENTRY_TELEPHONE, telephone)
        self.find_and_click(MOPL.FIELD_FOR_ENTRY_METRO_STATION)
        self.find_and_click(station)
        self.find_and_click(MOPL.BUTTON_NEXT_AND_PLACE_ORDER)

    @allure.step('Заполняем поля заказа во втором окне')
    def make_order_in_second_window(self, day_at_week, rent_time, color, comment):
        self.entry_data_to_field(MOPL.FIELD_FOR_ENTRY_RENTAL_COMMENT, comment)
        self.find_and_click(MOPL.FIELD_FOR_ENTRY_DATE)
        self.find_and_click(day_at_week)
        self.find_and_click(MOPL.FIELD_FOR_ENTRY_RENTAL_PERIOD)
        self.find_and_click(rent_time)
        self.find_and_click(color)
        self.find_and_click(MOPL.BUTTON_NEXT_AND_PLACE_ORDER)

    @allure.step('Соглашаемся на оформление заказа')
    def accept_window_yes(self):
        self.find_and_click(MOPL.BUTTON_YES)

    @allure.step('Проверяем на наличие надписи {expected_value}')
    def check_order_window(self, expected_value):
        actually_value = self.get_element(MOPL.TITLE_OF_ORDER_WINDOW)
        assert expected_value in actually_value.text, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value.text}"'
