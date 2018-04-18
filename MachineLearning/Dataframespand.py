import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ["A","B","C","D","E"],["W","X","Y","Z"])

print(df)
#
# print(df[df > 0])
#
# print(df[df["W"]>0]["X"])
#
# print(df[df["Z"]<0])
# print('\n')
print(df[(df["W"]>0) & (df["Y"]>1)])

print(df)
print(df.reset_index())

newind = "CA NY WY OR CO".split()
df["States"] = newind
df.set_index("States", inplace=True)
print(df)
o = [[1,2,3,4,5],[6,7,8,9,10],]

df["Num1"] = o[1]
print(df)