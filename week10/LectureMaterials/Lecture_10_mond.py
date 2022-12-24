#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 9

# In[ ]:


#See the excel file


# # Lecture 10: Machine Learning

# ## Installation of packages

# In[ ]:


#Install the package numpy and scikit-learn


# In[1]:


pip install numpy


# In[2]:


pip install scikit-learn


# In[9]:


#import the packages
import numpy as np
import sklearn.linear_model as skmod
import matplotlib.pyplot as plt


# ## Reminder of numpy

# In[4]:


#Our data: the goats and the altitude
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


# In[7]:


#Reorder your arrays
arr_x = np.array(alt)
arr_x = arr_x.reshape(-1,1)
print(arr_x)
arr_y = np.array(n_goats)
arr_y = arr_y.reshape(-1,1)
print(arr_y)


# ## The linear regression

# In[10]:


#Plot your data first
plt.scatter(arr_x, arr_y)


# In[11]:


#Create a linear regression model: LinearRegression()
model = skmod.LinearRegression()
#some parameters than you can change:
#fit_intercept (consider b=0 if False, default is True)


# In[13]:


#Train your model
model = model.fit(arr_x, arr_y)


# In[17]:


#get the result: the intercept (b)(.intercept_), 
#the coeff (w1)(.coef_) and the R2 (.score(x, y))
print(model.coef_) #w1
print(model.intercept_) #bias (b)
print(model.score(arr_x, arr_y)) #R2 (R2 = 1 => perfect)
#final equation => y' = -1.829 * x + 26.60


# In[20]:


#draw your model on the graph
plt.scatter(arr_x, arr_y)
plt.plot([0, 4], [-1.829 * 0 + 26.60, -1.829 * 4 + 26.60])


# In[21]:


#Now use your model to predict data (.predict(x))
arr_x_predict = np.array([0,1,2,3,4]).reshape(-1,1)
print(model.predict(arr_x_predict))


# In[23]:


#Predict the result without predict but with intercept and coeff
print(-1.829 * 0 + 26.60)
print(-1.829 * 1 + 26.60)
print(-1.829 * 2 + 26.60)
print(-1.829 * 3 + 26.60)
print(-1.829 * 4 + 26.60)


# In[24]:


#using predict in my graph
plt.scatter(arr_x, arr_y)
plt.plot([0, 4], model.predict(np.array([0,4]).reshape(-1,1)))


# In[ ]:


#YOUR TURN (15 minutes)
#Use the folowwing data to create a linear regression model and train it:
# feature 1 | Label
#--------------------
#   25      |   80
#   100     |   254
#   30      |   152
#   5       |   4
#   85      |   271

#The coeff use to preduce data was 2,56 and the intercept was 23
#How close are you (How high is the score)?
#Draw the graph of the datas and your prediction


# In[33]:


arr_x = np.array([25, 100, 30, 5, 85]).reshape(-1,1)
arr_y = np.array([80, 254, 152, 4, 271]).reshape(-1,1)
model = skmod.LinearRegression()
model = model.fit(arr_x, arr_y)
print(model.coef_)
print(model.intercept_)
print(model.score(arr_x, arr_y))
plt.scatter(arr_x, arr_y)
print(model.predict(np.array([0,100]).reshape(-1,1)))
plt.plot([0, 100], model.predict(np.array([0,100]).reshape(-1,1)))
plt.plot([0, 100], [23.9, 285])


# ## For mutiple dimension
# 

# In[34]:


#Our datas: the students work
x1 = [9, 10, 16, 22, 17, 7, 10, 24, 15]
x2 = [14, 18, 1, 22, 6, 12, 4, 28, 22]
y = [42.8, 48.8, 36.8, 81.1, 44.8, 32.4, 28.8, 100, 73.1]


# In[35]:


#Draw the data in 2d with colors
plt.scatter(x1, x2, c = y, cmap = 'Reds')


# In[36]:


#Draw in 3D
ax = plt.subplot(projection='3d')
ax.scatter(x1, x2, y)


# In[40]:


