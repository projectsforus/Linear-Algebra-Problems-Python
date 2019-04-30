import numpy as np
from gaussSeidel_module import *


def iterEqs(x, omega, a, b):
    n = len(x)
    for i in range(n):
        if i == 0:
            x[i] = omega * ((b[i] + x[i+1]) / a[i,i])-(omega - 1)*x[i]
        elif (i == (n - 1)):
            x[i] = omega * ((b[i] + x[i-1]) / a[i,i])-(omega - 1)*x[i]
        else:
            x[i] = omega * ((b[i] + x[i+1] + x[i-1]) / a[i,i])-(omega - 1)*x[i]
    return x


a = np.array([[4.0, -1.0, 0.0, 0.0], [-1.0, 4.0, -1.0, 0.0], [0.0, -1.0, 4.0, -1.0], [0.0, 0.0, -1.0, 3.0]])
b = np.array([15, 10, 10, 10])

x = np.zeros(4)
omega = 1.1
for i in range(len(b)):
    x[i] = b[i]/a[i,i]

x, numIter, omega = gaussSeidel(iterEqs, x, a, b)
print("\nNumber of iterations =", numIter)
print("\nRelaxation factor =", omega)
print("\nThe solution is:\n", x)
input("\nPress return to exit")