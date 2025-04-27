import random
import string
from datetime import datetime, timedelta
from data import const


russian_letters = ''.join([chr(i) for i in range(1040, 1104)])

def strip_billet_locator(locator):
    start_index = locator.find('%billet%')
    first_part = locator[:start_index].strip()
    second_part = locator[start_index + len('%billet%'):].strip()
    return first_part, second_part

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

def generate_random_day_at_week(billet):
    method, locator = billet
    head, tail = strip_billet_locator(locator)
    day_at_week = datetime.now() + timedelta(random.randint(1, 6))
    if int(day_at_week.strftime('%d')) in range(1, 6) and int(datetime.now().strftime('%d')) > 6:
        return  method, head + f"{day_at_week.strftime('%d')}') " + tail
    else:
        return  method, head + f"{day_at_week.strftime('%d')}')]"

def generate_random_rent_time(billet):
    method, locator = billet
    head, tail = strip_billet_locator(locator)
    return method, head + f"{random.choice(const['RENT_TIME'])}" + tail

def generate_random_color(billet):
    method, locator = billet
    head, tail = strip_billet_locator(locator)
    return method, head + f"{random.choice(const['COLOR'])}" + tail

def generate_random_metro_station(billet):
    method, locator = billet
    head, tail = strip_billet_locator(locator)
    return method, head + f"{random.randint(1, 8)}" + tail
