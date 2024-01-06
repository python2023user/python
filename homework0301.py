#1 Напишете функция, която получава три числа (int) и връща (return) най-малкото.
# • Принтирайте резултата на конзолата.
# • Използвайте подходящо име за функцията.

def get_min_number(a,b,c):
    return min(a,b,c)

a = int(input("Num 1: "))
b = int(input("Num 2: "))
c = int(input("Num 3: "))

print(get_min_number(a,b,c))

# 2 Напишите програма, която ще получава три цели числа от тип int.
# Направете следните функции:
# • sum_numbers(), която ще връща return сборът на първите две цели числа.
# • substract(), която ще връща разликата от върнатата стойност на първите две цели
# числа и третото число.
#
# Обединете двете функции в една главна с име add_and_subtract(), която ще
# получава трите цели числа като параметри.
# Принтирайте резултата на функцията subtract() на конзолата.

def sum_numbers(a, b):
    result = a + b
    return result

def substract(a, b):
    result = a - b
    return result

def add_and_subtract():
    a = int(input("Num 1: "))
    b = int(input("Num 2: "))
    c = int(input("Num 3: "))
    print(substract(sum_numbers(a,b), c))

add_and_subtract()

# 3 Напишите програма, която получава последователност от цели числа, разделени
# от празно място (single space).
# • Принтирайте лист само от четните числа (even numbers).
# • Използвайте filter()

def even_sort(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def result():
    numbers = input("Numbers: ")
    numbers = [int(num) for num in numbers.split(" ") if num and num.lstrip("-").isdigit()]
    if numbers == []:
        print("No numbers in this list! Process terminated!")
        exit()
    evens = filter(even_sort, numbers)
    return [even for even in evens]

print(result())

# 4 Напишите програма, която получава последователност от цели числа, разделени
# от празно място (single space).
# • Принтирайте сортиран (sorted) лист от числа във възходящ ред (ascending order).
# • Използвайте sorted()

def num_sorter():
    numbers = input("Numbers: ")
    numbers = [int(num) for num in numbers.split(" ") if num and num.lstrip("-").isdigit()]
    if numbers == []:
        print("No numbers in this list! Process terminated!")
        exit()
    return sorted(numbers)

print(num_sorter())

# 5 Напишите програма, която получава лист от цели числа, разделени от празно
# място (single space).
# • Принтирайте минималната и максималната стойност на дадените числа, както
# и сумата на всички цели числа от листа.
#
# - "The minimum number is {minimum number}“
# - "The maximum number is {maximum number}“
# - "The sum number is: {sum of all numbers}“
#
# • Използвайте min(), max() и sum().

def num_calcs(numbers):
    nums = [int(num) for num in numbers.split(" ") if num and num.lstrip("-").isdigit()]
    if nums == []:
        print("No numbers in this list! Process terminated!")
        exit()
    print(f"The minimum number is {min(nums)}\nThe maximum number is {max(nums)}\nThe sum number is: {sum(nums)}")

num_calcs(input("Type numbers: "))