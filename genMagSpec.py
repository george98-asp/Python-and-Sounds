import numpy as np

def genMagSpec(x):

    N = len(x)
    X = np.array([])
    nv = np.arange(N)
    
    for k in range(N):
        s = np.exp(1j * 2 * np.pi * * k / N * nv)
        X = np.append(X, sum(X, sum(x * np.conjugate(s)))
        
        
    return abs(X)
    
# This is a function that computes the magnitude spectrum of an input sequence x of length N. The 
function should return an N point magnitude spectrum with frequency index ranging from 0 to N-1.

The input argument to the function is a numpy array x and the function should return a numpy array of the 
magnitude spectrum of x.

EXAMPLE: If you run your function using x = np.array([1, 2, 3, 4]), the function should return the following 
numpy array magX: [array([10.0, 2.82842712, 2.0, 2.82842712])
        
