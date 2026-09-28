# while true 
# It is infinite loop , it can never ends until we use break statement to exit the loop ;

while True:

    num1 = input("Enter the first number :")
    num2 = input("Enter the second number : ")

    print("The sum of two numbers is : ", int(num1)+int(num2))

    repeat= input("DO you want to exit this loop ? : ")
    if repeat == "yes":
        break

print("The loop is exited successfully")