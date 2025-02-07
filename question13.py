# given a Numpy array , extract all prime numbers from it.

import numpy as np

arr = np.array([10, 15, 3, 5, 8, 11, 17, 20])
prime = []
for i in arr:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

sd = np.array(prime)

print(sd)