# Recursive means a function can call itself , giving us a benefit of looping through data in order to get a result ...# 
# function k andar function ko call kr rha hau 

# write a program of to find a factorail of any number using recursion function :...

def fact(n):
    if(n==1):
        return 1
    else:
        print(n*fact(n-1))        # recursion , function calling itself 
    
print(fact(6))   

print("Thankyou")



