import numpy as np
MD = np.array([[1,0,0,0],
               [1,1,0,0],
               [1,1,1,0],[1,1,1,0]])
print(MD)

#voltear el matriz
#MD = np.fliplr(MD)
#print(MD)

for i in range(4):
    for j in range(4):
        if i == j:
            MD[i, j] = -1
        else:
            MD[i, j] = 0