a = ["Thor", "Hulk", "Ironman", "Captain America"]


#to create a copy of a list
b=[]
b=a.copy()
print(b)

#find index of an element
print(a.index("Hulk"))

#to entend the list
c=["vision","Spiderman"]
a.extend(c)
print(a)                     # gives the extended string 


#to reverse the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)       # give the list in ascending sorted 

#to clear allthe data from the list 
a.clear()
print(a)                 # list a becomes empty 