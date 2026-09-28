
a = ["Piyush" , "Kirti", "Riddhi","Ankit", "Luv", "Kirti"]

#to find the length of a list
print(len(a))

# to count an occurence of a particular element www
print(a.count("Kirti"))
print(a.count("Riddhi"))

# to add to the list
a.append("Vanshika")
print(a)

# to add to a specific location
a.insert(3,"chirag")       # insert chirag at location 3 
print(a)


# to remove from a list
a.remove("Luv")
print(a)
# to remove from a certain location

print(a.pop(4))
print(a)