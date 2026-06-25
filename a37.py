import numpy as np
b1,b2,b3,b4,b5 = np.hsplit(b,5)
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(np.hstack((b1,b2,b3)))
print(np.concatenate((b1,b2), axis = 1))
