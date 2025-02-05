# Reshaping a 1D array of size 9 into a 3x3 matrix using Numpy

import numpy as np
arr = np.arange(9)
reshaped_arr = arr.reshape(3,3)
print("Reshaped 3x3 matrix:")
print(reshaped_arr)