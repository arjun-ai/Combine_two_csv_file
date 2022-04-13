import pandas as pd

# set files path
sales1 =pd.read_csv ("C:\\Users\\arju3\\OneDrive\\Desktop\\multiple_csv\\data_na.csv")
sales2 =pd.read_csv("C:\\Users\\arju3\\OneDrive\\Desktop\\multiple_csv\\data_nnmi.csv")
#print(sales1)
print("*** Merging multiple csv files into a single pandas dataframe ***")

# merge files
dataFrame =pd.merge(sales1, sales2)
#                   on='IP_Address', 
 #                  how='right')
dataFrame.to_csv('ECE_BR.csv')