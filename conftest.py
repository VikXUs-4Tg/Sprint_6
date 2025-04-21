import pytest
import random
import string
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def random_name():
    russian_letters = ''.join([chr(i) for i in range(1040, 1104)])
    allowed_chars = russian_letters
    name = ''.join(random.choices(allowed_chars, k=random.randint(2, 15)))
    return name

@pytest.fixture(scope='function')
def random_last_name():
    russian_letters = ''.join([chr(i) for i in range(1040, 1104)])
    allowed_chars = russian_letters
    last_name = ''.join(random.choices(allowed_chars, k=random.randint(2, 15)))
    return last_name

@pytest.fixture(scope='function')
def random_address():
    russian_letters = ''.join([chr(i) for i in range(1040, 1104)])
    allowed_chars = russian_letters + string.digits
    random_address = ''.join(random.choices(allowed_chars, k=random.randint(5, 49)))
    return random_address

@pytest.fixture(scope='function')
def random_telephone():
    random_telephone = ''.join(random.choices(string.digits, k=11))  # Генерируем 11 случайных цифр
    if random.choice([True, False]):
        random_telephone = '+' + random_telephone
    return random_telephone

@pytest.fixture(scope='function')
def random_comment():
    russian_letters = ''.join([chr(i) for i in range(1040, 1104)])
    allowed_chars = russian_letters + string.digits
    random_comment = ''.join(random.choices(allowed_chars, k=random.randint(0, 24)))
    return random_comment

@pytest.fixture(scope='function')
def random_day_at_week():
    day_at_week = datetime.now() + timedelta(random.randint(1, 6))
    if int(day_at_week.strftime('%d')) in range(1, 6) and int(datetime.now().strftime('%d')) > 6:
        day_xpath_locator = "//div[contains(@class, 'react-datepicker__day--0" + f"{day_at_week.strftime('%d')}') and contains(@class, 'outside-month')]"
    else:
        day_xpath_locator = "//div[contains(@class, 'react-datepicker__day--0" + f"{day_at_week.strftime('%d')}')]"
    random_day_at_week = (By.XPATH, f"{day_xpath_locator}")
    return random_day_at_week

@pytest.fixture(scope='function')
def random_rent_time():
    random_choice = f"//div[contains(text(), '{random.choice(['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])}') and contains(@class, 'Dropdown-option')]"
    random_rent_time = (By.XPATH, f"{random_choice}")
    return random_rent_time

@pytest.fixture(scope='function')
def random_color():
    random_choice = f"//label[contains(text(), '{random.choice(['чёрный жемчуг', 'серая безысходность'])}')]"
    random_color = (By.XPATH, f"{random_choice}")
    return random_color

@pytest.fixture(scope='function')
def random_metro_station():
    random_choice = f"//li[@data-index='{random.randint(7, 8)}']"
    random_metro_station = (By.XPATH, f"{random_choice}")
    return random_metro_station
