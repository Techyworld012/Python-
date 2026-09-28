import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

print(df.isna().sum())   # it gives the sum of all the null values in each column






