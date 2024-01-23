# 7. Достъп до елементи в низ
# Напишете програма, която инициализира низ и се опитва да достъпи символ на индекс 10. 
# Обработете IndexError и отпечатайте съобщение, което указва проблема.

def check(value):
    try:
        return value[10]
    except IndexError as e:
        return f"Error: {e}"

print(check("test"))

# 8. Въвеждане на Цяло Число
# Напишете програма, която подканва потребителя да въведе цяло число. 
# Обработете ValueError, ако потребителят въведе стойност, която не може да бъде конвертирана към цяло число

def number(value):
    try:
        return int(value)
    except ValueError as e:
        return f"Error: {e}"

print(number(input("Type a number: ")))

# 9. Конкатенация на Низове и Числа
# Напишете програма, която конкатенира низ и число. 
# Обработете TypeError, който може да възникне при опит за конкатенация на несъвместими типове.

def concat(value, value2):
    try:
        print(value + value2)
    except TypeError as e:
        print(f"Error: {e}")

concat("test", 66)

# 10. Валидация на Парола
# Напишете програма, която подканва потребителя да въведе парола.
# Използвайте try и except, за да обработите следните условия:
# •	Ако паролата е по-малко от 8 знака, предизвикайте грешка ValueError.
# •	Ако паролата не съдържа поне една цифра, предизвикайте грешка ValueError.
# •	Ако паролата не съдържа поне една главна буква, предизвикайте грешка ValueError.

import re
def pass_validate(password):
    def check_len(password):
        if len(password) >= 8:
            return check_upper(password)
        else:
            raise ValueError("Password is less than 8 characters!")
    def check_upper(password):
        if re.search("[A-Z]", password):
            return check_numbers(password)
        else:
            raise ValueError("Password must contain uppercase letters!")
    def check_numbers(password):
        if re.search("[0-9]", password):
            return True
        else:
            raise ValueError("Password must contain a numbers!")
    try:
        return check_len(password)
    except ValueError as e:
        return f"Error: {e}"

print(pass_validate(input("password: ")))

# 11. Делене на Двe Числа
# Напишете програма, която приема две числа като вход и изчислява резултата 
# от делението на първото число на второто.
# Обработете и ValueError (за нечислови входове) и ZeroDivisionError.

num1 = input("Number 1: ")
num2 = input("Number 2: ")
def calc(a, b):
    if not a.isnumeric() or not b.isnumeric():
        raise ValueError(f"Value '{a}' is not a number!" if not a.isnumeric() else f"Value '{b}' is not a number!")
    elif int(b) == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    else:
        return int(a) / int(b)
try:
    print(calc(num1, num2))
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

