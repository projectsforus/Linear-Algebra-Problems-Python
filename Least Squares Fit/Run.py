import numpy as np
from polyFit_module import *

xData = np.array([-0.45, 0.88, 3.2, 2.1, 7.7, 8.0, \
7.77, 7.66, 7.55, -1.5, -0.5])
yData = np.array([-7.6, -6.5, -5.4, -4.3, -3.2, 2.1, \
1.0, 0.9, 9.8, -2.0, 8.76])
while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        coeff = polyFit(xData, yData, m)
        print("Coefficients are:\n", coeff)
        print("Std. deviation =", stdDev(coeff, xData, yData))
    except SyntaxError: break
input("Finished. Press return to exit")