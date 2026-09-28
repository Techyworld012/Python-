import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

# Find employees with salary > 70,000, but show only their name, department and salary.

print(df.loc[df["salary"]>70000 , ["name","department","salary"]])

# Find employees with performance score greater than 8.5 and display:

print(df.loc[df["performance_score"]>8.5 , ["name","performance_score","projects_completed"]])