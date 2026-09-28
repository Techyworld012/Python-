import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

print(df["department"]=="IT")

print(df[(df["age"]>30)&(df["salary"]>60000)])

# find employees who belong to It or Belong to finance

print(df[(df["department"]=="IT")|(df["department"]=="Finance")])