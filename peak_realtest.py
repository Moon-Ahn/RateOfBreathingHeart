import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# 심박신호를 일정한 간격으로 공급
raw_signal = np.array([0.07915026
,0.14713599
,0.14321962
,0.08415075
,0.02889405
,0.004826814
,-0.011799965
,-0.017073054
,0.0564297
,0.15455423
,0.090695605
,-0.09463709
,-0.13751665
,0.019178651
,0.16632041
,0.15394282
,0.044691965
,-0.027072221
,-0.06543568
,-0.2063342
,-0.40747362
,-0.38196173
,-0.05384375
,0.26089707
,0.28249162
,0.09085349
,-0.047019456
,-0.022886097
,0.03321722
,-0.013392855
,-0.1176585
,-0.14706112
,-0.059289828
,0.07325651
,0.16395575
,0.19259542
,0.18307629
,0.13022873
,0.023760855
,-0.07751574
,-0.10509801
,-0.07573104
,-0.040117107
,-0.006086048
,0.032347105
,0.0496733
,0.011333525
,-0.062622815
,-0.09181871
,-0.038840838
,0.026366118
,0.033928942
,0.015493382
,0.011674969
,-0.012225021
,-0.07311997
,-0.11572407
,-0.09857805
,-0.045312017
,0.007608816
,0.050013542
,0.06447688
,0.027339943
,-0.030390747
,-0.024989314
,0.07386291
,0.17513317
,0.19873048
,0.18352476
,0.14758582
,0.040014833
,-0.10293862
,-0.17138788
,-0.1568401
,-0.14609003
,-0.15162474
,-0.08182885
,0.075509
,0.13114625
,-0.06427248
,-0.32139888
,-0.31623948
,-0.018681318
,0.28213894
,0.34183732
,0.20488712
,0.05490193
,-0.015272595
,-0.025131006
,-0.019719929
,-0.016774546
,-0.01622054
,-0.017821828
,-0.01085142
,0.016476663
,0.044884406
,0.039634734
,0.001423746
,-0.03349614
,-0.044753097
,-0.048706006
,-0.053259324
,-0.034854047
,0.002498411
,0.016536877
,9.40E-04
,-0.015024763
,-0.025826646
,-0.0363902
,-0.025160756
,0.01728693
,0.05119236
,0.046726014
,0.033328734
,0.04474843
,0.052212715
,0.00600012
,-0.06625274
,-0.07363644
,0.018015426
,0.12666416
,0.14546317
,0.07449725
,-0.007642105
,-0.0632467
,-0.11243923
,-0.18497929
,-0.26295966
,-0.25234562
,-0.091266334
,0.13244618
,0.2550472
,0.1825972
,-0.021778964
,-0.12135425
,0.07272137
,0.38550594
,0.42425215
,0.08978093
,-0.2701141
,-0.2717429
,0.06981383
,0.36763895
,0.22684051
,-0.34881845
,-0.7874695
,-0.45649663
,0.37495303
,0.5773696
,-0.2880183
-1.1774278
,-0.9835069
,0.034614682
,0.8101588
,0.8266883
,0.4493062
,0.24697375
,0.35317308
,0.48426193
,0.39938328
,0.14740467
,-0.1019091
,-0.25784582
,-0.31822926
,-0.31707543
,-0.29783133
,-0.28302097
,-0.26152372
,-0.2089254
,-0.10868819
,0.019076109
,0.11544606
,0.13966116
,0.10211634
,0.036777228
,-0.017941512
,-0.020052396
,0.041455694
,0.11623561
,0.14581552
,0.15872371
,0.20322295
,0.13158631
,-0.22901964
,-0.62528515
,-0.5943446
,-0.11953512
,0.35537347
,0.4801795
,0.30777574
,0.10915801
,0.048228845
,0.07562646
,0.0680134
,-0.010117874
,-0.117201254
,-0.21792714
,-0.23353355
,-0.046905037
,0.27073255
,0.4310872
,0.26856968
,-0.06305477
,-0.29103315
,-0.2996565
,-0.1859684
,-0.10937776
,-0.12448316
,-0.17620903
,-0.2010219
,-0.15987423
,-0.046602517
,0.08404806
,0.16689551
,0.19484371
,0.19577874
,0.18609512
,0.17638215
,0.18516932
,0.20888484
,0.1948088
,0.08925158
,-0.07434657
,-0.1737527
,-0.13196698
,-0.026408926
,2.17E-04
,-0.08884883
,-0.20739356
,-0.2684151
,-0.25119725
,-0.16931468
,-0.043763965
,0.08878794
,0.17862192
,0.1987947
,0.1697122
,0.12132881
,0.050173916
,-0.05309492
,-0.1469591
,-0.15401167
,-0.053363897
,0.07408659
,0.12584701
,0.08391084
,0.009170763
,-0.040497042
,-0.055420198
,-0.055587552
,-0.038231585
,0.021121226
,0.10691124
,0.17043823
,0.19329734
,0.19070615
,0.16025405
,0.06322542
,-0.10968277
,-0.2878257
,-0.38896853
,-0.4013616
,-0.36107606
,-0.27591857
,-0.11799747
,0.09901041
,0.28891453
,0.37358993
,0.35384113
,0.2809716
,0.19919513
,0.123752415
,0.056831717
,0.010944992
,-0.013431758
,-0.04896006
,-0.11446458
,-0.18287434
,-0.22407773
,-0.22971095
,-0.18154153
,-0.06819391
,0.057205364
,0.11410143
,0.09615566
,0.082238466
,0.12436616
,0.16381183
,0.11712388
,0.01670593
,-0.019763276
,0.035508513
,0.04940532
,-0.11312936
,-0.37314278
,-0.49240083
,-0.3537313
,-0.07480264
,0.081870586
,-0.013831675])  # 여기에 심박 신호 값을 추가합니다.

# 측정 시간 (15초)
duration = 15

# 샘플링 빈도 추정
fs = len(raw_signal) / duration

# 필터링 및 피크 찾기 (최소 피크 높이와 거리 조정)
filtered_signal = scipy.signal.medfilt(raw_signal, kernel_size=9)
peaks, _ = scipy.signal.find_peaks(filtered_signal, distance=fs//2, height=0.1)

# 심박수 파악
bpm = len(peaks) * 60 / duration

plt.figure(figsize=(15, 5))
plt.plot(raw_signal, label="Raw signal")
plt.plot(filtered_signal, label="Filtered signal", linestyle="--")
plt.plot(peaks, filtered_signal[peaks], 'r*', markersize=10, label="Peaks")
plt.title(f"Estimated Heart Rate: {bpm:.1f} BPM")
plt.legend()
plt.show()