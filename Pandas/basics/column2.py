import pandas as pd 

data = {"Months":["January","February","March","April","May","June","July","August","September","October","November","December"]}

a = pd.DataFrame(data)

print(a)

def extract(value):
    return value[0:3]

# a["Months"]=a["Months"].map(extract)    # For particular months columns 

   # OR

a = a["Months"].apply(extract)     # a only have 1 columns , thats why working 
 
print(a)