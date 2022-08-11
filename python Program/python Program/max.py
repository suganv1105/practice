# Python max Function Example

print("Maximum Value = ", max(19, 49, 229, 435, 212, 182))
print("Maximum Value = ", max(212, 58, 12, 142, 192, 502, 12, 172, 182))
print("Maximum Value = ", max(10, 20, 30, 40, 70))
print("Maximum Value = ", max(421, 2, 102,  122))

# Python max Function Example

# Python Tuple Max Example 
maxTuple = (12, 22, 32, 42, 52, 62, 72,82)
print("\n Original Tuple = ", maxTuple)
      
print("Maximum Value in a Tuple = ", max(maxTuple))


# Python Tuple Max Example 2
maxStringTuple = ('berry', 'orange', 'banana', 'mango')
print("\n Original String = ", maxStringTuple)
      
print("Maximum String in a Tuple = ", max(maxStringTuple))

# Python max Function Example

# Python List Max Example 
maxList = [187, 20, 42, 212, 502, 12, 172, 182]
print("\n Original List = ", maxList)
      
print("Maximum Value in a List = ", max(maxList))


# Python List Max Example 2
maxStringList = ['cherry', 'berry', 'banana', 'mango']
print("\n Original String = ", maxStringList)
      
print("Maximum String in a List = ", max(maxStringList))
# Python max Function Example

# Python Dictionary Max Example 
maxDictionary = {7: 100, 2: 40, 9: 10, 5: 60, 1: 420, 3: 120}
print("\n Original Dictionary = ", maxDictionary)
      
print("Maximum Key in a Dictionary = ", max(maxDictionary.keys()))
print("Maximum Value in a Dictionary = ", max(maxDictionary.values()))

# Python Dictionary Max Example 2
maxStringDictionary = {1: 'grape', 2: 'banana', 3: 'cherry'}
print("\n Original Dictionary = ", maxStringDictionary)
      
print("Maximum Key in string Dictionary = ", max(maxStringDictionary.keys()))
print("Maximum Value in String Dictionary = ", max(maxStringDictionary.values()))

# Python max Function Example

# Python Set Max Example 
maxSet = {19, 49, 229, 435, 212, 502, 172, 182}
print("\n Original Set = ", maxSet)
      
print("Maximum Value in a Set = ", max(maxSet))


# Python Set Max Example 2
maxStringSet = {'cherry', 'berry', 'kiwi', 'banana', 'grape'}
print("\n Original Set = ", maxStringSet)
      
print("Maximum String in a Set = ", max(maxStringSet))


# Python Program to find Sum of Digits of a Number using Recursion

Sum = 0
def Sum_Of_Digits(Number):
    global Sum
    if(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Sum_Of_Digits(Number //10)
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = Sum_Of_Digits(Number)
print("\n Sum of the digits of Given Number = %d" %Sum)

def sum_of_list(Number):
    Sum = 0
    if(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        sum_of_list(Number //10)
    return Sum


# Python List Max Example 
maxList = [187, 20, 42, 212, 502, 12, 172, 182]
print("\n Original List = ", maxList)
print("Maximum Value in a List = ", max(maxList, key = sum_of_list))

# Python Set Max Example 2
maxSet = {19, 49, 229, 435, 212, 502, 172, 182}
print("\n Original Set = ", maxSet)
print("Maximum Value in a Set = ", max(maxSet, key = sum_of_list))

# Python max Function Example

# Python List Max Example 
maxList1 = [187, 20, 42, 212]
maxList2 = [212, 58, 12, 142, 192, 502, 12, 172, 182]
maxList3 = [421, 2, 102,  122]

print("Maximum List = ", max(maxList1, maxList2, maxList3, key = len))

# Python Set Max Example 2
maxSet1 = {19, 49, 229, 435, 212, 502, 182, 1200}
maxSet2 = {9, 249, 977}
maxSet3 = {10, 20, 30, 40, 70}

print("Maximum Set = ", max(maxSet1, maxSet2, maxSet3, key = len))

print("Maximum 1 = ", max(maxList1, maxSet1, key = len))
print("Maximum 2 = ", max(maxList1, maxSet2, key = len))
print("Maximum 3 = ", max(maxList1, maxSet3, key = len))
print("Maximum 4 = ", max(maxList2, maxSet1, key = len))

