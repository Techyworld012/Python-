import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)

# ----> # Find employees who:
# are in IT OR Finance
# AND have salary greater than 60,000
# AND have performance score greater than 7.5

print(df.loc[   
    # rows
             (((df["department"]=="IT") | (df["department"]=="Finance")) &
             (df["salary"]>60000) &
             (df["performance_score"]>7.5)),
     # columns
             ["name","department","salary","performance_score"]
             ])


#---->  Find employees who have either more than 8 years of experience OR a performance score above 9, but whose salary is below 80,000.Display:

# name
# experience_years
# performance_score
# salary


print(df.loc[
           ((df["experience_years"]>8) | (df["performance_score"]>9) & 
            (df["salary"]<80000)) ,
            ["name","experience_years","performance_score","salary"]
])

# ---> Find employees from IT, Sales, or Finance who are between 25 and 40 years old, have completed at least 10 projects, and have a performance score of at least 8.

print(df.loc[
    ((df["department"].isin(["IT","sales","Finance"])) & 
     (df["age"].between(25,40)) & 
     (df["projects_completed"]>9)),

     ["name","department","age","projects_completed","performance_score"]
     ])

print(df.loc[df["department"].isin(["It"])])