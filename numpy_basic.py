import numpy as np 
# in python we can collect data in terms of 
# list 
# tuple 
# set 
# dict 
# string 

# numpy actually provides the array 
#that they can contain elements of a variety of types, 
# and they are quite fast when used to perform individual operations on a handful of elements


# List 
# data = np.array([1,2,3,4,5]) 
# print(data)

# to create the numpy array we use np.array(<sequence>) where sequence are tuple list etc 

# set 
# data1 = np.array({1,2,3,4,5})
# print(data1)
# print(type(data1))

 
# 2-D array is the matrix in the mathematics 
# that can be created as( it is the combination of the rows and the column )

# data2 = np.array([[1,2,3],[4,5,6]])
# print(data2)

# we can also crate the 3-D array
# it can be created as below 

# data3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(data3)
# print(type(data3))


# random number generation using the numpy 

# np.random.rand(arguments )  # get the 1-D array with the ramdom number 

# print(np.random.rand(5))

# np.random.rand(rows,columns) # to get the ramdom 2 - D array 

# print(np.random.rand(2,3)) # two rows and 3 columns 

# we can also generate the ramdom numbers array with the value in it normally distributed 
# np.random.randn(argument)

# data = np.arange(20,30)
# print(np.random.choice(data, size = 3 ))

# data = np.ones((2,2))
# print(data)



# generating the random numbers 
arr = np.integers(5,size = (2,4))
print(arr)



