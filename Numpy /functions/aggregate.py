import numpy as np 
arr1 = np.array([20,30,40,50])

print(np.sum(arr1))   # Using sum function in numpy
print(np.min(arr1))   # Using min function in numpy
print(np.max(arr1))   # Using max function in numpy     
print(np.mean(arr1))   # Using mean function in numpy
print(np.median(arr1))   # Using median function in numpy
print(np.cumsum(arr1))   # Using cumsum function in numpy
print(np.cumprod(arr1))   # Using cumprod function in numpy

Price = np.array([200,300,400,500])
Quantity = np.array([2,3,4,5])

# Now we want total values of all the quantities 
total = (np.cumprod([Price,Quantity],axis=0))   # Using cumprod function in numpy , it will return the cumulative product of all the values in the array

print(total[1].sum())   # it will return the total value of all the quantities