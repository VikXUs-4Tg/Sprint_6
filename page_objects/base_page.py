from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL
from data import const
import allure


class BasePage:

    def __init__(self, driver, wait_timer, start_page):
        self.driver = driver
        self.wait_timer = wait_timer
        self.start_page = start_page
        self.wait = WDW(self.driver, wait_timer)

    @allure.step("Открываем главную страницу")
    def open_page(self, page):
        self.driver.get(page)
        self.wait.until(EC.url_contains(page))

    def open_start_page(self):
        self.open_page(self.start_page)
        self.wait.until(EC.url_contains(self.start_page))

    def find_and_focus_by_script(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        self.wait.until(EC.element_to_be_clickable(element))

    @allure.step("Находим и нажимаем элемент {element}")
    def find_and_click(self, element):
        self.find_and_focus_by_script(element)
        self.driver.find_element(*element).click()

    @allure.step("Находим и нажимаем элемент {element}")
    def find_and_click_by_script(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))

    @allure.step("Находим текстовое поле {element} и вводим в него значение {data}")
    def entry_data_to_field(self, element, data):
        self.find_and_focus_by_script(element)
        self.driver.find_element(*element).send_keys(data)

    @allure.step("Возвращаем искомый элемент")
    def get_element(self, element):
        self.find_and_focus_by_script(element)
        return self.driver.find_element(*element)

    @allure.step("Нажимаем на логотип «Самоката» в хедере")
    def push_logo_scooter(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_SCOOTER))

    @allure.step("Проверяем, что после нажатия на логотип «Самоката» происходит перенаправление на главную страницу")
    def check_push_logo_scooter(self):
        assert self.wait.until(EC.url_contains(self.start_page)), f"\nОжидаемое значение:\n'{self.start_page}'\nФактическое значение:\n'{self.driver.current_url}'"

    @allure.step("Нажимаем на логотип «Яндекс» в хедере")
    def push_logo_yandex(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_YANDEX))

    @allure.step("Проверяем, что после нажатия на логотип «Яндекс» происходит перенаправление на страницу Дзен")
    def check_push_logo_yandex(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.wait.until(EC.url_contains(const['DZEN_URL'])), f"\nОжидаемое значение:\n'{const['DZEN_URL']}'\nФактическое значение:\n'{self.driver.current_url}'"

    @allure.step("Нажимаем на кнопку «Заказать» в хедере")
    def push_button_place_an_order_in_header(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*BPL.BUTTON_PLACE_AN_ORDER))

    @allure.step("Находим элемент по значению, взятому из атрибута {attribute} другого элемента {element}")
    def find_by_attribute_of_another_element(self, initial_locator, element, attribute):
        method, locator = initial_locator
        target_locator = self.driver.find_element(*element).get_attribute(attribute)
        return self.driver.find_element(*(method, target_locator))

    @staticmethod
    def find_in_parent(parent_of_element, element):
        return parent_of_element.find_element(*element)

    @staticmethod
    def wait_visibility_of_element_by_parent(timer, parent, element):
        WDW(parent, timer).until(EC.visibility_of_element_located(element))
