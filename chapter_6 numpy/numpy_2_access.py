# Accessing the Array Index
import numpy as np
arr = np.array([
    [1,2,3,4],
    [5.2,6,7.2,-2],
    [2,0.3,5.3,4.1],
    [4,1.2,5.3,4.1]])
final = arr[:3,::2]
print(final)