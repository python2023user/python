import sqlite3

## 

con = sqlite3.connect("products.db")
cur = con.cursor()

##

# 1. Извличане на информация – направете таблицата с хранителни
# продукти "Products" с 10 артикула, които имат име и цена в лева. Напишете
# SQL заявка, която извлича имената и цените на всички продукти със
# стойност на цената над 50 лева.

cur.execute("CREATE TABLE IF NOT EXISTS Products (Name TEXT, Price FLOAT)")
l = [["Хляб", 1.50],["Ориз", 3.00],["Кашкавал", 120.00],["Сирене", 73.00],["Кисело мляко", 1.20],["Сушеница", 130.00],["Леща", 3.50],["Домати", 2.50],["Мед", 8.00],["Масло", 6.00]]

for x in l:
    product_status = cur.execute(f"SELECT * FROM Products WHERE Name = ?", (x[0],))
    row = product_status.fetchone()
    if row == None:
        cur.execute(f"INSERT INTO Products VALUES('{x[0]}', '{x[1]}')")
        con.commit()
        print(f"1. Добавен продукт {x[0]}, цена {x[1]:.2f} лв.")
    else:
        continue
l = cur.execute("SELECT * from Products WHERE price > '50'")
print("1. Продукти над 50 лв.:")
for x in l.fetchall():
    print(f"-> {x[0]} - {x[1]} лв.")

# 2. Добавяне на нов запис - Въведете нов продукт в таблицата
# "Products" със зададено име и цена.

product_name = input("Име на продукт: ")
product_price = float(input("Цена: "))

def add_product(name, price):
    cur.execute("SELECT * FROM Products WHERE Name = ?", (name,))
    row = cur.fetchone()
    if row is None:
        cur.execute(f"INSERT INTO Products VALUES('{name}', '{price}')")
        con.commit()
        print(f"2. Добавен е нов продукт {name} с цена {price:.2f} лв.")
    else:
        print("2. Този продукт е вече добавен!")
add_product(product_name, product_price)

# 3. Изтриване на запис: Изтрийте всички продукти от таблицата
#"Products", които са с цена под 20 лева.

cur.execute("DELETE from Products WHERE price < '20'")
con.commit()
print("3. Изтриване на всички продукти под 20 лв.")
l = cur.execute("SELECT * from Products")
print("3. Оставащи продукти:")
for x in l.fetchall():
    print(f"-> {x[0]} - {x[1]:.2f} лв.")

# 4. Филтриране и сортиране - извлечете имената и цените на
# продуктите от таблицата "Products", подредени в намаляващ ред
# по цената и филтрирани, така че да бъдат включени само тези
# с цена над 100 лева.

l = cur.execute("SELECT * from products WHERE Price > '100' Order by Price DESC")
print("4. Оставащи продукти с цена над 100 лв. в намаляващ ред:")
for x in l.fetchall():
    print(f"-> {x[0]} - {x[1]:.2f} лв.")

##

con.close()

##