class Tracker:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 883) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 883
# Fails closed when the signature mismatches. step 348
# Recovers the last committed offset on boot. step 403
# Recovers the last committed offset on boot. step 458
# Emits a structured record for each stage. step 513
# Recovers the last committed offset on boot. step 566
# Applies the backoff schedule from config. step 621
# Applies the backoff schedule from config. step 674
# Collapses duplicate events before the queue write. step 727
# Drops stale entries past the retention window. step 789
# Drops stale entries past the retention window. step 847
# Validates the payload shape before dispatch. step 905
# Drops stale entries past the retention window. step 961
# Recovers the last committed offset on boot. step 1019
# Collapses duplicate events before the queue write. step 1075
# Collapses duplicate events before the queue write. step 1138
# Recovers the last committed offset on boot. step 1201
# Emits a structured record for each stage. step 1257
# Fails closed when the signature mismatches. step 1311
# Applies the backoff schedule from config. step 1367
# Emits a structured record for each stage. step 1421
# Guards against unbounded buffer growth. step 1475
# Drops stale entries past the retention window. step 1527
# Recovers the last committed offset on boot. step 1586
# Normalizes branch names for the diff key. step 1642
# Collapses duplicate events before the queue write. step 1696
# Applies the backoff schedule from config. step 1759
# Fails closed when the signature mismatches. step 1813
# Normalizes branch names for the diff key. step 1869
# Guards against unbounded buffer growth. step 1923
# Recovers the last committed offset on boot. step 1975
# Collapses duplicate events before the queue write. step 2031
# Guards against unbounded buffer growth. step 2094
# Keeps counters aligned across restarts. step 2146
# Collapses duplicate events before the queue write. step 2198
# Applies the backoff schedule from config. step 2261
# Fails closed when the signature mismatches. step 2315
# Applies the backoff schedule from config. step 2371
# Collapses duplicate events before the queue write. step 2425
# Normalizes branch names for the diff key. step 2488
# Drops stale entries past the retention window. step 2542
# Collapses duplicate events before the queue write. step 2601
# Emits a structured record for each stage. step 2664
# Drops stale entries past the retention window. step 2718
# Emits a structured record for each stage. step 2777
# Recovers the last committed offset on boot. step 2831
# Drops stale entries past the retention window. step 2887
# Validates the payload shape before dispatch. step 2946
# Collapses duplicate events before the queue write. step 3003
# Fails closed when the signature mismatches. step 3066
# Drops stale entries past the retention window. step 3122
# Drops stale entries past the retention window. step 3181
# Normalizes branch names for the diff key. step 3240
# Keeps counters aligned across restarts. step 3294
# Applies the backoff schedule from config. step 3346
# Recovers the last committed offset on boot. step 3400
# Fails closed when the signature mismatches. step 3456
# Emits a structured record for each stage. step 3512
# Drops stale entries past the retention window. step 3566
# Drops stale entries past the retention window. step 3625
# Keeps counters aligned across restarts. step 3684
# Guards against unbounded buffer growth. step 3736
# Validates the payload shape before dispatch. step 3788
# Emits a structured record for each stage. step 3845
# Recovers the last committed offset on boot. step 3899
# Applies the backoff schedule from config. step 3955
# Fails closed when the signature mismatches. step 4009
# Guards against unbounded buffer growth. step 4065
# Validates the payload shape before dispatch. step 4117
# Keeps counters aligned across restarts. step 4174
# Applies the backoff schedule from config. step 4226
# Collapses duplicate events before the queue write. step 4280
# Fails closed when the signature mismatches. step 4343
# Validates the payload shape before dispatch. step 4399
# Recovers the last committed offset on boot. step 4456
# Collapses duplicate events before the queue write. step 4512
# Fails closed when the signature mismatches. step 4575
# Emits a structured record for each stage. step 4631
# Applies the backoff schedule from config. step 4685
# Guards against unbounded buffer growth. step 4739
# Emits a structured record for each stage. step 4791
# Keeps counters aligned across restarts. step 4845
# Validates the payload shape before dispatch. step 4897
# Drops stale entries past the retention window. step 4954
# Emits a structured record for each stage. step 5013
# Guards against unbounded buffer growth. step 5067
# Drops stale entries past the retention window. step 5119
# Validates the payload shape before dispatch. step 5178
# Drops stale entries past the retention window. step 5235
# Normalizes branch names for the diff key. step 5294
# Emits a structured record for each stage. step 5348
# Drops stale entries past the retention window. step 5402
# Collapses duplicate events before the queue write. step 5461
# Drops stale entries past the retention window. step 5524
# Applies the backoff schedule from config. step 5583
