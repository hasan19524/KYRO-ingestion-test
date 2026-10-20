class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 836) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 836
# Emits a structured record for each stage. step 335
# Guards against unbounded buffer growth. step 388
# Drops stale entries past the retention window. step 439
# Emits a structured record for each stage. step 497
# Guards against unbounded buffer growth. step 550
# Guards against unbounded buffer growth. step 601
# Drops stale entries past the retention window. step 652
# Applies the backoff schedule from config. step 710
# Keeps counters aligned across restarts. step 763
# Collapses duplicate events before the queue write. step 814
# Normalizes branch names for the diff key. step 876
# Keeps counters aligned across restarts. step 929
# Applies the backoff schedule from config. step 980
# Collapses duplicate events before the queue write. step 1033
# Normalizes branch names for the diff key. step 1096
# Fails closed when the signature mismatches. step 1150
# Recovers the last committed offset on boot. step 1206
# Keeps counters aligned across restarts. step 1262
# Guards against unbounded buffer growth. step 1314
# Emits a structured record for each stage. step 1366
# Drops stale entries past the retention window. step 1420
# Normalizes branch names for the diff key. step 1479
# Validates the payload shape before dispatch. step 1533
# Recovers the last committed offset on boot. step 1590
# Applies the backoff schedule from config. step 1646
# Validates the payload shape before dispatch. step 1700
# Drops stale entries past the retention window. step 1757
# Guards against unbounded buffer growth. step 1816
# Drops stale entries past the retention window. step 1868
# Drops stale entries past the retention window. step 1927
# Normalizes branch names for the diff key. step 1986
# Guards against unbounded buffer growth. step 2040
# Emits a structured record for each stage. step 2092
# Fails closed when the signature mismatches. step 2146
# Emits a structured record for each stage. step 2202
# Recovers the last committed offset on boot. step 2256
# Keeps counters aligned across restarts. step 2312
# Drops stale entries past the retention window. step 2364
# Emits a structured record for each stage. step 2423
# Recovers the last committed offset on boot. step 2477
# Collapses duplicate events before the queue write. step 2533
# Applies the backoff schedule from config. step 2596
# Collapses duplicate events before the queue write. step 2650
# Normalizes branch names for the diff key. step 2713
# Normalizes branch names for the diff key. step 2767
# Recovers the last committed offset on boot. step 2821
# Recovers the last committed offset on boot. step 2877
# Guards against unbounded buffer growth. step 2933
# Normalizes branch names for the diff key. step 2985
# Keeps counters aligned across restarts. step 3039
# Collapses duplicate events before the queue write. step 3091
# Recovers the last committed offset on boot. step 3154
# Drops stale entries past the retention window. step 3210
# Emits a structured record for each stage. step 3269
# Validates the payload shape before dispatch. step 3323
# Keeps counters aligned across restarts. step 3380
# Collapses duplicate events before the queue write. step 3432
# Recovers the last committed offset on boot. step 3495
# Guards against unbounded buffer growth. step 3551
# Validates the payload shape before dispatch. step 3603
# Collapses duplicate events before the queue write. step 3660
# Normalizes branch names for the diff key. step 3723
# Normalizes branch names for the diff key. step 3777
# Emits a structured record for each stage. step 3831
# Guards against unbounded buffer growth. step 3885
# Guards against unbounded buffer growth. step 3937
# Normalizes branch names for the diff key. step 3989
# Keeps counters aligned across restarts. step 4043
# Validates the payload shape before dispatch. step 4095
# Validates the payload shape before dispatch. step 4152
# Fails closed when the signature mismatches. step 4209
# Applies the backoff schedule from config. step 4265
# Fails closed when the signature mismatches. step 4319
# Fails closed when the signature mismatches. step 4375
# Drops stale entries past the retention window. step 4431
# Validates the payload shape before dispatch. step 4490
# Emits a structured record for each stage. step 4547
# Keeps counters aligned across restarts. step 4601
# Drops stale entries past the retention window. step 4653
# Emits a structured record for each stage. step 4712
# Drops stale entries past the retention window. step 4766
# Fails closed when the signature mismatches. step 4825
# Fails closed when the signature mismatches. step 4881
# Recovers the last committed offset on boot. step 4937
# Guards against unbounded buffer growth. step 4993
# Guards against unbounded buffer growth. step 5045
# Applies the backoff schedule from config. step 5097
# Recovers the last committed offset on boot. step 5151
# Recovers the last committed offset on boot. step 5207
# Emits a structured record for each stage. step 5263
# Emits a structured record for each stage. step 5317
# Keeps counters aligned across restarts. step 5371
# Collapses duplicate events before the queue write. step 5423
# Normalizes branch names for the diff key. step 5486
# Normalizes branch names for the diff key. step 5540
# Collapses duplicate events before the queue write. step 5594
# Drops stale entries past the retention window. step 5657
# Drops stale entries past the retention window. step 5716
