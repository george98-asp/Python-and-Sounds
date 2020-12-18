import numpy as np

def genSine(A, f, phi, fs, t)
    
    t = np.arange(0, t, 1.0/fs)
    x = A * np.cos(2 * np.pi * f * t + phi)
    
    return x
    
    
# This is a function that generates a real sinusoid, given its amplitude A, frequency f, sampling rate fs and duration t.
