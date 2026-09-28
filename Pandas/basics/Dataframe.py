import pandas as pd 

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 40, 45],
#     'Salary': [50000, 60000, 70000, 80000, 90000]
# }
# df = pd.DataFrame(data)
# print(df)

csv = pd.read_csv('sample.csv',encoding='latin1')   # Using read_csv function in pandas
# print(csv.head())   # Using head function in pandas to display the first 5 rows of the dataframe    

# print(csv.shape)   # Using shape attribute in pandas to display the dimensions of the dataframe
print(csv.info())

# print(csv.describe())  # gives the count mean, std , min, max, 25%, 50%, 75% of the dataframe

# prac = pd.read_csv('datas.csv')   # Using read_csv function in pandas to read ods file  
# print(prac.head())   # Using head function in pandas to display the first 5 rows of the dataframe