import numpy as np 

a = np.array([10,20,30,40])
b = np.array([[10,20,30,40],[40,50,60,70],[34,54,32,54]])

# print(a[0:3])
# print(a[0:])

print(b[0:2,0:2])    # 2 elements of each 
print(b[0:2,0:3])   # it give both side 3 elements , coz it shows omly equal elements  

print(b[1,2:4])     # 1 indexed array ki 2usri 3eesri value  ,.... 60,70

print(b[2,1:])      # 2nd indexed pe ki 1st index se leke saari value 

# shape of array 

print(np.shape(b))   # shape is the numpy function , giving the rows:columns -> 3:4
print(np.size(b))     # no of elements in that array ;
print(np.ndim(b))     # 2 dimensions rows and columns only 

print(b.dtype)         # returns int64 

