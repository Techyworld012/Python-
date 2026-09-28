import numpy as np 

arr1 = np.array([[112,34,43],[34,22,76]])
arr2 = np.array([[12,25,43],[4,21,74]])

# print(arr1+arr2)      # operation method 
print(np.add(arr1,arr2))   # Using add function in numpy

# Likewise we can use other operations like substraction, multiplication, division etc.

# print(arr1-arr2)      # operation method
print(np.subtract(arr1,arr2))   # Using subtract function in numpy

# print(arr1*arr2)      # operation method
# print(np.multiply(arr1,arr2))   # Using multiply function in 

arr3 = np.array([2,4,5])
arr4 =np.array([2])
print(np.power(arr3,arr4))   # Using power function in numpy

print()

