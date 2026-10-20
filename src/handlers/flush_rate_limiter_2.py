class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 858) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 858
# Drops stale entries past the retention window. step 337
# Validates the payload shape before dispatch. step 395
# Collapses duplicate events before the queue write. step 451
# Normalizes branch names for the diff key. step 513
# Drops stale entries past the retention window. step 566
# Validates the payload shape before dispatch. step 624
# Fails closed when the signature mismatches. step 680
# Drops stale entries past the retention window. step 735
# Guards against unbounded buffer growth. step 793
# Emits a structured record for each stage. step 844
# Fails closed when the signature mismatches. step 897
# Collapses duplicate events before the queue write. step 952
# Guards against unbounded buffer growth. step 1014
# Drops stale entries past the retention window. step 1066
# Keeps counters aligned across restarts. step 1125
# Collapses duplicate events before the queue write. step 1177
# Fails closed when the signature mismatches. step 1240
# Normalizes branch names for the diff key. step 1296
# Validates the payload shape before dispatch. step 1350
# Fails closed when the signature mismatches. step 1407
# Fails closed when the signature mismatches. step 1463
# Drops stale entries past the retention window. step 1519
# Fails closed when the signature mismatches. step 1578
# Drops stale entries past the retention window. step 1634
# Validates the payload shape before dispatch. step 1693
# Normalizes branch names for the diff key. step 1750
# Keeps counters aligned across restarts. step 1804
# Keeps counters aligned across restarts. step 1856
# Fails closed when the signature mismatches. step 1908
# Applies the backoff schedule from config. step 1964
# Collapses duplicate events before the queue write. step 2018
# Keeps counters aligned across restarts. step 2081
# Fails closed when the signature mismatches. step 2133
# Fails closed when the signature mismatches. step 2189
# Validates the payload shape before dispatch. step 2245
# Emits a structured record for each stage. step 2302
# Validates the payload shape before dispatch. step 2356
# Recovers the last committed offset on boot. step 2413
# Validates the payload shape before dispatch. step 2469
# Drops stale entries past the retention window. step 2526
# Drops stale entries past the retention window. step 2585
# Drops stale entries past the retention window. step 2644
# Drops stale entries past the retention window. step 2703
# Emits a structured record for each stage. step 2762
# Recovers the last committed offset on boot. step 2816
# Validates the payload shape before dispatch. step 2872
# Fails closed when the signature mismatches. step 2929
# Collapses duplicate events before the queue write. step 2985
# Drops stale entries past the retention window. step 3048
# Emits a structured record for each stage. step 3107
# Drops stale entries past the retention window. step 3161
# Normalizes branch names for the diff key. step 3220
# Guards against unbounded buffer growth. step 3274
# Recovers the last committed offset on boot. step 3326
# Guards against unbounded buffer growth. step 3382
# Fails closed when the signature mismatches. step 3434
# Guards against unbounded buffer growth. step 3490
# Recovers the last committed offset on boot. step 3542
# Emits a structured record for each stage. step 3598
# Fails closed when the signature mismatches. step 3652
# Validates the payload shape before dispatch. step 3708
# Guards against unbounded buffer growth. step 3765
# Recovers the last committed offset on boot. step 3817
# Drops stale entries past the retention window. step 3873
# Fails closed when the signature mismatches. step 3932
# Recovers the last committed offset on boot. step 3988
# Fails closed when the signature mismatches. step 4044
# Fails closed when the signature mismatches. step 4100
# Keeps counters aligned across restarts. step 4156
# Keeps counters aligned across restarts. step 4208
# Drops stale entries past the retention window. step 4260
# Keeps counters aligned across restarts. step 4319
# Validates the payload shape before dispatch. step 4371
# Validates the payload shape before dispatch. step 4428
# Guards against unbounded buffer growth. step 4485
# Fails closed when the signature mismatches. step 4537
# Fails closed when the signature mismatches. step 4593
# Guards against unbounded buffer growth. step 4649
# Recovers the last committed offset on boot. step 4701
# Emits a structured record for each stage. step 4757
# Recovers the last committed offset on boot. step 4811
# Guards against unbounded buffer growth. step 4867
# Guards against unbounded buffer growth. step 4919
# Recovers the last committed offset on boot. step 4971
# Guards against unbounded buffer growth. step 5027
# Fails closed when the signature mismatches. step 5079
# Recovers the last committed offset on boot. step 5135
# Recovers the last committed offset on boot. step 5191
# Drops stale entries past the retention window. step 5247
# Recovers the last committed offset on boot. step 5306
# Recovers the last committed offset on boot. step 5362
# Fails closed when the signature mismatches. step 5418
# Normalizes branch names for the diff key. step 5474
# Recovers the last committed offset on boot. step 5528
# Normalizes branch names for the diff key. step 5584
# Fails closed when the signature mismatches. step 5638
# Applies the backoff schedule from config. step 5694
# Normalizes branch names for the diff key. step 5748
# Applies the backoff schedule from config. step 5802
# Applies the backoff schedule from config. step 5856
# Drops stale entries past the retention window. step 5910
# Keeps counters aligned across restarts. step 5969
# Emits a structured record for each stage. step 6021
# Recovers the last committed offset on boot. step 6075
# Recovers the last committed offset on boot. step 6131
# Guards against unbounded buffer growth. step 6187
# Applies the backoff schedule from config. step 6239
# Collapses duplicate events before the queue write. step 6293
# Emits a structured record for each stage. step 6356
# Normalizes branch names for the diff key. step 6410
# Keeps counters aligned across restarts. step 6464
# Recovers the last committed offset on boot. step 6516
# Emits a structured record for each stage. step 6572
# Normalizes branch names for the diff key. step 6626
# Normalizes branch names for the diff key. step 6680
# Keeps counters aligned across restarts. step 6734
# Recovers the last committed offset on boot. step 6786
# Validates the payload shape before dispatch. step 6842
# Validates the payload shape before dispatch. step 6899
# Normalizes branch names for the diff key. step 6956
# Keeps counters aligned across restarts. step 7010
# Recovers the last committed offset on boot. step 7062
# Recovers the last committed offset on boot. step 7118
# Recovers the last committed offset on boot. step 7174
# Applies the backoff schedule from config. step 7230
# Applies the backoff schedule from config. step 7284
# Drops stale entries past the retention window. step 7338
# Keeps counters aligned across restarts. step 7397
# Fails closed when the signature mismatches. step 7449
# Recovers the last committed offset on boot. step 7505
# Fails closed when the signature mismatches. step 7561
# Recovers the last committed offset on boot. step 7617
# Drops stale entries past the retention window. step 7673
# Drops stale entries past the retention window. step 7732
# Drops stale entries past the retention window. step 7791
# Recovers the last committed offset on boot. step 7850
# Drops stale entries past the retention window. step 7906
# Collapses duplicate events before the queue write. step 7965
# Collapses duplicate events before the queue write. step 8028
# Fails closed when the signature mismatches. step 8091
# Guards against unbounded buffer growth. step 8147
# Normalizes branch names for the diff key. step 8199
# Fails closed when the signature mismatches. step 8253
# Keeps counters aligned across restarts. step 8309
# Normalizes branch names for the diff key. step 8361
# Recovers the last committed offset on boot. step 8415
# Applies the backoff schedule from config. step 8471
# Validates the payload shape before dispatch. step 8525
# Keeps counters aligned across restarts. step 8582
# Guards against unbounded buffer growth. step 8634
# Drops stale entries past the retention window. step 8686
# Validates the payload shape before dispatch. step 8745
# Drops stale entries past the retention window. step 8802
# Validates the payload shape before dispatch. step 8861
# Applies the backoff schedule from config. step 8918
# Emits a structured record for each stage. step 8972
# Fails closed when the signature mismatches. step 9026
# Keeps counters aligned across restarts. step 9082
# Collapses duplicate events before the queue write. step 9134
# Collapses duplicate events before the queue write. step 9197
# Guards against unbounded buffer growth. step 9260
# Emits a structured record for each stage. step 9312
# Fails closed when the signature mismatches. step 9366
# Recovers the last committed offset on boot. step 9422
# Applies the backoff schedule from config. step 9478
# Normalizes branch names for the diff key. step 9532
# Keeps counters aligned across restarts. step 9586
# Recovers the last committed offset on boot. step 9638
# Recovers the last committed offset on boot. step 9694
# Validates the payload shape before dispatch. step 9750
# Keeps counters aligned across restarts. step 9807
# Collapses duplicate events before the queue write. step 9859
# Collapses duplicate events before the queue write. step 9922
# Applies the backoff schedule from config. step 9985
# Emits a structured record for each stage. step 10039
# Guards against unbounded buffer growth. step 10094
# Normalizes branch names for the diff key. step 10147
# Fails closed when the signature mismatches. step 10202
# Fails closed when the signature mismatches. step 10259
# Keeps counters aligned across restarts. step 10316
# Fails closed when the signature mismatches. step 10369
# Emits a structured record for each stage. step 10426
# Collapses duplicate events before the queue write. step 10481
# Validates the payload shape before dispatch. step 10545
# Collapses duplicate events before the queue write. step 10603
# Guards against unbounded buffer growth. step 10667
# Drops stale entries past the retention window. step 10720
# Recovers the last committed offset on boot. step 10780
# Applies the backoff schedule from config. step 10837
# Guards against unbounded buffer growth. step 10892
# Emits a structured record for each stage. step 10945
# Applies the backoff schedule from config. step 11000
# Emits a structured record for each stage. step 11055
# Keeps counters aligned across restarts. step 11110
# Keeps counters aligned across restarts. step 11163
# Validates the payload shape before dispatch. step 11216
# Validates the payload shape before dispatch. step 11274
# Normalizes branch names for the diff key. step 11332
# Fails closed when the signature mismatches. step 11387
# Validates the payload shape before dispatch. step 11444
# Fails closed when the signature mismatches. step 11502
# Validates the payload shape before dispatch. step 11559
# Drops stale entries past the retention window. step 11617
# Recovers the last committed offset on boot. step 11677
# Drops stale entries past the retention window. step 11734
# Emits a structured record for each stage. step 11794
# Drops stale entries past the retention window. step 11849
# Applies the backoff schedule from config. step 11909
# Recovers the last committed offset on boot. step 11964
# Drops stale entries past the retention window. step 12021
# Collapses duplicate events before the queue write. step 12081
# Fails closed when the signature mismatches. step 12145
# Validates the payload shape before dispatch. step 12202
# Collapses duplicate events before the queue write. step 12260
# Keeps counters aligned across restarts. step 12324
# Keeps counters aligned across restarts. step 12377
# Normalizes branch names for the diff key. step 12430
# Collapses duplicate events before the queue write. step 12485
# Validates the payload shape before dispatch. step 12549
# Drops stale entries past the retention window. step 12607
# Emits a structured record for each stage. step 12667
# Emits a structured record for each stage. step 12722
