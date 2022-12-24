import numpy as np
#the copy and the view
arr1 = np.array([1,2,3,4,5])
arr2 = arr1.view()
# arr3 = arr1.copy()
# arr2[0] = 25
# arr3[0] = 100
# print(arr1)
print(arr2)
# print(arr3)