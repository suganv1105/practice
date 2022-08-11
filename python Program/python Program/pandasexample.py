import pandas as pd
from pandas import Series
import numpy as np

arr = Series([15, 35, 55, 75])
print(arr)

arr = Series([12, 32, 52, -15, 122])
print(arr)

print('\nValues in this Array     : ', arr.values)
print('Index Values of this Array : ', arr.index)

arr = Series([25, 50, 75, 100, 125], index=[2, 4, 6, 8, 10])
print(arr)

print('\nValues in this Array     : ', arr.values)
print('Index Values of this Array : ', arr.index)

arr = Series([2, 33, 66, 70, 15], index = ['a', 'e', 'i', 'o', 'u'])
print(arr)
print(arr.index)

arr = Series(np.arange(6))
print(arr)

# Here, we are assigning the index names.
arr1 = Series(np.arange(6), index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(arr1)