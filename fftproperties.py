# In this file I am using some fft properties such as symmetry and zero-padding.

import numpy as np 
from scipy.signal import triang 
from scipy.fftpack import fft

x = triang(15)
fftbuffer = np.zeros(15)
fftbuffer [:8] = x [7:]
fftbuffer[8:] = x [:7]
X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)





import numpy as np
from scipy.fftpack import fft
import os, sys, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(_file_)), '../software/models/'))
import utilFunctions as UF

M = 501

hM1 = int(math.floor((M+1)/2)

hM2 = int(math.floor(M/2))

(fs, x) = UF.wavread('../sounds/soprano-E4.wav')

x1 = x[5000:5000 + M] * np.hamming(M)

N = 511
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)
