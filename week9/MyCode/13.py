import numpy as np
import sklearn.linear_model as skmod
import matplotlib.pyplot as plt
x = [1, 2.1, 3.5, 3.9, 5.3, 6]
# print(x)
x = np.array(x)
# print(x)
x = x.reshape((-1,1))
# print(x)

y = [8,9,10,11,12,13]
# print(y)
y = np.array(y)
# print(y)
y = y.reshape((-1,1))
# print(y)
model = skmod.LinearRegression()
model_trained = model.fit(x, y)
# print(model.intercept_)
#get the coef : the w1 value
# print(model.coef_)
#get the accuracy with R2
# print(model.score(x, y))



plt.scatter(x, y)
x_model = [0, 6]
y_model = [0.98573038 * 0 + 6.91851296, 0.98573038 * 6 + 6.91851296]
plt.plot(x_model, y_model)

#Now use your model to predict data (.predict(x))
x_model = np.array([0,6]).reshape(-1,1)
print(model.predict(x_model))


x_model = [0, 6]
y_model = [0.98573038 * 0 + 6.91851296, 0.98573038 * 6 + 6.91851296]
print(y_model)