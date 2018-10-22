
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
#import scipy.signal as signal


# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples
dat = np.fromfile("./data/with-aes.cfile", dtype="float32")
#dat = np.fromfile("./data/without-aes.cfile", dtype="float32")
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

#plt.specgram(dat, NFFT=8192, Fs=sampleRate, cmap=plt.cm.get_cmap("Greys"), Fc=1.4e9)

#plt.title("PSD of 'signal' loaded from file")
#plt.xlabel("Time (s)")
#plt.ylabel("Frequency (MHz)")
#plt.ylim(0, 1e7)
#plt.xlim(0.95, 1.06)

'''  
# Let's try a PSD plot of the same data
Pxx, freqs = plt.psd(dat, NFFT=1024, Fc=1.4e9, Fs=sampleRate)

print("Pxx length=%d", len(Pxx))
print("freqs length=%d", len(freqs))

plt.plot(freqs, Pxx)

#plt.show() 
#plt.savefig('psd.pdf', bbox_inches='tight')
'''
###########################################################################

'''
plt.figure(figsize=(5,5))
plt.subplot(2,1,1)
Pxx, freqs = plt.psd(dat, NFFT=1024, Fc=1.4e9, Fs=sampleRate)
#plt.xlabel('x')
#plt.legend()
#plt.grid()
plt.title("The Title of the Graph")

plt.subplots_adjust(wspace=0, hspace=0.5)

plt.subplot(2,1,2)
plt.plot(freqs, Pxx)
#plt.xlabel('x')
#plt.legend()
#plt.grid()
plt.title("The Title of the Graph")

#plt.show()
plt.savefig('psd.pdf', bbox_inches='tight')
'''
###########################################################################

#Time offset 0.75 to 0.84, there's an AES
# That means sample rage from 13000000 to 16800000

#Time offset 0.95 to 1.03, there's no AES
# That means sample rage from 19000000 to 20600000

plt.figure(figsize=(5,5))
plt.subplot(2,1,1)
#Pxx, freqs = plt.psd(dat[13000000:16800000], NFFT=1024, Fc=1.4e9, Fs=sampleRate)
Pxx, freqs = plt.psd(dat[19000000:20600000], NFFT=1024, Fc=1.4e9, Fs=sampleRate)
#plt.xlabel('x')
#plt.legend()
#plt.grid()
plt.title("The Title of the Graph")

plt.subplots_adjust(wspace=0, hspace=0.5)

plt.subplot(2,1,2)
plt.plot(freqs, Pxx)
#plt.xlabel('x')
#plt.legend()
#plt.grid()
plt.title("The Title of the Graph")

#plt.show()
plt.savefig('psd.pdf', bbox_inches='tight')
