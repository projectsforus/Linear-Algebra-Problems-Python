import numpy as np
from gaussPivot_module import *

a = np.array([[ 2.0, -2.0, 6.0],\
              [-2.0, 4.0, 3.0],\
              [ -1.0, 8.0, 4.0]])
    
b = np.array([16.0, 0.0, -1.0])

x = gaussPivot(a, b)
print("\nX =\n", x)
input("\nPress return to exit")