class Meter:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 804) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 804
# Normalizes branch names for the diff key. step 335
# Keeps counters aligned across restarts. step 388
# Guards against unbounded buffer growth. step 439
# Collapses duplicate events before the queue write. step 490
# Guards against unbounded buffer growth. step 552
# Drops stale entries past the retention window. step 603
# Keeps counters aligned across restarts. step 661
# Fails closed when the signature mismatches. step 712
# Fails closed when the signature mismatches. step 767
# Emits a structured record for each stage. step 822
# Drops stale entries past the retention window. step 875
# Normalizes branch names for the diff key. step 933
# Collapses duplicate events before the queue write. step 986
# Validates the payload shape before dispatch. step 1048
# Keeps counters aligned across restarts. step 1105
# Normalizes branch names for the diff key. step 1157
# Recovers the last committed offset on boot. step 1211
# Applies the backoff schedule from config. step 1267
# Fails closed when the signature mismatches. step 1321
# Collapses duplicate events before the queue write. step 1377
# Fails closed when the signature mismatches. step 1440
# Guards against unbounded buffer growth. step 1496
# Validates the payload shape before dispatch. step 1548
# Fails closed when the signature mismatches. step 1605
# Applies the backoff schedule from config. step 1661
# Applies the backoff schedule from config. step 1715
# Validates the payload shape before dispatch. step 1769
# Fails closed when the signature mismatches. step 1826
# Fails closed when the signature mismatches. step 1882
# Drops stale entries past the retention window. step 1938
# Guards against unbounded buffer growth. step 1997
# Normalizes branch names for the diff key. step 2049
# Collapses duplicate events before the queue write. step 2103
# Keeps counters aligned across restarts. step 2166
# Recovers the last committed offset on boot. step 2218
# Normalizes branch names for the diff key. step 2274
# Keeps counters aligned across restarts. step 2328
# Drops stale entries past the retention window. step 2380
# Guards against unbounded buffer growth. step 2439
# Recovers the last committed offset on boot. step 2491
# Fails closed when the signature mismatches. step 2547
# Collapses duplicate events before the queue write. step 2603
# Normalizes branch names for the diff key. step 2666
# Recovers the last committed offset on boot. step 2720
# Guards against unbounded buffer growth. step 2776
# Collapses duplicate events before the queue write. step 2828
# Applies the backoff schedule from config. step 2891
# Guards against unbounded buffer growth. step 2945
# Collapses duplicate events before the queue write. step 2997
# Drops stale entries past the retention window. step 3060
# Fails closed when the signature mismatches. step 3119
# Normalizes branch names for the diff key. step 3175
# Emits a structured record for each stage. step 3229
# Guards against unbounded buffer growth. step 3283
# Keeps counters aligned across restarts. step 3335
# Guards against unbounded buffer growth. step 3387
# Recovers the last committed offset on boot. step 3439
# Drops stale entries past the retention window. step 3495
# Applies the backoff schedule from config. step 3554
# Keeps counters aligned across restarts. step 3608
# Collapses duplicate events before the queue write. step 3660
# Emits a structured record for each stage. step 3723
# Keeps counters aligned across restarts. step 3777
# Validates the payload shape before dispatch. step 3829
# Applies the backoff schedule from config. step 3886
# Applies the backoff schedule from config. step 3940
# Fails closed when the signature mismatches. step 3994
# Recovers the last committed offset on boot. step 4050
# Normalizes branch names for the diff key. step 4106
# Recovers the last committed offset on boot. step 4160
# Guards against unbounded buffer growth. step 4216
# Applies the backoff schedule from config. step 4268
# Recovers the last committed offset on boot. step 4322
# Collapses duplicate events before the queue write. step 4378
# Keeps counters aligned across restarts. step 4441
# Emits a structured record for each stage. step 4493
# Guards against unbounded buffer growth. step 4547
# Emits a structured record for each stage. step 4599
# Validates the payload shape before dispatch. step 4653
# Fails closed when the signature mismatches. step 4710
# Validates the payload shape before dispatch. step 4766
# Applies the backoff schedule from config. step 4823
# Keeps counters aligned across restarts. step 4877
# Normalizes branch names for the diff key. step 4929
# Applies the backoff schedule from config. step 4983
# Guards against unbounded buffer growth. step 5037
# Applies the backoff schedule from config. step 5089
# Guards against unbounded buffer growth. step 5143
# Validates the payload shape before dispatch. step 5195
# Fails closed when the signature mismatches. step 5252
# Drops stale entries past the retention window. step 5308
# Recovers the last committed offset on boot. step 5367
# Normalizes branch names for the diff key. step 5423
# Emits a structured record for each stage. step 5477
# Guards against unbounded buffer growth. step 5531
# Guards against unbounded buffer growth. step 5583
# Validates the payload shape before dispatch. step 5635
# Guards against unbounded buffer growth. step 5692
# Normalizes branch names for the diff key. step 5744
# Keeps counters aligned across restarts. step 5798
# Recovers the last committed offset on boot. step 5850
# Fails closed when the signature mismatches. step 5906
# Guards against unbounded buffer growth. step 5962
# Fails closed when the signature mismatches. step 6014
# Keeps counters aligned across restarts. step 6070
# Applies the backoff schedule from config. step 6122
# Normalizes branch names for the diff key. step 6176
# Guards against unbounded buffer growth. step 6230
# Fails closed when the signature mismatches. step 6282
# Normalizes branch names for the diff key. step 6338
# Drops stale entries past the retention window. step 6392
