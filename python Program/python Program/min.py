# Python min Function Example

print("minimum Value = ", min(19, 49, 229, 435, 212, 182))
print("minimum Value = ", min(212, 58, 12, 142, 192, 502, 12, 172, 182))
print("minimum Value = ", min(10, 20, 30, 40, 70))
print("minimum Value = ", min(421, 2, 102,  122))

# Python min Function Example

# Python Tuple min Example 
minTuple = (12, 22, 32, 42, 52, 62, 72,82)
print("\n Original Tuple = ", minTuple)
      
print("minimum Value in a Tuple = ", min(minTuple))


# Python Tuple min Example 2
minStringTuple = ('berry', 'orange', 'banana', 'mango')
print("\n Original String = ", minStringTuple)
      
print("minimum String in a Tuple = ", min(minStringTuple))

# Python min Function Example

# Python List min Example 
minList = [187, 20, 42, 212, 502, 12, 172, 182]
print("\n Original List = ", minList)
      
print("minimum Value in a List = ", min(minList))


# Python List min Example 2
minStringList = ['cherry', 'berry', 'banana', 'mango']
print("\n Original String = ", minStringList)
      
print("minimum String in a List = ", min(minStringList))
# Python min Function Example

# Python Dictionary min Example 
minDictionary = {7: 100, 2: 40, 9: 10, 5: 60, 1: 420, 3: 120}
print("\n Original Dictionary = ", minDictionary)
      
print("minimum Key in a Dictionary = ", min(minDictionary.keys()))
print("minimum Value in a Dictionary = ", min(minDictionary.values()))

# Python Dictionary min Example 2
minStringDictionary = {1: 'grape', 2: 'banana', 3: 'cherry'}
print("\n Original Dictionary = ", minStringDictionary)
      
print("minimum Key in string Dictionary = ", min(minStringDictionary.keys()))
print("minimum Value in String Dictionary = ", min(minStringDictionary.values()))

# Python min Function Example

# Python Set min Example 
minSet = {19, 49, 229, 435, 212, 502, 172, 182}
print("\n Original Set = ", minSet)
      
print("minimum Value in a Set = ", min(minSet))


# Python Set min Example 2
minStringSet = {'cherry', 'berry', 'kiwi', 'banana', 'grape'}
print("\n Original Set = ", minStringSet)
      
print("minimum String in a Set = ", min(minStringSet))


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


# Python List min Example 
minList = [187, 20, 42, 212, 502, 12, 172, 182]
print("\n Original List = ", minList)
print("minimum Value in a List = ", min(minList, key = sum_of_list))

# Python Set min Example 2
minSet = {19, 49, 229, 435, 212, 502, 172, 182}
print("\n Original Set = ", minSet)
print("minimum Value in a Set = ", min(minSet, key = sum_of_list))

# Python min Function Example

# Python List min Example 
minList1 = [187, 20, 42, 212]
minList2 = [212, 58, 12, 142, 192, 502, 12, 172, 182]
minList3 = [421, 2, 102,  122]

print("minimum List = ", min(minList1, minList2, minList3, key = len))

# Python Set min Example 2
minSet1 = {19, 49, 229, 435, 212, 502, 182, 1200}
minSet2 = {9, 249, 977}
minSet3 = {10, 20, 30, 40, 70}

print("minimum Set = ", min(minSet1, minSet2, minSet3, key = len))

print("minimum 1 = ", min(minList1, minSet1, key = len))
print("minimum 2 = ", min(minList1, minSet2, key = len))
print("minimum 3 = ", min(minList1, minSet3, key = len))
print("minimum 4 = ", min(minList2, minSet1, key = len))




