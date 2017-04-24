
import numpy as np
import numpy.linalg as la


tol = 1e-7

def CG(A, b, x):
    r = b - A.dot(x)
    p = r
    k = 0
    while k < 1000:
        alpha = np.inner(r, r)/np.inner(p, A.dot(p))
        x = x + alpha*p
        rk = r
        r = r - alpha*A.dot(p)
        if la.norm(r) < tol:
            break
        beta = np.inner(r, r)/np.inner(rk, rk)
        p = r + beta*p
        k = k + 1

    return x

def test_problem2():
    A = np.array([
        [2, -1, -1],
        [-1, 3, -1],
        [-1, -1, 2]
        ])
    b = np.array([1, 0, 1])
    x0 = np.array([0, 0, 0])
    solCG = CG(A, b, x0)

    print(la.solve(A, b))
    print(solCG)

if __name__=="__main__":
    test_problem2()
