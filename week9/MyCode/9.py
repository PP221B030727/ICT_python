import numpy as np
x = [1, 2.1, 3.5, 3.9, 5.3, 6]
print(x)
x = np.array(x)
print(x)
x = x.reshape((-1,2))
print(x)

y = [8,9,10,11,12,13]
print(y)
y = np.array(y)
print(y)
y = y.reshape((-1,1))
print(y)