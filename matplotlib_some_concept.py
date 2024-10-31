import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()

# fig, ax = plt.subplots()
# plt.show()



# scatter plot

# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()

# Deacription behind the graph colour pattern and the plot 

# the main line of code :- ax.scatter('a', 'b', c='c', s='d', data=data):
# 'a' is used for the x-axis values.
# 'b' is used for the y-axis values.
# c='c': The color of the points is determined by the values in 'c'. Each point gets a different color based on its corresponding value in 'c'.
# s='d': The size of each point is determined by the corresponding value in 'd'. Larger values of 'd' create larger circles.
# data=data: This tells scatter() to look for 'a', 'b', 'c', and 'd' in the data dictionary.


  
# data2 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")
# print(data2)
# df = pd.DataFrame(data2)
# print(df)

# data3 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Titanic.csv")
# print(data3)
# df2 = pd.DataFrame(data3)
# print(df2)

# Different plots for data viziulization 
# line 
# scatter plot 
# histogram 
# Pie 
# box
# violin 
# heatmap 
# 3d plot 

# line plot of the different column in the dataframe 

# data2['SepalLengthCm'].plot()
# data2['SepalWidthCm'].plot()
# data2['PetalLengthCm'].plot()
# data2['PetalWidthCm'].plot()
# plt.show()

# plot 
# univariate - single variable(column )
# bivariate - two column 
# multivariate - more than 3 columns 

# variable wise or column wise 

# numerical variable 
# catagorical variable 


# dimension  
# 2-D  plot 
# 2-d plot 

# bar graph 
# data3['Pclass'].plot(kind= 'bar') # data from the above dataframe of data3
# plt.show()

# print(data3['Pclass'].value_counts()) # it gives the info about the number of the class in the datacolunm 

# histogarm 
# data3['Pclass'].plot(kind= 'hist') it gives the garph about the frequency of the class inside the variable 
# plt.show()

# pie chart 

# data3['Pclass'].plot(kind = 'pie')
# plt.show()

# x = np.linspace(0,10, 100)
# y = np.sin(x)
# # # print(x)
# # plt.plot(x) #line plot with respect to the value of x
# # plt.plot(y) #sine wave plot with respect to the value of the sine of x 
# # plt.show() #to show the graph 

# fig, ax = plt.subplots()
# ax.plot(x,y)

# ax.set(xlabel = 'x',ylabel = 'sin(x)',title = 'sine wave ')
# plt.show()

# scatter plot 

# x = np.random.randn(100)
# y = np.random.randn(100)

# fig,ax= plt.subplots()

# ax.scatter(x,y)
# ax.set(xlabel = "x-axis",ylabel = "Y- axis ")
# ax.set_title("scatter plot ")
# plt.show()

# bivariate analysis 
# x-num y- num
# x-num y- cat 
# x- cat y- cat 
# x- cat y- num 


# x = ["A","B","C","D","E"] # catagorical data
# y= [5,4,6,3,8] # numeric data 

# fig,ax= plt.subplots() 

# ax.bar(x,y)

# ax.set(xlabel = "x-axis(x)",ylabel = "Y- axis(y) ")
# ax.set_title("bar plot ")
# plt.show()


# taking real world scenario 
data3 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Titanic.csv")
# print(data3) 


# first set
# x = data3["Pclass"]
# y = data3["Fare"]

# fig,ax= plt.subplots() 

# ax.bar(x,y)

# ax.set(xlabel = "x-axis(Pclass)",ylabel = "Y- axis(Fare) ")
# ax.set_title("bar plot ")
# plt.show()


# second set 
# x = data3["Pclass"]
# y = data3["Age"]

# fig,ax= plt.subplots() 

# ax.bar(x,y)

# ax.set(xlabel = "x-axis(Pclass)",ylabel = "Y- axis(Age) ")
# ax.set_title("bar plot ")
# plt.show()



# another plot example of data from the data set 
# univariate plot 

# x = data3["Age"]

# fig,ax= plt.subplots() 

# ax.hist(x)

# ax.set(xlabel = "x-axis(Age)",ylabel = "Y- axis(Frequency) ")
# ax.set_title("histogram plot ")
# plt.show()

# 3-D plots using matplotlib1

# Make data
# np.random.seed(19680801) # helps to garnerate the numbers same everytime same when the random function is used to generate number 
# n = 100
# rng = np.random.default_rng()
# xs = rng.uniform(23, 32, n)
# ys = rng.uniform(0, 100, n)
# zs = rng.uniform(-50, -25, n)

# # Plot
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.scatter(xs, ys, zs)

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# plt.show()


# x = np.outer(np.linspace(-2, 2, 50), np.ones(50))
# y = x.copy().T # transpose of the data x
# z = np.cos(x**2 + y**2)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')

# ax.plot_surface(x,y,z)
# plt.show()



