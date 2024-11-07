import pandas as pd 
import numpy as np 
# this data is from the googleplay store 
df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/googleplaystore.csv")
data_copy = df.copy()

# print(df)
# 
# our data fram over which we are going to do alalysis 

#                                                      App             Category  Rating Reviews                Size     Installs  Type Price Content Rating                     Genres      Last Updated         Current Ver         Android Ver
# 0         Photo Editor & Candy Camera & Grid & ScrapBook       ART_AND_DESIGN     4.1     159                 19M      10,000+  Free     0       Everyone               Art & Design   January 7, 2018               1.0.0        4.0.3 and up
# 1                                    Coloring book moana       ART_AND_DESIGN     3.9     967                 14M     500,000+  Free     0       Everyone  Art & Design;Pretend Play  January 15, 2018               2.0.0        4.0.3 and up
# 2      U Launcher Lite – FREE Live Cool Themes, Hide ...       ART_AND_DESIGN     4.7   87510                8.7M   5,000,000+  Free     0       Everyone               Art & Design    August 1, 2018               1.2.4        4.0.3 and up
# 3                                  Sketch - Draw & Paint       ART_AND_DESIGN     4.5  215644                 25M  50,000,000+  Free     0           Teen               Art & Design      June 8, 2018  Varies with device          4.2 and up
# 4                  Pixel Draw - Number Art Coloring Book       ART_AND_DESIGN     4.3     967                2.8M     100,000+  Free     0       Everyone    Art & Design;Creativity     June 20, 2018                 1.1          4.4 and up
# ...                                                  ...                  ...     ...     ...                 ...          ...   ...   ...            ...                        ...               ...                 ...                 ...
# 10836                                   Sya9a Maroc - FR               FAMILY     4.5      38                 53M       5,000+  Free     0       Everyone                  Education     July 25, 2017                1.48          4.1 and up
# 10837                   Fr. Mike Schmitz Audio Teachings               FAMILY     5.0       4                3.6M         100+  Free     0       Everyone                  Education      July 6, 2018                 1.0          4.1 and up
# 10838                             Parkinson Exercices FR              MEDICAL     NaN       3                9.5M       1,000+  Free     0       Everyone                    Medical  January 20, 2017                 1.0          2.2 and up
# 10839                      The SCP Foundation DB fr nn5n  BOOKS_AND_REFERENCE     4.5     114  Varies with device       1,000+  Free     0     Mature 17+          Books & Reference  January 19, 2015  Varies with device  Varies with device
# 10840      iHoroscope - 2018 Daily Horoscope & Astrology            LIFESTYLE     4.5  398307                 19M  10,000,000+  Free     0       Everyone                  Lifestyle     July 25, 2018  Varies with device  Varies with device

# steps for the data cleaning and analysis  

# data-->clean 
# first we clean the data 

# create a profile of the data 

# EDA 
# 1. we create general profile of the data 
# 2. statistics based analysis on top of data 
# 3. graph based analysis and making the conclusion from the data 



# analysis over the data / cleaning the data 


# print(df.info()) # will provide the information about the data(data type, count , number of rows ,etc  )
# print(df.describe(include = "all")) # will describe the data column wise on the basis of the mean, SD , quantile, etc

 
# dat = df['App'] # list of different apps in the app column 
# print(dat)

# dat = df['App'].unique() # unique apps in the column 
# print(dat )

# no of unique apps 
# dat = len(df['App'].unique())
# print(dat )


# checking is duplicate value is present in the data 
# print(df[df.duplicated()])  # gives the info about the duplicated rows in the data 



# observation on data after nanalysing 
# i have to delet the duplicated data 
#  i can  convert my reviews columns data type onto int 
# there is k ans M in the size column we have to convert them into the same format 
# correct the install column as well 
# rectifing the data to the respective format and data type for possible column 


# data = data_copy['Price'].unique() # getting info about the column we want to clean or make as per our requirement 
# print(data)

