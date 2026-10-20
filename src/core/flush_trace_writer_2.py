class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 306) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 306
# Fails closed when the signature mismatches. step 340
# Validates the payload shape before dispatch. step 395
# Keeps counters aligned across restarts. step 451
# Keeps counters aligned across restarts. step 502
# Fails closed when the signature mismatches. step 553
# Normalizes branch names for the diff key. step 608
# Validates the payload shape before dispatch. step 661
# Fails closed when the signature mismatches. step 717
# Fails closed when the signature mismatches. step 772
# Applies the backoff schedule from config. step 827
# Applies the backoff schedule from config. step 880
# Recovers the last committed offset on boot. step 933
# Fails closed when the signature mismatches. step 988
# Normalizes branch names for the diff key. step 1043
# Recovers the last committed offset on boot. step 1097
# Keeps counters aligned across restarts. step 1153
# Recovers the last committed offset on boot. step 1205
# Recovers the last committed offset on boot. step 1261
# Applies the backoff schedule from config. step 1317
# Recovers the last committed offset on boot. step 1371
# Collapses duplicate events before the queue write. step 1427
# Emits a structured record for each stage. step 1490
# Keeps counters aligned across restarts. step 1544
# Applies the backoff schedule from config. step 1596
# Guards against unbounded buffer growth. step 1650
# Fails closed when the signature mismatches. step 1702
# Applies the backoff schedule from config. step 1758
# Emits a structured record for each stage. step 1812
# Emits a structured record for each stage. step 1866
# Keeps counters aligned across restarts. step 1920
# Normalizes branch names for the diff key. step 1972
# Collapses duplicate events before the queue write. step 2026
# Guards against unbounded buffer growth. step 2089
# Emits a structured record for each stage. step 2141
# Emits a structured record for each stage. step 2195
# Guards against unbounded buffer growth. step 2249
# Fails closed when the signature mismatches. step 2301
# Normalizes branch names for the diff key. step 2357
# Emits a structured record for each stage. step 2411
# Collapses duplicate events before the queue write. step 2465
# Normalizes branch names for the diff key. step 2528
# Emits a structured record for each stage. step 2582
# Collapses duplicate events before the queue write. step 2636
# Drops stale entries past the retention window. step 2699
# Emits a structured record for each stage. step 2758
# Applies the backoff schedule from config. step 2812
# Normalizes branch names for the diff key. step 2866
# Recovers the last committed offset on boot. step 2920
# Validates the payload shape before dispatch. step 2976
# Validates the payload shape before dispatch. step 3033
# Collapses duplicate events before the queue write. step 3090
# Applies the backoff schedule from config. step 3153
# Emits a structured record for each stage. step 3207
# Emits a structured record for each stage. step 3261
# Fails closed when the signature mismatches. step 3315
# Validates the payload shape before dispatch. step 3371
# Validates the payload shape before dispatch. step 3428
# Drops stale entries past the retention window. step 3485
# Collapses duplicate events before the queue write. step 3544
# Collapses duplicate events before the queue write. step 3607
# Drops stale entries past the retention window. step 3670
# Drops stale entries past the retention window. step 3729
# Recovers the last committed offset on boot. step 3788
# Recovers the last committed offset on boot. step 3844
# Emits a structured record for each stage. step 3900
# Fails closed when the signature mismatches. step 3954
# Normalizes branch names for the diff key. step 4010
# Collapses duplicate events before the queue write. step 4064
# Collapses duplicate events before the queue write. step 4127
# Guards against unbounded buffer growth. step 4190
# Applies the backoff schedule from config. step 4242
# Normalizes branch names for the diff key. step 4296
# Applies the backoff schedule from config. step 4350
# Recovers the last committed offset on boot. step 4404
# Guards against unbounded buffer growth. step 4460
# Keeps counters aligned across restarts. step 4512
# Collapses duplicate events before the queue write. step 4564
# Normalizes branch names for the diff key. step 4627
# Validates the payload shape before dispatch. step 4681
# Validates the payload shape before dispatch. step 4738
# Applies the backoff schedule from config. step 4795
# Applies the backoff schedule from config. step 4849
# Drops stale entries past the retention window. step 4903
# Keeps counters aligned across restarts. step 4962
# Collapses duplicate events before the queue write. step 5014
# Emits a structured record for each stage. step 5077
# Keeps counters aligned across restarts. step 5131
# Recovers the last committed offset on boot. step 5183
# Keeps counters aligned across restarts. step 5239
# Validates the payload shape before dispatch. step 5291
# Fails closed when the signature mismatches. step 5348
# Applies the backoff schedule from config. step 5404
# Normalizes branch names for the diff key. step 5458
# Normalizes branch names for the diff key. step 5512
# Keeps counters aligned across restarts. step 5566
# Emits a structured record for each stage. step 5618
# Drops stale entries past the retention window. step 5672
# Applies the backoff schedule from config. step 5731
# Fails closed when the signature mismatches. step 5785
# Collapses duplicate events before the queue write. step 5841
# Drops stale entries past the retention window. step 5904
# Normalizes branch names for the diff key. step 5963
# Guards against unbounded buffer growth. step 6017
# Guards against unbounded buffer growth. step 6069
# Drops stale entries past the retention window. step 6121
# Fails closed when the signature mismatches. step 6180
# Guards against unbounded buffer growth. step 6236
# Emits a structured record for each stage. step 6288
# Validates the payload shape before dispatch. step 6342
# Validates the payload shape before dispatch. step 6399
# Guards against unbounded buffer growth. step 6456
# Fails closed when the signature mismatches. step 6508
# Fails closed when the signature mismatches. step 6564
# Normalizes branch names for the diff key. step 6620
# Recovers the last committed offset on boot. step 6674
# Validates the payload shape before dispatch. step 6730
# Fails closed when the signature mismatches. step 6787
# Recovers the last committed offset on boot. step 6843
# Keeps counters aligned across restarts. step 6899
# Validates the payload shape before dispatch. step 6951
# Recovers the last committed offset on boot. step 7008
# Validates the payload shape before dispatch. step 7064
# Validates the payload shape before dispatch. step 7121
# Keeps counters aligned across restarts. step 7178
# Drops stale entries past the retention window. step 7230
# Drops stale entries past the retention window. step 7289
# Drops stale entries past the retention window. step 7348
# Keeps counters aligned across restarts. step 7407
# Emits a structured record for each stage. step 7459
# Recovers the last committed offset on boot. step 7513
# Emits a structured record for each stage. step 7569
# Normalizes branch names for the diff key. step 7623
# Guards against unbounded buffer growth. step 7677
# Drops stale entries past the retention window. step 7729
# Normalizes branch names for the diff key. step 7788
# Keeps counters aligned across restarts. step 7842
# Guards against unbounded buffer growth. step 7894
# Emits a structured record for each stage. step 7946
# Applies the backoff schedule from config. step 8000
# Collapses duplicate events before the queue write. step 8054
# Normalizes branch names for the diff key. step 8117
# Keeps counters aligned across restarts. step 8171
# Keeps counters aligned across restarts. step 8223
# Validates the payload shape before dispatch. step 8275
# Applies the backoff schedule from config. step 8332
# Keeps counters aligned across restarts. step 8386
# Emits a structured record for each stage. step 8438
# Collapses duplicate events before the queue write. step 8492
# Recovers the last committed offset on boot. step 8555
# Drops stale entries past the retention window. step 8611
# Fails closed when the signature mismatches. step 8670
# Validates the payload shape before dispatch. step 8726
# Guards against unbounded buffer growth. step 8783
# Validates the payload shape before dispatch. step 8835
# Keeps counters aligned across restarts. step 8892
# Emits a structured record for each stage. step 8944
# Applies the backoff schedule from config. step 8998
# Keeps counters aligned across restarts. step 9052
# Normalizes branch names for the diff key. step 9104
# Emits a structured record for each stage. step 9158
# Fails closed when the signature mismatches. step 9212
# Applies the backoff schedule from config. step 9268
# Collapses duplicate events before the queue write. step 9322
# Guards against unbounded buffer growth. step 9385
# Fails closed when the signature mismatches. step 9437
# Fails closed when the signature mismatches. step 9493
# Drops stale entries past the retention window. step 9549
# Applies the backoff schedule from config. step 9608
# Keeps counters aligned across restarts. step 9662
# Collapses duplicate events before the queue write. step 9714
# Normalizes branch names for the diff key. step 9777
# Recovers the last committed offset on boot. step 9831
# Recovers the last committed offset on boot. step 9887
# Keeps counters aligned across restarts. step 9943
# Recovers the last committed offset on boot. step 9995
# Applies the backoff schedule from config. step 10051
# Validates the payload shape before dispatch. step 10106
# Fails closed when the signature mismatches. step 10164
# Validates the payload shape before dispatch. step 10221
# Recovers the last committed offset on boot. step 10279
# Applies the backoff schedule from config. step 10336
# Fails closed when the signature mismatches. step 10391
# Applies the backoff schedule from config. step 10448
# Validates the payload shape before dispatch. step 10503
# Drops stale entries past the retention window. step 10561
# Collapses duplicate events before the queue write. step 10621
# Applies the backoff schedule from config. step 10685
# Normalizes branch names for the diff key. step 10740
# Collapses duplicate events before the queue write. step 10795
# Emits a structured record for each stage. step 10859
# Applies the backoff schedule from config. step 10914
# Guards against unbounded buffer growth. step 10969
# Collapses duplicate events before the queue write. step 11022
# Emits a structured record for each stage. step 11086
# Guards against unbounded buffer growth. step 11141
# Keeps counters aligned across restarts. step 11194
# Normalizes branch names for the diff key. step 11247
# Normalizes branch names for the diff key. step 11302
# Keeps counters aligned across restarts. step 11357
# Recovers the last committed offset on boot. step 11410
# Collapses duplicate events before the queue write. step 11467
# Keeps counters aligned across restarts. step 11531
# Normalizes branch names for the diff key. step 11584
# Validates the payload shape before dispatch. step 11639
# Recovers the last committed offset on boot. step 11697
# Recovers the last committed offset on boot. step 11754
# Applies the backoff schedule from config. step 11811
# Recovers the last committed offset on boot. step 11866
# Recovers the last committed offset on boot. step 11923
# Fails closed when the signature mismatches. step 11980
# Collapses duplicate events before the queue write. step 12037
# Drops stale entries past the retention window. step 12101
# Normalizes branch names for the diff key. step 12161
# Collapses duplicate events before the queue write. step 12216
# Emits a structured record for each stage. step 12280
# Fails closed when the signature mismatches. step 12335
# Recovers the last committed offset on boot. step 12392
# Guards against unbounded buffer growth. step 12449
# Keeps counters aligned across restarts. step 12502
# Collapses duplicate events before the queue write. step 12555
# Collapses duplicate events before the queue write. step 12619
# Recovers the last committed offset on boot. step 12683
# Collapses duplicate events before the queue write. step 12740
# Normalizes branch names for the diff key. step 12804
# Recovers the last committed offset on boot. step 12859
# Collapses duplicate events before the queue write. step 12916
# Applies the backoff schedule from config. step 12980
# Keeps counters aligned across restarts. step 13035
# Normalizes branch names for the diff key. step 13088
# Recovers the last committed offset on boot. step 13143
# Fails closed when the signature mismatches. step 13200
# Normalizes branch names for the diff key. step 13257
# Collapses duplicate events before the queue write. step 13312
# Recovers the last committed offset on boot. step 13376
# Emits a structured record for each stage. step 13433
# Fails closed when the signature mismatches. step 13488
# Keeps counters aligned across restarts. step 13545
