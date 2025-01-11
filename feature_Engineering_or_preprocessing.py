import pandas as pd 
import numpy as np


df = pd.DataFrame({'A':[1,2,np.nan,4],
                   'B': [5,np.nan,7,8],
                   'C':[9,10,11,np.nan]})

# print(df)
 
# Handling the nan values 

# different ways of filling the nan place in the dataframe 

# print(df.fillna(0)) # filling with zeros 

# df.fillna(df.mean()) # filling with the mean value of  that column 

# we can also fill with median also in the same way 

# backwarda and the forward finall :- backward fill fill the nan value with the value after the nan in the column 
# and the forwarfill fill the nan value place with the value before the nan 


# df.fillna(method= 'bfill') # for backward fill 
# df.fillna(method = 'ffill') # for forward fill 




# outlier based problem example 

# a sample DataFrame with outliers 

df = pd.DataFrame({'A':[1,2,3,4,5,6,100],
                   'B':[10,20,30,40,50,60,700],
                   'C':[100,200,300,400,500,600,7000]})



threshold = 0.95
df = df[(df>=df.quantile(1-threshold)).all(axis=1) & (df <= df.quantile(threshold)).all(axis=1)]
print(df)

