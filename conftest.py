import pytest
import random
import string

@pytest.fixture(scope='function')
def random_name():
    login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
    email_name= ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10)))
    email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
    return f"{login_name}@{email_name}.{email_domain}"

@pytest.fixture(scope='function')
def random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(6, 12)))
    return password

