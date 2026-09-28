import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)
# print(df.head(10))

# print(data.head())

print(data.shape)     # gives (rows,columns)

# print(data.columns)

# print(data.dtypes)  # gives all columns datatypes information 

# print(data.info)      # 

print(data.describe)