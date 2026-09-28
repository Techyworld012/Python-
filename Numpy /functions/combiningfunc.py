import numpy as np 

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(np.concatenate([arr1,arr2]))   # Using concatenate function in numpy

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])
print(np.concatenate([arr3,arr4],axis=0))   # Using concatenate, horizontal concatenation function in numpy
print(np.concatenate([arr3,arr4],axis=1))   # Using concatenate, vertical concatenation function in numpy

# or for horizontal concatenation we also can use hstack function in numpy
# print(np.hstack([arr3,arr4]))   # Using hstack function in numpy i.e axis = 0 ;;;;;

# or for vertical concatenation we also can use vstack function in numpy 
# print(np.vstack([arr3,arr4]))   # Using vstack function in numpy   i.e axis = 1 ;;;;;

a = np.array([1,2,3,4,5])
print(np.split(a,5))   # Using split function in numpy
print(np.array_split(a,5))   # Using array_split function in numpy
# split function not much in use in data analystics ....