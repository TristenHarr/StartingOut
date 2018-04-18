import numpy as np
import pandas as pd

outside = ["G1","G1","G1","G2","G2","G2"]
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(np.random.randn(6,2), hier_index, ["A","B"])
print(df["A"])
print(df["A"]["G1"])
print(df["A"]["G1"][2])

print(df.loc["G1"])

df.index.names = ["Name1","Name2"]
print(df.xs("G1"))

print(df.xs(1, level="Name2"))