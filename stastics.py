import pandas as pd 
import numpy as np 
from statistics import mode 
import statistics 
# data2 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")
# # print(data)

data1 = [23,24,32,45,12,43,67,45,32,56,32]
# print(data1)

# data3 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Titanic.csv")
# # print(data3)

# library required for the statistic pratical implement in python 
# scipy
# statmodel 
# statistics
# pandas 
# numpy
# matplotlib 
# seaborn

data_copy = data1.copy()
# store = np.mean(data1)
# print(store)

# calculating mean by using the logic 
# s=0
# for i in data_copy:
#     s= s+i
#     mean = s/len(data_copy)
# print(mean)

# simple way 
# print(sum(data_copy)/len(data_copy))


# print(np.median(data_copy))
# print(mode(data_copy))
# print(np.var(data_copy)) # population variance 
# print(statistics.variance(data_copy)) # sample variance 


# print(np.random.choice(11,20))  # for generating the 20  numbers array from 0 to 11

# print(np.random.randint(10,20,50)) # generate the random 50 integers between the 10 and 20 


# value1 = statistics.pvariance(data_copy) # population variance 
# value2 = statistics.variance(data_copy) # sample variance 
# print(value1,value2,sep="\n")


# logic for the variance without using the statistics library avilable function 
# def var(data):
#     n = len(data)
#     mean = sum(data)/n
#     deviation = [(x-mean)**2 for x in data]
#     variance = sum(deviation)/(n-1)   # in the place of the n-1 if we use n only then we get the population variance 
#     return variance # this variance is the sample variance 

# print(var(data_copy))


# using the numpy library 
# print(np.var(data_copy))   # this is populaltion variance 


# standard deviation 
# it is the square root of the variance 

# print(np.std(data_copy)) # numpy 

# print(statistics.stdev(data_copy)) #  sample std ( using the statistics library)
# print(statistics.pstdev(data_copy)) # population std 

# correlation and coverianc
# sample and population 
# central limit theorem 

# correlation and coveriance 
# I am using the data2 at the begning phase of the program 

# data2 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")
# print(data2)

# correlation 
# print(data2.corr(method="pearson",numeric_only=True))  # numeric_only ignore the non numeric column in the dadaframe

# print(np.cov(data2.drop(['Species'],axis=1))) # drop helps to ignore the non numeric value holding column  species in the dataframe 





