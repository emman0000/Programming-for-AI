import numpy as np

arr1 = np.arange(1,16).reshape(5,3)
arr2 = np.arange(1,7).reshape(3,2)

print(arr1)
print(arr2)

arr3 = np.dot(arr1,arr2)
print(arr3)
