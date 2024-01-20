from person import Person
from employee import Employee
class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

x = Teacher()
print(x.get_fired())
print(x.sleep())
print(x.teach())