# Упражнение 1: Създаване на клас
# Създайте клас наименуван Car със следните атрибути и методи:
# Атрибути:
# •	brand (низ)
# •	model (низ)
# •	year (цяло число)
# •	mileage (дробно число)
# Методи:
# •	__init__(self, brand, model, year, mileage): Метод-конструктор за инициализация на атрибутите.
# •	display_info(self): Метод за извеждане на информация за колата, включително бранда, модела, годината и пробега.

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        return f"Car: {self.brand}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage} km."

vw = Car("VW", "Passat", 2005, 190000)
print(vw.display_info())

# Упражнение 2: Наследяване
# Създайте детски клас ElectricCar, който наследява от класа Car.
# Добавете допълнителен атрибут battery_capacity (дробно число) към класа ElectricCar.
# Презаредете метода display_info, за да включите информация за капацитета на батерията.

class ElectricCar(Car):

    def __init__(self, brand, model, year, mileage, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(brand, model, year, mileage)
    def display_info(self):
        return f"Car: {self.brand}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage} km/\nBattery: {self.battery_capacity:.2f}%"


vw = ElectricCar("VW", "Passat", 2005, 190000, 40.00)
print(vw.display_info())

# Упражнение 3: Инкапсулация
# Създайте клас Person със следните частни атрибути:
# Атрибути:
# •	_name (низ)
# •	_age (цяло число)
# Добавете методи за получаване и задаване на стойностите на тези атрибути.

class Person:
    def __init__(self, name="default name", age="default age"):
        self.__name = name
        self.__age = age

    def set_name(self, newname):
        print(f"{self.__name} is changed to {newname}")
        self.__name = newname
    def set_age(self, newage):
        print(f"{self.__age} is changed to {newage}")
        self.__age = newage

    def get_name(self):
        print(f"Name: {self.__name}")

    def get_age(self):
        print(f"Age: {self.__age}")


x = Person()
x.set_name("Ivan")
x.set_age(34)
x.get_name()
x.get_age()

# Упражнение 4: Композиция
# Създайте клас Book със следните атрибути:
# Атрибути:
# •	title (низ)
# •	author (низ)
# Създайте още един клас Library, който съдържа списък от обекти от класа Book. 
# Добавете методи за добавяне на книга към библиотеката и извеждане на списъка с книги.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_object):
        self.books.append(book_object)
        print(f"Added {book_object.title} / {book_object.author}")

    def show_books(self):
        for bk in self.books:
            print(f"Title: {bk.title} - Author: {bk.author}")


b = Library()
book1 = Book("The Adventures of Huckleberry Finn", "Mark Twain")
b.add_book(book1)
book2 = Book("Treasure Island", "Robert Louis Stevenson")
b.add_book(book2)
book3 = Book("The Adventures of Tom Sawyer", "Mark Twain")
b.add_book(book3)

b.show_books()

# Упражнение 5: Полиморфизъм
# Създайте клас Shape с метод area. Създайте два подкласа, Circle и Rectangle, всеки със своята реализация на метода area.
# Демонстрирайте полиморфизма, като изчислите и изведете лицето на както кръг, така и правоъгълник, използвайки общ интерфейс.

class Shape:
    def area(self):
      pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    def area(self):
        print(f"{self.pi * (self.radius * self.radius)}")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print(f"{self.a * self.b}")

circle = Circle(5)
circle.area()

rectangle = Rectangle(34, 21)
rectangle.area()

# Упражнение 6: Инвентар на Продукти
# Клас Product (Продукт):
# •	Атрибути:
#  	name (име): Името на продукта.
#  	price (цена): Цената на продукта.
#  	quantity (количество): Количеството или наличност на продукта.
# •	Методи:
#  	display_info(): Показва информация за продукта, включително неговото име, цена и количество.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product: {self.name}\nPrice: {self.price} euro\nQuantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        i = 1
        for product in self.products:
            print(f"{i}. Product: {product.name} | Price: {product.price} euro | Quantity: {product.quantity} packs")
            i += 1

allproducts = Inventory()
product1 = Product("Salt", 0.60, 500)
allproducts.add_product(product1)
product2 = Product("Rice", 1.20, 150)
allproducts.add_product(product2)
product3 = Product("Sugar", 2.80, 80)
allproducts.add_product(product3)
product4 = Product("Bread", 1.50, 50)
allproducts.add_product(product4)
print(product3.display_info())
allproducts.display_inventory()