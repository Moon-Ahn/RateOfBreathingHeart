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

import pywt


def wavelet_peak_detection(data, wavelet, scales):
    # Compute Continuous Wavelet Transform (CWT)
    cwt_matrix, _ = pywt.cwt(data, scales, wavelet)

    # Find the local maxima of the CWT matrix
    cwt_max_index = np.unravel_index(np.argmax(np.abs(cwt_matrix), axis=None), cwt_matrix.shape)
    return cwt_max_index


scales = np.arange(1, 100)
wavelet = 'morl'
max_cwt_index = wavelet_peak_detection(signal, wavelet, scales)

print(f"Dominant frequency index: {max_cwt_index}")