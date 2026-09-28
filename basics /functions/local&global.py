# Local variables 
# Local variables  are the varaibles restricted to run throughout the program , it can only be used to patticular block of code ;

# Global varibles 
# Global varaibels is made to use throughout the program ; it is not restrictes to some block of code ;

x = 25 

def hello():
    # To use the global variable x in this fucntion we use 
    # Global x       ,, now this can be changes by this function also 
    x=24
    print(x)        # this is is the local function variable ;

print(x)    # this is accessing global variable 

hello()

# if we require to use global variable to be use inside the function , so we always use it like "   Global x     "
