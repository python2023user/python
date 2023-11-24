#1

a = int(input("a = "))
b = int(input("b = "))
area = a * b
print(area)


#2

name = input("Name: ")
print("Hello " + name + "!")


#3

first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
town = input("Town: ")
print(f"You are {first_name} {last_name}, a {age} - years old person from {town}.")


#4

date = input("Date (DD/MM/YYYY): ")
date = date.split("/")
d = int(date[0])
m = int(date[1])
y = int(date[2]) + 1
print(f"{d}/{m}/{y}")


#5

a = 5
b = 21
c = 23
l = []
l.append(a)
l.append(b)
l.append(c)
print(sum(l))


#6

a_list = [12, 3242, 5123, 624, 12, 1, 4213, 51]
result = sum(a_list)
print(result)