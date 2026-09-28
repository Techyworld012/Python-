# iteration using for loop 

fruits = ["apple","banana","chickoo",1,4,44.5]

for i in fruits:
    print(i)             # accessign elements using for loop 

# Iteration using for loop with range and length function 
print("Iteration using for loop with range and length function : ") 
for j in range(len(fruits)):
    print(fruits[j])


# Iteration using while loop 

print("Iteration using while loop ")

a = ["man","woman","others","transgender"]

k = 0 
while k<(len(a)):
    print(a[k])
    k+=1

# Using shorthand for loop 
print("Using shorthand for loop ")

[print (i) for i in a ]

 