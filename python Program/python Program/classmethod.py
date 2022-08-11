# Python Class Method

class Employee:
    company = 'Tutorial python'

    @classmethod
    def message(cls):
        print('The Message is From %s Class' % cls.__name__)
        print('The Company Name is %s' % cls.company)


Employee.message()
Employee().message()  # Other way of calling classmethod


print('----------')

class Employee:
    value = 100

    def printValue(cls):
        print('The Value = %d' % cls.value)


Employee.printValue = classmethod(Employee.printValue)
Employee.printValue()


print('----------')

class Employee:
    company = 'Tutorial python'

    @classmethod
    def message(cls):
        print('The Company Name is %s' % cls.company)
        print('The Message is From %s Class' % cls.__name__)
        cls.func_msg()

    @staticmethod
    def func_msg():
        print("Welcome to Python Programming")


Employee.message()

print('----------')


class Employee:
    company = 'Tutorial python'

    @staticmethod
    def add(a, b, c):
        return a + b + c

    @classmethod
    def avg(cls):
        x = cls.add(10, 20, 40)
        return (x / 3)


average = Employee.avg()
print('The Average Of three Numbers = ', average)

print('----------')


class Employee:
    company = 'Tutorial python'

    @classmethod
    def func_newName(cls, new_Name):
        cls.company = new_Name


emp = Employee()

print(Employee.company)
print(emp.company)

print('----------')
Employee.func_newName('Python')

print(Employee.company)
print(emp.company)

print('----------')



class Employee:

    def __init__(self, fullname, age, gender, salary):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.salary = salary

    @classmethod
    def func_string_split(cls, employee_str):
        fullname, age, gender, salary = employee_str.split('-')
        return cls(fullname, age, gender, salary)


emp_from_csv1 = 'Suresh-27-Male-120000'
emp_from_csv2 = 'John-29-Male-100000'
emp_from_csv3 = 'Tracy-25-Female-155000'

emp1 = Employee.func_string_split(emp_from_csv1)
print(emp1.fullname)
print(emp1.gender)
print(emp1.salary)
print(emp1.age)

print('----------')
emp3 = Employee.func_string_split(emp_from_csv3)
print(emp3.fullname)
print(emp3.gender)
print(emp3.age)


class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string_to_Date(cls, string_Date):
        day, month, year = map(int, string_Date.split('-'))
        return cls(day, month, year)


dt = Date.string_to_Date('31-12-2018')
print(dt.day)
print(dt.month)
print(dt.year)
