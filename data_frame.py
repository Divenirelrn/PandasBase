import pandas as pd
import numpy as np


#由列表创建
df = pd.DataFrame([['xiaojun', 18], ['liruonan', 24], ['lixiaokou', 26]], columns=['name', 'age'], dtype=float)
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

#由字典创建
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

#由numpy数组创建
data = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(data)
print(df)