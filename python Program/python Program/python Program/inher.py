class Employee:
    pass
class Department(Employee):
    pass

print('--------------')
class Employee:
    x = 10
    def func_msg(self):
        print('Welcome to Employee Class')


class Department(Employee):
    a = 250
    def func_message(self):
        print('Welcome to Department Class')
        print('This class is inherited from Employee')


emp = Employee()
print(emp.x)
emp.func_msg()

print('--------------')
dept = Department()
print(dept.a)
dept.func_message()
print('--------------')


class Employee:
    def func_msg(self):
        print('Welcome to Employee Class')


class Department(Employee):
    pass


emp = Employee()
emp.func_msg()
dept = Department()
dept.func_msg()  # Calling Parent Method
print('--------------')

class Employee:
    x = 10

    def func_msg(self):
        print('Welcome to Employee Class')


class Department(Employee):
    a = 250
    b = Employee.x + 22

    def func_message(self):
        print('Welcome to Department Class')

    def func_changed(self):
        print('New Value = ', Employee.x + 449)


emp = Employee()
print(emp.x)
emp.func_msg()

print('--------------')
dept = Department()
print(dept.a)
print(dept.b)
dept.func_message()
dept.func_changed()

print('--------------')
class Employee:

    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income

    def func_msg(self):
        print('Welcome to Employee Class')

    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)


class Department(Employee):
    pass


emp = Employee('Suresh', '27', '650000')
emp.func_msg()
emp.func_information()
dept = Department('Jenny', '25', '850005')
dept.func_msg()  # Calling Parent Method func_msg(self)
dept.func_information()  # Calling Parent Method func_information(self)
print('--------------')


class Employee:

    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income

    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)


class Department(Employee):

    def __init__(self, fullname, age, income):
        Employee.__init__(self, fullname, age, income)


emp = Employee('John', '27', '650000')
emp.func_information()
dept = Department('Jenny', '25', '850005')
print(dept.fullname)
dept.func_information()
print('--------------')


class Employee:

    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income

    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)


class Department(Employee):

    def __init__(self, fullname, age, income, dept_name):
        Employee.__init__(self, fullname, age, income)
        self.dept_name = dept_name

    def func_info(self):
        print(self.fullname, self.age, 'Working as a',
              self.dept_name, 'is earning', self.income)


emp = Employee('John', '27', '650000')
emp.func_information()
dept = Department('Jenny', '25', '850005', 'Developer')
dept.func_information()
dept.func_info()
print('--------------')


class MainClass:

    def func_message(self):
        print('Welcome to Main Class')


class Child(MainClass):

    def func_child(self):
        print('Welcome to Child Class')
        print('This class is inherited from Main Class')


class ChildDerived(Child):

    def func_Derived(self):
        print('Welcome to Derived Class')
        print('This class is inherited from Child Class')



chldev = ChildDerived()
chldev.func_Derived()
chldev.func_child()
chldev.func_message()
print('------------')


class MainClass1:

    def func_main1(self):
        print('This Welcome Message is from Main Class 1')


class MainClass2:

    def func_main2(self):
        print('This is an another Message coming from Main Class 2')


class ChildClass(MainClass1, MainClass2):

    def func_child(self):
        print('This is coming from Child Class')


chd = ChildClass()
chd.func_main1()
chd.func_main2()
chd.func_child()


class Employee:

    def func_message(self):
        print('Welcome to Employee Class')


class Department(Employee):

    def func_message(self):
        print('Welcome to Department Class')
        print('This class is inherited from Employee')


emp = Employee()
emp.func_message()
dept = Department()
dept.func_message()
print('------------')


class MainClass:

    def func_message(self):
        print('Welcome to Main Class')


class Child(MainClass):

    def func_child(self):
        print('This class is inherited from Main Class')


class ChildDerived(Child):

    def func_Derived(self):
        print('This class is inherited from Child Class')


print(issubclass(ChildDerived, Child))
print(issubclass(ChildDerived, MainClass))

print('------------')
print(issubclass(Child, MainClass))

print('------------')
print(issubclass(Child, ChildDerived))


class MainClass:

    def func_message(self):
        print('Welcome to Main Class')


class Child(MainClass):

    def func_child(self):
        print('This class is inherited from Main Class')


class ChildDerived(Child):

    def func_Derived(self):
        print('This class is inherited from Child Class')


mn = MainClass()
print(isinstance(mn, MainClass))

print('------------')
chd = Child()
print(isinstance(chd, Child))
print(isinstance(chd, MainClass))
print(isinstance(chd, ChildDerived))

print('------------')
dev = ChildDerived()
print(isinstance(dev, ChildDerived))
print(isinstance(dev, Child))
print(isinstance(dev, MainClass))


class Employee:

    def message(self):
        print('This message is from Employee Class')


class Department(Employee):

    def message(self):
        print('This Department class is inherited from Employee')


class Sales(Employee):

    def message(self):
        print('This Sales class is inherited from Employee')


emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()

print('------------')
sl = Sales()
sl.message()


class Employee:

    def add(self, a, b):
        print('The Sum of Two = ', a + b)


class Department(Employee):

    def add(self, a, b, c):
        print('The Sum of Three = ', a + b + c)


emp = Employee()
emp.add(10, 20)

print('------------')
dept = Department()
dept.add(50, 130, 90)
