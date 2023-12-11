#1 Напишете програма, която при въведен ден, месец и година проверява дали датата е валидна.
# method 1
# dm = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# datecheck = input("DD/MM/YYYY: ").split("/")
# d = int(datecheck[0])
# m = int(datecheck[1])
# y = int(datecheck[2])
# if (1 <= d <= 31) and (1 <= m <= 12):
#     if d <= dm[m]:
#         if d == 29 and m == 2:
#             if y % 4 == 0 or y % 400 == 0 and y % 100 != 0:
#                 print("Валидна дата")
#                 exit()
#             else:
#                 print("Невалидна дата")
#                 exit()
#         print("Валидна дата")
#     else:
#         print("Невалидна дата")
# else:
#     print("Невалидна дата")

# method 2

import datetime
checkd = input("DD/MM/YYYY: ").split("/")
d = int(checkd[0])
m = int(checkd[1])
y = int(checkd[2])
try:
    dcheck = datetime.datetime(y,m,d)
    print("Валидна дата")
except:
    print("Невалидна дата")

#2 Напишете програма, която генерира 100 текстови файла, които имена започват със случайни цифри между 1 и 9. След като
# сте ги генерирали създайте 9 папки наименувани с цифри между 1 и 9 и преместете всички файлове започващи със
# съответната цифра в съответната папка и накрая принтирате на конзолата струкурата, която се е получила. При
# приключване на програмата изтрийте всички генерирани файлове и папки.

import os
import random
import shutil
x = 1
l = []
while (x <= 100):
   n = random.randrange(1, 10)
   a = random.randrange(ord("a"),ord("z")+1)
   b = random.randrange(ord("A"),ord("Z")+1)
   c = random.randrange(ord("a"),ord("z")+1)
   d = random.randrange(ord("A"),ord("Z")+1)
   fname = str(n) + chr(a) + chr(b) + chr(c) + chr(d) + ".txt"
   l.append(fname)
   with open(fname, 'w') as f:
        f.write(fname)
        f.close()
   x += 1
print("100 файла са създадени...")

for x in range(1,10):
  if not os.path.exists(f"{str(x)}"):
     os.makedirs(f"{str(x)}")
print("9 папки са създадени...")

for fl in l:
    nf = str(fl[0])
    os.rename(f"{fl}", f"{nf}/{fl}" )
print("Файловете са преместени...")

for x in range(1,10):
    if os.path.exists(str(x)):
        shutil.rmtree(str(x))
    else:
        print(f"Грешка: Папка '{x}' не съществува!")

print("Всички файлове и папки са изтрити. Край на програмата!")