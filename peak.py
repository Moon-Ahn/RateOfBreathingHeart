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
###########

threshold = 2
peaks, _ = scipy.signal.find_peaks(signal, distance=100//(10*2), height=threshold)

plt.plot(t, signal)
plt.plot(t[peaks], signal[peaks], 'r*', markersize=10)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()