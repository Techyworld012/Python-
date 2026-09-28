# write a program to print this pattern
# 1
 # 21
 # 321
 # 4321
 # 54321

for i in range(1,6):
    for j in range (i,0,-1):
        print(j,end=" ")
              
    print() 

# Write a program to print this pattern and check the output

for m in range(1,6):
    for n in range (0,m):
        print("*",end=" ")
    print()    
for p in range(1,6):
    for q in range (5,p,-1):
        print("*",end=" ")
    print()      