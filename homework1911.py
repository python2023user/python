# 1

a = 16                   # int
b = 2.4                  # float
result = a // b          
print(result)            # float

result = int(result)     
print(result)            # int

# 2

fname = "Georgi\n"
sname = "Krastev\n"
lname = "Krastev"

print(fname, sname, lname)

# 3

a_arr = ["BMW", "Audi", "Lada", "Mercedes"]
print(a_arr[-2:]) 

# 4

a_dict = {"car1":"BMW", "car2":"Audi", "car3":"Lada", "car4":"Mercedes"}
last2 = list(a_dict)[-2:]
print(a_dict[last2[0]] + " " + a_dict[last2[1]]) 