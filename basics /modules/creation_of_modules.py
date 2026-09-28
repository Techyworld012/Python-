# How to create a python modules and use it in our program 

#To create a module, all you need to do is create a .py file in a similar path to your python file. Inside that file, you can add required functions you need your program to perform.

# To call the module inside your program, all you need to do is use import keyword followed by the name of your .py file.

# lets create a one module file and import it here 

import demo          # check the file , demo.py is created there 

a = demo.add(2,3)
print(a)

b = demo.employee["Name"]        # check the demo.py file 
print(b)