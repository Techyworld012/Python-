# write a python program to sort a doctionary by value 

nums = {"a":21,"b":45,"c":9,"d":12,"e":13,}

a = sorted(nums.values())
print(a)             


#   # Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.

a={}

for i in range(1,16):
    a[i]=i*i

print(a)


# Write a program to multiply all the items in a dictionary.
c = {"a":21,"b":45,"c":9,"d":12,"e":13,}

product= 1

for i in c.values():
    product*=i

print(product)



# Write a python program to sort a dictionary by key.

# as same as 1st programm 