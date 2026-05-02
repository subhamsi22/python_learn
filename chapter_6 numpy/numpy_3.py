#  basic numpy operations 
import numpy as np
a  = np.array([
    [1,2,3],
    [4,5,6]
])
print("add 1 to every elements ",a+1) # this add every element to 1 
print("substract 1 from each elements", a-1)
print(sum(a))
print(a.dtype)