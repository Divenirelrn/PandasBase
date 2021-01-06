import pandas as pd
import numpy as np


dates = pd.date_range("20200101", periods=6)
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=["a", "b", "c", "d"])
print(df)

# df.to_csv("./df.csv")
# data = pd.read_csv("./df.csv")
# print(data)

# df.to_pickle("./df.pkl")
data = pd.read_pickle("./df.pkl")
print(data)



