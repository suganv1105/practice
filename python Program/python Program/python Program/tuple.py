x = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing the Tuple using two indexes
a = x[2:6] 
print("Both Indexes = ", a)

# Slicing the Tuple using First indexes
b = x[:6] 
print("No First Index = ", b)

# Slicing the Tuple using Second indexes
c = x[2:] 
print("No Second Index = ", c)

# Slicing the Tuple without using two indexes
d = x[:] 
print("No Indexes = ", d)

# Slicing the Tuple using Negative indexes
e = x[-3:] 
print("Negative First Index = ", e)

# Slicing the Tuple using Negative indexes
f = x[:-2] 
print("Negative Second Index = ", f)

# Python tuple sum function

x = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("Tuple : ", x)

total = sum(x)
print("The Sum of Integer Tuple is : ", total)

numbers = (9, -5, 7, 0, 24, -1, 2, 10)
print("\nNumbers Tuple : ", numbers)
print("The Sum of a Numbers Tuple is : ", sum(numbers))
print("sdf ","ert")


# Python tuple min function

fruits = ('Banana', 'Orange', 'Blackberry', 'Apple', 'Kiwi', 'Grape')
print("Tuple : ", fruits)

minimum = min(fruits)
print("The Minimum Value in Fruits Tuple is : ", minimum)
maximum = max(fruits)
print("The Maximum Value in Fruits Tuple is : ", maximum)


numbers = (9, -5, 7, 0, 24, -1, 2, 10)
print("\nNumbers Tuple : ", numbers)
print("The Minimum Value Numbers Tuple is : ", min(numbers))


# Python tuple len function

fruits = ('Apple', 'Banana', 'Orange', 'Blackberry', 'Kiwi', 'Grape')
print("Tuple : ", fruits)

length = len(fruits)
print("The length of a Fruits Tuple is : ", length)

numbers = (9, -5, 7, 0, 24, -1, 2, 10)
print("\nNumbers Tuple : ", numbers)
print("The length of a Numbers Tuple is : ", len(numbers))

# Python tuple sorted function

fruits = ('Banana', 'Orange', 'Blackberry', 'Apple', 'Kiwi', 'Grape')
print("Old Tuple : ", fruits)

new_fruits = sorted(fruits)
print("Sorted Tuple : ", new_fruits)

numbers = (9, -5, 7, 0, 24, -1, 2, 10)
print("\nNumber Tuple : ", numbers)

new_numbers = sorted(numbers)
print("Sorted Numbers Tuple is : ", new_numbers)

# Python tuple index function

fruits = ('Banana', 'Orange', 'Blackberry', 'Apple', 'Kiwi', 'Grape')
print("Tuple : ", fruits)

print("The index position of Apple : ", fruits.index('Apple'))
print("The index position of Orange : ", fruits.index('Orange'))
print("The index position of Kiwi : ", fruits.index('Kiwi'))
      
numbers = (9, -5, 7, 0, 24, -1, 2, 10)
print("\nNumber Tuple : ", numbers)

print("The index position of -1 : ", numbers.index(-1))
print("The index position of 0 : ", numbers.index(0))
print("The index position of 10 : ", numbers.index(10))

# Python tuple count function

fruits = ('Banana', 'Kiwi', 'Grape', 'Apple', 'Kiwi', 'Grape')
print("Tuple : ", fruits)

print("Number of Times Apple is Repeated : ", fruits.count('Apple'))
print("Number of Times Kiwi is Repeated : ", fruits.count('Kiwi'))
print("Number of Times Grape is Repeated : ", fruits.count('Grape'))
      
numbers = (2, -5, 7, 9, 2, -5, 2, 10)
print("\nNumber Tuple : ", numbers)

print("Number of Times 2 is Repeated : ", numbers.count(2))
print("Number of Times -5 is Repeated : ", numbers.count(-5))
print("Number of Times 10 is Repeated : ", numbers.count(10))


Fruits = ('Apple', 'Orange', 'Banana', 'Kiwi', 'Grape', 'Blackberry')
x = (9, 4, -5, 0, 22, -1, 2, 14)

#Finding Sum of all item in a Tuple using Python Sum() Method
print('Sum of all items in a x Tuple = ', sum(x))

#Calculating Length of a Tuple using Python len() Method
print('Length of a Fruits Tuple = ', len(Fruits))
print('Length of a x Tuple = ', len(x))

#Finding Minimum item in a Tuple using Python min() Method
print('Minimum item in a Fruits Tuple = ', min(Fruits))
print('Minimum item in a x Tuple = ', min(x))

#Finding Maximum item in a Tuple using Python max() Method
print('Maximum item in a Fruits Tuple = ', max(Fruits))
print('Maximum item in a x Tuple = ', max(x))

# Sorting the Tuple using Python Sorted() Method
print('After Sorting Fruits Tuple = ', sorted(Fruits))
print('After Sorting x Tuple = ', sorted(x))

# Index position of an item in a Tuple using index() Method
print('The Index position of Banana = ', Fruits.index('Banana'))
print('The Index position of -1 = ', x.index(-1))

# Counting items in a Tuple using Python count() Method
y = (9, 4, 1, 4, 9, -1, 2, 4)
print('Number of Times 4 is repeated = ', y.count(4))
print('Number of Times 9 is repeated = ', y.count(9))

# Converting List into Tuple
z = [1, 2, 3, 4, 5]
print(tuple(z))
