import numpy as np

arr1 = np.array([[112,34,43],[34,22,76]])
print(np.sort(arr1))   # Using sort function in numpy , it will sort the values

# Searchsorted function in numpy
arr2 = np.array([1,2,3,4,5])     # search sort is apllicable to sorted array 
print(np.searchsorted(arr2,3))   # Using searchsorted function in numpy , it will return the index of the value 3 in arr2



# Filter function , How to filters the values in numpy array
arr3 = np.array([1,2,3,4,5])
filter_arr = arr3 > 2   # filter condition
print(filter_arr)   # it will return the boolean values for the filter condition
new = arr3[filter_arr]   # it will return the values which are greater than 2,all true
print(new)   # it will return the values which are greater than 2