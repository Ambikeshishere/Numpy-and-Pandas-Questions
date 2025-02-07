#Load a CSV file nameeed 'data.csv' into pandas DataFrame and print the first 5 rows.

import pandas as pd
data = pd.read_csv('data.csv')
print(data.head(5))
