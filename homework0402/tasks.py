# 1. Напишете програма, която намира детерминанта на дадена матрица.
# Създайте функция, която изчислява детерминантата на квадратна матрица.

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant_value = 0
    for j in range(n):
        cofactor = (-1) ** (0 + j) * determinant(get_minor(matrix, 0, j))
        determinant_value += matrix[0][j] * cofactor
    return determinant_value

def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

matrix = [
    [2, 3, -1],
    [4, 2, 5],
    [1, -3, 2]
]

print(determinant(matrix)) 

# 2. Използвайки NumPy, създайте два случайни многомерни масива и изведете техния елементарен продукт.
# Генерирайте два случайни NumPy масива и изведете техния елементарен (поелементен) продукт.

import numpy as np

array1 = np.random.random((3, 3))
array2 = np.random.random((3, 3))
print("Масив 1:")
print(array1)
print("\nМасив 2:")
print(array2)

elementwise_product = array1 * array2

print("\nЕлементарен продукт:")
print(elementwise_product)

# 3. Създайте NumPy масив от числа и намерете средното им.
# Създайте NumPy масив и използвайте вградените функции за намиране на средната стойност.

import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print(arr1.mean())

# 4. Използвайки NumPy, умножете два масива поелементно.
# Създайте два NumPy масива и умножете техните елементи поелементно.

import numpy as nm
ar1 = nm.array([1,2,3,4,5,6])
ar2 = nm.array([7,8,9,10,11,12])
print(nm.multiply(ar1,ar2))

# 5. Напишете функция, която извлича най-голямото число от NumPy масив.

import numpy as nm

ar1 = nm.array([1,2,3,4,5,6])
print(ar1.max())

# 6. Създайте случаен NumPy масив и изведете индекса на минималния елемент.

import numpy

ar1 = numpy.array([1,2,3,4,5,6])
print(ar1.min())

# 7. Заредете CSV файл в DataFrame и изведете първите 5 реда.
# - Използвайте библиотеката Pandas, за да заредите CSV файл в DataFrame и изведете първите 5 реда. (може да си свалите от интернет CSV file)

import pandas as pn

f = pn.read_csv("currency.csv")
f = pn.DataFrame(data=f)
print(f.iloc[:5])

# 8. Изчислете средната стойност на определена колона в DataFrame.
# - Използвайте Pandas, за да изчислите средната стойност на определена колона в DataFrame.

import pandas as pn

r = pn.read_csv("currency.csv")
r = pn.DataFrame(data=r)
print(r['Index'].mean())

# 9. Филтрирайте данните в DataFrame според определено условие.
# - Използвайте Pandas, за да филтрирате данните в DataFrame според определено условие.

f = pn.read_csv("currency.csv")
result = f.query('Index < 15')
print(result)

# 10. Добавете нова колона към DataFrame, базирана на стойности от друга колона.
# - Използвайте Pandas, за да добавите нова колона към DataFrame, която зависи от стойностите на друга колона.

f = pn.read_csv("currency.csv")
f["new"] = f['Company']
print(f['new'])

# 11 Използвайте функцията groupby върху DataFrame и изведете агрегирани стойности.

f = pn.read_csv("currency.csv")
print(f.groupby('Subscription Date').mean(numeric_only=True))

# 12 Имплементирайте стек със стандартни операции (push, pop).
# - Напишете клас или функции за стек с основните операции - добавяне и изваждане на елемент.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self,value):
        self.stack.pop(value)

    def show(self):
        # return enumerate(self.stack)
        result = [r for r in enumerate(self.stack)]
        print("Index, Value")
        print(*result, sep='\n')

stack = Stack()
stack.push(1)
print("push value '1' to stack")
stack.push(2)
print("push value '2' to stack")
stack.push(3)
print("push value '3' to stack")
stack.push(4)
print("push value '4' to stack")
stack.show()

stack.pop(1)
print("remove index '1'")
stack.show()

# 13. Напишете функция за обръщане на реда на елементите в стека.
# - Напишете функция, която обръща реда на елементите в стека, без да използвате допълнителен стек.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self,value):
        self.stack.pop(value)

    def show(self):
        return self.stack

    def reverse(self):
        self.stack.reverse()
        return self.stack

stack = Stack()
stack.push(1)
print("push value '1' to stack")
stack.push(2)
print("push value '2' to stack")
stack.push(3)
print("push value '3' to stack")
stack.push(4)
print("push value '4' to stack")
print("Original stack: ", stack.show())
print("Reversed stack: ", stack.reverse())

# 14 Създайте опростена версия на опашка (queue) със стандартни операции (enqueue, dequeue).
# - Напишете клас или функции за опростена опашка с операции за добавяне и изваждане на елемент.

class Queque:
    def __init__(self):
        self.queque = []

    def enqueque(self, value):
        self.queque.append(value)

    def dequeque(self):
        self.queque.pop(0)

    def show(self):
        return self.queque

numbers = Queque()
numbers.enqueque(1)
numbers.enqueque(2)
numbers.enqueque(3)
print("Before: ")
print(numbers.show())
numbers.dequeque()
print("After: ")
print(numbers.show())

# 15. Създайте бинарно дърво и напишете функция за обхождане му в дълбочина (DFS).
# - Създайте бинарно дърво и напишете функция за обхождане му в дълбочина (DFS).

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(node):
    if node is not None:
        dfs(node.left)
        dfs(node.right)
        print(node.data)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

dfs(root)

# 16 Използвайки библиотеката NetworkX, създайте ориентиран граф и изведете неговите върхове и ребра. Използвайте също matplotlib.
# NetworkX е библиотека за работа с графи в Python. Тя предоставя инструменти за създаване, анализ и визуализация на графи.
# За да решите тази задача, трябва да инсталирате библиотеката (ако все още не сте го направили) и да я използвате за създаване на ориентиран граф.

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3), (3, 1) ])

print("Върхове: ", G.nodes())
print("Ребра: ", G.edges())
nx.draw(G, with_labels=True)
plt.show()