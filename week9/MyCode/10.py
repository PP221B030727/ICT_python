import sklearn.linear_model as skmod
import numpy as np
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
model = skmod.LinearRegression()
model_trained = model.fit(x, y)

#get the result: the intercept (b)(.intercept_), the coeff (w1)(.coef_) and the R2 (.score(x, y))
#get b value
print(model.intercept_)
#get the coef : the w1 value
print(model.coef_)
#get the accuracy with R2
print(model.score(x, y))