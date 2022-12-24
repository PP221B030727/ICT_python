import sklearn.linear_model as skmod
import numpy as np
import matplotlib.pyplot as plt



x1 = [7, 0, 3, 3, 5]
x2 = [2, 0, 7, 3, 9]
y = [44, 0, 25, 21, 39]

#Make the linear regression between these datas.
#What are the weights and the bias? Write the final equation of your model.
#What would be the prediction for x1 = 5 and x2 = 6


x1 = np.array(x1).reshape((-1,1))
x2 = np.array(x2).reshape((-1,1))
y  = np.array(y).reshape((-1,1))

arr_x = np.hstack([x1,x2])
# print(arr_x)

model = skmod.LinearRegression()
model_tr = model.fit(arr_x,y)
print(model_tr.coef_)##y' = 2.21*x1 + 1.69*x2 - ошибка 
print(model_tr.intercept_)#ошибка 
# y' = 6*x1 + 1*x2-1.4210e-14 



print(model_tr.predict(arr_x))
print(6*5+1*6-1.42e-14)