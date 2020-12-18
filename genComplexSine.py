import numpy as np

def genComplexSine(k, N):

    n = np.arange(0, N)
    cSine = np.exp(-(1) * 1j * 2 * np.pi * k * n / N )
   
    return cSine
   
# This is a function that generates a complex sinusoid that is used in DFT computation of lenght N (samples).
