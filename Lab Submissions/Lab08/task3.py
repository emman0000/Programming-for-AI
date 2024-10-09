import numpy as np

#create a matrix 3x3 consisting only of even numbers
#mutiply each element with 4
#then multiply the resultant matrix with 3x3 identity matrix

arr = np.arange(20,38,2).reshape(3,3)
print(arr)
new_array = np.multiply(arr,4)

identity_matrix = np.identity(3)
result = np.dot(new_array , identity_matrix)
print(identity_matrix)
print(result)

