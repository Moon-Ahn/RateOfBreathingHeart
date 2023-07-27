import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# 호흡신호를 일정한 간격으로 공급
raw_signal = np.array([-0.13070208
,-0.13313238
,-0.13717818
,-0.14308916
,-0.15134983
,-0.16278747
,-0.17902705
,-0.19648659
,-0.21136354
,-0.22901106
,-0.25114673
,-0.27361745
,-0.29474533
,-0.3134356
,-0.32818294
,-0.3375827
,-0.3399341
,-0.33381915
,-0.32439578
,-0.3181448
,-0.3116275
,-0.3006637
,-0.28498816
,-0.26456714
,-0.24023294
,-0.211797
,-0.17877293
,-0.14257026
,-0.10573125
,-0.07022452
,-0.037283897
,-0.007673502
,0.018753767
,0.042536974
,0.06446576
,0.0860405
,0.107112646
,0.12565517
,0.14109492
,0.15376091
,0.162817
,0.1680777
,0.1707871
,0.1721394
,0.17297459
,0.1729486
,0.17100239
,0.16770005
,0.16462886
,0.16209686
,0.15972924
,0.15910137
,0.16157031
,0.16556978
,0.16995323
,0.17447567
,0.17855895
,0.1815728
,0.18319774
,0.18420863
,0.18440473
,0.1819042
,0.17519248
,0.16405576
,0.15062523
,0.13560236
,0.11890799
,0.104580075
,0.09412563
,0.08537468
,0.07799995
,0.0730609
,0.07036707
,0.068024814
,0.06548552
,0.06468159
,0.069865406
,0.08090168
,0.09110884
,0.09739941
,0.10031457
,0.10190806
,0.1040065
,0.10647029
,0.110240534
,0.11491296
,0.11908311
,0.12225407
,0.123983085
,0.12425551
,0.12296587
,0.11959171
,0.11422038
,0.10782373
,0.10106647
,0.09391004
,0.086373985
,0.07867122
,0.07095033
,0.06277686
,0.05360627
,0.044468045
,0.036129713
,0.027821183
,0.019839048
,0.01256299
,0.00522995
,-0.003048658
,-0.012037754
,-0.02079463
,-0.029673934
,-0.03900397
,-0.048227668
,-0.056421638
,-0.06332195
,-0.070512116
,-0.07900727
,-0.08834982
,-0.09685993
,-0.10259408
,-0.10536307
,-0.10438734
,-0.098701775
,-0.08903521
,-0.076170266
,-0.062084436
,-0.050643355
,-0.04308331
,-0.037784636
,-0.033362716
,-0.028613985
,-0.02430734
,-0.025007397
,-0.0322195
,-0.039445966
,-0.041593224
,-0.039517194
,-0.036670268
,-0.035199016
,-0.0321275
,-0.022090763
,8.25E-04
,0.03570026
,0.07162076
,0.10156256
,0.13616005
,0.19119185
,0.2574266
,0.31311315
,0.3521316
,0.37765986
,0.39126992
,0.39373922
,0.3861314
,0.36825585
,0.3413068
,0.30867004
,0.27233982
,0.2341435
,0.19619656
,0.15855479
,0.12044859
,0.08201671
,0.044016838
,0.006501436
,-0.030766249
,-0.06778693
,-0.104813576
,-0.14074087
,-0.17364168
,-0.20239449
,-0.22609258
,-0.24432826
,-0.25785112
,-0.2679689
,-0.27493215
,-0.27780986
,-0.2759676
,-0.26922047
,-0.25656116
,-0.23271918
,-0.19804513
,-0.16495681
,-0.14021248
,-0.12227082
,-0.109624445
,-0.10045534
,-0.093539536
,-0.088730454
,-0.08626783
,-0.085885584
,-0.08723742
,-0.09051651
,-0.09596461
,-0.10407695
,-0.11823544
,-0.14073896
,-0.1661987
,-0.18786676
,-0.20339961
,-0.21246663
,-0.21571814
,-0.2141407
,-0.20784849
,-0.19629133
,-0.17990512
,-0.15967649
,-0.13679492
,-0.114275694
,-0.09413546
,-0.07636118
,-0.061714113
,-0.050940096
,-0.044009507
,-0.041130006
,-0.042779565
,-0.04901147
,-0.058585882
,-0.06935954
,-0.07995045
,-0.09072757
,-0.1030432
,-0.116677284
,-0.12931597
,-0.13908815
,-0.14556742
,-0.1489476
,-0.14984441
,-0.14970541
,-0.15016234
,-0.15151167
,-0.15300477
,-0.15324056
,-0.150913
,-0.14534402
,-0.13552952
,-0.12088132
,-0.10214615
,-0.08144426
,-0.06111169
,-0.041888714
,-0.023184061
,-0.004292011
,0.014667749
,0.033377647
,0.051258802
,0.06714463
,0.080199
,0.08906746
,0.09304643
,0.09344196
,0.09144688
,0.088398695
,0.086722374
,0.08907962
,0.09817886
,0.114616394
,0.13691568
,0.16355884
,0.1923511
,0.22041106
,0.24447799
,0.2620262
,0.27274454
,0.27775192
,0.27815127
,0.27498692
,0.26949733
,0.26227188
,0.25364345
,0.24398446
,0.23323679
,0.22226633
,0.21227306
,0.20311551
,0.19423452
,0.18518466
,0.17491159
,0.1615985
,0.14479083
,0.12600279
,0.10621351
,0.08557767
,0.064152
,0.04308015
,0.024793208
,0.010473132
-2.78E-04
,-0.007504702
,-0.009239078
,-0.002963722
,0.011801183
,0.031086087
,0.04941225
,0.06444472
,0.0739916
,0.078371406
,0.076978624
,0.060091257
,0.027107239
,-0.006376028
,-0.03324318
,-0.054490924
,-0.0692901
,-0.079316676
,-0.079886675
,-0.06596941
,-0.04453045
,-0.021070063
,0.004692614
,0.03068173
,0.052297354
,0.06620532
,0.07098538
,0.06505293
,0.047096968
,0.018092275
,-0.01819235
,-0.057035267
,-0.09419292
,-0.12713397
,-0.15623224
,-0.1832093
,-0.20970833
,-0.23848313
,-0.27169752
,-0.30988866
,-0.35360628
,-0.40126282
,-0.4483096
,-0.4888919
,-0.51843965
,-0.5350903
,-0.5374024
,-0.52441525
,-0.49720097
,-0.4582193
,-0.4107299
,-0.36311293
,-0.32539654
,-0.29561162
,-0.26361132
,-0.22483587
,-0.18059683
,-0.13217306
,-0.07985997
,-0.026223898
,0.024442196
,0.06952977
,0.10799408
,0.14140725
,0.17447329
,0.20931983
,0.2430985
,0.27293086
,0.29924822
,0.32375097
,0.34632564
,0.36525393
,0.37933886
,0.38811815
,0.39065683
,0.38501847
,0.36899257
,0.34308982
,0.31183606
,0.2804116
,0.25163305
,0.22669375
,0.2071825
,0.19424549
,0.18708947
,0.18489769
,0.1870918
,0.19193661
,0.19777805
,0.20346546
,0.20803598
,0.21082687
,0.21147346
,0.20975065
,0.20482683
,0.19507045
,0.17840934
,0.1545291
,0.1265508
,0.099291325
,0.0771327
,0.06254959
,0.056048155
,0.057491302
,0.066438794
,0.0818398
,0.10214448
,0.12436485
,0.1448921
,0.15865123
,0.15924406
,0.14637935
,0.1240648
,0.09475684
,0.06257999
,0.032881737
,0.008648872
,-0.00904727
,-0.024853706
,-0.049076796
,-0.081992745
,-0.11240995
,-0.13409233
,-0.14803433
,-0.15658689
,-0.16156745
,-0.16459143
,-0.16836631
,-0.17536855
,-0.1865691
,-0.20298076
,-0.22261953
,-0.23717993
,-0.24213916
,-0.24264634
,-0.24284387
,-0.2416535
,-0.23796448
,-0.23136136
,-0.22172979
,-0.20996113
,-0.19685006
,-0.18268271
,-0.16816735
,-0.15444803
,-0.14232102
,-0.1320892
,-0.12366441
,-0.11556202
,-0.105118096
,-0.09114528
,-0.07515085
,-0.05926615
,-0.044081867
,-0.028814435
,-0.012141585
,0.006539941
,0.025752902
,0.035250127
,0.020706952
,-0.021821499
,-0.0812574
,-0.13757783
,-0.18049741
,-0.2089966
,-0.22168636
,-0.21959376
,-0.20461321
,-0.17802668
,-0.14332724
,-0.10573459
,-0.06798792
,-0.030029893
,0.008883119
,0.04799795
,0.0851506
,0.11874986
,0.14797485
,0.17280161
,0.1939038
,0.21164572
,0.22640169
,0.23889112
,0.24890697
,0.25602484
,0.26158488
,0.26714092
,0.27220047
,0.27593467
,0.27899936
,0.28183037
,0.28287292
,0.28034922
,0.27416012
,0.26412076
,0.24939013
,0.23057204
,0.2099992
,0.18965548
,0.17036057
,0.15266943
,0.13733935
,0.12484217
,0.11420238
,0.104124546
,0.09405577
,0.08380127
,0.073919415
,0.06530857
,0.05816245
,0.05100119
,0.04225421
,0.03250575
,0.022524238
,0.011645794
-2.78E-04
,-0.012021065
,-0.022108674
,-0.027891517
,-0.024998069
,-0.015388727
,-0.00785625
,-0.00529635
,-0.006352067
,-0.012055516
,-0.022194147
,-0.033780813
,-0.044571638
,-0.054183602
,-0.063628316
,-0.076467395
,-0.09480274
,-0.116393924
,-0.13795519
,-0.15687943
,-0.17083216
,-0.18045712
,-0.18873596
,-0.19652367
,-0.20538491
,-0.21512079
,-0.22551626
,-0.24048507
,-0.25870955
,-0.27637735
,-0.29323462
,-0.30854642
,-0.31926322
,-0.32251853
,-0.31753406
,-0.30454805
,-0.28436893
,-0.25825
,-0.22732824
,-0.1924293
,-0.15398991
,-0.11293423
,-0.072110295
,-0.035192013
,-0.005165815
,0.017450094
,0.035297155
,0.051824212
,0.0703336
,0.09158909
,0.11304355
,0.13300872
,0.15024424
,0.16365725
,0.1731689
,0.17923588
,0.18555272
,0.19531018
,0.2061997
,0.21500924
,0.22100121
,0.22347343
,0.22107413
,0.21423303
,0.2046918
,0.19327025
,0.18016762
,0.16586545
,0.15174377
,0.13945457
,0.12924242
,0.12206411
,0.11925197
,0.11937815
,0.12060225
,0.12113923
,0.11851013
,0.111147285
,0.09821379
,0.079330325
,0.054521203
,0.024112105
,-0.010462999
,-0.048141003
,-0.09329736
,-0.1494016
,-0.20788258
,-0.25867832
,-0.29899275
,-0.32826567
,-0.3480213
,-0.36017224
,-0.36495572
,-0.36209464
,-0.35172492
,-0.33428273
,-0.31044158
,-0.28229666
,-0.25237352
,-0.22188354
,-0.19093573
,-0.15629792
,-0.12083781
,-0.09719789
,-0.0853585
,-0.07159901
,-0.048219085
,-0.019719124
,0.006873965
,0.0323596
,0.058363676
,0.08056128
,0.10375512
,0.13960934
,0.18298316
,0.22086239
,0.24910748
,0.2683072
,0.27923036
,0.28371316
,0.28462666
,0.28385383
,0.2830447
,0.282708
,0.2811682
,0.27712107
,0.26936337
,0.25672433
,0.239883
,0.22051626
,0.19982433
,0.17813104
,0.15569383
,0.13287377
,0.10880613
,0.082660556
,0.05644393
,0.032453775
,0.01066792
,-0.00823164
,-0.024567127
,-0.042433262
,-0.062604666
,-0.08163738
,-0.099553585
,-0.11739445
,-0.13302583
,-0.14374536
,-0.1480093
,-0.14601237
,-0.14025652
,-0.13342083
,-0.12687665
,-0.121112466
,-0.115662545
,-0.109505296
,-0.10202634
,-0.094115674
,-0.08722463
,-0.081998184
,-0.07883786
,-0.078239694
,-0.08048533
,-0.08537114
,-0.091654
,-0.097490326
,-0.10247362
,-0.108452305
,-0.11462933
,-0.11737868
,-0.11776456
,-0.117657244
,-0.11278111
,-0.09841472
,-0.07671511
,-0.05476582
,-0.036477447
,-0.021383405
,-0.009574831
,-0.001365662
,0.004027844
,0.007762313
,0.011620402
,0.016937792
,0.023850024
,0.032919943
,0.04383117
,0.05288902
,0.057891995
,0.058480024
,0.053763717
,0.0448651
,0.0329836
,0.024178326
,0.029060185
,0.05006355
,0.0801768
,0.11178094
,0.14109671
,0.16746724
,0.1978233
,0.2462636
,0.32034183
,0.4127842
,0.5060898
,0.5841912
,0.6458062
,0.70178854
,0.75580454
,0.79876363
,0.8208859
,0.8205149
,0.801245
,0.7629559
,0.70400953
,0.6304598
,0.5504246
,0.46793747
,0.38554382
,0.3034706
,0.2203803
,0.13620186
,0.05467367
,-0.015089989
,-0.07075548
,-0.12283516
,-0.17869997
,-0.23822975
,-0.29854584
,-0.35725212
,-0.41321707
,-0.4616723
,-0.4992571
,-0.5276079
,-0.5474744
,-0.5585482
,-0.56372
,-0.5674014
,-0.5710919
,-0.5733764
,-0.573683
,-0.5728638
,-0.5721345
,-0.5748137
,-0.5842937
,-0.59722996
,-0.605157
,-0.60376114
,-0.59401584
,-0.57889456
,-0.5614617
,-0.54382575
,-0.52764726
,-0.51478815
,-0.507393
,-0.50576794
,-0.50664556
,-0.50547314
,-0.5003879
,-0.49227858
,-0.48122787
,-0.4652102
,-0.4418671
,-0.4099114
,-0.36956835
,-0.3223045
,-0.2702155
,-0.2155385
,-0.1598134
,-0.104486465
,-0.051574707
,-0.00327301
,0.038573265
,0.074300766
,0.10627556
,0.13709307
,0.16680813
,0.19312334
,0.21559858
,0.23498654
,0.2503152
,0.25826144
,0.25623918
,0.24622488
,0.23253202
,0.21768641
,0.20352244
,0.1919949
,0.1832633
,0.17750025
,0.17581224
,0.17826247
,0.18324351
,0.18914008
,0.19507885
,0.20080519
,0.20787239
,0.21737862
,0.22816956
,0.23809254
,0.2453233
,0.24976933
,0.25196612
,0.2518599
,0.24997723
,0.24711323
,0.24348068
,0.23944122
,0.23502529
,0.22894704
,0.21963531
,0.20619613
,0.188582
,0.16832718
,0.14787763
,0.12887415
,0.111887306
,0.09716834
,0.08447066
,0.07354008
,0.06695475
,0.06873387
,0.077054545
,0.08533698
,0.089874804
,0.09021455
,0.08707771
,0.08137357
,0.0732007
,0.06281912
,0.050921142
,0.037665725
,0.023340464
,0.005508184
,-0.02145359
,-0.057539016
,-0.097254604
,-0.13722804
,-0.17536703
,-0.20911911
,-0.23681438
,-0.25706902
,-0.26898047
,-0.27200216
,-0.27430347
,-0.28767222
,-0.30544132
,-0.3145008
,-0.31064183
,-0.29294324
,-0.2627132
,-0.2230637
,-0.17756045
,-0.12880325
,-0.078188896
,-0.027255654
,0.022329211
,0.069303155
,0.112847924
,0.15178776
,0.18492115
,0.21303165
,0.2381022
,0.26152682
,0.283414
,0.30253243
,0.31729823
,0.32857478
,0.34046346
,0.35589713
,0.37324846
,0.38759056
,0.3952545
,0.39849177
,0.40617812
,0.41966057
,0.42780876
,0.4252714
,0.41386104
,0.3943591
,0.3678708
,0.3360566
,0.30015326
,0.26096082
,0.2196002
,0.17806101
,0.13811564
,0.10048747
,0.06556344
,0.03398776
,0.005907536
,-0.019609451
,-0.04379654
,-0.066525936
,-0.08389306
,-0.09338617
,-0.099855185
,-0.10890865
,-0.12370443
,-0.14572525
,-0.1712153
,-0.19656777
,-0.22269487
,-0.24968743
,-0.27474582
,-0.29592264
,-0.31400454
,-0.3298136
,-0.34375834
,-0.3563999
,-0.36689723
,-0.37472004
,-0.38087678
,-0.38598555
,-0.38956368
,-0.39083907
,-0.39017624
,-0.3883913
,-0.38503718
,-0.37892544
,-0.36872154
,-0.35293233
,-0.33056986
,-0.30189824
,-0.26823103
,-0.23036468
,-0.1887101
,-0.14431357
,-0.09824169
,-0.051519513
,-0.00576818
,0.036801934
,0.07446182
,0.107085824
,0.13557577
,0.16047537
,0.18188846
,0.20040584
,0.21595156
,0.22735572
,0.23485303
,0.23929119
,0.23975736
,0.2357701
,0.2287116
,0.21993601
,0.21052414
,0.20101687
,0.1921986
,0.18546787
,0.18008354
,0.17382792
,0.16547015
,0.15611967
,0.14734048
,0.13962126
,0.13428399
,0.1308136
,0.12700921
,0.122273564
,0.117173254
,0.11205137
,0.105982006
,0.09819937
,0.08969933
,0.08244389
,0.07741594
,0.074035406
,0.07106298
,0.06734961
,0.062146664
,0.05452752
,0.044076443
,0.03231156
,0.020917773
,0.010035753
-8.60E-04
,-0.011933923
,-0.023627043
,-0.037653804
,-0.056474566
,-0.085434854
,-0.12732583
,-0.17455488
,-0.21862584
,-0.25671947
,-0.2882976
,-0.31364423
,-0.33349577
,-0.34831753
,-0.35828024
,-0.36529753
,-0.37195215
,-0.37930602
,-0.38627625
,-0.38960505
,-0.38673675
,-0.37733638
,-0.36092722
,-0.3367052
,-0.30479264
,-0.26562595
,-0.2175479
,-0.16012955
,-0.09801149
,-0.034839153
,0.027605772
,0.08711147
,0.14220452
,0.19166279
,0.23444319
,0.26962662
,0.29690087
,0.31681538
,0.33018768
,0.3376788
,0.33976054
,0.33695304
,0.33012837
,0.3205396
,0.3084771
,0.29265118
,0.2737725
,0.25540715
,0.23894739
,0.2225748
,0.20470935
,0.18591215
,0.16781342
,0.15173164
,0.13795117
,0.12556928
,0.1136747
,0.10193765
,0.09115887
,0.08156687
,0.07373077
,0.06943977
,0.06718862
,0.06392062
,0.058766544
,0.052723587
,0.045645177
,0.03542745
,0.022057295
,0.007484317
,-0.007085323
,-0.021499515
,-0.03564644
,-0.049393833
,-0.0623613
,-0.07478005
,-0.086455345
,-0.09503454
,-0.101309896
,-0.10962403
,-0.12241185
,-0.13909942
,-0.15835053
,-0.17898023
,-0.19955167
,-0.21909988
,-0.23711213
,-0.25323623
,-0.2677871
,-0.2815972
,-0.29379314
,-0.30232036
,-0.30644512
,-0.30574954
,-0.29933608
,-0.2872181
,-0.27194142
,-0.25672054
,-0.24262309
,-0.22998059
,-0.21944046
,-0.2106427
,-0.20162988
,-0.1885736
,-0.16759658
,-0.13724756
,-0.099021435
,-0.056292295
,-0.010947943
,0.037080765
,0.088076115
,0.14083004
,0.19241023
,0.24002111
,0.28191555
,0.31800628
,0.34936094
,0.3767357
,0.40028846
,0.4198587
,0.43562442
,0.4474746
,0.45415953
,0.45531827
,0.451528
,0.44304597
,0.43019935
,0.41384643
,0.39485836
,0.37153518
,0.34105122
,0.3052987
,0.26890278
,0.23334992
,0.19874835
,0.16626644
,0.13577855
,0.105814695
,0.0755744
,0.045155287
,0.01672411
,-0.007115841
,-0.025762796
,-0.04084134
,-0.05505705
,-0.06881833
,-0.081204176
,-0.09167409
,-0.09962022
,-0.105238795
,-0.10950172
,-0.11312783
,-0.117292166
,-0.12385142
,-0.13263202
,-0.14304888
,-0.15592694
,-0.17001295
,-0.18357837
,-0.19733965
,-0.21235204
,-0.22926277
,-0.24885935
,-0.27180707
,-0.29989088
,-0.33706075
,-0.3826471
,-0.42932618
,-0.4731703
,-0.51360434
,-0.5476167
,-0.57014936
,-0.57705903
,-0.5661434
,-0.536654
,-0.4909047
,-0.4309976
,-0.3587587
,-0.27860045
,-0.19594431
,-0.11531615
,-0.03334117
,0.052886248
,0.1344819
,0.20555472
,0.26722455
,0.31999636
,0.36386156
,0.39915442
,0.4278518
,0.45145357
,0.4694916
,0.48046517
,0.48335958
,0.4774487
,0.4616354
,0.43679264
,0.4056611
,0.37042627
,0.33206272
,0.29100102
,0.24752796
,0.20118785
,0.15345752
,0.11018932
,0.07645351
,0.053877354
,0.04164517
,0.036173522
,0.034599066
,0.03660226
,0.040723205
,0.043685198
,0.043931127
,0.04232812
,0.039584875
,0.035374403
,0.029780626
,0.022735596
,0.012702107
,-0.001064062
,-0.016299486
])

# 측정 시간 (15초)
duration = 60

# 샘플링 빈도 추정
fs = len(raw_signal) / duration

# 필터링 및 피크 찾기 (최소 피크 높이와 거리 조정)
filtered_signal = scipy.signal.medfilt(raw_signal, kernel_size=19)
peaks, _ = scipy.signal.find_peaks(filtered_signal, distance=int(fs), height=0.1)

# 호흡 수 파악
brpm = len(peaks) * 60 / duration

plt.figure(figsize=(15,5))
plt.plot(raw_signal, label="Raw signal")
plt.plot(filtered_signal, label="Filtered signal", linestyle="--")
plt.plot(peaks, filtered_signal[peaks], 'r*', markersize=10, label="Peaks")
plt.title(f"Estimated Breathing Rate: {brpm:.1f} BPM")
plt.legend()
plt.show()