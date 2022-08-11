# Python zip Example
 
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
 
zip_result = zip(list1, list2)
 
print(zip_result)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
 
zip_result = zip(list1, list2)
 
for x, y in zip_result:
    print(x, y)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday']
 
zip_result = zip(list1, list2, list3)
 
for x, y, z in zip_result:
    print(x, y, z)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday']
 
zip_result = zip(list1, list2, list3)
 
for val in zip_result:
    print(val)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd', 'e')
tuple3 = ('Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday')
 
zip_result = zip(tuple1, tuple2, tuple3)
 
for val in zip_result:
    print(val)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
tuple1 = ('Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday')
 
zip_result = zip(list1, list2, tuple1)
 
for val in zip_result:
    print(val)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']
tuple1 = ('Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday')
 
zip_result = zip(list1, list2, tuple1)
 
for val in zip_result:
    print(val)


list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['Sunday', 'Monday', 'Tues', 'Friday']
 
zip_result = zip(list1, list2, list3)
print(list(zip_result))
 
print('\nTo Zip directly inside a List')
print(list(zip(list1, list2, list3)))

list1 = [1, 2, 3, 4]
list2 = ['Sunday', 'Monday', 'Tues', 'Friday']
 
zip_result = zip(list1, list2)
print(set(zip_result))
 
print('\nTo Zip directly inside a Set')
print(set(zip(list1, list2)))
 
print('\n*********Dictionary Example******')
result = zip(list1, list2)
print(dict(result))
 
print('\nTo Zip directly inside a List')
print(dict(zip(list1, list2)))

list1 = [10, 20, 30, 40, 50]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday']
 
[print(list1, list2, list3) for list1, list2, list3 in zip(list1, list2, list3)]


list1 = [10, 20, 30, 40, 50]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['Sunday', 'Monday', 'Tuesday', 'Thursday', 'Friday']
 
[print(values) for values in zip(list1, list2, list3)]

list1 = [10, 20, 30, 40]
list2 = ['a', 'b', 'c', 'd']
list3 = ['Sunday', 'Monday', 'Thursday', 'Friday']
 
list_result = list(zip(list1, list3))
print(list_result)
 
x, y = zip(*list_result)
print('Values in x = ', x)
print('Values in y = ', y)

list1 = [10, 20, 30, 40]
list2 = ['a', 'b', 'c', 'd']
list3 = ['Sunday', 'Monday', 'Thursday', 'Friday']
 
list_result = list(zip(list1, list2, list3))
print(list_result)
 
x, y, z = zip(*list_result)
print('Values in x = ', x)
print('Values in y = ', y)
print('Values in z = ', z)

list1 = [10, 20, 30, 40]
list2 = ['a', 'b', 'c', 'd']
list3 = ['Sunday', 'Monday', 'Thursday', 'Friday']
 
result = zip(list1, list2, list3)
 
x, y, z = zip(*result)
print('Values in x = ', x)
print('Values in y = ', y)
print('Values in z = ', z)
