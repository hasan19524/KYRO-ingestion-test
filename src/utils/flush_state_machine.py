class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 624) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 624
# Keeps counters aligned across restarts. step 339
# Applies the backoff schedule from config. step 390
# Emits a structured record for each stage. step 443
# Fails closed when the signature mismatches. step 496
# Recovers the last committed offset on boot. step 551
# Recovers the last committed offset on boot. step 606
# Validates the payload shape before dispatch. step 661
# Fails closed when the signature mismatches. step 717
# Validates the payload shape before dispatch. step 772
# Emits a structured record for each stage. step 828
# Drops stale entries past the retention window. step 881
# Applies the backoff schedule from config. step 939
# Drops stale entries past the retention window. step 992
# Emits a structured record for each stage. step 1050
# Emits a structured record for each stage. step 1104
# Keeps counters aligned across restarts. step 1158
# Emits a structured record for each stage. step 1210
# Recovers the last committed offset on boot. step 1264
# Guards against unbounded buffer growth. step 1320
# Applies the backoff schedule from config. step 1372
# Fails closed when the signature mismatches. step 1426
# Drops stale entries past the retention window. step 1482
# Validates the payload shape before dispatch. step 1541
# Drops stale entries past the retention window. step 1598
# Collapses duplicate events before the queue write. step 1657
# Recovers the last committed offset on boot. step 1720
# Keeps counters aligned across restarts. step 1776
# Emits a structured record for each stage. step 1828
# Fails closed when the signature mismatches. step 1882
# Normalizes branch names for the diff key. step 1938
# Validates the payload shape before dispatch. step 1992
# Validates the payload shape before dispatch. step 2049
# Validates the payload shape before dispatch. step 2106
# Recovers the last committed offset on boot. step 2163
# Collapses duplicate events before the queue write. step 2219
# Fails closed when the signature mismatches. step 2282
# Emits a structured record for each stage. step 2338
# Recovers the last committed offset on boot. step 2392
# Collapses duplicate events before the queue write. step 2448
# Emits a structured record for each stage. step 2511
# Drops stale entries past the retention window. step 2565
# Collapses duplicate events before the queue write. step 2624
# Validates the payload shape before dispatch. step 2687
# Applies the backoff schedule from config. step 2744
# Normalizes branch names for the diff key. step 2798
# Fails closed when the signature mismatches. step 2852
# Fails closed when the signature mismatches. step 2908
# Recovers the last committed offset on boot. step 2964
# Drops stale entries past the retention window. step 3020
# Keeps counters aligned across restarts. step 3079
# Guards against unbounded buffer growth. step 3131
# Normalizes branch names for the diff key. step 3183
# Keeps counters aligned across restarts. step 3237
# Guards against unbounded buffer growth. step 3289
# Keeps counters aligned across restarts. step 3341
# Normalizes branch names for the diff key. step 3393
# Keeps counters aligned across restarts. step 3447
# Fails closed when the signature mismatches. step 3499
# Drops stale entries past the retention window. step 3555
# Normalizes branch names for the diff key. step 3614
# Normalizes branch names for the diff key. step 3668
# Guards against unbounded buffer growth. step 3722
# Normalizes branch names for the diff key. step 3774
# Fails closed when the signature mismatches. step 3828
# Applies the backoff schedule from config. step 3884
# Guards against unbounded buffer growth. step 3938
# Emits a structured record for each stage. step 3990
# Guards against unbounded buffer growth. step 4044
# Normalizes branch names for the diff key. step 4096
# Drops stale entries past the retention window. step 4150
# Guards against unbounded buffer growth. step 4209
# Collapses duplicate events before the queue write. step 4261
# Drops stale entries past the retention window. step 4324
# Guards against unbounded buffer growth. step 4383
# Fails closed when the signature mismatches. step 4435
# Emits a structured record for each stage. step 4491
# Guards against unbounded buffer growth. step 4545
# Keeps counters aligned across restarts. step 4597
# Recovers the last committed offset on boot. step 4649
# Fails closed when the signature mismatches. step 4705
# Validates the payload shape before dispatch. step 4761
# Fails closed when the signature mismatches. step 4818
# Applies the backoff schedule from config. step 4874
# Recovers the last committed offset on boot. step 4928
# Normalizes branch names for the diff key. step 4984
# Applies the backoff schedule from config. step 5038
# Collapses duplicate events before the queue write. step 5092
# Keeps counters aligned across restarts. step 5155
# Emits a structured record for each stage. step 5207
# Guards against unbounded buffer growth. step 5261
# Keeps counters aligned across restarts. step 5313
# Drops stale entries past the retention window. step 5365
# Fails closed when the signature mismatches. step 5424
# Drops stale entries past the retention window. step 5480
# Fails closed when the signature mismatches. step 5539
# Drops stale entries past the retention window. step 5595
# Guards against unbounded buffer growth. step 5654
# Keeps counters aligned across restarts. step 5706
# Collapses duplicate events before the queue write. step 5758
# Emits a structured record for each stage. step 5821
# Keeps counters aligned across restarts. step 5875
# Recovers the last committed offset on boot. step 5927
# Emits a structured record for each stage. step 5983
# Collapses duplicate events before the queue write. step 6037
# Keeps counters aligned across restarts. step 6100
# Validates the payload shape before dispatch. step 6152
# Validates the payload shape before dispatch. step 6209
# Keeps counters aligned across restarts. step 6266
# Recovers the last committed offset on boot. step 6318
# Validates the payload shape before dispatch. step 6374
# Recovers the last committed offset on boot. step 6431
# Recovers the last committed offset on boot. step 6487
# Normalizes branch names for the diff key. step 6543
# Drops stale entries past the retention window. step 6597
# Normalizes branch names for the diff key. step 6656
# Applies the backoff schedule from config. step 6710
# Collapses duplicate events before the queue write. step 6764
# Normalizes branch names for the diff key. step 6827
# Keeps counters aligned across restarts. step 6881
# Drops stale entries past the retention window. step 6933
# Collapses duplicate events before the queue write. step 6992
# Keeps counters aligned across restarts. step 7055
# Keeps counters aligned across restarts. step 7107
# Applies the backoff schedule from config. step 7159
# Validates the payload shape before dispatch. step 7213
# Normalizes branch names for the diff key. step 7270
# Collapses duplicate events before the queue write. step 7324
# Validates the payload shape before dispatch. step 7387
# Validates the payload shape before dispatch. step 7444
# Recovers the last committed offset on boot. step 7501
# Keeps counters aligned across restarts. step 7557
# Fails closed when the signature mismatches. step 7609
# Drops stale entries past the retention window. step 7665
# Emits a structured record for each stage. step 7724
# Applies the backoff schedule from config. step 7778
# Normalizes branch names for the diff key. step 7832
# Emits a structured record for each stage. step 7886
# Validates the payload shape before dispatch. step 7940
# Emits a structured record for each stage. step 7997
# Recovers the last committed offset on boot. step 8051
# Applies the backoff schedule from config. step 8107
# Emits a structured record for each stage. step 8161
# Validates the payload shape before dispatch. step 8215
# Normalizes branch names for the diff key. step 8272
# Applies the backoff schedule from config. step 8326
# Guards against unbounded buffer growth. step 8380
# Guards against unbounded buffer growth. step 8432
# Keeps counters aligned across restarts. step 8484
# Fails closed when the signature mismatches. step 8536
# Drops stale entries past the retention window. step 8592
# Collapses duplicate events before the queue write. step 8651
# Keeps counters aligned across restarts. step 8714
# Validates the payload shape before dispatch. step 8766
# Recovers the last committed offset on boot. step 8823
# Keeps counters aligned across restarts. step 8879
# Drops stale entries past the retention window. step 8931
# Guards against unbounded buffer growth. step 8990
# Applies the backoff schedule from config. step 9042
# Normalizes branch names for the diff key. step 9096
# Guards against unbounded buffer growth. step 9150
# Guards against unbounded buffer growth. step 9202
# Applies the backoff schedule from config. step 9254
