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


# array of range 
# arr = np.arange(0,10,2) # np.arange(start,stop,step)
# print(arr) # [0,2,4,6,8]


# Zeros (all element in the 2-D array i.e matrix is only zeros) and Ones( all the element in the matrix is one)

# zeros = np.zeros((2,3))
# ones = np.ones((3,2))
# print(zeros)
# print(ones)

# Array attributes - it provides the info about the array's propertis 

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape) # rows and the column of the 2-D array and also the depth in the 3-D array  
# print(arr.ndim) # dimension of the array 
# print(arr.size) # total number of the elements in the array 
# print(arr.dtype) # data type of the element in the array 


#  Indexing and the Slicing - it allow to access parts of an array 

#  Basic Indexing 
# arr = np.array([10,20,30,40])
# print(arr[0])  # first element
# print(arr[-1]) #  last element
# print(arr[1]) #  second element


# Slicing  

# arr = np.array([1,2,3,4,5])
# # print(arr[start:end])
# print(arr[1:3]) # element between the index 1 and 3  including element at index 1 
# print(arr[1:]) #all the element from index one to the last of array
# print(arr[:-1]) # all the element from from to last except the last element 

# Basic operations 
# NumPy performs element-wise operations much faster than loops in regular Python 

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1 + arr2) # add the element at the respective index of the two array
# print(arr1 * arr2) # it do the multiplication of the element of the respective index

# print(arr1 + 12) # add 12 to the each element of the array (also called as broadcasting )

# Shape Manipulation 

# Reshape 

# while doing the reshaping the new shape of array must able to conatin the element of the old array 
# product of the row and column of the reshaped array must be equal to the size of the old array 
# arr = np.array([1,2,3,4,5,6])
# reshaped_arr = arr.reshape(2,3) # here the product of the 2 and 3 is 6 which is the size of the old array 
# print(reshaped_arr)

# reshaped_arr2 = arr.reshape(3,2,1) # it will reshape the array into the 3-D array 
# print(reshaped_arr2)


# Flatten and Ravel 
# both helps to reshape the array but flatten makes the copy of the data but the ravel only provides the view of original data 
# ravel doesn't copy the data 

# arr = np.array([[1,2], [3,4]])
# flattened = arr.flatten()
# print(flattened)
# test = arr.ravel()
# print(test)


# Aggregate functions 

# some aggegrate function avilable in the NumPy are 
# sum, meam, Min and Max 
# arr = np.array([1,2,3,4,5])
# print(arr.sum()) 
# print(arr.mean()) 
# print(arr.min()) 
# print(arr.max()) 

# Matrix Oprtions

# matrix1 = np.array([[1,2],[3,4]])
# matrix2 = np.array([[5,6],[7,8]])

# matrix multiplication (np.dot())
# result = np.dot(matrix1, matrix2)
# print(result)

# trnspose of matrix (matrix_name.T)
# trans = matrix2.T
# print(trans)

# inverse of the matrix  (np.linalg.inv(matrix_name))
# inverse = np.linalg.inv(matrix1)
# print(inverse)

# Eigenvalues and the Eigenvectors of a square matrix 
# eigvals, eigvecs = np.linalg.eig(matrix1)
# print(eigvals,eigvecs,sep = "\n")

# Broadcasting in NumPy 
# Broadcasting allows NumPy to work with arrays of different shapes during arithmetic operations
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([[1], [2], [3]])

# broadcasted_sum = arr1 + arr2
# print(broadcasted_sum)
# arr1 (shape (1,3)) and arr2 (shape (3, 1)) are broadcast to compatible shapes (3, 3) for element-wise addition
# output
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]
# how = 
# First row: [1, 2, 3] + [1, 1, 1] = [2, 3, 4]
# Second row: [1, 2, 3] + [2, 2, 2] = [3, 4, 5]
# Third row: [1, 2, 3] + [3, 3, 3] = [4, 5, 6]
