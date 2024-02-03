# 1. Фибоначи: Създайте рекурсивна функция, която изчислява n-
# тия елемент от редицата на Фибоначи.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Input 'n' = "))
print(f"Number {n} of Fibonacci is {fibonacci(n)}")

# 2. Сума на Числа: Създайте рекурсивна функция, която намира
# сумата на всички цели числа от 1 до n.

def numbers_sum(n):
    if n == 1:
        return n
    else:
        return n + numbers_sum(n - 1)

n = int(input("Number: "))
print(f"The sum of numbers to {n} is {numbers_sum(n)}")

# 3. Обръщане на Низ: Напишете рекурсивна функция, която
# обръща даден низ без да използва вградени функции.

def string_revers(value):
    if len(value) == 0:
        return value
    else:
        revers = value[0]
        return string_revers(value[1:]) + revers
string = "abcd"
print(f"Reversed '{string}': {string_revers(string)}")

# 4 Палиндром: Напишете рекурсивна функция, която проверява
# дали даден низ е палиндром (четене отпред назад и отзад
# напред дава еднакви резултати).

def palindrome_check(value):
    if len(value) <= 1:
        return True
    if value[0] != value[-1]:
        return False
    return palindrome_check(value[1:-1])

string = "abcdcba"
print(f"Polindrom check for '{string}': {palindrome_check(string)}")