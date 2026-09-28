# all string fucntion required for string maninpulation ;
name = " piyush is an INCOME TAX INSPECTOR"

print(len(name))

print(name.count("I"))

print(name.capitalize())

print(name.upper())

print(name.lower())

print(name.index("I",15,34))  # INDEX OF "I" between 15 and 34th index 
# name.find method can also be used ;; 

# to write variables inside a string we can use format method ;
cast = "Baniya"
age=21
b="my cast is {} and i am {} years old"
print(b.format(cast,age))


# it fills the given character and centralizes the string 

print(cast.center(40,"*"))  # it fills the given character and centralizes the string




