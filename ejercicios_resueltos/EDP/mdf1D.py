import numpy as np

def CenteredFluxes(a, b, beta, u0, h, k, nt):
    """
    Método de Diferencias Finitas: flujos centrados
    Argumentos:
        a, b: Intervalo x
        beta : advection velocity
        u0: array of initial values [u_1^0, u_2^0..., u_{N}^0]
        h, k :  x step and t step
        nt: number of time iterations
    Devuelve:
        solucion: lista de aproximaciones en los instantes
            n=0,...,n=nt
    """

    nx = len(u0)
    lam = k/h
    solucion = [u0]
    # Bucle en tiempo
    for n in range(nt):  # n = 0,1,...nt-1
        # Bucle en espacio
        u = np.zeros(nx)  # u_0, u_1,..., u_nx
        for i in range(1, nx-1):  # 0,1,...,nx-1
            u[i] = 0.5*(u0[i]) - \
                    lam*beta/2 * (u0[i+1] - u0[i-1])
        u[0] = u0[nx-1]
        # u[nx-1] = u0[1]
        solucion.append(u)
        u0 = u.copy()
    return solucion

def LaxFriedrichs(a, b, beta, u0, h, k, nt):
    """
    Método de Diferencias Finitas: flujo de Lax-LaxFriedrichs
    Argumentos:
        a, b: Intervalo x
        beta : advection velocity
        u0: array of initial values [u_1^0, u_2^0..., u_{N}^0]
        h, k :  x step and t step
        nt: number of time iterations
    Devuelve:
        solucion: lista de aproximaciones en los instantes
            n=0,...,n=nt
    """

    nx = len(u0)
    lam = k/h
    solucion = [u0]
    # Bucle en tiempo
    for n in range(nt):  # n = 0,1,...nt-1
        # Bucle en espacio
        u = np.zeros(nx)  # u_0, u_1,..., u_nx

        u[1:nx-1] = 0.5*(u0[0:nx-2]+u0[2:nx]) - \
            lam*beta/2 * (u0[2:nx] - u0[0:nx-2])

        # for i in range(1, nx-1):  # 0,1,...,nx-1
        #     u[i] = 0.5*(u0[i-1]+u0[i+1]) - \
        #             lam*beta/2 * (u0[i+1] - u0[i-1])

        u[0] = u0[nx-2]
        u[nx-1] = u0[2]
        solucion.append(u)
        u0 = u.copy()
    return solucion
