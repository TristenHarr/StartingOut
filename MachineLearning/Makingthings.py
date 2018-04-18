import numpy as np
import pandas as pd

sal = pd.read_csv("Salaries.csv")


Stuff = sal.groupby("Id")
