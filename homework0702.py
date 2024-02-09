# 1. Сортиране - Bubble Sort: Имплементирайте алгоритъм за Bubble
# Sort и тествайте със списък от цели числа.

def bubble_sort(f):
    for _ in range(len(l)-1):
        for n in range(len(l)-1):
            if f[n] > f[n + 1]:
                f[n], f[n+1] = f[n+1], f[n]
    return f
l = [3, 1, 5, 15, 8, 6, 7, 2, 4, 11, 9, 14, 10, 13, 12]
print(bubble_sort(l))

# 2. Selection Sort: Имплементирайте алгоритъма за сортиране
# Selection Sort

def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

l = [3, 1, 5, 15, 8, 6, 7, 2, 4, 11, 9, 14, 10, 13, 12]
print(selection_sort(l))

# 3. Insertion Sort: Създайте функция, която използва алгоритъма
# Insertion Sort за сортиране на масив от числа.

def Insertion_Sort(f):
    for i in range(1, len(l)):
        value = l[i]
        j = i - 1
        while j >= 0 and l[j] > value:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = value

    return l

l = [3, 1, 5, 15, 8, 6, 7, 2, 4, 11, 9, 14, 10, 13, 12]
print(Insertion_Sort(l))

# 4. Binary search. Имлементирайте Binary search алгоритъм за
# намиране дали дадено число съществува в даден лист. За целта си
# създайте масив от 100 елемента със случайни числа и друго
# случайно число, което да търсите в масива.

import random
def binary_search(l,i):
    if len(l) == 1:
        if l[0] == i:
            return True
        else:
            return False
    elif l[len(l)//2] == i:
        return True
    elif l[len(l)//2] < i:
        return binary_search(l[len(l)//2:], i)
    elif l[len(l)//2] > i:
        return binary_search(l[:len(l) // 2], i)
x = []
for i in range(1,101):
    x.append(random.randrange(1,1001))
x.sort()
search_number = random.randrange(1,1001)
print(f"Binary search for {search_number}, status: {binary_search(x,search_number)}")