#
import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr)
#
# # creating array from list
# a = [1, 2, 3, 4, 5]
# print(type(a))
# arr = np.array(a)
# print(type(arr))
# print(arr)
#
# #mixed element array
# a = [2.5, 3.5, 7, 4.5, 8]
# arr = np.array(a)
# print(arr)
#
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[9,12,13]]
# print('List of List = ', a)
# print()
#
# arr = np.array(a)
# print(arr)
#
# a = [1, 2, 3, 4, 5]
# arr = np.array(a)
#
# print('Original Array      = ', arr)
# print('Add 5 to Array      = ', arr + 5)
# print('Multiply arr with 2 = ', arr * 2)
#
# tup = (10, 20, 30)
# arr = np.array(tup)
#
# print(arr)
#
# two_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(two_arr)
#
# three_arr = np.array([[1, 2, 3], [10, 20, 30], [6, 7, 8]])
# print(three_arr)
#
# a=np.arange(8)
# print(a)
# print(np.arange(10))
# print(np.arange(15))
#
# print(np.linspace(0, 1, 3))
# print(np.linspace(0, 10, 5))
# print(np.linspace(1, 0, 7))
# print(np.linspace(10, 100, 20))
# # print('--------')
#
# #
# print(np.zeros((2, 2)))
# print(np.zeros((2, 3)))
# print(np.zeros((4, 7)))
#
# print(np.ones((3,3,7)))
# #
# #
# #
# #
# print(np.random.random(5))
# print(np.random.random((4, 4)))
# print(np.random.random((2, 3, 4)))
# #
# print(np.empty(3))
# print(np.empty((2, 3)))
# print(np.empty((2, 4)))
# print(np.empty((2, 3, 5)))
# #
# # # Returns one dimensional array of 4’s of size 5
# print(np.full((9), 17))
# #
# # Returns 3 * matrix of number 9
# print(np.full((3, 4), 9))
# print(np.full((4, 4), 8))
# print(np.full((2, 5, 6), 7))
# #
# #
print(np.eye(2))
print(np.eye(3))
print(np.eye(5))
# #
print(np.diag([3]))
print(np.diag([1, 2]))
print(np.diag([1, 2, 3, 4]))
print(np.diag([1, 2, 3, 4, 5, 6]))
# #
arr = np.array([10, 15, 25, 35, 45, 55, 65])
print(arr)

print(arr[0])
print(arr[2])
print(arr[5])
print(arr[6])
print(arr[2:5])

a = np.array([10, 20, 30, 40, 50])
print(a)
print(a[0])
a[0] = 150
print(a)
#
a[3] = 111
print(a)
#
b = np.array([
    [10, 50, 100],
    [250, 500, 1000]
])
print(b)
#
b[0, 0] = 99
print(b)

b[1, 1] = 222
print(b)
#
b[1, 2] = 444
print(b)
#
arr1 = np.array([10, 25, 50, 75, 100, 125, 150, 200, 250])
print(arr1)

print(arr1[1:5])
print(arr1[2:7])
print(arr1[4:8])
print(arr1[3:9])

print(arr1[3:])
print(arr1[:7])
#
#
print('**********************')
arr1 = np.array([10, 50, 100, 150, 250])

arr2 = np.array([
                 [26, 48, 91, 57, 120],
                 [33, 95, 68, 109, 155],
                 [111, 194, 7, 22, 124],
                 [ 82, 119, 18, 156, 81],
                 [ 38, 10, 151, 24, 14]
                ])



print(arr1[::-1])
# Reverse the row position only
print(arr2[::-1,])
#
#
#
# # Reverse both the row and column position
print(arr2[::-1, ::-1])
#
#
# a = np.array([10, 50, 100, 150, 250])
#
#
#
# b = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
#              [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
#              [38, 10, 151, 24, 14]])
#
# print('Array Dimension = ', a.ndim)
# print('No of Elements in an Array = ', a.size)
# #print('Array Memory Layout = ', a.flags)
# print('Array Length in Bytes = ', a.itemsize)
# print('Total bytes consumed by an Array = ', a.nbytes)
#
# print('\nArray Dimension = ', b.ndim)
# print('No of Elements in an Array = ', b.size)
# #print('Array Memory Layout = ', b.flags)
# print('Array Length in Bytes = ', b.itemsize)
# print('Total bytes consumed by an Array = ', b.nbytes)
#
# arr1 = np.array([10, 50, 100, 150, 250])
#
# arr2 = np.array([[26, 48, 91, 57, 120], [33, 95, 68, 109, 155],
#                 [111, 194, 7, 22, 124], [ 82, 119, 18, 156, 81],
#                 [ 38, 10, 151, 24, 14]])
#
# arr3 = np.array([[12, 11, 0, 9, 7], [10, 4, 11, 6, 9],
#                 [9, 2, 10, 9, 11], [ 5, 14, 0, 11, 8]])
#
# print("Array 1.      : ", arr1)
# print("Array 1 Shape : ", arr1.shape)
#
# print("Array 2       : \n", arr2)
# print("Array 2 Shape : ", arr2.shape)
#
# print("Array 3       : \n", arr3)
# print("Array 3 Shape : ", arr3.shape)
#
#
# arr = np.random.randint(0, 5, size = 10)
# print('Original Array = ', arr)
#
# uniq = np.unique(arr)
# print('Unique Items in arr = ', uniq)
#
# arr2 = np.random.randint(10, 100, size = (3, 5))
# print('\n---Two Dimensional Random Original Array----\n', arr2)
#
# uniq2 = np.unique(arr2)
# print('Unique Items in arr2 = ', uniq2)
#
# arr3 = np.random.randint(15, 25, size = (2, 3, 8))
# print('\n----Three Dimensional Random Original Array----\n', arr3)
#
# uniq3 = np.unique(arr3)
# print('Unique Items in arr3 = ', uniq3)
#
#
# arr = np.random.randint(0, 5, size = 10)
# print('Original Array = ', arr)
#
# uniq, cnt = np.unique(arr, return_counts = True)
# print('Unique Items in arr = ', uniq)
# print('Count Items in arr = ', cnt)
#
# arr2 = np.random.randint(10, 100, size = (3, 5))
# print('\n---Two Dimensional Random Original Array----\n', arr2)
#
# uniq2, cnt2 = np.unique(arr2, return_counts = True)
# print('Unique Items in arr2 = ', uniq2)
# print('Count Items in arr2 = ', cnt2)
#
# arr3 = np.random.randint(15, 25, size = (2, 3, 8))
# print('\n----Three Dimensional Random Original Array----\n', arr3)
#
# uniq3, cnt3 = np.unique(arr3, return_counts = True)
# print('Unique Items in arr3 = ', uniq3)
# print('Count Items in arr3 = ', cnt3)


