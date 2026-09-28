import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

print(df.loc[0:2,["name","salary"]]) # gives only 3 rows of name and salary 

print(df.loc[10:20, ["name", "department", "city"]])