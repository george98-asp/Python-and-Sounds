In this file I am showing how to create a sinusoid using Python packages.

import matplotlib.pyplot as plt
import numpy as np 

A = .8
f0 = 1000
phi = np.pi/2
fs = 44100
t = np.arange (-0.002, .002, 1.0/fs)
x = A * np.cos ( 2* np.pi * f0 * t +phi)

plt.plot (t, x)
plt.axis([-.002, .002, -.8, .8 ])
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()

Save the above in a text editor file.

To execute the command, open python in the terminal and go to the directory where your file is saved and write 
python3 <text editor file name>
