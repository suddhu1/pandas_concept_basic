import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# data_frame = pd.DataFrame()
# print(type(data_frame))
# to create the data frame we can use List 
# dict 
# series 
# numpy arrray 


# List

# using the list to create the data frame 
# examples 


# data = [1,2,3,4,5]
# print(pd.DataFrame(data))

# output of the above code 
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5

# the 0 in the top refers to the column index 
# and the left most coumn represent the rows index 

# example 2

# data2 = [["sudarshan",21],["aayush",20],["prabhat",23]]
# print(pd.DataFrame(data2))

# output of the above code 
# in row and coulumn format 

#      0        1
# 0  sudarshan  21
# 1     aayush  20
# 2    prabhat  23

# data22 = [["sudarshan",21],["aayush",20],["prabhat",23]]
# data_frame22 = pd.DataFrame(data22,columns=["Name","Age"])
# print(data_frame22)

# output of the above code:

#         Name  Age
# 0  sudarshan   21
# 1     aayush   20
# 2    prabhat   23

# data23 = [["sudarshan",21],["aayush",20],["prabhat",23]]
# data_frame23 = pd.DataFrame(data23,columns=["Name","Age"],index=["first","second","third"])
# print(data_frame23)

#  output of the above code 

#           Name      Age
# first   sudarshan   21
# second     aayush   20
# third     prabhat   23



# using the dictonary( dict )

# data3 = {"name":["sudarshan","aayush","prabhat"], "Age":[21,20,22]}
# print(pd.DataFrame(data3))

# output of the above code 

#         name  Age
# 0  sudarshan   21
# 1     aayush   20
# 2    prabhat   22

# data4 = [{"sudarshan":21,"aayush":20},{"prabhat":22,"rajiv":21}]
# print(pd.DataFrame(data4))

#    sudarshan  aayush  prabhat  rajiv
# 0       21.0    20.0      NaN    NaN
# 1        NaN     NaN     22.0   21.0


# data5 = [{"sudarshan":21,"aayush":20},{"sudarshan":22,"aayush":21}]
# print(pd.DataFrame(data5))

#    sudarshan  aayush
# 0         21      20
# 1         22      21


  
# reading the data from the external files in the dataframe using the pandas


# data = pd.read_csv("test.csv")
# pd.DataFrame(data)

# reading the table from the top by default it will reade 5 rows 
# if we want less or more we can especify usinf n=integer in paramater 
# print(data.head()) 


# Select the columns using .iloc (rows: all, columns: first two)
# column_access_of  = data.iloc[:,:2]
# print (column_access_of)


# # taking the sample data from the list of the data in large amount

# sampless = data.sample()      # by default it will give the only one row 
# sampless = data.sample(n=3)   # it will pick randome 3( specified ) columns from the dataframe 
# print(sampless)               # printing the data sample selected 


# numpy and the pandas 

# storage = np.random.randn(5,3) # method from the numpy 
# storage2 = pd.DataFrame(storage) # fron  pandas datafram facility 
# print(storage) # gives the ramdom values table of 5 rows and the 3 column 
# print(storage2) # converts the above data into the row and the column format with index

# print(storage2.apply(np.mean)) # provides the mean value of each column 
# print(storage2.apply(np.median)) # provides the median of each column 
# print(storage2.apply(lambda x: x.max())) # maximum value of each column 
# print(storage2.apply(lambda y: y.min())) # minimun value of the each column
# print(storage2.axes)  # if the row and the column index have the name then the name  of the index will be shown 

# print(storage2[data.iloc[:,:2]].apply(lambda x:x+100))   need to work in this statement 

# using the map function and the lambda function in the program 

# storage2.iloc[:,1] = storage2.iloc[:,1].map(lambda x: x+100)
# print(storage2.iloc[:,1])



# reindex function of pandas 
#  it create the new index with the nan value until we are not passing the logic for filling the value 


# data = {"name":["sudarshan","aayush","prabhat"], "Age":[21,20,22]}
# df = pd.DataFrame(data, index = ['r1',"r2",'r3'])
# # print(df)
# df2 = df.reindex(["r1",'raw2',"r3"])
# print(df2)

# df2 = df.reindex(["r1",'raw2',"r3"],fill_value="pending")
# print(df2)


# slicing the data from the dataframe 
# loc(location )
# iloc(int location )

# dataframe = np.random.rand(8,4)
# df = pd.DataFrame(dataframe,index=['a','b','c','d','e','f','g','h'], columns=['A','B','C','D'])
# print(df)


# df.loc[row,columns]

# df2 = df.loc[: ,['A','B']] # accessing the column/slicing the column 
# print(df2)

# df3 = df.loc[['a','b'],['A','B']] # slicing the both the rows and the columns 
# print(df3)


# same with the iloc function also but in the 
# plce of the index name we use index integer place 



# merge and the joins 

# conbining the two or more dataframes 
# join =  conbine the datafram based on the index ( left join by default )
# merge = combine the dataframe based on the key( column )( inner join by default)

# create sample data 

# data1 = {'A':[1,2,3],'B':[4,5,6]}
# df1 = pd.DataFrame(data1,index=['a','b','c'])

# data2 ={'C':[10,20,30],'D':[40,50,60]}
# df2 = pd.DataFrame(data2,index=['a','c','d'])

# check with the sample data 
# print(data1,data2)
# print(df1,df2,sep='\n\n')

# storage = df1.join(df2)
# print (storage )  
#    A  B     C     D
# a  1  4  10.0  40.0
# b  2  5   NaN   NaN  # we are not getting the  value for the b row because the b row is not in the data2 
# c  3  6  20.0  50.0
# we do not get d row because the in left join the only the common on the both dataframe is joined and the noncommon element id ignored 


# merge 
# data1 = {'A':[1,2,3],'B':[4,5,6],'key':['a','b','c']}
# df1 = pd.DataFrame(data1)

# data2 ={'C':[10,20,30],'D':[40,50,60],'key':['a','c','d']}
# df2 = pd.DataFrame(data2)

# print(pd.merge(df1,df2))
#    A  B key   C   D
# 0  1  4   a  10  40
# 1  3  6   c  20  50



# left= pd.DataFrame({
#     'name': ['John Doe', 'Jane Smith', 'Emily Lee', 'Mark Brown', 'Lucy Grey'],
#     'id': [101, 102, 103, 104, 105],
#     'subject': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English']
# })


# right = pd.DataFrame(
#     {'name': ['Alex Green', 'Sara White', 'Tom Black', 'Kate Blue', 'Harry Stone'],
#     'id': [201, 202, 203, 204, 205],
#     'subject': ['Computer Science', 'Mathematics', 'Physics', 'History', 'Chemistry']
# })


# storage = pd.merge(left,right,on=["subject"])  # merge will be done on the basis of the subject name 
# print(storage) 


# data3 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Titanic.csv")
# print(data3)

data2 = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/Iris.csv")
# print(data2)
df = pd.DataFrame(data2)
# different plot for graph analysis of the data
# line, 
# scatter plot
# Bar plot 
# histogram 
# pie 
# box
# violine 
# heatmap 
# 3d plot 

df['SepalLengthCm'].plot()

plt.show()
