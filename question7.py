# Create a Pandas DataFrame with two columns: "Name" and "Age", containing 3 rows of Sample Data

import pandas as pd

data = {'Name': ['ABHAY', 'UDAY', 'Abhyudaya'],
        'Age': [20, 21, 22]}
df = pd.DataFrame(data)
print(df)