#Transform our data for scikit-learn
arr_x1 = np.array(x1).reshape(-1,1)
arr_x2 = np.array(x2).reshape(-1,1)
arr_y = np.array(y).reshape(-1,1)
# print(arr_x1)
arr_x = np.hstack([arr_x1, arr_x2])
print(arr_x)


# In[42]:


#create and train the model
model = skmod.LinearRegression()
model_trained = model.fit(arr_x, arr_y)


# In[44]:


#get the result and write the equation
print(model_trained.coef_)
print(model_trained.intercept_)
#y' = 2.21*x1 + 1.69*x2 - 1.51


# In[47]:


#Prediction with the equation
print(2.21*5 + 1.69*6 - 1.51)


# In[48]:


#use the model for prediction
arr_pred = np.array([[5, 6], [6, 18]])
print(arr_pred)
print(model_trained.predict(arr_pred))


# In[ ]:


#YOUR TURN (15 minutes)
#Here is your data
#x1 = [7, 0, 3, 3, 5]
#x2 = [2, 0, 7, 3, 9]
#y = [44, 0, 25, 21, 39]
#Make the linear regression between these datas.
#What are the weights and the bias? Write the final equation of your model.
#What would be the prediction for x1 = 5 and x2 = 6


# ## The polynomial regression

# In[49]:


#Remember: A polynomial regression of degree two is just 
#a linear regression with two features where the second feature
#is the square of the first one


# In[65]:


#Our data: the number of goats
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


# In[66]:


#The simplest way to do it: the square method
alt_sq = []
for i in alt:
    alt_sq.append(i**2)
print(alt_sq)


# In[67]:


#CReate the arrays
arr_x = np.array(alt).reshape(-1,1)
arr_x2 = np.array(alt_sq).reshape(-1,1)
arr_X = np.hstack([arr_x, arr_x2])
arr_y = np.array(n_goats).reshape(-1,1)


# In[68]:


#Create the model and train it
model = skmod.LinearRegression()
model = model.fit(arr_X, arr_y)


# In[70]:


#show the coefficients
print(model.coef_)
print(model.intercept_)
#equation: y' = 8.23*x -1.9665 * x^2 + 16.65


# In[88]:


#create data for model
model_x = list(np.arange(0,6,0.1))
model_y = []
for i in model_x:
    model_y.append(model.predict(np.array([[i, i**2]]))[0])


# In[89]:


#Draw your datas and the model
plt.scatter(arr_x, arr_y)
# print(model.predict(np.array([[1, 1], [4, 16]])))
plt.plot(model_x, model_y)


# In[ ]:





# In[ ]:


#YOUR TURN (15 minutes)
#Find the link between these values (use linear and polynomial regression)
#
# feature  Label
# 13       505
# 3        35
# 17       836
# 0        -6
# 2         16
#The equation used is 2,56*x^2 + x*6 -6, 
#Can you find it with your regression?


# In[94]:


x = [13, 3, 17, 0, 2]
y = [505, 35, 836, -6, 16]
x2 = []
for i in x:
    x2.append(i**2)
x_arr = np.array(x).reshape(-1,1)
x2_arr = np.array(x2).reshape(-1,1)
y_arr = np.array(y).reshape(-1,1)
X = np.hstack([x_arr, x2_arr])
model = skmod.LinearRegression()
model = model.fit(X, y_arr)
print(model.coef_)
print(model.intercept_)


# In[95]:


#Let's show the difference with a linear regression - make the linear model
model_lin = skmod.LinearRegression()
model_lin = model_lin.fit(x_arr, y_arr)


# In[97]:


#show the linear model's equations
print(model_lin.coef_)
print(model_lin.intercept_)


# In[98]:


#crate model x and y
model_x = np.arange(0,20,0.1)
model_y = 2.56*model_x**2 + 6*model_x -6


# In[101]:


#draw the datas, the linear and polynomial model on the same graph
plt.scatter(x_arr, y_arr)
plt.plot(model_x, model_y)
plt.plot([0,20], model_lin.predict(np.array([[0], [20]])))


# In[ ]:





# In[ ]:




