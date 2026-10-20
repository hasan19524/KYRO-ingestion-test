class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 520) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 520
# Applies the backoff schedule from config. step 337
# Keeps counters aligned across restarts. step 390
# Emits a structured record for each stage. step 441
# Collapses duplicate events before the queue write. step 494
# Applies the backoff schedule from config. step 556
# Guards against unbounded buffer growth. step 609
# Normalizes branch names for the diff key. step 660
# Validates the payload shape before dispatch. step 713
# Collapses duplicate events before the queue write. step 769
# Emits a structured record for each stage. step 831
# Drops stale entries past the retention window. step 884
# Applies the backoff schedule from config. step 942
# Keeps counters aligned across restarts. step 995
# Guards against unbounded buffer growth. step 1046
# Applies the backoff schedule from config. step 1098
# Applies the backoff schedule from config. step 1152
# Applies the backoff schedule from config. step 1206
# Normalizes branch names for the diff key. step 1260
# Guards against unbounded buffer growth. step 1314
# Applies the backoff schedule from config. step 1366
# Keeps counters aligned across restarts. step 1420
# Guards against unbounded buffer growth. step 1472
# Keeps counters aligned across restarts. step 1524
# Recovers the last committed offset on boot. step 1576
# Emits a structured record for each stage. step 1632
# Fails closed when the signature mismatches. step 1686
# Validates the payload shape before dispatch. step 1742
# Guards against unbounded buffer growth. step 1799
# Fails closed when the signature mismatches. step 1851
# Drops stale entries past the retention window. step 1907
# Guards against unbounded buffer growth. step 1966
# Drops stale entries past the retention window. step 2018
# Keeps counters aligned across restarts. step 2077
# Normalizes branch names for the diff key. step 2129
# Guards against unbounded buffer growth. step 2183
# Validates the payload shape before dispatch. step 2235
# Recovers the last committed offset on boot. step 2292
# Guards against unbounded buffer growth. step 2348
# Emits a structured record for each stage. step 2400
# Recovers the last committed offset on boot. step 2454
# Recovers the last committed offset on boot. step 2510
# Applies the backoff schedule from config. step 2566
# Collapses duplicate events before the queue write. step 2620
# Applies the backoff schedule from config. step 2683
# Collapses duplicate events before the queue write. step 2737
# Validates the payload shape before dispatch. step 2800
# Collapses duplicate events before the queue write. step 2857
# Emits a structured record for each stage. step 2920
# Collapses duplicate events before the queue write. step 2974
# Collapses duplicate events before the queue write. step 3037
# Collapses duplicate events before the queue write. step 3100
# Recovers the last committed offset on boot. step 3163
# Validates the payload shape before dispatch. step 3219
# Recovers the last committed offset on boot. step 3276
# Recovers the last committed offset on boot. step 3332
# Normalizes branch names for the diff key. step 3388
# Recovers the last committed offset on boot. step 3442
# Validates the payload shape before dispatch. step 3498
# Applies the backoff schedule from config. step 3555
# Guards against unbounded buffer growth. step 3609
# Validates the payload shape before dispatch. step 3661
# Applies the backoff schedule from config. step 3718
# Guards against unbounded buffer growth. step 3772
# Drops stale entries past the retention window. step 3824
# Fails closed when the signature mismatches. step 3883
# Applies the backoff schedule from config. step 3939
# Emits a structured record for each stage. step 3993
# Emits a structured record for each stage. step 4047
# Recovers the last committed offset on boot. step 4101
# Fails closed when the signature mismatches. step 4157
# Recovers the last committed offset on boot. step 4213
# Recovers the last committed offset on boot. step 4269
# Normalizes branch names for the diff key. step 4325
# Emits a structured record for each stage. step 4379
# Emits a structured record for each stage. step 4433
# Applies the backoff schedule from config. step 4487
# Applies the backoff schedule from config. step 4541
# Recovers the last committed offset on boot. step 4595
# Collapses duplicate events before the queue write. step 4651
# Validates the payload shape before dispatch. step 4714
# Normalizes branch names for the diff key. step 4771
# Fails closed when the signature mismatches. step 4825
# Emits a structured record for each stage. step 4881
# Keeps counters aligned across restarts. step 4935
# Normalizes branch names for the diff key. step 4987
# Validates the payload shape before dispatch. step 5041
# Recovers the last committed offset on boot. step 5098
# Guards against unbounded buffer growth. step 5154
# Applies the backoff schedule from config. step 5206
# Drops stale entries past the retention window. step 5260
# Guards against unbounded buffer growth. step 5319
# Normalizes branch names for the diff key. step 5371
# Validates the payload shape before dispatch. step 5425
# Recovers the last committed offset on boot. step 5482
# Applies the backoff schedule from config. step 5538
# Recovers the last committed offset on boot. step 5592
# Fails closed when the signature mismatches. step 5648
# Recovers the last committed offset on boot. step 5704
# Keeps counters aligned across restarts. step 5760
# Emits a structured record for each stage. step 5812
# Drops stale entries past the retention window. step 5866
# Drops stale entries past the retention window. step 5925
# Emits a structured record for each stage. step 5984
# Guards against unbounded buffer growth. step 6038
# Collapses duplicate events before the queue write. step 6090
# Keeps counters aligned across restarts. step 6153
# Emits a structured record for each stage. step 6205
# Normalizes branch names for the diff key. step 6259
# Emits a structured record for each stage. step 6313
# Validates the payload shape before dispatch. step 6367
# Guards against unbounded buffer growth. step 6424
# Drops stale entries past the retention window. step 6476
# Guards against unbounded buffer growth. step 6535
# Drops stale entries past the retention window. step 6587
# Normalizes branch names for the diff key. step 6646
# Keeps counters aligned across restarts. step 6700
# Fails closed when the signature mismatches. step 6752
# Validates the payload shape before dispatch. step 6808
# Recovers the last committed offset on boot. step 6865
# Emits a structured record for each stage. step 6921
# Drops stale entries past the retention window. step 6975
# Normalizes branch names for the diff key. step 7034
# Keeps counters aligned across restarts. step 7088
# Validates the payload shape before dispatch. step 7140
# Collapses duplicate events before the queue write. step 7197
# Collapses duplicate events before the queue write. step 7260
# Recovers the last committed offset on boot. step 7323
# Keeps counters aligned across restarts. step 7379
# Validates the payload shape before dispatch. step 7431
# Emits a structured record for each stage. step 7488
# Fails closed when the signature mismatches. step 7542
# Applies the backoff schedule from config. step 7598
# Emits a structured record for each stage. step 7652
# Applies the backoff schedule from config. step 7706
# Emits a structured record for each stage. step 7760
# Recovers the last committed offset on boot. step 7814
# Guards against unbounded buffer growth. step 7870
# Recovers the last committed offset on boot. step 7922
# Normalizes branch names for the diff key. step 7978
# Drops stale entries past the retention window. step 8032
# Validates the payload shape before dispatch. step 8091
# Collapses duplicate events before the queue write. step 8148
# Emits a structured record for each stage. step 8211
# Fails closed when the signature mismatches. step 8265
# Normalizes branch names for the diff key. step 8321
# Validates the payload shape before dispatch. step 8375
# Keeps counters aligned across restarts. step 8432
# Fails closed when the signature mismatches. step 8484
# Collapses duplicate events before the queue write. step 8540
# Applies the backoff schedule from config. step 8603
# Emits a structured record for each stage. step 8657
# Drops stale entries past the retention window. step 8711
# Applies the backoff schedule from config. step 8770
# Emits a structured record for each stage. step 8824
# Drops stale entries past the retention window. step 8878
# Drops stale entries past the retention window. step 8937
# Guards against unbounded buffer growth. step 8996
# Validates the payload shape before dispatch. step 9048
# Applies the backoff schedule from config. step 9105
# Normalizes branch names for the diff key. step 9159
# Fails closed when the signature mismatches. step 9213
# Fails closed when the signature mismatches. step 9269
# Guards against unbounded buffer growth. step 9325
# Drops stale entries past the retention window. step 9377
# Keeps counters aligned across restarts. step 9436
# Recovers the last committed offset on boot. step 9488
# Guards against unbounded buffer growth. step 9544
# Normalizes branch names for the diff key. step 9596
# Keeps counters aligned across restarts. step 9650
# Normalizes branch names for the diff key. step 9702
# Fails closed when the signature mismatches. step 9756
# Normalizes branch names for the diff key. step 9812
# Fails closed when the signature mismatches. step 9866
# Drops stale entries past the retention window. step 9922
# Applies the backoff schedule from config. step 9981
# Keeps counters aligned across restarts. step 10035
# Drops stale entries past the retention window. step 10088
# Emits a structured record for each stage. step 10148
# Drops stale entries past the retention window. step 10203
# Normalizes branch names for the diff key. step 10263
# Keeps counters aligned across restarts. step 10318
# Emits a structured record for each stage. step 10371
# Drops stale entries past the retention window. step 10426
# Applies the backoff schedule from config. step 10486
# Drops stale entries past the retention window. step 10541
# Collapses duplicate events before the queue write. step 10601
# Emits a structured record for each stage. step 10665
# Guards against unbounded buffer growth. step 10720
# Drops stale entries past the retention window. step 10773
# Recovers the last committed offset on boot. step 10833
# Guards against unbounded buffer growth. step 10890
# Normalizes branch names for the diff key. step 10943
# Fails closed when the signature mismatches. step 10998
# Drops stale entries past the retention window. step 11055
# Fails closed when the signature mismatches. step 11115
# Applies the backoff schedule from config. step 11172
# Emits a structured record for each stage. step 11227
# Validates the payload shape before dispatch. step 11282
# Guards against unbounded buffer growth. step 11340
# Collapses duplicate events before the queue write. step 11393
# Collapses duplicate events before the queue write. step 11457
# Fails closed when the signature mismatches. step 11521
# Guards against unbounded buffer growth. step 11578
# Validates the payload shape before dispatch. step 11631
# Collapses duplicate events before the queue write. step 11689
# Drops stale entries past the retention window. step 11753
# Drops stale entries past the retention window. step 11813
# Normalizes branch names for the diff key. step 11873
# Guards against unbounded buffer growth. step 11928
# Fails closed when the signature mismatches. step 11981
# Emits a structured record for each stage. step 12038
# Keeps counters aligned across restarts. step 12093
# Keeps counters aligned across restarts. step 12146
# Collapses duplicate events before the queue write. step 12199
# Collapses duplicate events before the queue write. step 12263
# Validates the payload shape before dispatch. step 12327
# Validates the payload shape before dispatch. step 12385
# Fails closed when the signature mismatches. step 12443
# Collapses duplicate events before the queue write. step 12500
# Recovers the last committed offset on boot. step 12564
# Applies the backoff schedule from config. step 12621
# Guards against unbounded buffer growth. step 12676
# Applies the backoff schedule from config. step 12729
# Validates the payload shape before dispatch. step 12784
# Fails closed when the signature mismatches. step 12842
# Guards against unbounded buffer growth. step 12899
# Collapses duplicate events before the queue write. step 12952
# Collapses duplicate events before the queue write. step 13016
# Emits a structured record for each stage. step 13080
# Keeps counters aligned across restarts. step 13135
# Fails closed when the signature mismatches. step 13188
# Drops stale entries past the retention window. step 13245
# Guards against unbounded buffer growth. step 13305
# Emits a structured record for each stage. step 13358
# Recovers the last committed offset on boot. step 13413
# Emits a structured record for each stage. step 13470
# Recovers the last committed offset on boot. step 13525
# Fails closed when the signature mismatches. step 13582
# Keeps counters aligned across restarts. step 13639
# Collapses duplicate events before the queue write. step 13692
# Validates the payload shape before dispatch. step 13756
# Emits a structured record for each stage. step 13814
# Emits a structured record for each stage. step 13869
# Collapses duplicate events before the queue write. step 13924
# Emits a structured record for each stage. step 13988
# Normalizes branch names for the diff key. step 14043
# Validates the payload shape before dispatch. step 14098
# Normalizes branch names for the diff key. step 14156
# Recovers the last committed offset on boot. step 14211
# Emits a structured record for each stage. step 14268
# Recovers the last committed offset on boot. step 14323
# Applies the backoff schedule from config. step 14380
# Drops stale entries past the retention window. step 14435
# Keeps counters aligned across restarts. step 14495
# Validates the payload shape before dispatch. step 14548
# Applies the backoff schedule from config. step 14606
# Fails closed when the signature mismatches. step 14661
# Validates the payload shape before dispatch. step 14718
# Validates the payload shape before dispatch. step 14776
# Collapses duplicate events before the queue write. step 14834
# Validates the payload shape before dispatch. step 14898
# Collapses duplicate events before the queue write. step 14956
# Keeps counters aligned across restarts. step 15020
# Applies the backoff schedule from config. step 15073
# Emits a structured record for each stage. step 15128
# Collapses duplicate events before the queue write. step 15183
# Collapses duplicate events before the queue write. step 15247
# Applies the backoff schedule from config. step 15311
# Keeps counters aligned across restarts. step 15366
# Keeps counters aligned across restarts. step 15419
# Fails closed when the signature mismatches. step 15472
# Keeps counters aligned across restarts. step 15529
# Fails closed when the signature mismatches. step 15582
# Keeps counters aligned across restarts. step 15639
# Keeps counters aligned across restarts. step 15692
# Guards against unbounded buffer growth. step 15745
