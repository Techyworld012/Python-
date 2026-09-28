# print this pattern 
""" 1
    12
    123
    1234
    12345 """

# for i in range(1, 6):  # outer loop

#     for j in range(1, i+1):  # inner loop

#         print( j ,end =" ")

#     print()

 # write a program to print this pattern 
 # 1
 # 22
 # 333
 # 4444
 # 55555

for x in range(1, 6):  # outer loop

    for y in range(1, x+1):  # inner loop

        print( x ,end =" ")

    print()

# write a program to display this pattern 
 # 11111
 # 2222
 # 333
 # 44 
 # 5
print( " NEXT PATTEN ")
for m in range(1,6):
    for n in range (6,m,-1):
        print(m,end=" ")
              
    print() 

# WRITE A PROGRAM TO PRINT THIS PATTERN
#     *
#    **
#   ***
#  ****
# *****
print("NEXT PATTERN")

for i in range(1,6):
      for j in range (5,i,-1):
        print(" ",end=" ")
      for k in range(i):
        print("*",end=" ")
              
      print() 
    

