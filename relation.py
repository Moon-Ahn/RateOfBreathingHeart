import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

###########
def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)
time = np.arange(0, 10, 0.001)
sin1 = sin_wave(1, 10, time)
sin2 = sin_wave(2, 5, time)
sin3 = sin_wave(4, 1, time)
signal = sin1 + sin2 + sin3
t=time
fs=100
###########

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size // 2:]

correlation = autocorr(signal)
peaks, _ = scipy.signal.find_peaks(correlation, distance=fs//(10*2))

plt.plot(correlation)
plt.plot(peaks, correlation[peaks], 'r*', markersize=10)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.show()