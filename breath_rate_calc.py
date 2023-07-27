import numpy as np

#레이더 모듈에서 50msec 가격마다 측정하여 10개씩 묶어 500msec 간격으로 블루투스를 통해 신호 전달
#10초 동안의 200개 데이터를 기준으로 호습수를 주파수 분석결과로 카운팅

# 1초 ~ 5초 이내 간격으로 호흡 수를 계산하여 디스플레이하는 것이 적당할 것으로 판단됨..
# 블루투스 신호가 들어 올 때마다 계산하여 표시하면 값이 왔따 갔따 하는 것처럼 보일 수 있음.
# 1초마다 계산하더라도 5초 동안의 평균 호습수를 계산하여 표시하는 방안되 괜찮음.


# 아래 breath_signal은 실제 신호를 사용하면 됨.
# 본 코드에서는 10초에 3번 호흡(분당 18회)하는 신호를 임의로 생성하여 진행
t = np.arange(0, 10, 0.05)                  # 10초동안 50msec 간격으로 신호 생성을 위해
breath_signal = 0.2*np.cos(2*np.pi*0.3*t)   # 1초에 0.3번 호흡하는 신호 생성
num_of_samples = len(breath_signal)         # 데이터 수 200개

signal_energy = np.power(breath_signal, 2)  # 전체 신호에 대하여 제곱하여 다 더한다...
평균에너지 = np.sum(signal_energy)
print("평균에너지 : ", np.sum(signal_energy))


# 호흡 신호의 에너지를 계산했을 때 1이하이면 호흡은 없는 것으로 가정해도 됨...
if 평균에너지 < 1:
    print('호흡신호 없는 상태, 호흡 수는 0.')




Y = np.fft.fft(breath_signal) / num_of_samples # 주파수 분석
######################
import matplotlib.pyplot as plt

# 주파수 영역 생성
freq = np.fft.fftfreq(num_of_samples)

# 그래프 표시
plt.plot(freq, np.abs(Y))
plt.title('Breath Signal FFT')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()
######################

Y = Y[range(int(num_of_samples / 2))]          # 주파수 분석 결과 에서 절반만 가져다 쓴다
                                               # fft 결과인 Y의 버퍼의 왼쪽 절반은 양의 주파수, 오른쪽 절반은 음의 주파수를 의미하여, 양의 주파수 부분만 사용
amplitude_Hz = 2 * abs(Y)                      # 주파수별 크기를 계산, 각 요소별 절대값에 2배
amplitude_Hz[0:2] = 0                          # 0, 0.1인 주파수 부분 제거
                                               # 측정이 되지 않는 부분인데 노이즈로 인해 해당 저주파 부분인 크게 나오는 경우 방지하기 위함.

max_index = np.argmax(amplitude_Hz)            #에서 가장 큰 값을 갖는 index 추출
                                               #index의 값에 따라 호흡 주기가 결정됨.


# breathing_ratedms 해당 index가 의미하는 주파수 값(1초 기준)
breathing_rate = max_index / 10                #여기서 10은 10초 (num_of_samples / 0.05(50msec))를 의미함.

# 60초 / 1분 단위로 변환
breathing_rate_min = breathing_rate*60
print(breathing_rate_min)



# self.update_breath_sign_plot(x)