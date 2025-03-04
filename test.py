import numpy as np

A = np.array([
    [1, 2, 4],
    [3, 5, 9]
])

B = np.array([
    [2, 1],
    [4, 9],
    [5, 1]
])

print(A @ B)

W = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

x = np.array([[1, 2, 3]])


print(W @ x.T)