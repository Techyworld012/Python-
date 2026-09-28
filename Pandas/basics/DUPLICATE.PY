import pandas as pd

data = pd.read_csv('datas.csv')
print(data.head())   # Using head function in pandas to display the first 5 rows of the dataframe
print(data.columns)

print(data['EEID '].duplicated().sum())
# here we get to know about the duplicated valus in the column 'EEID'...

print(data.drop_duplicates("EEID "))   # Using drop_duplicates function in pandas to remove the duplicated values in the column 'EEID' ,, Check the output 
