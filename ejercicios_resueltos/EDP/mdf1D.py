import numpy as np

# Datos
nx = 50
nt = 50
a = 0.2
X0, X1 = 0, 1  # Intervalo espacial [0,1]

h = (X1-X0)/(nx+1)
dt = 0.9*h/a  # CFL
lam = dt/h


def initial_value(x):
    P = (X0+X1)/2
    return np.exp(-50*(x-P)**2)


x = np.linspace(X0, X1, nx)
u0 = initial_value(x)

u = [u0]
for n in range(nt):  # n = 0,1 ... nt-1
    u1 = np.zeros(nx)
    for i in range(1, nx-1):  # i = 0,1,... nx-1
        u1[i] = u0[i] - lam/2 * a*(u0[i+1] - u0[i-1])
        #u1[i] = (u0[i+1] + u0[i-1])/2 - lam/2 * a*(u0[i+1] - u0[i-1])
    # Condiciones de contorno de tipo "inflow"
    u1[0] = u0[-1]
    u1[-1] = u1[-2]
    # u1[-1] = u0[0]
    u.append(u1)
    u0 = u1

u2 = u1.copy()
