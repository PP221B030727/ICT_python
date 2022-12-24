import numpy as np
import sklearn.linear_model as skmod
import matplotlib.pyplot as plt
x1 = [9, 10, 16, 22, 17, 7, 10, 24, 15]
x2 = [14, 18, 1, 22, 6, 12, 4, 28, 22]
y = [42.8, 48.8, 36.8, 81.1, 44.8, 32.4, 28.8, 100, 73.1]
arr_x1 = np.array(x1).reshape(-1,1)
arr_x2 = np.array(x2).reshape(-1,1)
arr_y = np.array(y).reshape(-1,1)
arr_x = np.hstack([arr_x1, arr_x2])

model = skmod.LinearRegression()
model_trained = model.fit(arr_x, arr_y)


print(model_trained.coef_)
print(model_trained.intercept_)




# print(arr_x)
# print(2.21*5 + 1.69*6 - 1.51)

# arr_pred = np.array([[5, 6], [6, 18]])
# print(arr_pred)
# print(model_trained.predict(arr_pred))