import csv

import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, ifft
from typing import List, Tuple

def initialize_outside_range_to_zero(lst, start, end):
    lst[:start * 2] = [0.0] * (start * 2)
    lst[(end + 1) * 2:] = [0.0] * ((len(lst) - (end + 1)) * 2)
    return lst


def check_vital_signal_detected(signal, energy_level=0.1):
    signal_energy = sum([x * x for x in signal])
    return signal_energy > energy_level

def cutoff_bandpass_filter(input_signal, cutoff_freq_begin, cutoff_freq_end):
    s_fft = fft(input_signal)
    fs = 20.0
    index_weight = fs / len(s_fft)

    cutoff_start_index = int(np.floor(cutoff_freq_begin / index_weight))
    cutoff_end_index = int(np.ceil(cutoff_freq_end / index_weight))

    s_fft2 = initialize_outside_range_to_zero(s_fft.tolist(), cutoff_start_index, cutoff_end_index)

    return ifft(s_fft2).real.tolist()

def find_zero_crossings(signal):
    zero_crossings = []
    for i in range(1, len(signal)):
        if (signal[i - 1] < 0 and signal[i] >= 0) or (signal[i - 1] >= 0 and signal[i] < 0):
            if signal[i - 1] < 0 and signal[i] >= 0:
                zero_crossings.append(i)

    return zero_crossings

def find_peak_indices(signal, threshold=0.0):
    peak_indices = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i - 1] and signal[i] > signal[i + 1] and signal[i] > threshold:
            peak_indices.append(i)

    return peak_indices

def check_vital_signal_detected(signal, energy_level=0.1):
    signal_energy = sum([x * x for x in signal])
    return signal_energy > energy_level

def median_filter(signal, window_size):
    padding = window_size // 5
    padded_signal = [signal[0]] * padding + signal + [signal[-1]] * padding

    return [
        sorted(padded_signal[i:i+window_size])[padding]
        for i in range(len(signal))
    ]

def processing_received_msg(
        breath_signal: List[float],
        unwrap_signal: List[float]
    ) -> Tuple[int, int]:

    breath_signal_bpm = 0
    heart_signal_bpm = 0

    # 주기 감지부 결정


    filtered_breath_signal = cutoff_bandpass_filter(
        breath_signal,
        0.15,
        0.3
    )
    filtered_breath_signal = filtered_breath_signal[:len(filtered_breath_signal) // 2]

    filtered_heart_signal = cutoff_bandpass_filter(
        unwrap_signal,
        0.7,
        2.0
    )
    filtered_heart_signal = filtered_heart_signal[:len(filtered_heart_signal) // 2]

    if check_vital_signal_detected(filtered_breath_signal, 1.0):
        crossing_indices_for_breath = find_zero_crossings(filtered_breath_signal)
        peak_indices_for_breath = find_peak_indices(filtered_breath_signal)

        breath_signal_bpm = len(crossing_indices_for_breath) * 2
    else:
        pass

    if check_vital_signal_detected(filtered_heart_signal, 0.1):
        filtered_heart_signal_median = median_filter(filtered_heart_signal, 1)
        crossing_indices_for_heartbeat = find_zero_crossings(filtered_heart_signal_median)
        peak_indices_for_heartbeat = find_peak_indices(filtered_heart_signal_median)

        heart_signal_bpm = len(crossing_indices_for_heartbeat) * 2
    else:
        pass
    # 그래프 출력
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(breath_signal, label='Original Breath Signal')
    plt.plot(filtered_breath_signal, label='Filtered Breath Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Breath Signal')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(unwrap_signal, label='Original Heart Signal')
    plt.plot(filtered_heart_signal, label='Filtered Heart Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Heart Signal')
    plt.legend()

    plt.tight_layout()
    plt.show()

    return breath_signal_bpm, heart_signal_bpm

# calc.csv 파일에서 데이터 읽어오기
breath_signal = []
heart_signal = []

with open('calc.csv', 'r') as file:
    reader = csv.reader(file)
    #next(reader)  # 첫 번째 행은 헤더이므로 건너뜁니다.
    for row in reader:
        breath_signal.append(float(row[2]))  # 3행의 데이터를 breath_signal에 추가합니다.
        heart_signal.append(float(row[3]))  # 3행의 데이터를 breath_signal에 추가합니다.

print(heart_signal)
unwrap_signal = [0.5, 0.4, 0.3, 0.2, 0.1]  # 예시로 주어진 데이터

processing_received_msg(breath_signal, heart_signal)