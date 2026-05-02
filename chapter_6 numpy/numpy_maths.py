import numpy as np
arr1  = np.array([
    [1,2,3],
    [4,5,6]

] ,
dtype=np.float64)

arr2  = np.array([
    [11,22,33],
    [44,55,66]

] ,
dtype=np.float64)


print("the sum of this 2 array is ",np.add(arr1,arr2))
print("sum is ", sum(arr1))
print("the sqrt is ",np.sqrt(arr1))