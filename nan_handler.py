import pandas as pd
import numpy as np


df = pd.DataFrame([[0, np.nan, 2],
                   [4, 6, np.nan],
                   [1, 2, 3]])
print(df)

df1 = df.dropna(axis=0, how='any')
print(df1)

df2 = df.fillna(value=0)
print(df2)

print(df.isnull())



