import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)


# check the median value ofthe salary column
# fillna

value = df["salary"].median()

print(value)

# fill the null values in salary column with median value

df["salary"] = df["salary"].fillna(df["salary"].median())   # filling null values with median value

print(df["salary"])

# filling the unknown city columns with "Unknown" value

df["city"] = df["city"].fillna("Unknown")

print(df["city"])