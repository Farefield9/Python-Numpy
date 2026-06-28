import numpy as np
g = np.array([[1,2,3],[4,5,6]])
g2 = np.concatenate([g,g],axis = 1)
print(g2)
