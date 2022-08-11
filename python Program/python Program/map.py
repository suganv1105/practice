# Python map function
 
def addition(num):
    return num + num
 
numbers = [10, 20, 30, 40, 50]
 
map_result = map(addition, numbers)
print(list(map_result))

def addition(num):
    return num + num
 
chars = ['a', 'b', 'c', 'd', 'e']
numbers = [10, 20, 30, 40, 50]
 
map_result = map(addition, chars)
print('Chars List = ', list(map_result))
 
result = map(addition, numbers)
print('Numbers List = ', list(result))

def addition(a, b):
    return a + b
 
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [150, 250, 350, 450, 550]
 
map_result = map(addition, numbers1, numbers2)
print(list(map_result))
 
fruits1 = ['apple', 'orange', 'kiwi']
fruits2 = ['banana', 'cherry', 'berry']
 
result = map(addition, fruits1, fruits2)
print(list(result))



import math
 
def factorial_func(num):
    return math.factorial(num)
 
def len_func(x):
    return len(x)
 
numbers = [1, 2, 3, 4, 5, 6, 7]
 
map_result = map(factorial_func, numbers)
print(list(map_result))
 
fruits = ['apple', 'orange', 'kiwi', 'banana', 'pineapple']

result = map(len_func, fruits)
print(list(result))

numbers = [10, 20, 30, 40, 50, 60]
 
map_result = map(lambda x: x * x, numbers)
print(list(map_result))
 
fruits = ['apple', 'orange', 'kiwi', 'banana', 'pineapple']
 
result = map(lambda a:a.upper(), fruits)
print(list(result))
 
result2 = map(lambda a:a.capitalize(), fruits)
print(list(result2))


numbers1 = [10, 20, 30, 40, 50]
numbers2 = [150, 250, 350, 450, 550]
 
map_result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(map_result))
 
fruits1 = ['apple', 'orange', 'kiwi']
fruits2 = ['banana', 'cherry', 'berry']
 
result = map(lambda a, b: a + b, fruits1, fruits2)
print(list(result))


def square_func(num):
    return num**2
 
def tripple_func(num):
    return num * num * num
 
def four_func(num):
    return num**4
 
function_list = [square_func, tripple_func, four_func]
 
for i in range(1, 10):
    number = map(lambda x: x(i), function_list)
    print("For ", i, " = " , list(number))


def square_func(num):
    return num**2
 
numbers = [10, 20, 30, 40, 50]
 
list_result = map(square_func, numbers)
my_list = list(list_result)
print(my_list)
 
tuple_result = map(square_func, numbers)
my_tuple = tuple(tuple_result)
print(my_tuple)
 
set_result = map(square_func, numbers)
my_set = set(set_result)
print(my_set)


fruits = ['apple', 'berry', 'kiwi']
 
result = map(list, fruits)
print(list(result))
 
result2 = map(tuple, fruits)
print(tuple(result2))

