# Looping concepts in dictionary 

Student = {
    "name":"john",
    "class":"6th",
    "roll_no":23
}

for x in Student:
    print(x,":",Student[x])


# Using values functions 
for i in Student.values():   # this access values directly ;
    print(i)

# Using items functions 

for y,z in Student.items():
    print(y,"-",z)    