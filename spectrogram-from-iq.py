
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal


# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples
dat = np.fromfile("./data/data.cfile", dtype="float32")
sampleRate=20000000

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

plt.specgram(dat, NFFT=8192, Fs=sampleRate
    , cmap=plt.cm.get_cmap("Greys"), Fc=1.4e9)

#plt.title("PSD of 'signal' loaded from file")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (MHz)")
#plt.ylim(0, 1e7)
#plt.xlim(0.95, 1.06)

#ax = plt.axes()
#ax.yaxis.set_major_locator(plt.MaxNLocator(10))
#formatter = plt.FixedFormatter(["343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353"])
#ax.yaxis.set_major_formatter(formatter)

#plt.show()  # if you've done this right, you should see a fun surprise here!

#plt.savefig('spectrogram-from-iq.png', fotmat='png', bbox_inches='tight', dpi=1000)

plt.savefig('spectrogram-from-iq.pdf', fotmat='pdf', bbox_inches='tight')
    
##########################################################################

'''
# Let's try a PSD plot of the same data
plt.psd(dat, NFFT=1024, Fs=sampleRate)
plt.xlim(1.5e6, 6e6)
plt.ylim(-75, -53)

ax = plt.axes()
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.yaxis.set_major_locator(plt.MaxNLocator(5))

formatter = plt.FixedFormatter(["344.5", "345", "346", "347", "348", "349"])
ax.xaxis.set_major_formatter(formatter)

#plt.title("PSD of 'signal' loaded from file")
ax.set_xlabel('Frequency (MHz)', fontsize=14)
ax.set_ylabel('Amplitude (dB/Hz)', fontsize=14)
#ax.set_ylabel('needed bar diameter (cm)')
#plt.show() 
plt.savefig('psd.pdf', bbox_inches='tight')
'''

###########################################################################

'''
# And let's look at it on the complex plan
# Note that showing *every* data point would be time- and processing-intensive
# so we'll just show a few
plt.scatter(np.real(dat[0:100000]), np.imag(dat[0:100000]))
plt.title("Constellation of the 'signal' loaded from file")
plt.show() 
'''

