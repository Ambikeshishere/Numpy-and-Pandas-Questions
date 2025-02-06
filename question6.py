# Create a Pandas Series from a Python List : [10, 20, 30, 40, 50]

import pandas as pd

list = [10, 20, 30, 40, 50]

series = pd.Series(list)
print(series)
print(type(series))
print(series.dtype)
print(series.shape)