import pandas as pd
import numpy as np


dates = pd.date_range("20200101", periods=6)
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=["a", "b", "c", "d"])
print(df)

print(df['a'])
print(df.a)

#select by label
print(df.loc['20200101'])
print(df.loc[:, ['a', 'b']])

#select by position
print(df.iloc[3:5, 1:3])

#setter
df.iloc[2,2] = 100
print(df)

df[df.a > 0.5] = 0
print(df)