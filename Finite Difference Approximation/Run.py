from cubicSpline_module import curvatures
import numpy as np

xData = np.array([7.5, 2.5, 0.5, 9.5, 1.2, 3.0])
yData = np.array([2.5, 2.5, 2.1, 7.5, 9.8, 2.0])


print(curvatures(xData, yData))
input("Press return to exit")