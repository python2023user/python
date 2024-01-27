# 1. Инсталиране и използване на библиотеката requests:
# Задача: Използвайте requests за изтегляне на съдържанието на уебстраница
# и отпечатване на HTML кода на конзолата.

import requests

response = requests.get('https://news.bg')
if response.status_code == 200:
    print(response.content)

# 2. Разликата между пълно и частично импортиране:
# Задача: Импортирайте модула math цялостно и след това само
# функцията sqrt от него.
# Използвайте и двете за изчисляване на квадратен корен.

import math
from math import sqrt

print(math.sqrt(16)) # Цялостно импортиране
print(sqrt(16)) # Импортиране само на функцията sqrt от библиотеката math

# 3.Работа с модули и класове:
# Задача: Дефинирайте клас Calculator с методи за
# основни математически операции и създайте
# инстанция на този клас, за да извършите изчисления.

class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
  
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

calculator = Calculator()
print(calculator.add(2, 3))
print(calculator.subtract(5, 2))
print(calculator.multiply(4, 6))  
print(calculator.divide(10, 2)) 

# 4.Използване на псевдоними (aliases):
# Задача: Импортирайте библиотеката datetime като dt и
# използвайте я, за да отпечатате текущата дата и час.

import datetime as dt

print(dt.datetime.now())

# 5. Използване на библиотеката os за взаимодействие с операционната система:
# Задача: Използвайте os за намиране на
# текущата работна директория и промяна на директорията.

import os

print(f"Текуща работна директория '{os.getcwd()}'")
new_directory_name = "New"
if os.path.exists(os.getcwd() + "\\" + new_directory_name):
    print("Новата директория е вече създадена!")
else:
    new_directory = os.makedirs(new_directory_name)
    print(f"Създадена е нова директория '{os.getcwd()}\\{new_directory_name}'")
os.chdir(os.getcwd() + "\\" + new_directory_name)
print(f"Новата работна директория е променена на '{os.getcwd()}'")

print("Желаете ли да се върнете в предишната директория и да изтриете текущата: yes/no?")
request = input().lower()
if request == "yes":
    os.chdir('..')
    os.removedirs(new_directory_name)
    print(f"Новата директория е изтрита.\nТекуща работна директория '{os.getcwd()}'\nКрай на програмата!")
elif request == "no":
    print("Край на програмата!")
else:
    print("Невалиден избор! Край на програмата!")

# 6. Използване на библиотеката random за генериране на случайни числа:
# Задача: Използвайте random за генериране на 5 случайни числа между 1 и 10 и ги отпечатайте.

import random

i = 1
while i <= 5:
    print(random.randrange(1, 11))
    i += 1
