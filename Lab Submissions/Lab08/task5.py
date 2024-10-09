import numpy as np
from numpy import random

arr= random.choice([2,5,9,10,], size = (4,4))
print(arr)

identity= np.identity(4)
print(identity)
mult_mat = np.multiply(arr,identity)
print(mult_mat)

odd_mat = random.choice([3,5,7,9,11],size = (4,4))
print(odd_mat)
addition_mat = np.add(mult_mat,odd_mat)
print(addition_mat)

