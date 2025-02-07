#Add a new "Salary" to the Previous DataFrame with values [50000,60000,70000].

import pandas as pd
data = {'name' : ['ABHAY', 'UDAY', 'Abhyudaya'], 'age' : [20, 21, 22], 'Salary' : [50000,60000,70000 ]}  
df = pd.DataFrame(data)
print(df)