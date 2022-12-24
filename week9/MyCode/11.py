import numpy as np

import matplotlib.pyplot as plt


import sklearn.linear_model as skmod


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
plt.scatter(x, y)
x_model = [0, 6]
y_model = [0.98573038 * 0 + 6.91851296, 0.98573038 * 6 + 6.91851296]
plt.plot(x_model, y_model)