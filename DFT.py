In this file I am showing how to implement the DFT equations in Python.

import numpy as np
import matplotlib.pyplot as plt

N = 64
k0 = 7
x = np.exp(1j * 2* np.pi * k0 / N * np.arange(N))

X = np.array([])

for k in range(N):
  s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
  X = np.append(X, sum(x*np.conjugate(s)))
  
plt.plot (np.arange(N), abs(x))
plt.axis([0, N-1, 0, N])

plt.show()



To execute follow the instructions in the files sine.py or complexsine.py.
