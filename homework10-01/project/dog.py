from animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."

x = Dog()

print(x.eat())
print(x.bark())