#Program to find the solution for the given linear equations.
#Developed by:Udhaya dharshini.T 
#RegisterNumber:212225230288
import numpy as np
A = np.array([[1, 3],
              [2, 5]])
B = np.array([5, -3])
x = np.linalg.solve(A, B)
print(x)



