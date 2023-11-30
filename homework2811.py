#1

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
if num1 >= num2:
    print(num1)
else:
    print(num2)

#2

age = int(input("Age: "))
gndr = input("Gender: ")

if gndr == "m":
    if age >= 16:
        print("Hello Mr. How are you today?")
    else:
        print("Hello Master. How are you today?")
if gndr == "f":
    if age >= 16:
        print("Hello Ms. How are you today?")
    else:
        print("Hello Miss. How are you today?")

#3

num = int(input("Number: "))
numstat = num % 2 == 0
if numstat == True:
    print(f"{num} -> even")
if not numstat == True:
    print(f"{num} -> odd")

#4

days = {"Monday":12, "Thuesday": 12, "Wednesday":14, "Thursday":14, "Friday":12, "Saturday":16, "Sunday":16}
day = str(input("Enter day: ")).title()
if day in days.keys():
    print(f"The price for {day} is {days.get(day)}.")
else:
    print(f"Incorrect day: \'{day}\'")


#######################################
#5 method 1

def tstat(time):
    if time == 1: return "time"
    return "times"

dayscount = {"Monday":0, "Thuesday": 0, "Wednesday":0, "Thursday":0, "Friday":0, "Saturday":0, "Sunday":0}
print("Number -> day:")
for d in dayscount.keys():
    print(f"{list(dayscount).index(d) + 1} -> {d}")

Nstart = 0
Nmax = 15
# Nmax = int(input("Enter limit: "))
while True:
    N = input("Enter number [1-7]: ")
    if bool(N) == False or int(N) == 0:
        print("Empty request! Process terminated!")
        break
    N = int(N)
    Nstatus = N <= 7
    if Nstatus:
        cday = list(dayscount)[N - 1]
        dayscount[cday] += 1
        Nstart += 1
        # print(f"{Nstart}/{Nmax} {cday} - {dayscount[cday]} {tstat(dayscount[cday])} ")
    else:
        print(f"Incorrect day: \'{N}\'! Process terminated!")
        break
    if Nstart == Nmax:
        print(f"Inputing complete after {Nstart} {tstat(Nstart)}.")
        for d in dayscount.keys():
            print(f"{d} - {dayscount.get(d)} {tstat(dayscount.get(d))}")
        break


#######################################
#5 method 2

def tskin(time):
    if time == 1: return "time"
    return "times"

days = {"Monday":0, "Thuesday": 0, "Wednesday":0, "Thursday":0, "Friday":0, "Saturday":0, "Sunday":0}
print(", ".join(list(days)))
N = 0
Nmax = 15
# Nmax = int(input("Enter limit: "))
while True:
     day = str(input("Enter day: ")).title()
     if bool(day) == False:
         print("Empty request! Process terminated!")
         break
     if day in days.keys():
         days[day] += 1
         N += 1
        #  print(f"{N}/{Nmax} {day} - {days[day]} {tskin(days[day])}")
     else:
         print(f"Incorrect day: \'{day}\'! Process terminated!")
         break
     if N == Nmax:
         print(f"Inputing complete after {N} {tskin(N)}.")
         for d in days.keys():
             print(f"{d} - {days.get(d)} {tskin(days.get(d))} ")
         break
     