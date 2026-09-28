# Bitwise Operators 

a = 10
b=8
c=5
d=4

# AND operations 

print(a&b)  # bitwise AND operator , output is 8 , 1010 & 1000 = 1000
print(c&d)  # bitwise AND operator , output is 4 , 0101 & 0100 = 0100

# OR operations
print(a|b)  # bitwise OR operator , output is 10 , 1010 | 1000 = 1010

# XOR operations
print(a^b)  # bitwise XOR operator , output is 2 , 1010 ^ 1000 = 0010

# LEFT SHIFT operations
print(a>>2)  # bitwise LEFT SHIFT operator , output is 2 , 1010 >> 2 = 0010

# Right SHIFT operations
print(a<<2)  # bitwise RIGHT SHIFT operator , output is 40 , 1010 << 2 = 1010_00