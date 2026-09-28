import datetime

x = datetime.datetime.now()
print(x)

y = datetime.datetime(1997,10,14)
print(y)
# print(y.strftime("%A"))
# print(y.strftime("%B"))
# print(y.strftime("%a"))
# print(y.strftime("%m"))
# print(y.strftime("%Y"))

# this are useful , or others % codes are also there , suppose we want am pm ...



# Random module 
import random

# a = random.randint(1,10)
# print(a)

# l = ["head", "tail","invlaid"]
# toss = random.choice(l)
# print(toss)


# math module 

import math

# max and min u already know 

a = pow(2,4)    # 2 raised to 4 
print(a)

b = math.sqrt(49)
print(b)

c = abs(-12.345)   # we got the absolute value , means positive value 
print(c)

d = math.ceil(2.4)      # largest closing value 
print(d)

e = math.floor(2.4)     # lower closing value 
print(e)