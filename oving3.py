import numpy as np
import numpy.linalg as la

f = lambda x, y: 2*x**2 + y**2 - 2*x*y + 2*x**3 + x**4

gF = lambda x, y: np.array([4*x - 2*y + 6*x**2 + 4*x**3, 2*y + -2*x])

