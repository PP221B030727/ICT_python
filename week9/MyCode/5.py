import numpy as np
# reshape your array from 1D to 2D
arr1 = np.array([1,2,3,4,5,6])
print(arr1.shape)
print(arr1)
arr1 = arr1.reshape((3,2)) #делаем из 1 мерного массива 2 мерное
print(arr1.shape)

print(arr1)



arr1 = np.array([1,2,4,5,6,8])
print(arr1.shape)
print(arr1)
print(arr1.reshape((3,2)))# 3*2==arr.size()