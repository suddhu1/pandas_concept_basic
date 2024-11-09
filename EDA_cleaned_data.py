import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# data = pd.read_csv("cleaned_googleplaystore_data.csv")
# print(data )

# data_copy = data.copy()
# data_copy = data_copy.drop_duplicates(subset=['App'],keep="first")
# data_copy = data_copy.reset_index(drop=True)

# print(data_copy.info())
# print(data_copy)

# print(data_copy["Category"].unique())
# index_values = data_copy.index[data_copy['Category'] == '1.9'].tolist()
# print(index_values)
# data_copy = data_copy.drop(data_copy.index[index_values])
# data_copy = data_copy.reset_index(drop=True)
# print(data_copy.groupby(["Category"])["Installs"].sum().sort_values(ascending=False))  # to get the info about the category with the most instal


# doing analysis 
# df_cat_install = data_copy.groupby(["Category"])["Installs"].sum().sort_values(ascending=False)[:10]
# df_cat_install = df_cat_install.reset_index()
# print(df_cat_install)

# visiulation of the analysis 
# sns.barplot(x="Installs",y="Category",data = df_cat_install)
# plt.show()

# top 5 app in the catagory with the most installs (multivariate analysis )
# df_cat_app_install  = data_copy.groupby(["Category","App"])["Installs"].sum().reset_index()
# print(df_cat_app_install)

# print(df_cat_app_install[df_cat_app_install["Category"]=="ART_AND_DESIGN"].sort_values(ascending=False,by="Installs")[ : 5]) # can be done same with all the others category


# apps = ['GAME','COMMUNICATION','PRODUCTIVITY','SOCIAL']
# sns.set_context("poster")
# sns.set_style("darkgrid")

# plt.figure(figsize=(10,30))

# for i,app in enumerate(apps):
#     df2 = df_cat_app_install[df_cat_app_install == app].sort_values(ascending=False,by="Installs")[:5]
#     df3 = df2.head(5)
#     plt.subplot(4,2,i+1)
#     sns.barplot(data=df3,x="Installs",y="App")
#     plt.xlabel('Installatioin in Millions')
#     plt.ylabel('')
#     plt.title(app,size = 20)

# plt.tight_layout()
# plt.subplots_adjust(hspace= .3)
# plt.show() 