import numpy as np
n,m =map(int,raw_input().split())

array = np.array([map(lambda x : int(x),raw_input().split()) for i in range(n)])
    
print array.transpose()
print array.flatten()