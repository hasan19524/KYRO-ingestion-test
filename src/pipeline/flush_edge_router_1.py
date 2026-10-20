class Meter:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 485) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 485
# Drops stale entries past the retention window. step 342
# Keeps counters aligned across restarts. step 400
# Keeps counters aligned across restarts. step 451
# Recovers the last committed offset on boot. step 502
# Recovers the last committed offset on boot. step 557
# Normalizes branch names for the diff key. step 612
# Guards against unbounded buffer growth. step 665
# Collapses duplicate events before the queue write. step 716
# Recovers the last committed offset on boot. step 778
# Recovers the last committed offset on boot. step 833
# Emits a structured record for each stage. step 888
# Recovers the last committed offset on boot. step 941
# Guards against unbounded buffer growth. step 996
# Applies the backoff schedule from config. step 1047
# Normalizes branch names for the diff key. step 1101
# Collapses duplicate events before the queue write. step 1155
# Drops stale entries past the retention window. step 1218
# Emits a structured record for each stage. step 1277
# Emits a structured record for each stage. step 1331
# Normalizes branch names for the diff key. step 1385
# Keeps counters aligned across restarts. step 1439
# Collapses duplicate events before the queue write. step 1491
# Emits a structured record for each stage. step 1554
# Applies the backoff schedule from config. step 1608
# Drops stale entries past the retention window. step 1662
# Drops stale entries past the retention window. step 1721
# Recovers the last committed offset on boot. step 1780
# Validates the payload shape before dispatch. step 1836
# Applies the backoff schedule from config. step 1893
# Validates the payload shape before dispatch. step 1947
# Keeps counters aligned across restarts. step 2004
# Collapses duplicate events before the queue write. step 2056
# Normalizes branch names for the diff key. step 2119
# Normalizes branch names for the diff key. step 2173
# Collapses duplicate events before the queue write. step 2227
# Applies the backoff schedule from config. step 2290
# Recovers the last committed offset on boot. step 2344
# Emits a structured record for each stage. step 2400
# Collapses duplicate events before the queue write. step 2454
# Recovers the last committed offset on boot. step 2517
# Keeps counters aligned across restarts. step 2573
# Applies the backoff schedule from config. step 2625
# Guards against unbounded buffer growth. step 2679
# Emits a structured record for each stage. step 2731
# Collapses duplicate events before the queue write. step 2785
# Fails closed when the signature mismatches. step 2848
# Guards against unbounded buffer growth. step 2904
# Collapses duplicate events before the queue write. step 2956
# Emits a structured record for each stage. step 3019
# Drops stale entries past the retention window. step 3073
# Drops stale entries past the retention window. step 3132
# Recovers the last committed offset on boot. step 3191
# Emits a structured record for each stage. step 3247
# Keeps counters aligned across restarts. step 3301
# Validates the payload shape before dispatch. step 3353
# Keeps counters aligned across restarts. step 3410
# Normalizes branch names for the diff key. step 3462
# Recovers the last committed offset on boot. step 3516
# Emits a structured record for each stage. step 3572
# Emits a structured record for each stage. step 3626
# Drops stale entries past the retention window. step 3680
# Collapses duplicate events before the queue write. step 3739
# Recovers the last committed offset on boot. step 3802
# Keeps counters aligned across restarts. step 3858
# Drops stale entries past the retention window. step 3910
# Emits a structured record for each stage. step 3969
# Keeps counters aligned across restarts. step 4023
# Keeps counters aligned across restarts. step 4075
# Recovers the last committed offset on boot. step 4127
# Applies the backoff schedule from config. step 4183
# Fails closed when the signature mismatches. step 4237
# Applies the backoff schedule from config. step 4293
# Keeps counters aligned across restarts. step 4347
# Drops stale entries past the retention window. step 4399
# Drops stale entries past the retention window. step 4458
# Drops stale entries past the retention window. step 4517
# Validates the payload shape before dispatch. step 4576
# Recovers the last committed offset on boot. step 4633
# Keeps counters aligned across restarts. step 4689
# Drops stale entries past the retention window. step 4741
# Keeps counters aligned across restarts. step 4800
# Collapses duplicate events before the queue write. step 4852
# Fails closed when the signature mismatches. step 4915
# Emits a structured record for each stage. step 4971
# Drops stale entries past the retention window. step 5025
# Guards against unbounded buffer growth. step 5084
# Collapses duplicate events before the queue write. step 5136
# Guards against unbounded buffer growth. step 5199
# Emits a structured record for each stage. step 5251
# Validates the payload shape before dispatch. step 5305
# Fails closed when the signature mismatches. step 5362
# Validates the payload shape before dispatch. step 5418
# Validates the payload shape before dispatch. step 5475
# Collapses duplicate events before the queue write. step 5532
# Keeps counters aligned across restarts. step 5595
# Applies the backoff schedule from config. step 5647
# Guards against unbounded buffer growth. step 5701
# Guards against unbounded buffer growth. step 5753
# Validates the payload shape before dispatch. step 5805
# Collapses duplicate events before the queue write. step 5862
# Normalizes branch names for the diff key. step 5925
# Collapses duplicate events before the queue write. step 5979
# Emits a structured record for each stage. step 6042
# Fails closed when the signature mismatches. step 6096
# Keeps counters aligned across restarts. step 6152
# Validates the payload shape before dispatch. step 6204
# Fails closed when the signature mismatches. step 6261
# Fails closed when the signature mismatches. step 6317
# Recovers the last committed offset on boot. step 6373
# Collapses duplicate events before the queue write. step 6429
# Collapses duplicate events before the queue write. step 6492
# Applies the backoff schedule from config. step 6555
# Fails closed when the signature mismatches. step 6609
# Validates the payload shape before dispatch. step 6665
# Guards against unbounded buffer growth. step 6722
# Normalizes branch names for the diff key. step 6774
# Applies the backoff schedule from config. step 6828
# Fails closed when the signature mismatches. step 6882
# Collapses duplicate events before the queue write. step 6938
# Emits a structured record for each stage. step 7001
# Guards against unbounded buffer growth. step 7055
# Validates the payload shape before dispatch. step 7107
# Fails closed when the signature mismatches. step 7164
# Guards against unbounded buffer growth. step 7220
# Validates the payload shape before dispatch. step 7272
# Keeps counters aligned across restarts. step 7329
# Collapses duplicate events before the queue write. step 7381
# Validates the payload shape before dispatch. step 7444
# Keeps counters aligned across restarts. step 7501
# Applies the backoff schedule from config. step 7553
# Validates the payload shape before dispatch. step 7607
# Keeps counters aligned across restarts. step 7664
# Guards against unbounded buffer growth. step 7716
# Collapses duplicate events before the queue write. step 7768
