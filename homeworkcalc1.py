
inpt = input("Operation (example: 3 + 5): ")
inpt2 = inpt.split(" ", 1)
drop = inpt2[1].split(" " , 1)
op = drop[0]
inpt = inpt.split(op, 1)
first = int(inpt[0])
second = int(inpt[1])
if op == "+": result = first + second
if op == "-": result = first - second
if op == "/": result = first / second
if op == "*": result = first * second
print(first, op, second, "=", int(result))