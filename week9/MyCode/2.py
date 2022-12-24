import numpy as np

# arr = np.array([[1,2,3], [4,5,6]])
# print(arr)

# print(arr[0][2])



#the copy and the view
list1 = [1,2,3]
list2 = list1.copy()
list2[0] = 25
print(list2)
print(list1)
