import random
import string
from datetime import datetime, timedelta


russian_letters = ''.join([chr(i) for i in range(1040, 1104)])

def generate_random_name():
    allowed_chars = russian_letters
    name = ''.join(random.choices(allowed_chars, k=random.randint(2, 15)))
    return name

def generate_random_last_name():
    allowed_chars = russian_letters
    last_name = ''.join(random.choices(allowed_chars, k=random.randint(2, 15)))
    return last_name

def generate_random_address():
    allowed_chars = russian_letters + string.digits
    random_address = ''.join(random.choices(allowed_chars, k=random.randint(5, 49)))
    return random_address

def generate_random_telephone():
    random_telephone = ''.join(random.choices(string.digits, k=11))  # Генерируем 11 случайных цифр
    if random.choice([True, False]):
        random_telephone = '+' + random_telephone
    return random_telephone

def generate_random_comment():
    allowed_chars = russian_letters + string.digits
    random_comment = ''.join(random.choices(allowed_chars, k=random.randint(0, 24)))
    return random_comment

def generate_random_day_at_week():
    day_at_week = datetime.now() + timedelta(random.randint(1, 6))
    if int(day_at_week.strftime('%d')) in range(1, 6) and int(datetime.now().strftime('%d')) > 6:
        return f"//div[contains(@class, 'react-datepicker__day--0" + f"{day_at_week.strftime('%d')}') and contains(@class, 'outside-month')]"
    else:
        return f"//div[contains(@class, 'react-datepicker__day--0" + f"{day_at_week.strftime('%d')}')]"

def generate_random_rent_time_xpath():
    return f"//div[contains(text(), '{random.choice(['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])}') and contains(@class, 'Dropdown-option')]"

def generate_random_color_xpath():
    return f"//label[contains(text(), '{random.choice(['чёрный жемчуг', 'серая безысходность'])}')]"

def generate_random_metro_station_xpath():
    return f"//li[@data-index='{random.randint(1, 8)}']"