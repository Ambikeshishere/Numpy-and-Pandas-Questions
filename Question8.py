#Given the DataFrame df, Print only first two rows data = {'name' : ['ABHAY', 'UDAY', 'Abhyudaya'], 'age' : [20, 21, 22]} df = pd.DataFrame(data) 

import pandas as pd
data = {'name' : ['ABHAY', 'UDAY', 'Abhyudaya'], 'age' : [20, 21, 22]}  
df = pd.DataFrame(data)
print(df.head(2))