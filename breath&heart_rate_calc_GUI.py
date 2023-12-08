import csv
import sys
import numpy as np
from scipy.fft import fft, ifft
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QPushButton, QLineEdit, QFileDialog, QLabel, QGridLayout

class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Signal Processing')
        self.setGeometry(300, 300, 800, 600)

        self.figure = Figure(figsize=(5, 10), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        self.loadBtn = QPushButton('Load')
        self.loadBtn.clicked.connect(self.load_file)

        self.startBtn = QPushButton('Start')
        self.startBtn.clicked.connect(self.start_processing)

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setText('0.15')  # 초기값 설정
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setText('0.3')  # 초기값 설정
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setText('0.7')  # 초기값 설정
        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setText('2.0')  # 초기값 설정

        self.breathRateLabel = QLabel()  # Breath Rate를 표시할 레이블
        self.heartRateLabel = QLabel()  # Heart Rate를 표시할 레이블

        layout = QGridLayout()
        layout.addWidget(self.loadBtn, 0, 0)
        layout.addWidget(QLabel('Cutoff Bandpass Filter Values:'), 0, 1)
        layout.addWidget(self.lineEdit1, 0, 2)
        layout.addWidget(self.lineEdit2, 0, 3)
        layout.addWidget(self.lineEdit3, 0, 4)
        layout.addWidget(self.lineEdit4, 0, 5)
        layout.addWidget(self.breathRateLabel, 0, 6)  # 레이아웃에 Breath Rate 레이블 추가
        layout.addWidget(self.heartRateLabel, 0, 7)  # 레이아웃에 Heart Rate 레이블 추가
        layout.addWidget(self.startBtn, 0, 8)
        layout.addWidget(self.canvas, 1, 0, 1, 9)

        self.setLayout(layout)

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            with open(fname[0], 'r') as file:
                reader = csv.reader(file)
                self.breath_signal = []
                self.heart_signal = []
                for row in reader:
                    self.breath_signal.append(float(row[2]))
                    self.heart_signal.append(float(row[3]))

            self.plot(self.breath_signal, self.heart_signal)

    def start_processing(self):

        # 초기값 설정
        breath_signal_bpm = 0
        heart_signal_bpm = 0

        cutoff_freq_begin1 = float(self.lineEdit1.text())
        cutoff_freq_end1 = float(self.lineEdit2.text())
        cutoff_freq_begin2 = float(self.lineEdit3.text())
        cutoff_freq_end2 = float(self.lineEdit4.text())

        filtered_breath_signal = self.cutoff_bandpass_filter(self.breath_signal, cutoff_freq_begin1, cutoff_freq_end1)
        filtered_heart_signal = self.cutoff_bandpass_filter(self.heart_signal, cutoff_freq_begin2, cutoff_freq_end2)

        ##그래프 길이를 맞추어 출력##
        filtered_breath_signal = filtered_breath_signal[:len(filtered_breath_signal) // 2]
        filtered_heart_signal = filtered_heart_signal[:len(filtered_heart_signal) // 2]

        if self.check_vital_signal_detected(filtered_breath_signal, 1.0):
            crossing_indices_for_breath = self.find_zero_crossings(filtered_breath_signal)
            peak_indices_for_breath = self.find_peak_indices(filtered_breath_signal)

            breath_signal_bpm = len(crossing_indices_for_breath) / 4
        else:
            pass

        if self.check_vital_signal_detected(filtered_heart_signal, 5.0):
            filtered_heart_signal_median = self.median_filter(filtered_heart_signal, 3)
            crossing_indices_for_heartbeat = self.find_zero_crossings(filtered_heart_signal_median)
            peak_indices_for_heartbeat = self.find_peak_indices(filtered_heart_signal_median)

            heart_signal_bpm = len(crossing_indices_for_heartbeat) / 4
        else:
            pass

        print("BreathRate:", breath_signal_bpm)
        print("HeartRate:", heart_signal_bpm)
        print()

        self.breathRateLabel.setText(f"BreathRate: {breath_signal_bpm}")
        self.heartRateLabel.setText(f"HeartRate: {heart_signal_bpm}")

        self.plot(self.breath_signal, self.heart_signal, filtered_breath_signal, filtered_heart_signal)

    def plot(self, breath_signal, heart_signal, filtered_breath_signal=None, filtered_heart_signal=None):

        self.figure.clear()
        ax1 = self.figure.add_subplot(211)
        ax1.plot(breath_signal, label='Original Breath Signal')
        if filtered_breath_signal:
            ax1.plot(filtered_breath_signal, label='Filtered Breath Signal')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Amplitude')
        ax1.set_title('Breath Signal')
        ax1.legend()

        ax2 = self.figure.add_subplot(212)
        ax2.plot(heart_signal, label='Original Heart Signal')
        if filtered_heart_signal:
            ax2.plot(filtered_heart_signal, label='Filtered Heart Signal')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Amplitude')
        ax2.set_title('Heart Signal')
        ax2.legend()

        self.canvas.draw()

    def cutoff_bandpass_filter(self, input_signal, cutoff_freq_begin, cutoff_freq_end):
        s_fft = fft(input_signal)
        fs = 20.0
        index_weight = fs / len(s_fft)

        cutoff_start_index = int(np.floor(cutoff_freq_begin / index_weight))
        cutoff_end_index = int(np.ceil(cutoff_freq_end / index_weight))

        s_fft2 = self.initialize_outside_range_to_zero(s_fft.tolist(), cutoff_start_index, cutoff_end_index)

        return ifft(s_fft2).real.tolist()

    def initialize_outside_range_to_zero(self, lst, start, end):
        lst[:start * 2] = [0.0] * (start * 2)
        lst[(end + 1) * 2:] = [0.0] * ((len(lst) - (end + 1)) * 2)
        return lst

    def check_vital_signal_detected(self, signal, energy_level=0.1):
        signal_energy = sum([x * x for x in signal])
        print("signal: ",signal_energy)
        return signal_energy > energy_level

    def find_zero_crossings(self, signal):
        zero_crossings = []
        for i in range(1, len(signal)):
            if (signal[i - 1] < 0 and signal[i] >= 0) or (signal[i - 1] >= 0 and signal[i] < 0):
                if signal[i - 1] < 0 and signal[i] >= 0:
                    zero_crossings.append(i)
        return zero_crossings

    def find_peak_indices(self, signal, threshold=0.0):
        peak_indices = []
        for i in range(1, len(signal) - 1):
            if signal[i] > signal[i - 1] and signal[i] > signal[i + 1] and signal[i] > threshold:
                peak_indices.append(i)
        return peak_indices

    def median_filter(self, signal, window_size):
        padding = window_size // 5
        padded_signal = [signal[0]] * padding + signal + [signal[-1]] * padding
        return [
            sorted(padded_signal[i:i+window_size])[padding]
            for i in range(len(signal))
        ]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())
