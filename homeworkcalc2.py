operation = input('operation (+, -, /, *): ')
first = int(input('number1: '))
second = int(input('number2: '))
if operation == "+": result = first + second
if operation == "-": result = first - second
if operation == "/": result = first / second
if operation == "*": result = first * second
print(first, operation, second, "=", int(result))