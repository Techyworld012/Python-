# this is functions part 3 which talks about mathematical functions


a = {"ironman","hulk","captain","thor"}
b = {"superman","batman","wonderman","ironman"}
c = {"ironman","hulk"}

# union

print(a.union(b))

# differnce

print(a.difference(c))  # values in a that are not present in c 

# intersection

print(a.intersection(c))  # common values in a  and c 

# symmetric difference

print(a.symmetric_difference(b))  # common values removed , resultant