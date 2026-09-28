import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)
# print(df)

# print(df.loc[rowselection], column selection )

# print(df.loc[1,"salary"])    # gives the loaction of 1st row of salary column

# print(df.loc[0:4, ["name", "salary"]])  # gives the name and salary of the 5 columns

print(df.loc[5])    # printing the row number 5 

print(df.loc[5:10])  # printing the row number fro m index 5 to 10

print(df.loc[5,"salary"])   # gives the salary of 5th index 

print(df["salary"]>70000)   # it will give the true or false result 

print(df[df["salary"]>70000].head()) # it will give the result , or actual  full   rows 

print([df[df["salary"]>90000]].head())