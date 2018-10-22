
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal
#from scipy.fftpack import fft
from scipy.fftpack import fft, fftfreq, fftshift

# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples
dat = np.fromfile("./data/data.cfile", dtype="float32")
Fs=20000000

# Look at the data. Is it complex?
#dat

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
dat = dat[0::2] + 1j*dat[1::2]

# Note: a quicker way to turn the interleaved I and Q samples  into complex values
# (courtesy of http://stackoverflow.com/a/5658446/) would be:
# dat = dat.astype(np.float32).view(np.complex64)

# Now look at the data again. Verify that it is complex:
#dat 

#########################################################################

# Plot the spectogram of this data
#plt.specgram(dat, NFFT=8192, Fs=sampleRate)

#plt.specgram(dat, NFFT=16384, Fs=sampleRate
#    , cmap=plt.cm.get_cmap("Greys"), Fc=1.4e9)

#plt.specgram(dat, NFFT=8192, Fs=sampleRate, cmap=plt.cm.get_cmap("Greys"), Fc=1.4e9)

'''
fft_out = fft(dat)
plt.plot(dat, np.abs(fft_out))
plt.show()
'''
T = 1/Fs
N = len(dat)
yf = fft(dat)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()

##########################################################################

# Let's try a PSD plot of the same data
#plt.psd(dat, NFFT=1024, Fs=sampleRate)

#plt.savefig('psd.pdf', bbox_inches='tight')

###########################################################################

#plt.show()

