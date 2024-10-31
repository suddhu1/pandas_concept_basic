import math 
import pandas as pd 
import numpy as np 
from numpy.random import randn
from statistics import mode 
from statsmodels.stats.weightstats import ztest
import statistics 
import seaborn as sns 
import matplotlib.pyplot as plt 
import scipy.stats as stat 
import pylab
from scipy import stats 
from scipy.stats import chi2
# data2 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")
# # print(data)

# data1 = [23,24,32,45,12,43,67,45,32,56,32]
# print(data1)

# data3 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Titanic.csv")
# print(data3)

# library required for the statistic pratical implement in python 
# scipy
# statmodel 
# statistics
# pandas 
# numpy
# matplotlib 
# seaborn

# data_copy = data1.copy()
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



# distribution of the data 

# to chaeck the nornality of the data 
# z-test 
# t-test 
# chi-test
# anova test (f test)



# to check the distribution of the dat 

# data = [23,24,32,45,12,43,67,32,56,32] # data define 
# data_copy = data.copy() # making copy of the data 

# sns.histplot(data=data_copy, kde = True)
# plt.show()
# sns.histplot(data_copy, kde=True, stat="density")  # Histogram with KDE overlay
# plt.show()

# Using kdeplot separately
# sns.kdeplot(data_copy)
# plt.show()

# Using displot for combined options
# sns.displot(data_copy, kde=True)
# plt.show()


# data 
# df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")

# sns.histplot(df["SepalLengthCm"],kde = True) # checking the distribution of the data 
# plt.show()


# sns.histplot(df["SepalWidthCm"],kde = True)
# plt.show()


# log normal data 
# creating lognormal data 
# sample = np.random.lognormal(mean= 23.0, sigma= 2.0, size= 100)

# plotting of the data generated 
# sns.histplot(sample,kde = True)
# plt.show()

# if we take the log(lognormal data ) then we get the normally distributed data 

# plotting the data converting the lognormal data into the normal dist data 
# sns.histplot(np.log(sample))
# plt.show()


#  Q-Q plot (Quantile - Quantile plot )
# In Q-Q plot there is the red line in the plot. if the data is above the red line the data is normally distributed

# def plot_data(sample):
#     plt.figure(figsize=(10,8))
#     plt.subplot(1,2,1)
#     sns.histplot(sample,kde=True)
#     plt.subplot(1,2,2)
#     stat.probplot(sample,dist= "norm", plot=pylab  )
#     plt.show()

# plot_data(np.log(sample))


# df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")

# def plot_data(sample):
#     plt.figure(figsize=(10,8))
#     plt.subplot(1,2,1)
#     sns.histplot(sample,kde=True)
#     plt.subplot(1,2,2)
#     stat.probplot(sample,dist= "norm", plot=pylab  )
#     plt.show()

# plot_data((df["PetalWidthCm"]))




# different test for checking the normality of the data 

# df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")


# result = stats.shapiro(df["SepalWidthCm"]) # it gives the pvalue of the data 
# print(result) 

# output
# ShapiroResult(statistic=np.float64(0.9837916445014413), pvalue=np.float64(0.07517918532015967))
# if pvalue<0.05:
#     print("reject the null hypothesis ")
# else:
#     print("accept the null hypothesis")



# checling the normality of the SepalWidthCm fron the data on the basis of the pvalue of the data 
# result = stats.shapiro(df["SepalWidthCm"]) # we can perform the same test with the stats.normaltest() and stats.anderson()
# if result.pvalue<0.05:
#     print("reject the null hypothesis ")
# else:
#     print("accept the null hypothesis") # null hypothesis is our data is normally distributed  


# different stats test 

# z-test 
# t-test 
# chi-square
# anova test 




# how to know wether to accept or reject the hpothesis 

# if zscore > critical_value :    
#     print("reject")
# if zscore < critical_value :
#     print("accept ")

# the critical_value can be knowm from the help of the z-score table 


# some nedded library for the tests 

# import math 
# import pandas as pd 
# import numpy as np 
# from numpy.random import randn
# from statistics import mode 
# from statsmodels.stats.weightstats import ztest
# import statistics
# from scipy import stats  


# implementing the z_test in the python example  
# mean_iq = 110
# sd_iq = 15/math.sqrt(50)
# alpha = 0.05
# null_hupothesis_mean = 100
# # generating random data based on the mean_id and sample size 
# data = randn(50)+ mean_iq
# z_stat,p_value = ztest(data,value=null_hupothesis_mean, alternative='larger' )
# if p_value <= 0.05:
#     print(" reject  ")
# else:
#     print("accept ")


# implementing the t_test 

# types of t test 
# one sample t test ( with respect to one independent sample )
# two- sample t test ( w.r.t two independent sample )
# paired t- test (two sample from the same population on different time inteval )

# example

# creating data 

# one sample 

# my_cricket_score = [22,45,23,55,66,42,68,23,12,53,31,12,21,45,23,5,23,54,23,10]
# mean_score = np.mean(my_cricket_score)
# null_hypothesis = mean_score
# t_stat,p_value = stats.ttest_1samp(my_cricket_score,Value=null_hypothesis)
# if p_value <= 0.05:
#     print(" reject  ")
# else:
#     print("accept ")


# Paired t-test 

# my_total_cric_score_innings = np.random.randint(20,90,100)
# sample1 = np.random.choice(my_total_cric_score_innings,20)
# sample2 = np.random.choice(my_total_cric_score_innings,20)
# mean1= np.mean(sample1)
# mean2= np.mean(sample2)
# # print(sample1,sample2,sep="\n")


# t_stat,p_value = stats.ttest_rel(sample1,sample2)
# print(p_value)
# if p_value <= 0.05:
#     print(" reject  ")
# else:
#     print("accept ")


# Chi-square test 
# Chi-square test id done over the catagorical data 

df = sns.load_dataset("tips") # loding the dataset using the seaborn function 
# print(df.info())
# print(df[['sex','smoker']])
# print(df['sex'].value_counts())
# print(df['smoker'].value_counts())
data_table = pd.crosstab(df['sex'],df['smoker'])
data_array = data_table.values 
stats_test,p,dof,Expected_values = stats.chi2_contingency(data_array)
# print(Expected_values)
# print(data_array)

# Zippinf the obsserved and the expected values 
# for o,e in zip(data_array,Expected_values):
    # print(((o - e)**2)/e)
    # print(o,e)


# # for i in zip(data_array,Expected_values):
# #     print(i)

chisquare_test = sum([(o-e)**2/e for o,e in zip(data_array,Expected_values)])
print(sum(chisquare_test))

dof = 1 
alpha = 0.05

print(chi2.ppf(1-alpha, df = dof ))

