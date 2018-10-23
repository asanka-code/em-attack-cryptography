
# Reference: http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html


# includes core parts of numpy, matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal


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

#########################################################################

def getSegment(time_offset):
    # Segment window (seconds)
    w = 0.08
    # Segment starting offset (sample points)
    start = time_offset * sampleRate
    # Segment ending offset (sample points)
    end = start + (w * sampleRate)
    #print("start=%d", int(start))
    #print("end=%d", int(end))
    return int(start), int(end)


def plotSpectrogram(timeOffset, fileName):
    start, end = getSegment(timeOffset)    
    plt.specgram(dat[start:end], NFFT=4096, Fs=sampleRate, cmap=plt.cm.get_cmap("Greys"))
    #plt.xlabel("Time (s)")
    #plt.ylabel("Frequency (MHz)")
    plt.axis('off')
    ax = plt.axes()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)    
    plt.ylim(-2000000, 2000000)    
    plt.savefig(fileName +'.png', fotmat='png', bbox_inches='tight', pad_inches=0)
    #plt.savefig('spectrogram-from-iq.pdf', fotmat='pdf', bbox_inches='tight')
    return 1
    
#########################################################################

# AES region
plotSpectrogram(0.76, 'with-aes')
# normal region
plotSpectrogram(0.95, 'without-aes')
