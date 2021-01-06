import pandas as pd


df = pd.DataFrame({'a':[5,5,5,3,3,9,9], 'b':[6,2,1,5,6,2,9], 'c':[8,5,4,6,3,4,2]})
print(df)

print(df.sort_index(ascending=False)) #依据索引排序

print(df.sort_values(by="a")) #依据a列排序（类似于excel）
