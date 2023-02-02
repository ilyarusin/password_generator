# Генератор безопасных паролей

from random import *

# Строковые константы:
DIGITS = '0123456789'
LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_CASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''  # Переменная, содержащая все символы

passwords_amount = int(input('Введите сколько нужно паролей для генерации: '))
password_lenght = int(input('Введите длину пароля: '))
password_with_nums = input('Будет ли пароль включать цифры 0123456789 ? (Да/Нет) ').strip()
password_with_upper_case = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (Да/Нет) ').strip()
password_with_lower_case = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? (Да/Нет) ').strip()
password_with_special_chars = input('Включать ли символы !#$%&*+-=?@^_  ? (Да/Нет) ').strip()
password_with_excluded_chars = input('Исключать ли неоднозначные символы il1Lo0O ? (Да/Нет)  ').strip()

if password_with_nums in ('Да', 'да', 'д'):
    chars += choice(DIGITS)
if password_with_upper_case in ('Да', 'да', 'д'):
    chars += choice(UPPER_CASE_LETTERS)
if password_with_lower_case in ('Да', 'да', 'д'):
    chars += choice(LOWER_CASE_LETTERS)
if password_with_special_chars in ('Да', 'да', 'д'):
    chars += choice(PUNCTUATION)
if password_with_excluded_chars in ('Да', 'да', 'д'):
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, characters):
    password = ''
    for k in range(password_lenght):
        password += choice(chars)
    return password

for _ in range(passwords_amount):
    print(generate_password(password_lenght, chars))