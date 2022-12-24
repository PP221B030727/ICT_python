import sklearn.linear_model as skmod
import numpy as np
import matplotlib.pyplot as plt

# ## The polynomial regression

# In[49]:


#Remember: A polynomial regression of degree two is just 
#a linear regression with two features where the second feature
#is the square of the first one


#Our data: the number of goats
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


#The simplest way to do it: the square method
alt_sq = []
for i in alt:
    alt_sq.append(i**2)
# print(alt_sq)



arr_x = np.array(alt).reshape(-1,1)
arr_x2 = np.array(alt_sq).reshape(-1,1)
arr_X = np.hstack([arr_x, arr_x2])
arr_y = np.array(n_goats).reshape(-1,1)




#Create the model and train it
model = skmod.LinearRegression()
model = model.fit(arr_X, arr_y)

#show the coefficients
print(model.coef_)
print(model.intercept_)
#equation: y' = 8.23*x -1.9665 * x^2 + 16.65


#create data for model 
# print(np.arange(0,6,0.1))#с 0 - 6 шагом 0.1
model_x = list(np.arange(0,6,0.1))
model_y = []
for i in model_x:
    model_y.append(model.predict(np.array([[i, i**2]]))[0])

#Draw your datas and the model
plt.scatter(arr_x, arr_y)
# print(model.predict(np.array([[1, 1], [4, 16]])))
plt.plot(model_x, model_y)
plt.show()