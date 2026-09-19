import random
import string


def generate_email():
    login = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"{login}@yandex.ru"


def generate_password(length=10):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_name():
    return "Тестовый" + "".join(random.choices(string.digits, k=4))


def generate_login():
    return generate_email()