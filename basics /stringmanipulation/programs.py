  
A= "OOTD.YOLO.ASAP.BRB.GTG.OTW"

# Write a program to to separate the above string into comma separated values. 

b = A.split(".")
print(b)       # gives values in list  

print(A.replace("."," , "))  # it replaces the "." with " , " and gives the output as comma separated values

# write a program to sort the above string in alphabetical order.

print(sorted(A))  # it sorts the list in alphabetical order and gives the output as list



# Write a program to remove a given character from the string .

name = "Hello "

name = name.replace("e","")   # remove e 
print(name)  # it removes the given character from the string and gives the output as string


# write a program to remove all the dots from the follwing string 
X= "P.I.Y.U.S.H"
X = X.replace("."," ")
print(X)  # it removes all the dots from the string and gives the output as string 


# Write a program to check the number of occurences of a substring in a string 

Y = "Pabiyuabiyuabsh"
print(Y.count("ab"))   # count the number of ab in the string 

 