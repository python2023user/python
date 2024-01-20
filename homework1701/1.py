#1 1. Create a class called Calculator that has the following static methods:
# • add(*args) - sums all the arguments passed to the function and returns the result
# • multiply(*args) - multiplies all the numbers and returns the result
# • divide(*args) - divides all the numbers (starting from the first one) and returns the result
# • subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result

# TEST CODE:
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

# OUTPUT:
# 19
# 30
# 50.0
# 70

class Calculator:
    def add(*args):
        return sum(args)

    def multiply(*args):
        result = 1
        for num in args:
            result = num * result
        return result
    def divide(*args):
        result = None
        for num in range(1,len(args)):
            if result == None:
                result = args[num - 1] / args[num]
            else:
                result = result / args[num]
        return result

    def subtract(*args):
        result = None
        for num in range(1, len(args)):
            if result == None:
                result = args[num - 1] - args[num]
            else:
                result = result - args[num]
        return result




print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))