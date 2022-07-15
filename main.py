import numpy as np
from numpy.linalg import eig

ep = 10**-3
N = 5
A = np.array([[5,-2,3],[-3,0,1],[2,-1,-7]])
b = np.array([[-1],[2],[3]])

print(np.diag(A))
if any(np.diag(A)) != 0:
    D = np.diag(np.diag(A))
    L = np.tril(A,-1) * (-1)
    U = np.triu(A,1) * (-1)

    inv = np.subtract(D,L)

    try:
        g = np.linalg.inv(inv)
    except:
        print("Singular Matrix, Inverse not possible.")
    T = np.matmul(g,U)
    c = np.matmul(g,b)

    u,v = eig(T)
    m = max(abs(u))

    x_0 = 0
    y_0 = 0
    z_0 = 0

    X_0 = np.array([[x_0],[y_0],[z_0]])

    k = 1

    if m<1:
        while k <= N:
            P = np.matmul(T,X_0)
            X_i = np.add(P,c)
            error_met = np.subtract(X_i,X_0)
            if all(abs(error_met) <= ep):
                break
            k = k+1
            X_0 = X_i
    elif m >= 1:
        print("problem does not have unique solutions can not solve using gauss seidal method")
    print(X_i)
elif any(np.diag(A)) == 0:
    print("problem has diagonal element zero can not solve using gauss seidal method")
