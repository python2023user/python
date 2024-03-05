# 1. Тестване на Функция за Събиране - Напишете функции add(a, b),
# substract(a,b). Създайте тестове с pytest или unittest, които проверяват
# функциите

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

# 2.Тестване на Валидация на Е-мейл - създайте функция
# is_valid_email(email), която проверява дали даден стринг е валиден е-мейл
# адрес. Напишете тестове, които проверяват функционалността на
# функцията с валидни и невалидни е-мейл адреси.

def is_valid_email(email):
    if '@' in email and '.' in email.split('@')[1]:
        return True
    else:
        return False

# print(is_valid_email('someabv.bg'))

# 3. Mocking на Системно Време - Имате функция is_weekend(), която
# проверява дали текущата дата е събота или неделя. Използвайте
# unittest.mock за симулиране на различни дати и
# напишете тестове, които проверяват дали функцията
# правилно идентифицира уикендите.

import datetime
def is_weekend():
    d = datetime.datetime.today()
    current_day = d.strftime("%A")
    if current_day == "Saturday" or current_day == 'Sunday':
        return True
    else:
        return False
