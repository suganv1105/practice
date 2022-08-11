class emp1:
    print("welcome")
    print("oops concept")
    print("HI")

class emp2:
    pass

class employee:
    name='xyz'
    ID=1234
    def printemp(self):
        print(self.name)
        print(self.ID)

e=employee()
e.printemp()
print(e.name)
print(e.ID)
print(employee.name)
print(employee.ID)

class ConstructExample:
    def _init_(self, id, name):
        print('-------------')
        self.id = id
        self.name = name
        print(self.id)
        print(self.name)


c = ConstructExample(2, 'sugan')
d = ConstructExample(3, 'mark')


#-------------------------------------------------------------------------------------
class Header:
    def _init_(self):
        print("welcome to student program")
        print('----------------')
class Footer:
    def _init_(self):
        print('-----------------')
class Student:
    def _init_(self, id, name):
        self.id = id
        self.name = name
    def printmess(self):
        print(f"id={self.id} and name={self.name}")
h = Header()
s1 = Student(1, 'sugan')
s1.printmess()
f = Footer()

h1 = Header()
s2 = Student(2, 'gopi')
s2.printmess()
f1 = Footer()

# ----------------------------------------------------------------------------------
class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()

# -----------------------------------------------------------------------------------
# Python program to understand the classmethod

class Student:
    # create a variable

    name = "Geeksforgeeks"

    # create a function

    def print_name(obj):
        print("The name is : ", obj.name)

    # create print_name classmethod

# before creating this line print_name()
# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()
# ----------------------------------------------------------------------------------------
# Python program to demonstrate
# use of a class method and StaticMethod.

from datetime import date


class Person:

    def _init_(self, name, age):
        self.name = name

        self.age = age

        # a class method to create a

    # Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
person.display()
# -----------------------------------------------------------------------------------------------