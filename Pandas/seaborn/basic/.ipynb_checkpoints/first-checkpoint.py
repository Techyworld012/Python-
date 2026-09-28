import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# data = {"Days": [1, 2, 3, 4, 5], 
#         "Sales": [100, 200, 300, 400, 500]}

data = pd.read_csv("datas.csv")

print(data)

# data = pd.DataFrame(data)
# print(data)        

# sns.lineplot(data=data, x="Days", y="Sales")
# plt.show()