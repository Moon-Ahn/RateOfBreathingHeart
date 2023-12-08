import os
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

folder_path = r'F:\차신호실험\11월24일(조수석,특정신호)'  # 폴더 경로를 변경하세요
output_file = r'F:\차신호실험\11월24일(조수석,특정신호)_통합.csv'  # 원하는 출력 파일 이름을 입력하세요

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

data_frames = []

# 사용자 지정 헤더 생성  (중요)
#column_names = ['Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5']
# time, unwrapPhaseSignal, filterBreathSignal, filterHeartSignal, status,
#             leBlinkingCount, reBlinkingCount, leDownElapsed, reDownElapsed, co2, bkStatus, fatigueSignal
column_names = ['time', 'unwrapPhaseSignal', 'filterBreathSignal', 'filterHeartSignal', 'status','leBlinkingCount',
                'reBlinkingCount', 'leDownElapsed', 'reDownElapsed','co2','bkStatus','fatigueSignal']

# def add_noise(signal, noise_level=0.01):
#     noise = np.random.normal(0, noise_level, len(signal))
#     return signal + noise
#
# def time_stretch(signal, factor):
#     original_indices = np.arange(len(signal))
#     new_indices = np.linspace(0, len(signal), int(len(signal) * factor))
#     interpolator = interp1d(original_indices, signal)
#     return interpolator(new_indices)
#
# def jitter_signal(signal, jitter_amount):
#     jittered_signal = signal + (np.random.randn(len(signal)) * jitter_amount)
#     return jittered_signal

for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)

    # 사용자 지정 헤더를 적용하여 데이터프레임을 불러옵니다.
    data_frame = pd.read_csv(file_path, header=None, names=column_names)

    data_frames.append(data_frame)
    print(data_frame)

merged_csv = pd.concat(data_frames)

merged_csv.to_csv(os.path.join(folder_path, output_file), index=False)