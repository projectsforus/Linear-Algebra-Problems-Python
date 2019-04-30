import numpy as np

def gaussElimin(a, b):
    n = len(b)
    # Elimination Phase
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a [i, k] / a[k, k]
                a[i, k + 1 : n] = a[i , k + 1 : n] - lam * a[k, k + 1 : n]
                b[i] = b[i] - lam * b[k]
                
    # Back substitution
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1 : n], b[k + 1 : n])) / a[k, k]
    return b

a = np.array([[6.0, -4.0, 1.0], [-4.0, 6.0, -4.0], [1.0, -4.0, 6.0]])
b = np.array([3.0 , 2.0 , 5.0])

x = gaussElimin(a, b)
print(x)
input("\nPress return to exit")