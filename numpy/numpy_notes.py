# numpy is a array collection of same data type 
# the number of the dimension is called rank 
# the size of each dimension is called shape 

import numpy as np


                        #numpy functions
#np.array  use for cereating a array 
arr = np.array([1,2,3])
# print(arr)



# np.zeros use for create a array only 0 values
arr =  np.zeros([2,1])#there 2 and 1 are coloum and rows 
# print(arr)

#np.ones use for create a aray with only 1 values
arr  =  np.ones([2,1])
# print(arr)

#np.arrange use for create a aray with specifice range 
arr  = np.arange(3,54,2)
# print(arr)



# np.linespace use for create a array with a even spaced number 
arr = np.linspace(0,1,5)
# print(arr)


# np.random.rand use for create a randome array values 
arr =  np.random.rand(2,3)
# print(arr)

# np.reshape  resahepe the array without changing the data 
arr =  np.reshape(np.arange(1,11,1),(2,5))
# print(arr)



#np.flattend use for make a multi dimensional array into one dimensional array 
# arr  = np.array([
#     [1,2,3,4],
#     [5,6,7,8]
#     ])
# # print(arr) # it show a 2d array 
# g =  np.reshape.flatten(arr)
# print(g)


# T use to transpose the array 
arr  = np.array([
     [1,2,3,4],
     [5,6,7,8]
     ])
t  = arr.T
# print(t)

#np.concatenate use for combine the 2 array 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
t = np.concatenate((arr1,arr2))
# print(t)

                    # np maths functions 

#np.sum use for make the sum total in the array elements
arr  =  np.array([1,2,3])
sum = np.sum(arr)
# print(sum)

#np.mean calculate the mean of the array 
arr  =  np.array([1,2,3])
mean  = np.mean(arr)
# print(mean.dtype)

#min and max use for find the array min and max
arr  = np.array([2,3,5])
mean =  np.mean(arr)
max =  np.max(arr)
# print(mean)
# print(max) 

#np.sqrt use for find the suare root of the array 
arr =  np.array([1,2,3,4])
# print(np.sqrt(arr))


                    #sort and search 


#np.sort use for maek the array sort
arr =  np.array([5,1,2,8,3,4])
# print(np.sort(arr))

#np.argsort retunr the index number of the array in sort format 

arr =  np.array([5,1,2,8,3,4])
# print(np.argsort(arr))

#np.where is use for return the index number where the condition follow
arr  = np.array([1,2,3,4,5,6])
# print(np.where(arr>3))


#np.save and np.load use for save the array in binary format and read them back 
arrt  =  np.array([1,2,3,4])
# np.save("arrt.npy",arrt)


# g = np.load("arrt.npy")
# print(g)


#np.savetxt and np.loadtxt use for save the array in txt format and readt them back 

arrr =  np.array([1,2,3,4])
np.savetxt("arrr.txt",arrr)

g =  np.loadtxt("arrr.txt")
print(g)



