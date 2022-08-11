def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


print(greet('Paul'))
print(greet.__doc__)


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        print('postive number')
        return num
    else:
        print('negative number')
        return -num


print(absolute_value(2))
print(absolute_value(-4))


def my_func():
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)

num1 = 10
num2 = 14
num3 = 12


def largest(x, y, z):
    if (x >= y) and (x >= z):
        largest = num1
    elif (y >= x) and (y >= z):
        largest = num2
    else:
        largest = num3
    return largest


x=largest(num1,num2,num3)
print('the largest value is ',x)
