import math
from romberg_module import *

def f(x): return 4.0 * (x ** 3) * math.cos(x ** 3)
I, n = romberg(f, 0, math.sqrt(math.pi))
print("Integral =", I)
print("numEvals =", n)
input("\nPress return to exit")