
import numpy as np 
import sklearn.linear_model as skmod 
import matplotlib.pyplot as plt
feature = [25,100,30,5,85]
Label = [80,254,152,4,271]
x = np.array(feature)

y = np.array(Label)
x = x.reshape(-1,1)
y = y.reshape(-1,1)
model = skmod.LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
plt.scatter(x,y)
plt.plot([0, 100], model.predict(np.array([0,100]).reshape(-1,1)))
plt.plot([0, 100], [23.9, 285])
plt.show()

