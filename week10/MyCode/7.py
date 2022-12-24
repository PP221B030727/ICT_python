import sklearn.linear_model as skmod
import numpy as np
import matplotlib.pyplot as plt


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




#Let's show the difference with a linear regression - make the linear model
model_lin = skmod.LinearRegression()
model_lin = model_lin.fit(x_arr, y_arr)




#show the linear model's equations
print(model_lin.coef_)
print(model_lin.intercept_)




#crate model x and y
model_x = np.arange(0,20,0.1)
model_y = 2.56*model_x**2 + 6*model_x -6




#draw the datas, the linear and polynomial model on the same graph
plt.scatter(x_arr, y_arr)
plt.plot(model_x, model_y)
plt.plot([0,20], model_lin.predict(np.array([[0], [20]])))
plt.show()
