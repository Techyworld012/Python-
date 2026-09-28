# this page contians more string fucntions 

a = "njosdsd"
name = "   *****pIYUSH ,, "
data = "hello. my name is piyush. i am student"
student1 = "Pavan"

print(a.swapcase())  # converts upper case to lower case and lower case to upper case

print(name.strip(",,*, "))   # removes the unnecesasary characters from the start and end of the string

# split method 

print(data.split("."))  # splits the string into list of words based on the given character
                        # we got the all the elements separated by "." in the list



# ljust method 

print(student1.ljust(20,"-") ,"He is my chuiya friend")  # it fills the given character and left justifies the string")

print(student1.rjust(20,"-") ,"He is my chuiya friend")  # it fills the given character and right justifies the string")


Student2 = " Ansh is an chemistry expert"

print(Student2.replace("chemistry","chudai"))

