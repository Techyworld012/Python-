import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

# Find employees whose performance_score is not missing.

print(df.loc[df["performance_score"].notna(),["name","department","performance_score"]])   # it gives the employees whose performance_score is not missing


