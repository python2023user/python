#method 1
num = input("Enter number:")
try:
    num = int(num)
except:
    print(f"The value cannot be int {num}! Exiting...")
    exit()

if type(num) != bool:
    if num % 3 == 0 or num % 5 == 0:
         print(f"The number '{num}' is correct!")
    else:
         print(f"The number '{num}' is incorrect!")
else:
    print(f"The value is boolean {num}! Exiting...")
    exit()

#method 2

num = input("Enter number: ")

if num.isnumeric():
    num = int(num)
else:
    print(f"The value '{num}' cannot be int! Exiting...")
    exit()

print((type(num) != bool) and ((num % 3 == 0 or num % 5 == 0) and f"The number '{num}' is correct!" or f"The number '{num}' is incorrect!") or f"'{num}' is boolean!")
