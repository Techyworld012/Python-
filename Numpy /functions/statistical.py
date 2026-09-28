import numpy as np 
import statistics as stats

baked_food = np.array([200,300,400,120,220,320,280,170])

print(np.mean(baked_food))   # Using mean function in numpy  # avg value 
print(np.median(baked_food))   # Using median function gives central value of the array
print(np.std(baked_food))   # Using standard deviation std function in numpy
print(stats.mode(baked_food))   # Using mode function in statistics gives the most frequently occurring value in the array

print(np.var(baked_food))   # Using variance function in numpy gives the variance of the array,, variance is the sqaure of std value ..



price = np.array([200,300,250,150,350])
sales = np.array([10,20,30,17 , 3 ])

print(np.corrcoef(price,sales))   # Using corrcoef function in numpy gives the correlation coefficient of the two arrays   , +ve values means the good thing or rising , while -ve indicates neagtive ,,,....

# Output of this shows price is increasing , but sales is decreasing showing negative value 
# like -0.2 is decreasing , while price is increasing , so it is not good for business ,,, while +ve values shows both are increasing or decreasing together which is good for business
