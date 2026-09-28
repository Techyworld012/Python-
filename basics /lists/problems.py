# This is the problem solving 

A=["Ross","Rachel","Monica","Joe"]

# Write a program to swap first and forth element.
A[0],A[3]=A[3],A[0]        # simple method to swap elements 
print(A)                    


# Write a program to add a new value at second position.
A.insert(2,"vanshika")     # vanshika inserted at 2nd position 
print(A)

# Write a program to delete a value from 3rd position.
A.remove("Monica")  # or A.pop(2)
print(A)


B = [13, 7, 12, 10,45 , 63,33]


# Write a program to multiply all the numbers in the list.
mul = 1 

for i in B:
    mul = mul*i
print(mul)    

# Write a program to get the largest number from the list.
lar = 1 
for j in B:
    if(j>lar):
        lar=j
print(lar)        


# Write a program to get the smallest number from the list.

 
for k in B:
    if(k<lar):
        lar=k
print(lar)                # so basically to get the smaller number , we required to get    the                        largest number first , then iteratio again , as shown above ,


  # important things 

  # Another method to find the largest and smallest numbr from the list , is to use 
  # B.sort() function , after sorting in ascending order the last elements is the largest , u can access it by B[-1] , and the first element was the smallest number ;;;;;.....