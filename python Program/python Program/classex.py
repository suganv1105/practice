class Sample:
    print("welcome")

obj1=Sample()
obj2=Sample()



class Employee:
    company = 'Besant tech'
 
emp = Employee()
print(emp.company)
 
print("-------------")
print(Employee.company)



class Employee1:
    company = 'Tutorial phython'
 
    def func_message(self):
        print('Welcome to Python Programming')
 
emp = Employee1()
print(emp.company)
emp.func_message()
 
print("-------------")
print(Employee1.company)
print(Employee1.func_message)

class Employee3:
    company = 'Tutorial phython'

    def __init__(self):
        print('Hello World')
 
    def func_message(self):
        print('Welcome to Python Programming')
 
emp1 = Employee3() # Created an Instance
 
print(emp1.company)
emp1.func_message()

class Employee4:
    company = 'Tutorial besant'
 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print('Welcome to Python Programming')
 
emp1 = Employee4('Mike', 25, 'Male') 

print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)

class Employee5:
    company = 'Tutorial phython'

    def __init__(self, n, a, gen):
        self.name = n
        self.age = a
        self.gender = gen

    def func_message(self):
        print('Welcome to Python Programming')

emp1 = Employee5('Johnson', 29, 'Male')
 
print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)

class Employee6:
    company = 'Tutorial phtyon'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print('Welcome to Python Programming')
 
emp1 = Employee6('Mike', 25, 'Male')
print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
 
print()
emp2 = Employee6('Tracy', 27, 'Female')
print(emp2.company)
emp2.func_message()
print(emp2.name)
print(emp2.age)
print(emp2.gender)


class Employee7:
    company = 'Tutorial pthyon'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print(self.name + ' is learning Python Programming')
 
emp1 = Employee7('Mike', 25, 'Male')
print(emp1.company)
print(emp1.name) # Mike
print(emp1.age) #25
print(emp1.gender)
emp1.func_message()
 
print()
emp2 = Employee7('Tracy', 27, 'Female')
print(emp2.company)
print(emp2.name) #Tracy
print(emp2.age) # 27
print(emp2.gender)
emp2.func_message()


class Employee8:
    company = 'Tutorial python'
 
    def func_message(self):
        print('Welcome to Python Programming')
 
emp1 = Employee8()
emp2 = Employee8()
emp3 = Employee8()
 
emp2.company = 'Python'
emp3.company = 'Apple'
 
emp1.func_message()
 
print(emp1.company)
print(emp2.company)
print(emp3.company)
print(emp1.company)


class Employee9:
    company = 'Tutorial python'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print(self.name + ' is learning Python Programming')

emp1 = Employee9('Mike', 25, 'Male')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()
 
emp1.name = 'John'
print(emp1.name)
emp1.func_message()


class Employee10:
    company = 'Tutorial python'
 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print(self.name + ' is learning Python Programming')
 
emp1 = Employee10('John', 25, 'Male')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()
 
del emp1.name 
print(emp1.name)


class Employee11:
    company = 'Tutorial python'
 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print(self.name + ' is learning Python Programming')
 
emp1 = Employee11('John', 25, 'Male')
emp2 = Employee('Nancy', 27, 'Female')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()
 
del emp1.name
print(emp2.name)
print(emp1.name)


class Employee12:
    company = 'Tutorial python'
 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    def func_message(self):
        print(self.name + ' is learning Python Programming')
 
emp1 = Employee12('John', 25, 'Male')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()
 
del emp1
emp1.func_message()


