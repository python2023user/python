#1. Напишете програма, която чете число n, въведено от потребителя и отпечатва числата от 1 до n през 3.
# • Прочетете входните данни от конзолата – едно цяло число n
# • Направете for цикъл от 1 до n (включително) и задайте стъпка 3. Това означава, че при
# всяка итерация на цикъла, променливата i ще увеличава стойността си с 3, вместо с 1.
# Принтирайте променливата при всяка итерация.

n = int(input("Number: "))
for x in range(1, n + 1, 3):
    print(x)

#2. Напишете програма, която чете цяло положително число n, въведено от потребителя и
# печата числата от n до 1 в обратен ред. Въведеното число n, винаги ще бъде по-голямо от 1.
# • Прочетете едно цяло число от конзолата – броят на числата, които предстои да бъдат въведени
# • Направете for цикъл от n до 0, като намалявате променливата i с 1 при всяка итерация и
# я принтирате.

n = int(input("Number: "))
for x in range(n):
    print(n)
    n -= 1

#3. Напишете програма, която чете текст (стринг), въведен от потребителя и печата всеки символ от
# текста на отделен ред.
# !!! За да итерира for цикълът през въведената дума на мястото на фунцията range(), използвайте директно
# променливата, в която преди това сте записали входа от конзолата.

s = input("String: ")
for x in s:
    print(x)

#4. Напишете програма, която отпечатва числата в диапазона от 1 до 1000, които завършват на 7.
# • Едно число завършва на 7, когато резултатът от модулното деление на числото и 10 е равен на 7
# • Направете for цикъл от 1 до 1000 и проверете за всяко число дали завършва на 7.
# Изпълнилите условието числа принтирайте на конзолата
# • Можете да използвате и цикъл със стъпка 10
# method 1
    
for x in range(1, 1001):
    if x % 10 == 7:
        print(x)

# method 2 
        
for x in range(1, 1001):
    if x == 7:
        for i in range(x, 1001, 10):
           print(i)      

#5. Да се напише програма, която чете n-на брой цели числа, подадени от потребителя и
# проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
# • Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# • Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

n = int(input("Num limit: "))
i = 1
numlist = []
while i <= n:
    numlist.append(int(input(f"Enter number {i} of {n}: ")))
    i += 1
evens = []
odds = []
for x in range(1, len(numlist)):
    if x % 2 == 0:
        evens.append(numlist[x])
    else:
        odds.append(numlist[x])
evoddl = [sum(evens), sum(odds)]

if sum(evens) - sum(odds) == 0:
    print(f"Yes\nSum = {sum(evens)}")
else:
    print(f"No\nDiff = {max(evoddl) - min(evoddl)}")