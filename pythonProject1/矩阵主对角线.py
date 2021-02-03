import numpy as np
n = np.mat(input())
s = 0
for i in range(n.shape[0]):
    s += n[i,i]
print(s)