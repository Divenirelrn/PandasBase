import pandas as pd
import numpy as np


#由numpy数组创建
s = pd.Series(np.array([1,2,3]))
print(s)

#指定index
s = pd.Series(np.array([1,2,3]), index=['a', 'b', 'c'])
print(s)

#由字典创建
s = pd.Series({1: 'a', 2: 'b', 3: 'c'})
print(s)

#由list创建（指定类型）
s = pd.Series([1,2,3], dtype=float)
print(s)

#apply方法
s = pd.Series([1,2,3,4,5]).apply(lambda x: x * 2)
print(s)


