
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq, fftshift

sampleRate=20000000

'''
# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples
dat = np.fromfile("./data/with-aes.cfile", dtype="float32")
sampleRate=20000000

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
dat = dat[0::2] + 1j*dat[1::2]

# Note: a quicker way to turn the interleaved I and Q samples  into complex values
# (courtesy of http://stackoverflow.com/a/5658446/) would be:
# dat = dat.astype(np.float32).view(np.complex64)
'''

#########################################################################

def getData(cfileName):
    data = np.fromfile(cfileName, dtype="float32")
    data = data[0::2] + 1j*data[1::2]
    return data

def getSegment(timeOffset):
    # Segment window (seconds)
    w = 0.08
    # Segment starting offset (sample points)
    start = timeOffset * sampleRate
    # Segment ending offset (sample points)
    end = start + (w * sampleRate)
    #print("start=%d", int(start))
    #print("end=%d", int(end))
    return int(start), int(end)


def plotSpectrogram(data, timeOffset, specFileName):
    start, end = getSegment(timeOffset)    
    plt.specgram(data[start:end], NFFT=4096, Fs=sampleRate, cmap=plt.cm.get_cmap("Greys"))
    #plt.xlabel("Time (s)")
    #plt.ylabel("Frequency (MHz)")
    plt.axis('off')
    ax = plt.axes()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)    
    plt.ylim(-2000000, 2000000)    
    plt.savefig('./spectrograms/' + specFileName +'.png', fotmat='png', bbox_inches='tight', pad_inches=0)
    #plt.savefig('spectrogram-from-iq.pdf', fotmat='pdf', bbox_inches='tight')
    return 1
    
def plotFFT(data, timeOffset, fftFileName):
    start, end = getSegment(timeOffset)            
    N = len(data[start:end])
    T = 1.0 / sampleRate
    yf = fft(data[start:end])
    freqs = fftfreq(N, T)
    shifted_freqs = fftshift(freqs)
    new_yf = np.concatenate((yf[N/2:N], yf[0:N/2]))
    plt.plot(shifted_freqs, np.abs(new_yf))    
    #print('len(shifted_freqs)=%d' % len(shifted_freqs))    
    #print('len(new_yf)=%d' % len(new_yf))        
    plt.savefig('./spectrograms/' + fftFileName +'.png', fotmat='pdf', bbox_inches='tight')
    return 1
    
#########################################################################

# 3DES region
data = getData("./3DES/3des-6.cfile")
#plotSpectrogram(data, 0.53, '3des.1')
plotFFT(data, 0.53, '3des.1')

# AES region
data = getData("./AES/aes-2.cfile")
#plotSpectrogram(data, 7.40, 'aes.1')
plotFFT(data, 7.40, 'aes.1')