# Price column 
# ['0' '$4.99' '$3.99' '$6.99' '$1.49' '$2.99' '$7.99' '$5.99' '$3.49'
#  '$1.99' '$9.99' '$7.49' '$0.99' '$9.00' '$5.49' '$10.00' '$24.99'
#  '$11.99' '$79.99' '$16.99' '$14.99' '$1.00' '$29.99' '$12.99' '$2.49'
#  '$10.99' '$1.50' '$19.99' '$15.99' '$33.99' '$74.99' '$39.99' '$3.95'
#  '$4.49' '$1.70' '$8.99' '$2.00' '$3.88' '$25.99' '$399.99' '$17.99'
#  '$400.00' '$3.02' '$1.76' '$4.84' '$4.77' '$1.61' '$2.50' '$1.59' '$6.49'
#  '$1.29' '$5.00' '$13.99' '$299.99' '$379.99' '$37.99' '$18.99' '$389.99'
#  '$19.90' '$8.49' '$1.75' '$14.00' '$4.85' '$46.99' '$109.99' '$154.99'
#  '$3.08' '$2.59' '$4.80' '$1.96' '$19.40' '$3.90' '$4.59' '$15.46' '$3.04'
#  '$4.29' '$2.60' '$3.28' '$4.60' '$28.99' '$2.95' '$2.90' '$1.97'
#  '$200.00' '$89.99' '$2.56' '$30.99' '$3.61' '$394.99' '$1.26' 'Everyone'
#  '$1.20' '$1.04']

data_copy["Price"] = data_copy["Price"].str.replace("$","")
data_copy["Price"] = data_copy["Price"].str.replace("Everyone",str(np.nan))
data_copy["Price"] = data_copy["Price"].astype("float")

# matching the data of the column size to the single unite 
# here we assume 1M = 1000
data_copy["Size"] = data_copy["Size"].str.replace("M","000") # converting mb into kb 
data_copy["Size"] = data_copy["Size"].str.replace("k","")
data_copy["Size"] = data_copy["Size"].str.replace('Varies with device', str(np.nan)) # non numeroic data concertes to nan 
data_copy["Size"] = data_copy["Size"].str.replace("1,000+",str(np.nan))
data_copy["Size"] = data_copy["Size"].astype("float")

# print(data_copy["Size"].unique()) # to see the optimized Size column 


# correcting the curernt version column to get the numeric value 
data_copy["Current Ver"] = data_copy["Current Ver"].str.replace("Varies with device", str(np.nan))

# print(data_copy["Current Ver"].isnull().sum())  # getting the info about the null value in the column 


# correcting the androis ver ccolumn as per our requirement 
data_copy["Android Ver"] = data_copy["Android Ver"].str.replace("and up","")
data_copy["Android Ver"] = data_copy["Android Ver"].str.replace("Varies with device", str(np.nan))
data_copy["Android Ver"] = data_copy["Android Ver"].str.replace("W","")
# print(data_copy["Android Ver"].unique())

# correcting the Install colimn 
data_copy["Installs"] = data_copy["Installs"].str.replace("+","")
data_copy["Installs"] = data_copy["Installs"].str.replace(",","")
# print(data_copy["Installs"].unique())
data_copy["Installs"] = data_copy["Installs"].str.replace("Free",str(np.nan))
data_copy["Installs"] = data_copy["Installs"].astype("float")
# print(data_copy["Installs"].unique())

# Convert the date column to datetime format
data_copy['Last Updated'] = pd.to_datetime(data_copy['Last Updated'], format='%B %d, %Y',errors='coerce')
# print(data_copy.loc[1348 ,"Last Updated"])

# Extract year, month, and day into separate columns
data_copy['year'] = data_copy['Last Updated'].dt.year
data_copy['month'] = data_copy['Last Updated'].dt.month
data_copy['day'] = data_copy['Last Updated'].dt.day

#saving the cleaned data to the new csv file 
data_copy.to_csv("cleaned_googleplaystore_data.csv", index= False)