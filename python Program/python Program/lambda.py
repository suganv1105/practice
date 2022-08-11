syntax:lambda arguments: expression

num = lambda: True
 
print(num())
--------------------------------

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))
--------------------------------
   
add = lambda x, y : x + y
 
print(add(10, 20))
--------------------------------
add = lambda x, y : x + y
print(add(10, 20))
multi = lambda x, y : x * y
print(multi(5, 20))
multi = lambda x, y, z : x * y * z
print(multi(5, 2, 6))
--------------------------------
message = lambda: print("Hello World!")
 
message()
--------------------------------
add = lambda x = 10, y = 20, z = 30 : x + y + z
print(add()) # 10 + 20 + 30
 
multi = lambda x = 10, y = 20, z = 30 : x * y * z
print(multi()) # 10 * 20 * 30
 
sub = lambda x = 10, y = 45: y - x
print(sub()) # 45 - 10
--------------------------------
add = lambda x = 10, y = 20, z = 30 : x + y + z
print(add(12, 14, 16)) # 12 + 14 + 16
print(add(75, 126)) # 75 + 126 + 30
print(add(222)) # 222 + 20 + 30
print(add()) # 10 + 20 + 30

print("Multiplication Values")
multi = lambda x = 10, y = 20, z = 30 : x * y * z
print(multi(2, 4, 5)) # x = 2, y = 4, z = 5
print(multi(100, 22)) # x = 100, y = 22, z = 30
print(multi(9)) # x = 9, y = 20, z = 30
print(multi()) # 10 * 20 * 30
--------------------------------
add = lambda : 10 + 20
print(add())
 
print("Multiplication Values")
multi = lambda : 10 * 20
print(multi())
 
print("Subtraction")
sub = lambda : 225 - 20
print(sub())
--------------------------------
def new_func(n):
    return lambda x : x * n
 
number = new_func(2)
number2 = new_func(3)
 
print(number(50))
print(number2(50))
--------------------------------

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number)
 
new_num = list(filter(lambda x : x % 2 == 0, number))
print(new_num)
--------------------------------

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number)
 
even_num = list(filter(lambda x : x % 2 == 0, number))
print(even_num)
 
odd_num = list(filter(lambda x : x % 2 != 0, number))
print(odd_num)
 
num_div_by_3 = list(filter(lambda x : x % 3 == 0, number))
print(num_div_by_3)
--------------------------------


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)
 
new_num = list(map(lambda x : x % 2 == 0, number))
print(new_num)
--------------------------------

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)
 
double_num = list(map(lambda x : x * 2, number))
print(double_num)
 
triple_num = list(map(lambda x : x * 3, number))
print(triple_num)
 
square_num = list(map(lambda x : x ** 2, number))
print(square_num)
--------------------------------

number1 = [10, 20, 30]
number2 = [15, 25, 35]
print(number1)
print(number2)
 
print("***********==========*************")
add_num = list(map(lambda x, y : x + y, number1, number2))
print(add_num)
 
sub_num = list(map(lambda x, y : x - y, number1, number2))
print(sub_num)
 
mul_num = list(map(lambda x, y : x * y, number1, number2))
print(mul_num)

number = [10, 20, 30, 15, 25, 35, 45]
print(number)
 
print("***********==========*************")
add_num = reduce((lambda x, y : x + y), number)
print(add_num)
 
sub_num = reduce((lambda x, y : x - y), number)
print(sub_num)
 
mul_num = reduce((lambda x, y : x * y), number)
print(mul_num)
