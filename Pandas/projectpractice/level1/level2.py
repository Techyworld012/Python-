import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

print(df["salary"].head())     # salary ki pehli 5 value 

print(df[["name","salary","department"]].head())    # inn columns ki values 

print(df[0:5])     # get rows from 0 to 4 