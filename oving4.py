
import numpy as np
import numpy.linalg as la


tol = 1e-7

def CG(A, b, x):
    r = b - np.dot(A, x)
    p = r
    k = 0
    while k < 1000:
        alpha = np.inner(r, r)/np.inner(p, np.dot(A, p))
        x = x + alpha*p
        rk = r
        r = r - alpha*np.dot(A, pk)
        if r < tol:
            break
        beta = np.inner(r, r)/np.inner(rk, rk)
        p = r + beta*p
        k = k + 1

    return x

def test_problem2():
    A = np.mat([
        [2, -1, -1],
        [-1, 3, -1],
        [-1, -1, 2]
        ])
    b = np.array([1, 0, 1])
    x0 = np.array([0, 0, 0])
    solCG = CG(A, b, x0)

    print(la.solve(A, b))
    print(solCG)
