import pandas as pd

data = pd.read_csv('synergy_logistics_database.csv')

count_rows = data.shape[0]
count_columns = data.shape[1]

print('Rows '+ str(count_rows) +'\n')
print('Columns '+ str(count_columns) +'\n')

print(data.head(10))

