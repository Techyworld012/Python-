# this is the part 2 of the functions 

a = {"ironman","hulk","captain","thor"}
b = {"superman","batman","wonderman"}
c = {"ironman","hulk"}

# is disjoint()


print(a.isdisjoint(b))  # b's elements is not present in a  , return true 
print(a.isdisjoint(c))   # c's element is present in a , returns false 

# issubset()

print(c.issubset(a))   # c is a subset of a , return true 
print(a.issubset(c))    # a is not a subset , returns false 

# issuperset()
print(a.issuperset(c))    # a is superset of c ,returns true 

# update
a.update(b)    # update the values of b to a , and make a unique values set 
print(a)    

# clear

a.clear()    # va,eus got cleared up 
print(a)     


