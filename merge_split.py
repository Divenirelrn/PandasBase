import pandas as pd
import numpy as np


df1 = pd.DataFrame(np.random.rand(3,4), columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.random.rand(3,2), columns=["d", "e"])
df3 = pd.DataFrame(np.random.rand(3,4), columns=["a", "b", "c", "d"])

#concat
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], ignore_index=True, join="outer")) #outer为并，inner为交

print('\n')

#merge
print(pd.merge(df1, df2, how="outer", on="d"))
