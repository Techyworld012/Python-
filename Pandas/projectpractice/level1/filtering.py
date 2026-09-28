import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

# Find all employees whose age is greater than 40.

# print(df.columns)

print(df["salary"].head())

print(df[df["age"]>40].head())

# Find all employees whose salary is less than 50,000.

print(df[df["salary"]<50000].head())

# Find all employees whose performance score is greater than 8.

print(df[df["performance_score"]>8].head())


