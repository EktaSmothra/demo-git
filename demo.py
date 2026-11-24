import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
#c = np.array([[5, 6], [7, 8]])

sum = a + b

product = a @ b

print("Array Shape:", a.shape)
print("Sum of matrices: ", sum)
print("Mean of Matrix A:", np.mean(a))
print("Matrix Multiplication Result:\n", product)
