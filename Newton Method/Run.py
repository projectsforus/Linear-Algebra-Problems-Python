import numpy as np
import math
from newtonPoly_module import *


xData = np.array([1.2, 0.5, 8.4, 3.2, 6.5, 1.1])
yData = np.array([4.2, 1.9, 4.8, 7.4, 2.1, 2.8])
a = coeffts(xData, yData)
print(" x yInterp yExact")
print("-----------------------")
for x in np.arange(0.0, 8.1, 0.5):
    y = evalPoly(a, xData, x)
    yExact = 4.8 * math.cos(math.pi * x / 20.0)
    print('{:3.1f} {:9.5f} {:9.5f}'.format(x, y, yExact))
input("\nPress return to exit")