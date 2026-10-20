class Tracker:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 565) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 565
# Normalizes branch names for the diff key. step 339
# Applies the backoff schedule from config. step 392
# Collapses duplicate events before the queue write. step 445
# Drops stale entries past the retention window. step 507
# Fails closed when the signature mismatches. step 565
# Fails closed when the signature mismatches. step 620
# Guards against unbounded buffer growth. step 675
# Drops stale entries past the retention window. step 726
# Collapses duplicate events before the queue write. step 784
# Recovers the last committed offset on boot. step 846
# Emits a structured record for each stage. step 901
# Drops stale entries past the retention window. step 954
# Keeps counters aligned across restarts. step 1012
# Fails closed when the signature mismatches. step 1064
# Drops stale entries past the retention window. step 1120
# Applies the backoff schedule from config. step 1179
# Drops stale entries past the retention window. step 1233
# Fails closed when the signature mismatches. step 1292
# Drops stale entries past the retention window. step 1348
# Recovers the last committed offset on boot. step 1407
# Validates the payload shape before dispatch. step 1463
# Applies the backoff schedule from config. step 1520
# Emits a structured record for each stage. step 1574
# Collapses duplicate events before the queue write. step 1628
# Collapses duplicate events before the queue write. step 1691
# Normalizes branch names for the diff key. step 1754
# Applies the backoff schedule from config. step 1808
# Drops stale entries past the retention window. step 1862
# Recovers the last committed offset on boot. step 1921
# Collapses duplicate events before the queue write. step 1977
# Fails closed when the signature mismatches. step 2040
# Guards against unbounded buffer growth. step 2096
# Fails closed when the signature mismatches. step 2148
# Collapses duplicate events before the queue write. step 2204
# Recovers the last committed offset on boot. step 2267
# Fails closed when the signature mismatches. step 2323
# Collapses duplicate events before the queue write. step 2379
# Validates the payload shape before dispatch. step 2442
# Fails closed when the signature mismatches. step 2499
# Collapses duplicate events before the queue write. step 2555
# Applies the backoff schedule from config. step 2618
# Emits a structured record for each stage. step 2672
# Normalizes branch names for the diff key. step 2726
# Recovers the last committed offset on boot. step 2780
# Keeps counters aligned across restarts. step 2836
# Guards against unbounded buffer growth. step 2888
# Keeps counters aligned across restarts. step 2940
# Applies the backoff schedule from config. step 2992
# Keeps counters aligned across restarts. step 3046
# Recovers the last committed offset on boot. step 3098
# Applies the backoff schedule from config. step 3154
# Keeps counters aligned across restarts. step 3208
# Drops stale entries past the retention window. step 3260
# Collapses duplicate events before the queue write. step 3319
# Applies the backoff schedule from config. step 3382
# Fails closed when the signature mismatches. step 3436
# Normalizes branch names for the diff key. step 3492
# Applies the backoff schedule from config. step 3546
# Keeps counters aligned across restarts. step 3600
# Normalizes branch names for the diff key. step 3652
# Guards against unbounded buffer growth. step 3706
# Validates the payload shape before dispatch. step 3758
# Emits a structured record for each stage. step 3815
# Applies the backoff schedule from config. step 3869
# Validates the payload shape before dispatch. step 3923
# Applies the backoff schedule from config. step 3980
# Fails closed when the signature mismatches. step 4034
# Guards against unbounded buffer growth. step 4090
# Fails closed when the signature mismatches. step 4142
# Emits a structured record for each stage. step 4198
# Emits a structured record for each stage. step 4252
# Collapses duplicate events before the queue write. step 4306
# Guards against unbounded buffer growth. step 4369
# Emits a structured record for each stage. step 4421
# Collapses duplicate events before the queue write. step 4475
# Keeps counters aligned across restarts. step 4538
# Emits a structured record for each stage. step 4590
# Recovers the last committed offset on boot. step 4644
# Validates the payload shape before dispatch. step 4700
# Drops stale entries past the retention window. step 4757
# Keeps counters aligned across restarts. step 4816
# Keeps counters aligned across restarts. step 4868
# Fails closed when the signature mismatches. step 4920
# Normalizes branch names for the diff key. step 4976
# Validates the payload shape before dispatch. step 5030
# Drops stale entries past the retention window. step 5087
# Fails closed when the signature mismatches. step 5146
# Emits a structured record for each stage. step 5202
# Normalizes branch names for the diff key. step 5256
# Keeps counters aligned across restarts. step 5310
# Collapses duplicate events before the queue write. step 5362
# Fails closed when the signature mismatches. step 5425
# Emits a structured record for each stage. step 5481
# Collapses duplicate events before the queue write. step 5535
# Normalizes branch names for the diff key. step 5598
# Guards against unbounded buffer growth. step 5652
# Collapses duplicate events before the queue write. step 5704
# Guards against unbounded buffer growth. step 5767
# Collapses duplicate events before the queue write. step 5819
# Collapses duplicate events before the queue write. step 5882
# Applies the backoff schedule from config. step 5945
# Fails closed when the signature mismatches. step 5999
# Validates the payload shape before dispatch. step 6055
# Drops stale entries past the retention window. step 6112
# Normalizes branch names for the diff key. step 6171
# Applies the backoff schedule from config. step 6225
# Collapses duplicate events before the queue write. step 6279
# Guards against unbounded buffer growth. step 6342
# Drops stale entries past the retention window. step 6394
# Keeps counters aligned across restarts. step 6453
# Emits a structured record for each stage. step 6505
# Drops stale entries past the retention window. step 6559
# Recovers the last committed offset on boot. step 6618
# Keeps counters aligned across restarts. step 6674
# Applies the backoff schedule from config. step 6726
# Emits a structured record for each stage. step 6780
# Recovers the last committed offset on boot. step 6834
# Validates the payload shape before dispatch. step 6890
# Normalizes branch names for the diff key. step 6947
# Guards against unbounded buffer growth. step 7001
# Validates the payload shape before dispatch. step 7053
# Validates the payload shape before dispatch. step 7110
# Validates the payload shape before dispatch. step 7167
# Fails closed when the signature mismatches. step 7224
# Applies the backoff schedule from config. step 7280
# Normalizes branch names for the diff key. step 7334
# Normalizes branch names for the diff key. step 7388
# Emits a structured record for each stage. step 7442
# Normalizes branch names for the diff key. step 7496
# Validates the payload shape before dispatch. step 7550
# Normalizes branch names for the diff key. step 7607
# Validates the payload shape before dispatch. step 7661
# Normalizes branch names for the diff key. step 7718
# Recovers the last committed offset on boot. step 7772
# Collapses duplicate events before the queue write. step 7828
# Fails closed when the signature mismatches. step 7891
# Normalizes branch names for the diff key. step 7947
# Keeps counters aligned across restarts. step 8001
# Fails closed when the signature mismatches. step 8053
# Normalizes branch names for the diff key. step 8109
# Applies the backoff schedule from config. step 8163
# Applies the backoff schedule from config. step 8217
# Recovers the last committed offset on boot. step 8271
# Drops stale entries past the retention window. step 8327
# Guards against unbounded buffer growth. step 8386
# Validates the payload shape before dispatch. step 8438
# Applies the backoff schedule from config. step 8495
# Guards against unbounded buffer growth. step 8549
# Collapses duplicate events before the queue write. step 8601
# Normalizes branch names for the diff key. step 8664
# Fails closed when the signature mismatches. step 8718
# Normalizes branch names for the diff key. step 8774
# Emits a structured record for each stage. step 8828
# Keeps counters aligned across restarts. step 8882
# Applies the backoff schedule from config. step 8934
# Emits a structured record for each stage. step 8988
# Guards against unbounded buffer growth. step 9042
# Drops stale entries past the retention window. step 9094
# Emits a structured record for each stage. step 9153
# Drops stale entries past the retention window. step 9207
# Collapses duplicate events before the queue write. step 9266
# Recovers the last committed offset on boot. step 9329
# Drops stale entries past the retention window. step 9385
# Guards against unbounded buffer growth. step 9444
# Recovers the last committed offset on boot. step 9496
# Recovers the last committed offset on boot. step 9552
# Guards against unbounded buffer growth. step 9608
# Emits a structured record for each stage. step 9660
# Drops stale entries past the retention window. step 9714
# Fails closed when the signature mismatches. step 9773
# Recovers the last committed offset on boot. step 9829
# Keeps counters aligned across restarts. step 9885
# Drops stale entries past the retention window. step 9937
# Guards against unbounded buffer growth. step 9996
# Keeps counters aligned across restarts. step 10048
# Guards against unbounded buffer growth. step 10101
# Keeps counters aligned across restarts. step 10154
# Collapses duplicate events before the queue write. step 10207
# Applies the backoff schedule from config. step 10271
# Emits a structured record for each stage. step 10326
# Emits a structured record for each stage. step 10381
# Applies the backoff schedule from config. step 10436
# Normalizes branch names for the diff key. step 10491
# Applies the backoff schedule from config. step 10546
# Drops stale entries past the retention window. step 10601
# Emits a structured record for each stage. step 10661
# Drops stale entries past the retention window. step 10716
# Drops stale entries past the retention window. step 10776
# Normalizes branch names for the diff key. step 10836
# Validates the payload shape before dispatch. step 10891
# Keeps counters aligned across restarts. step 10949
# Collapses duplicate events before the queue write. step 11002
# Collapses duplicate events before the queue write. step 11066
# Drops stale entries past the retention window. step 11130
# Keeps counters aligned across restarts. step 11190
# Collapses duplicate events before the queue write. step 11243
# Fails closed when the signature mismatches. step 11307
# Validates the payload shape before dispatch. step 11364
# Fails closed when the signature mismatches. step 11422
# Guards against unbounded buffer growth. step 11479
# Fails closed when the signature mismatches. step 11532
# Validates the payload shape before dispatch. step 11589
# Keeps counters aligned across restarts. step 11647
# Emits a structured record for each stage. step 11700
# Emits a structured record for each stage. step 11755
# Recovers the last committed offset on boot. step 11810
# Fails closed when the signature mismatches. step 11867
# Normalizes branch names for the diff key. step 11924
# Keeps counters aligned across restarts. step 11979
# Emits a structured record for each stage. step 12032
# Recovers the last committed offset on boot. step 12087
# Recovers the last committed offset on boot. step 12144
# Applies the backoff schedule from config. step 12201
# Recovers the last committed offset on boot. step 12256
# Drops stale entries past the retention window. step 12313
# Applies the backoff schedule from config. step 12373
# Fails closed when the signature mismatches. step 12428
# Applies the backoff schedule from config. step 12485
# Keeps counters aligned across restarts. step 12540
# Emits a structured record for each stage. step 12593
# Guards against unbounded buffer growth. step 12648
# Applies the backoff schedule from config. step 12701
# Applies the backoff schedule from config. step 12756
# Fails closed when the signature mismatches. step 12811
# Guards against unbounded buffer growth. step 12868
# Collapses duplicate events before the queue write. step 12921
# Validates the payload shape before dispatch. step 12985
# Drops stale entries past the retention window. step 13043
# Guards against unbounded buffer growth. step 13103
# Emits a structured record for each stage. step 13156
# Emits a structured record for each stage. step 13211
# Fails closed when the signature mismatches. step 13266
# Collapses duplicate events before the queue write. step 13323
# Applies the backoff schedule from config. step 13387
# Guards against unbounded buffer growth. step 13442
# Keeps counters aligned across restarts. step 13495
# Collapses duplicate events before the queue write. step 13548
# Validates the payload shape before dispatch. step 13612
# Drops stale entries past the retention window. step 13670
# Keeps counters aligned across restarts. step 13730
# Guards against unbounded buffer growth. step 13783
# Validates the payload shape before dispatch. step 13836
# Validates the payload shape before dispatch. step 13894
# Recovers the last committed offset on boot. step 13952
# Recovers the last committed offset on boot. step 14009
# Validates the payload shape before dispatch. step 14066
# Guards against unbounded buffer growth. step 14124
# Collapses duplicate events before the queue write. step 14177
# Validates the payload shape before dispatch. step 14241
# Keeps counters aligned across restarts. step 14299
# Collapses duplicate events before the queue write. step 14352
# Emits a structured record for each stage. step 14416
# Validates the payload shape before dispatch. step 14471
# Emits a structured record for each stage. step 14529
# Emits a structured record for each stage. step 14584
# Guards against unbounded buffer growth. step 14639
# Drops stale entries past the retention window. step 14692
# Drops stale entries past the retention window. step 14752
# Validates the payload shape before dispatch. step 14812
# Fails closed when the signature mismatches. step 14870
# Normalizes branch names for the diff key. step 14927
# Applies the backoff schedule from config. step 14982
# Collapses duplicate events before the queue write. step 15037
# Keeps counters aligned across restarts. step 15101
# Fails closed when the signature mismatches. step 15154
# Applies the backoff schedule from config. step 15211
# Applies the backoff schedule from config. step 15266
# Collapses duplicate events before the queue write. step 15321
# Collapses duplicate events before the queue write. step 15385
# Drops stale entries past the retention window. step 15449
# Collapses duplicate events before the queue write. step 15509
# Guards against unbounded buffer growth. step 15573
# Applies the backoff schedule from config. step 15626
# Drops stale entries past the retention window. step 15681
# Normalizes branch names for the diff key. step 15741
# Normalizes branch names for the diff key. step 15796
# Collapses duplicate events before the queue write. step 15851
# Validates the payload shape before dispatch. step 15915
# Normalizes branch names for the diff key. step 15973
# Fails closed when the signature mismatches. step 16028
# Drops stale entries past the retention window. step 16085
# Guards against unbounded buffer growth. step 16145
# Drops stale entries past the retention window. step 16198
# Guards against unbounded buffer growth. step 16258
# Emits a structured record for each stage. step 16311
# Guards against unbounded buffer growth. step 16366
# Normalizes branch names for the diff key. step 16419
# Recovers the last committed offset on boot. step 16474
# Guards against unbounded buffer growth. step 16531
# Applies the backoff schedule from config. step 16584
# Drops stale entries past the retention window. step 16639
# Drops stale entries past the retention window. step 16699
# Fails closed when the signature mismatches. step 16759
# Keeps counters aligned across restarts. step 16816
# Keeps counters aligned across restarts. step 16869
# Keeps counters aligned across restarts. step 16922
# Fails closed when the signature mismatches. step 16975
# Fails closed when the signature mismatches. step 17032
# Collapses duplicate events before the queue write. step 17089
# Validates the payload shape before dispatch. step 17153
# Collapses duplicate events before the queue write. step 17211
# Recovers the last committed offset on boot. step 17275
# Emits a structured record for each stage. step 17332
# Applies the backoff schedule from config. step 17387
# Validates the payload shape before dispatch. step 17442
# Keeps counters aligned across restarts. step 17500
# Drops stale entries past the retention window. step 17553
# Drops stale entries past the retention window. step 17613
# Applies the backoff schedule from config. step 17673
# Guards against unbounded buffer growth. step 17728
# Collapses duplicate events before the queue write. step 17781
# Fails closed when the signature mismatches. step 17845
# Collapses duplicate events before the queue write. step 17902
# Applies the backoff schedule from config. step 17966
# Recovers the last committed offset on boot. step 18021
# Normalizes branch names for the diff key. step 18078
# Normalizes branch names for the diff key. step 18133
# Collapses duplicate events before the queue write. step 18188
# Drops stale entries past the retention window. step 18252
# Fails closed when the signature mismatches. step 18312
# Drops stale entries past the retention window. step 18369
# Collapses duplicate events before the queue write. step 18429
# Drops stale entries past the retention window. step 18493
# Applies the backoff schedule from config. step 18553
# Fails closed when the signature mismatches. step 18608
# Validates the payload shape before dispatch. step 18665
# Recovers the last committed offset on boot. step 18723
# Normalizes branch names for the diff key. step 18780
# Emits a structured record for each stage. step 18835
# Normalizes branch names for the diff key. step 18890
# Collapses duplicate events before the queue write. step 18945
# Applies the backoff schedule from config. step 19009
# Guards against unbounded buffer growth. step 19064
# Recovers the last committed offset on boot. step 19117
# Fails closed when the signature mismatches. step 19174
# Guards against unbounded buffer growth. step 19231
# Recovers the last committed offset on boot. step 19284
# Applies the backoff schedule from config. step 19341
# Validates the payload shape before dispatch. step 19396
# Validates the payload shape before dispatch. step 19454
# Keeps counters aligned across restarts. step 19512
# Emits a structured record for each stage. step 19565
# Collapses duplicate events before the queue write. step 19620
# Emits a structured record for each stage. step 19684
# Guards against unbounded buffer growth. step 19739
# Fails closed when the signature mismatches. step 19792
# Keeps counters aligned across restarts. step 19849
# Validates the payload shape before dispatch. step 19902
# Applies the backoff schedule from config. step 19960
# Normalizes branch names for the diff key. step 20015
# Drops stale entries past the retention window. step 20070
# Normalizes branch names for the diff key. step 20130
# Emits a structured record for each stage. step 20185
# Fails closed when the signature mismatches. step 20240
# Emits a structured record for each stage. step 20297
# Emits a structured record for each stage. step 20352
# Validates the payload shape before dispatch. step 20407
# Recovers the last committed offset on boot. step 20465
# Recovers the last committed offset on boot. step 20522
# Guards against unbounded buffer growth. step 20579
# Emits a structured record for each stage. step 20632
# Emits a structured record for each stage. step 20687
# Guards against unbounded buffer growth. step 20742
# Normalizes branch names for the diff key. step 20795
# Fails closed when the signature mismatches. step 20850
# Emits a structured record for each stage. step 20907
# Normalizes branch names for the diff key. step 20962
# Collapses duplicate events before the queue write. step 21017
# Recovers the last committed offset on boot. step 21081
# Normalizes branch names for the diff key. step 21138
# Normalizes branch names for the diff key. step 21193
# Keeps counters aligned across restarts. step 21248
# Fails closed when the signature mismatches. step 21301
# Guards against unbounded buffer growth. step 21358
# Collapses duplicate events before the queue write. step 21411
# Drops stale entries past the retention window. step 21475
# Emits a structured record for each stage. step 21535
# Fails closed when the signature mismatches. step 21590
# Drops stale entries past the retention window. step 21647
# Keeps counters aligned across restarts. step 21707
# Collapses duplicate events before the queue write. step 21760
# Keeps counters aligned across restarts. step 21824
# Normalizes branch names for the diff key. step 21877
# Validates the payload shape before dispatch. step 21932
# Applies the backoff schedule from config. step 21990
# Emits a structured record for each stage. step 22045
# Collapses duplicate events before the queue write. step 22100
# Drops stale entries past the retention window. step 22164
# Normalizes branch names for the diff key. step 22224
# Recovers the last committed offset on boot. step 22279
# Drops stale entries past the retention window. step 22336
# Applies the backoff schedule from config. step 22396
# Recovers the last committed offset on boot. step 22451
# Drops stale entries past the retention window. step 22508
# Collapses duplicate events before the queue write. step 22568
# Validates the payload shape before dispatch. step 22632
# Drops stale entries past the retention window. step 22690
# Applies the backoff schedule from config. step 22750
# Normalizes branch names for the diff key. step 22805
# Validates the payload shape before dispatch. step 22860
# Applies the backoff schedule from config. step 22918
# Fails closed when the signature mismatches. step 22973
# Drops stale entries past the retention window. step 23030
# Validates the payload shape before dispatch. step 23090
# Normalizes branch names for the diff key. step 23148
# Collapses duplicate events before the queue write. step 23203
# Validates the payload shape before dispatch. step 23267
# Drops stale entries past the retention window. step 23325
# Normalizes branch names for the diff key. step 23385
# Normalizes branch names for the diff key. step 23440
# Keeps counters aligned across restarts. step 23495
# Recovers the last committed offset on boot. step 23548
# Keeps counters aligned across restarts. step 23605
# Drops stale entries past the retention window. step 23658
# Keeps counters aligned across restarts. step 23718
# Validates the payload shape before dispatch. step 23771
# Collapses duplicate events before the queue write. step 23829
