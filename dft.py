import numpy as np


def DFT(x):

    N = len(x)
    X = np.array([])
    nv = np.arange(N)
    
    for k in range(N):
        s = np.exp(1j * 2 * np.pi * k / N * nv)
        X = np.append(X, sum(x * np.conjugate(s)))
        
        
    return X
    
    
#This is a function that implements the discrete Fourier transform (DFT). Given a sequence x of length
N, the function should return its DFT, its spectrum of length N with the frequency indexes ranging from 0 
to N-1.
