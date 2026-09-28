# write a program to print this pattern 

for i in range (1, 11):  # outer loop
    for j in range (1,i+1):
        print(i*j,end=" ")
    print(" ")    