import pandas as pd 

data = pd.read_csv('datas.csv')

# print(data)  # Using head function in pandas to display the first 5 rows of

# data['SALARY'] = pd.to_numeric(data['SALARY'], errors='coerce')

# to crate a new column in the dataframe we can use loc function in pandas
# data.loc[condition , new coloumn name] = value

data.loc[data['SALARY'] >= 25000,"Salarystatus"]= "NIcejob"
data.loc[data['SALARY'] <= 25000,"Salarystatus"]= "decentjob"

print(data)