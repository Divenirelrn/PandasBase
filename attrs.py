import pandas as pd


df = pd.DataFrame({'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]})

print(df)
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())