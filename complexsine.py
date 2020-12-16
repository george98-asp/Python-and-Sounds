In this file I am showing how to create a complex sinusoid using Python Packages. For executing, follow the instructions in the sine.py file.



import matplotlib.pyplot as plt
import numpy as np

N = 500
k = 3
n = np.arange(-N/2, N/2)
s = np.exp (1j * 2 * np.pi *k *n / N)

plt.plot (n, np.real(s))
plt.axis([-N/2, N/2-1, -1, 1])
plt.xlabel ('n')
plt.ylabel ('amplitude')

plt.show()
