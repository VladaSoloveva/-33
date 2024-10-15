"""Действующие данные для авторизации в системе"""
import os
from dotenv import load_dotenv
from faker import Faker
import string
load_dotenv()

fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()

valid_phone = os.getenv('phone')
valid_login = os.getenv('login')
valid_password = os.getenv('password')
invalid_ls = '352010007897'
valid_email = 'vc55598@bk.ru'
valid_pass_reg = '1234554321'

def generate_string_rus(n):
    return 'п' * n

def generate_string_en(n):
    return 'k' * n

def english_chars():
    return 'gkenlenvnejtnbgjlke'

def russian_chars():
    return 'влтилваилтшкеретады'

def chinese_chars():
    return '的一是不了人我在来以个中上们'

def special_chars():
    return f'{string.punctuation}'