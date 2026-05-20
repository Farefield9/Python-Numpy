import numpy as np
a = np.array([[1,2],[5,6]])
b = np.array([[3,4],[7,8]])
print(np.concatenate((a,b),axis= 1))
