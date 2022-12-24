import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as skmod

alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]

arr_x = np.array(alt)
arr_x = arr_x.reshape(-1,1)
print(arr_x)
arr_y = np.array(n_goats)
arr_y = arr_y.reshape(-1,1)
print(arr_y)

# plt.scatter(arr_x, arr_y)
# plt.show()



model = skmod.LinearRegression()


model = model.fit(arr_x, arr_y)


print(model.coef_) #w1
print(model.intercept_) #bias (b)
print(model.score(arr_x, arr_y)) #R2 (R2 = 1 => perfect)



#draw your model on the graph
plt.scatter(arr_x, arr_y)
plt.plot([0, 4], [-1.829 * 0 + 26.60, -1.829 * 4 + 26.60])
# plt.show()
arr_x_predict = np.array([0,1,2,3,4]).reshape(-1,1)
print(model.predict(arr_x_predict))



# print(-1.829 * 0 + 26.60)
# print(-1.829 * 1 + 26.60)
# print(-1.829 * 2 + 26.60)
# print(-1.829 * 3 + 26.60)
# print(-1.829 * 4 + 26.60)
plt.scatter(arr_x, arr_y)
plt.plot([0, 4], model.predict(np.array([0,4]).reshape(-1,1)))
print(plt.show())



