# write a proggram to find sum of first 10 odd numbers using while loop;

count=0
sum = 0
n=1
while(n<=20):
    if(n%2==1):
        sum+=n
        count+=1
        if(count==10):
            break
    n+=1

print("Sum of first 10 odd numbers is : ",sum)


#  Write a program to check if a number is divisible by 8 and 12 upto 100 numbers 

for i in range(1,101):
    if(i%8==0  and i%12 ==0):
        print(i)
print("THis are the only numbers which are divisible by 8 and 12 upto 100 numbers")        