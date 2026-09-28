import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

# Instead of writing this all 

# (df["department"] == "IT") | (df["department"] == "Finance")

# write this 

# df[df["department"].isin(["IT", "Finance"])]     


# find employees from it , hr , marketing , using isin()

print(df["department"].isin(["IT","HR","Marketing"]))


# between function 

print(df[df["age"].between(25,35)])

# find the employees whose salary is between 50000, 90000

print(df[df["salary"].between(50000,90000)])

