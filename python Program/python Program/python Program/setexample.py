# set Declaration

# Empty set
mySet = {}
mySet = set()

# Set with Integer Keys
mySet = {1, 2, 3, 4, 5}

# Set with String Keys
mySet = {'apple', 'kiwi', 'banana', 'orange'}

# Set with Mixed Data Types
mySet = {1, 2, 1.5, 2.5, 'apple'}
mySet = {'banana', 1, 2, (1, 2, 3)}

# Python Set using set()
mySet = set([1, 2, 3, 4, 5])
mySet = set((1, 2, 3, 4, 5, 6, 7))

# set() example 2
mySet = (['apple', 'kiwi', 'banana', 'orange'])
mySet = (('apple', 'kiwi', 'banana', 'orange'))

# set Declaration

# Empty set
mySet1 = {}
mySet2 = set()

# Set with Integer Keys
mySet3 = {1, 2, 3, 4, 5}

# Set with String Keys
mySet4 = {'apple', 'kiwi', 'banana', 'orange'}

print(mySet1)
print(mySet2)
print(mySet3)
print(mySet4)

# Python set Declaration

# Set with Mixed Data Types
mySet1 = {1, 2, 1.5, 2.5, 'apple'}
mySet2 = {'banana', 1, 2, (1, 2, 3)}

print(mySet1)
print(mySet2)

# Python Set using set()
mySet3 = set([1, 2, 3, 4, 5])
mySet4 = set((1, 2, 3, 4, 5, 6, 7))

print(mySet3)
print(mySet4)

# set() example 2
mySet5 = (['apple', 'kiwi', 'banana', 'orange'])
mySet6 = (('apple', 'kiwi', 'banana', 'orange'))

print(mySet5)
print(mySet6)

# Python set Declaration

# {} Vs set()
mySet = {'Tutorialpython'}
mySet1 = set('Tutorialpython')

print(mySet)
print(mySet1)

mySet2 = {123456}
mySet3 = set('123456')

print(mySet2)
print(mySet3)


# Add Items to set

mySet = {1, 2, 4, 5}
print("Old Set Items = ", mySet)

# Set add
mySet.add(3)
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'cherry', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set add
FruitSet.add('banana')
print("New Set Items = ", FruitSet)

# set update

mySet = {1, 2, 4, 5}
print("Old Set Items = ", mySet)

# Set update
mySet.update([2, 3, 6, 7])
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set update
FruitSet.update({'banana', 'cherry'})
print("New Set Items = ", FruitSet)

# set update

mySet = {1, 2, 5, 6}
print("Old Set Items = ", mySet)

# Set update
mySet.update([2, 3, 6, 7], {5, 8, 9})
print("New Set Items = ", mySet)

# set remove

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Old Set Items = ", mySet)

# Set remove()
mySet.remove(4)
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'banana', 'cherry', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set remove()
FruitSet.remove('orange')
print("New Set Items = ", FruitSet)

# set clear

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Old Set Items = ", mySet)

# Set clear()
mySet.clear()
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'banana', 'cherry', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set clear()
FruitSet.clear()
print("New Set Items = ", FruitSet)

# set discard

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Old Set Items = ", mySet)

# Set discard()
mySet.discard(7)
mySet.discard(4)
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'banana', 'cherry', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set discard()
FruitSet.discard('Mango')
print("New Set Items = ", FruitSet)

# set discard

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Old Set Items = ", mySet)

# Set discard()
mySet.discard(7)
mySet.discard(4)
print("New Set Items = ", mySet)

FruitSet = {'apple', 'Mango', 'orange', 'banana', 'cherry', 'kiwi'}
print("\nOld Set Items = ", FruitSet)

# Set discard()
FruitSet.discard('Mango')
print("New Set Items = ", FruitSet)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)

