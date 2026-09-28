import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

print(df[0:5])

print(df[10:20])   # print the rows number 10 to 20 
