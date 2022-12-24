import pandas as pd

df = pd.read_csv(r'C:\Users\user\Desktop\ICT\week1\Lecture_Materials\Apple_price_csv.csv')
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

