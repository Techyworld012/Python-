import pandas as pd 

data = pd.read_csv("practicesample.csv")

df = pd.DataFrame(data)


# create a new column called annual salary 
# currently we have monthly salary columns,we will create a new column called annual salary by multiplying the monthly salary with 12

df["annual_salary"]= df["salary"]*12

# printing values without null values in annual salary column

print(df["annual_salary"])