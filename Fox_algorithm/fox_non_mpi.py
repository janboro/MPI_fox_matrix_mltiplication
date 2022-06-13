import numpy as np

# A = np.array([[1]])
# B = np.array([[4]])

# A = np.array([[1, 2, 3]])
# B = np.array([[4, 5, 6]])

A = np.array([[0, 1], [2, 3]])
B = np.array([[4, 5], [6, 7]])

assert np.shape(A) == np.shape(B), "Matrix shape mismatch"
assert np.shape(A)[0] == np.shape(A)[1], "Matrix shape mismatch"
matrix_order = len(A)
no_processes = len(A) * len(A[0])

C = np.zeros((len(A), len(A[0])))

for i in range(matrix_order):
    for j in range(matrix_order):
        for k in range(matrix_order):
            C[i][j] += A[i][k] * B[k][j]

print(C)
