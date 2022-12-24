#!/usr/bin/env python
# coding: utf-8

# # Lecture 9: Machine Learning

# In[2]:


pip install numpy


# In[3]:


pip install scikit-learn


# In[4]:


#import the packages (numpy and linear_model from scikit)
import numpy as np
import sklearn.linear_model as skmod


# ## Introduction to numpy

# In[7]:


#Create your fisrt numpy array in 1 dimension
list_ = [1,2,3,4,5]
print(list_)
arr = np.array([1,2,3,4,5])
print(arr)


# In[8]:


#Create your first 2 dimensionnal arry
arr = np.array([[1,2,3], [4,5,6]])
print(arr)


# In[9]:


#getting access to numpy array items
print(arr[0][2])


# In[12]:


#the copy and the view
list1 = [1,2,3]
list2 = list1.copy()
list2[0] = 25
print(list2)
print(list1)


# In[16]:


#the copy and the view
arr1 = np.array([1,2,3,4,5])
arr2 = arr1.view()
arr3 = arr1.copy()
arr2[0] = 25
arr3[0] = 100
print(arr1)
print(arr2)
print(arr3)


# In[18]:


#The shape of an array
arr = np.array([[1,2,3], [4,5,6]])
print(arr.shape)
print(arr)


# In[24]:


#reshape your array from 1D to 2D
arr1 = np.array([1,2,3,4,5,6])
print(arr1.shape)
print(arr1)
arr1 = arr1.reshape((3,2))
print(arr1.shape)
print(arr1)


# In[27]:


#reshape your array from 1D to another D (with -1)
arr1 = np.array([1,2,3,4,5,6])
print(arr1.shape)
print(arr1)
arr1 = arr1.reshape((-1,2))
print(arr1.shape)
print(arr1)


# In[28]:


#from line to column
arr1 = np.array([1,2,3,4,5,6])
print(arr1.shape)
print(arr1)
arr1 = arr1.reshape((-1,1))
print(arr1.shape)
print(arr1)


# In[32]:


#The avantage of numpy, the use of array for addition or multiplication for example
l1 = [1,2,3]
l1 = np.array(l1)
print(l1 + 2)
#
l1 = [1,2,3]
l1 = np.array(l1)
print(l1 * 2)


# In[33]:


#YOUR TURN (5 minutes)
#Change this array [1,5,9,31,45,78]
#into this one:
#[[1,5],
#[9,31],
#[45,78]]
#It should be a copy not a view
arr = np.array([1,5,9,31,45,78])
arr = arr.reshape((3,2))
print(arr)


# ## The linear regression

# In[38]:


#Transformation of data in the requiered array for scikit-learn
x = [1, 2.1, 3.5, 3.9, 5.3, 6]
print(x)
x = np.array(x)
print(x)
x = x.reshape((-1,1))
print(x)

y = [8,9,10,11,12,13]
print(y)
y = np.array(y)
print(y)
y = y.reshape((-1,1))
print(y)


# In[37]:


#Create a linear regression model: LinearRegression()
model = skmod.LinearRegression()


# In[ ]:


#some parameters than you can change:
#fit_intercept (consider b=0 if False, default is True)


# In[39]:


#Train your model
model_trained = model.fit(x, y)


# In[42]:


#get the result: the intercept (b)(.intercept_), the coeff (w1)(.coef_) and the R2 (.score(x, y))
#get b value
print(model.intercept_)
#get the coef : the w1 value
print(model.coef_)
#get the accuracy with R2
print(model.score(x, y))


# In[44]:


import matplotlib.pyplot as plt
plt.scatter(x, y)
x_model = [0, 6]
y_model = [0.98573038 * 0 + 6.91851296, 0.98573038 * 6 + 6.91851296]
plt.plot(x_model, y_model)


# In[46]:


#Now use your model to predict data (.predict(x))
x_model = np.array([0,6]).reshape(-1,1)
print(model.predict(x_model))


# In[47]:


#Predict the result without predict but with intercept and coeff
x_model = [0, 6]
y_model = [0.98573038 * 0 + 6.91851296, 0.98573038 * 6 + 6.91851296]
print(y_model)

