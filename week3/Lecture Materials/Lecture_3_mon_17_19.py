#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# from 22 september to 2 october included => online classes/videos


# # Creating a DataFrame

# In[1]:


import pandas as pd


# ## Using a dictionnary

# In[ ]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
# Taste : 5, 6, 9, 8
# Sugar content : 'high', 'high', 'high', 'low'
# YOUR TURN : Create a dataframe from the dictionnary (10 minutes)
#1st create a dcitionnary dictio = {'key' : value(list here)}
#2nd pd.DataFrame(dictio)
# Do not call a dicitonary "dict" (it's like float, int, string, ...)
# 5/10 minutes => 17:20


# In[7]:


# Create the dictionnary
dictio = {
    "Brand" : ['Coca', 'pepsi', 'Sprite', 'water'],
    "Taste" : [5, 6, 9, 8],
    "Sugar_content" : ['high', 'high', 'high', 'low']
}
print(dictio)


# In[8]:


# Create the dataframe
df = pd.DataFrame(dictio)
print(df)


# In[11]:


# Take csv data to dictionnary adn create dataframe
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    df= pd.DataFrame(csvfile)
print(df)


# ## Using a list

# In[ ]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
#Taste : 5, 6, 9, 8
#Sgar content : 'high', 'high', 'high', 'low'
#YOUR TURN : 
#Create a dtaframe from the lists


# In[14]:


# Create the lists
brand = ['Coca', 'pepsi', 'Sprite', 'water']
taste = [5, 6, 9, 8]
sugar_content = ['high', 'high', 'high', 'low']


# In[15]:


#Create dataframe from lists
# with pd.DataFrame()
df = pd.DataFrame([brand, taste, sugar_content])
print(df)


# In[19]:


#The zip function
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped_list = list(zip(a,b))
print(zipped_list)


# In[20]:


zipped_list = list(zip(brand,taste))
print(zipped_list)


# In[23]:


#YOUR TURN
# Come back to your previous dataframe and use the zip function (5 minutes) : 17:35
print(brand)
df = pd.DataFrame(list(zip(brand, taste, sugar_content)), columns = ['brand', 'taste', 'sugar'])
print(df)


# In[26]:


#With the csv file (easier)
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.reader(file)
    column_names = csvfile.__next__()
    
    df = pd.DataFrame(csvfile, columns = column_names)
    
print(df)


# ## Using read_csv method

# In[27]:


#create dataframe from read_csv method
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv")
print(df)


# In[29]:


#datetime object?
print(type(df['Date'][0]))


# In[95]:


# with the date in datetime object
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 
                 parse_dates = ["Date"])
print(type(df['Date'][0]))


# # Modify the dataframe

# In[53]:


# Change the column names (2 methods)
df.columns = ['Date', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Adj Close', 'Volume']
# print(df)
#with rename method
df = df.rename(columns = {'Date' : 'Date_and_time'})
print(df)


# In[54]:


#sort values
df = df.sort_values('Open_price')
print(df)


# In[55]:


# Reset index of dataframe
df = df.reset_index(drop = True)
print(df)


# In[59]:


#Use your own index: (set_index function)
df = df.set_index(['Date'])
print(df)


# In[64]:


# use several indexes
df = df.set_index(['Date', 'Open'])
print(df)


# In[ ]:


#Your TURN
#Use your csv data to get your df and put dates as index (10 minutes) 18:00


# In[65]:


# Why indexes and not columns (use %timeit function)
# get_ipython().run_line_magic('timeit', "print('hi')")


# In[71]:


# print(df)
# get_ipython().run_line_magic('timeit', "data = df[df['Open'] == 28.057501]")


# In[72]:


# get_ipython().run_line_magic('timeit', 'data = df.loc[2]')


# In[74]:


#display columns of dataframe (2 methods)
# print(df['Date'])
# print(df.Sugar content)


# In[77]:


#Adding a new columns to your DataFrame
df['Name'] = ['Gaétan' for i in range(0,1763)]
df['Surname'] = 'Chardon'
print(df)


# In[82]:


# Apply a function to your dataframe
def foo(x):
    return x*8
df['Open'] = df['Open'].apply(foo)
print(df)


# In[86]:


# iterate on a Dataframe
for index, item in df.iterrows():
    print(item['Date'])


# In[87]:


# Concatenate two dataframes
df = pd.concat([df, df])
print(df)


# In[88]:


for index, item in df.iterrows():
    print(index)


# In[89]:


dictio = {
    "Brand" : ['Coca', 'pepsi', 'Sprite', 'water'],
    "Taste" : [5, 6, 9, 8],
    "Sugar_content" : ['high', 'high', 'high', 'low']
}
df1 = pd.DataFrame(dictio)
df = pd.concat([df1, df1])
print(df)


# In[90]:


# Delete the duplicate drop_duplicates function (see doc)
df = df.drop_duplicates()
print(df)


# # Save the Dataframe

# In[91]:


#Save it to excel
writer = pd.ExcelWriter(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.xlsx")
df.to_excel(writer, 'DataFrame')
writer.save()


# In[94]:


#SAve it to csv
df.to_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.csv", index = False)


# In[93]:


# save it to json
df.to_json(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.json")


# # Useful functions

# In[96]:


print(df)


# In[98]:


# Getting info about the dataframe
print(df.info())


# In[99]:


# Getting shapes of dataframe
print(df.shape)


# In[100]:


# description of the dataframe
print(df.describe())


# In[101]:


# Count similar values (.value_counts() method)
print(df.value_counts('Open'))


# In[102]:


# get correlation
print(df.corr())


# In[104]:


# Quick plotting
df.plot(x = 'Date', y = ['Open', 'High'])


# In[ ]:


#YOUR TURN 
#Plot the evolution of volume exchanged through the time of your csv file (10 minutes) => 18:37
#pip install matplotlib 
#(required for plotting)

