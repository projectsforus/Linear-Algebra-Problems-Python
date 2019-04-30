import numpy as np
import math
from newtonRaphson2_module import *

def f(x):
    f = np.zeros(len(x))
    f[0] = math.sin(x[0]) + x[1] ** 2 + math.log(x[2]) - 4.2
    f[1] = 5.0 * x[0] + 2.5 ** x[1] - x[2] ** 4 + 1.2
    f[2] = x[0] + x[1] + x[2] - 4.8
    return f

x = np.array([1.0, 1.0, 1.0])
print(newtonRaphson2(f, x))
input("\nPress return to exit")