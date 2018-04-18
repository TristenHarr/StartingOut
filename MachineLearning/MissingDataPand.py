import numpy as np
import pandas as pd

d = {"A":[1,2,np.nan],"B":[4,np.nan,np.nan],"C":[1,2,3]}

df = pd.DataFrame(d)

print(df)

print(df.fillna(0))


