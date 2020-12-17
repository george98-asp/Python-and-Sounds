# In this file I am showing how to import fft with python and analyze a sound through models_interface.

import numpy as np 
from scipy.signal import triang 
from scipy.fftpack import fft

x = triang(15)
X = fft(x)
mX = abs(X)
pX = np.angle(X)
