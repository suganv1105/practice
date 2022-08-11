myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#index    0  1  2  3  4  5  6  7  8
#        -9 -8 -7 -6 -5 -4 -3 -2 -1

#List Slicing
print('Original List:',myList)
print('First Element:',myList[0]) #Prints the first element of the list or 0th element of the list
print('Element at 2nd Index position:',myList[2]) #Prints the 2nd element of the list
print('Elements from 0th Index to 4th Index:',myList[0: 5]) #Prints elements of the list from 0th index to 4th index. IT DOESN'T INCLUDE THE LAST INDEX
print('Element at -7th Index:',myList[-7]) #Prints the -7th or 3rd element of the list

#To append an element to a list
myList.append(10)
print('Append:',myList)

#To find the index of a particular element
print('Index of element \'6\':',myList.index(6)) #returns index of element '6'

#To sort the list
myList.sort()

#To pop last element
print('Poped Element:',myList.pop())

#To remove a particular element from the lsit BY NAME
myList.remove(6)
print('After removing \'6\':',myList)

#To insert an element at a specified Index
myList.insert(5, 6)
print('Inserting \'6\' at 5th index:',myList)

#To count number of occurences of a element in the list
print('No of Occurences of \'1\':',myList.count(1))

#To extend a list that is insert multiple elemets at once at the end of the list
myList.extend([11,0])
print('Extending list:',myList)

#To reverse a list
myList.reverse()
print('Reversed list:',myList)

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])
# Prints ['c', 'd', 'e', 'f', 'g']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[-7:-2])

# Return every 2nd item between position 2 to 7
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:-5])

# Return every 2nd item between position 6 to 1
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:1:-2])

# Slice the first three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[:3])
# Prints ['a', 'b', 'c']

# Slice the last three items from the list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:])
# Prints ['g', 'h', 'i']

L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])
# Prints ['e', 'd', 'c', 'b', 'a']

# Modify multiple list items
L = ['a', 'b', 'c', 'd', 'e']
L[1:4] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'e']

# Replace multiple elements in place of a single element
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'c', 'd', 'e']

# Insert at the start
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3]
print(L)
# Prints [1, 2, 3, 'a', 'b', 'c']

# Insert at the end
L = ['a', 'b', 'c']
L[len(L):] = [1, 2, 3]
print(L)
# Prints ['a', 'b', 'c', 1, 2, 3]

# Insert in the middle
L = ['a', 'b', 'c']
L[1:1] = [1, 2, 3]
print(L)
# Prints ['a', 1, 2, 3, 'b', 'c']

L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []
print(L)
# Prints ['a']

L = ['a', 'b', 'c', 'd', 'e']
del L[1:5]
print(L)
# Prints ['a']

L1 = ['a', 'b', 'c', 'd', 'e']
L2 = L1[:]
print(L2)
# Prints ['a', 'b', 'c', 'd', 'e']
print(L2 is L1)
# Prints False
