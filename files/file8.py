import pandas as pd
data=pd.read_csv('football.csv')
print(data.head(5))
print(data.describe())