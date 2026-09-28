import numpy as np 

arr1 = np.array([[112,34,43],[34,22,76]])
arr2 = np.array([[12,25,43],[4,21,74]])
print(np.append(arr1,arr2))   # Using append function in numpy , 2d coverted to 1d and all values got appended 
print(np.append(arr1,[23,34]))   # 23 and 34 got added to the end of arr1 , 2d coverted to 1d and all values got appended


arr3 = np.array([1,2,3,4,5])
print(np.insert(arr3,2,23))   # Using insert function in numpy , 23 got inserted at index 2 of arr3

print(np.insert(arr1,1,[55,56,57],axis=0))  # 55, 56, 57 got inserted at index 1 of arr1 along axis 0

# print(np.insert(arr1,1,[55,56],axis=1))  # 55, 56 got inserted at index 1 of arr1 along axis 1   ,,

# check both the output given above 


# Delete fucntions 
arr4 = np.array([1,2,3,4,5])
print(np.delete(arr4,2))   # Using delete function in numpy , 3 got deleted
print(np.delete(arr4,[1,2]))   # 1st and 2nd index got eleminted

