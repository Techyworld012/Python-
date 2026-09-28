# Write a fucntion to find the maximum of three numbers in python .

# ------------------------------------------------------
# def max(a,b,c):
#     if(a>b and a>c):
#         print("Max number is : ",a)
#     elif(b>a and b>c):
#         print("Max number is : ",b)
#     else:
#         print("Max number is : ",c)    

# max(2,7,4)  
# ---------------------------------------------------------          

# Write a program to create and print the list where the values are the square of numbers between 1 to 30 ;

def sq_list():
    l = []
    for i in range(1,31):
        l.append(i*i)
    return l    

print(sq_list())

# Write a python function to sum the number in a list .

def add(numbers):
    total=0
    for i in numbers:
        total=total+i
    return(total)

print(add([2,3,4,5,6]))


# Write a python program to solve the fibnacci sequence ;

def fib(num):
    if num==1:
        return (0)
    elif num == 2 :
        return (1)
    else:
        return (fib(num-1)+fib(num-2))
    
print(fib(10))    



    



