import numpy as np
import pandas as pd

labels = ["a","b","c"]
my_data = [10,20,30]
arr = np.array(my_data)
d = {"a":10,"b":20,"c":30}
the_series = pd.Series(data=my_data)
Spec = pd.Series(data=my_data, index=labels)


ser1 = pd.Series([1,2,3,4],["USA","Germany", "USSR", "Japan"])
ser2 = pd.Series([1,2,5,4],["USA","Germany","Italy","Japan"])
ser3 = ser1 + ser2
print(ser3)
print(ser1,"",ser2, sep="\n")

print(ser1.keys()[0])
