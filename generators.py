import random
import string

def generate_login():
    random_number = random.randint(1000, 999999)
    return f'{random_number}@yandex.ru'

def generate_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))