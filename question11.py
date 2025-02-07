# Create a 5x5 matrix with random numbes and replace all values greater than 0.5 with 1 and others with 0


import numpy as np
data = np.random.rand(5,5)
data[data > 0.5] = 1
data[data <= 0.5] = 0
print(data)
print(data.shape)
print(data.size)
print(data.dtype)   
print(data.ndim)