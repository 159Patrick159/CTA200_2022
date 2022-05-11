import numpy as np

def z_iterator(z0,N,x,y):
    """Iterates for future values of z for given recursive def Zn+1 = Zn^2 + C
     where C = x + iy x and y are floats. Also z0 is complex"""
    # Initialze arrays for z
    z_C = np.zeros(N,dtype='complex')
    z_abs = np.zeros(N,dtype='float')
    # Set initial conditions
    z_C[0] = z0
    z_abs[0] = z0.real**2 + z0.imag**2
    # Set array for number of iteration before divergence
    iters = [0]
    # Compute C explicitly for each iteration
    C = x + y*1j
    # Compute next iteration of z through its definition
    for i in range(1,N):
        z_C[i] = z_C[i-1]**2 + C
        z_abs[i] = z_C.real[i]**2 + z_C.imag[i]**2
        if np.isnan(z_abs[i]):
            iters.append(i)
    return(z_abs,iters)
