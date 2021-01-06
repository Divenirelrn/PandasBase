import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#默认是折线图
#df.plot.line() # 折线的全写方式
#df.plot.bar() # 柱状图
#df.plot.hist() # 直方图
#df.plot.scatter() # 散点图

#Series
s = pd.Series(np.random.randn(20),
              index=pd.date_range('1/1/2000', periods=20))
s.plot()
plt.show()

#DataFrame
df = pd.DataFrame(np.random.randn(6, 4),
                  index=pd.date_range('1/1/2000', periods=6),
                  columns=list("ABCD"))
print(df.head()) #读取前五行数据
df.plot()
plt.show()

#指定x与y
df.plot.scatter(x="A", y="B")
plt.show()




