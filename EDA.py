import pandas as pd 
# this data is from the googleplay store 
df = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-CompleteGuide/refs/heads/main/googleplaystore.csv")
print(df)
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


# deleting duplicate data 
data = df.drop_duplicates( ) # dropping the duplicate value and storing the unique in the data variable 
# print(df.shape) # shape of orginal daraframe 
# print(data.shape) # shape of dataframe after cleaning the duplicate value 


# converting the datatype of the reviews column into the int type 



