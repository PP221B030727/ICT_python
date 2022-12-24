#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 6

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[30]:


headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://news.google.com/search?q=microsoft', headers = headers)
# print(resp.content)
soup = BeautifulSoup(resp.content)
print(resp.content)


# In[7]:


print(soup.prettify())


# In[11]:


for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    print(i.text)


# In[15]:


for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    print("https://news.google.com" + i['href'][1:])


# In[19]:


import datetime
for i in soup.find_all('time', class_ = "WW6dff uQIVzc Sksgp slhocf"):
    print(datetime.datetime.strptime(i['datetime'], "%Y-%m-%dT%H:%M:%SZ"))


# In[31]:


links = []
for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    links.append("https://news.google.com" + i['href'][1:])
print(links[0])
resp = requests.get(links[0], headers = headers)
# print(resp.content)
soup = BeautifulSoup(resp.content)
print(soup.find('a', jsname = "tljFtd").text)


# # Lecture 7 : Data cleaning

# In[32]:


#import
import pandas as pd


# In[33]:


# Read csv file into a pandas dataframe
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv")
print(df)


# ## Finding missing values

# In[34]:


#Find the standard missing values isnull function
print(df.isnull())


# In[84]:







# In[47]:


#Unexpected format missing values : check if value can be int for example
import numpy as np
for index, line in df.iterrows():
    try:
        int(line['OWN_OCCUPIED'])
        print(line['OWN_OCCUPIED'])
        df.loc[index, 'OWN_OCCUPIED'] = np.nan
    except:
        pass
print(df)


# In[49]:


#Check the sum of missing values
print(df.isnull().sum().sum())


# In[62]:


#YOUR TURN (15 minutes)
#Find all missing values in the provided dataframe
#Check all the null
#Find the other types of missing values
#There are '-', 'ERROR', wrong date, 'NaN', no data
#Until 18:10
na_values = ['-', 'ERROR']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\Apple_price_to_clean.csv",
                na_values = na_values,
                parse_dates = ['Date'])
print(type(df['Date'][0]))
# print(df.isnull().sum())


# ## Replacing missing values

# In[60]:


#delete lines with dropna with subset and inplace aeguments
df.dropna(inplace = True)
print(df)


# In[67]:


# Location based replacement with the loc function
print(df)
df = df.loc[6, 'OWN_OCCUPIED'] = 'Y'
# print(df)


# ## Replace missing values with a number (fillna() function with inplace arg)
# 

# In[73]:


#Replacing the missing values with a median 
#(calculate median and then use the replace with a number)
print(df['NUM_BEDROOMS'].mean())
df.fillna(int(df['NUM_BEDROOMS'].mean()), inplace = True)
print(df)


# In[75]:


#Replacing the values by the one before or after : df.fillna(method='bfill')
print(df)
df['NUM_BEDROOMS'] = df['NUM_BEDROOMS'].fillna(method = 'bfill')
print(df)


# In[ ]:


#YOUR TURN (5 minutes)
#replace all the missing values in the previous dataframe with the frontfilling method (check the pandas fillna() 
#method on docs)
#put 0 for the first ones
#18:25
df = df.fillna(method = 'ffill')


# ## Removing useless data

# In[79]:


#Use the drop() function with inplace and axis arg
print(df)
df = df.drop(['NUM_BATH'], axis = 1)
print(df)


# In[81]:


#Use the drop duplicates to remove useless lines
df = df.drop_duplicates()
print(df)


# In[83]:


#YOUR TURN (5 minutes)
#Drop all duplicates in your df
#check how many duplicates are in the csv files : check length before and after
#=> 18:35
na_values = ['-', 'ERROR']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\Apple_price_to_clean.csv",
                na_values = na_values)

print(df)
df = df.drop_duplicates()
print(df)


# ## Outliers

# In[90]:


#Read csv with clean data
na_value = ['na', '--']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv", na_values = na_value)
print(df)
df.dropna(inplace = True, subset = ['SQ_M'])
print(df)


# In[91]:


#With the describe method
print(df.describe())


# In[92]:


# With the plot method
df.plot(y = 'SQ_M')


# In[93]:


df = df[df['SQ_M'] < 10000]
df.plot(y = 'SQ_M')


# In[ ]:


#YOUR TURN (10 min)
#Find the outliers in your dataset and remove them
#=> 18:46

