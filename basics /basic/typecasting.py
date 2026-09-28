""" There are two types of typecasting in Python:

 implicit and explicit. Implicit typecasting is done by the interpreter automatically,done by pythin itself  
 
 while explicit typecasting is done by the programmer or user  using built-in functions.  """

a = 12    # of type int 
b=1.2      # of type float
c = a+b
print(c)    # of type float , autorecognize by interpreter or python 
print(type(c))   # <class 'float'>


# explicit typecasting 

d = "123"  # of string type 
e = 3.4    # of type float

d = int(d)  # explicit typecasting from string to integer , converted from string to int 

print(type(d))  # <class 'int'>  
