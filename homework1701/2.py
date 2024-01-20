# 2. Create a class called Integer. Upon initialization, it should receive a single parameter value (int).
# It should have 3 additional methods:
# • from_float(float_value) - creates a new instance by flooring the provided floating
# number. If the value is not a float, return the message "value is not a float"
# • from_roman(value) - creates a new instance by converting the roman number (as string) to
# an int
# • from_string(value) - creates a new instance by converting the string to an int (if the value
# cannot be converted, return a message "wrong type")

# TEST CODE:
# first_num = Integer(10)
# print(first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num.value)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))

# OUTPUT:
# 10
# 4
# "value is not a float"
# "wrong type"

import roman

class Integer:
    def __init__(self, value):
        self.value = value
    def from_float(float_value):
        if isinstance(float_value, float) == True:
            return "value is float"
        else:
            return "value is not a float"

    def from_roman(value):
        number = value.upper()
        try:
            return Integer(int(roman.fromRoman(number)))
        except:
            return Integer("Wrong number!!!")

    def from_string(value):
        value = str(value)
        try:
            return int(value)
        except:
            return "wrong type"
        
first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))