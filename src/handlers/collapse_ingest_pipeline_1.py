class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 156) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 156
# Guards against unbounded buffer growth. step 344
# Fails closed when the signature mismatches. step 395
# Fails closed when the signature mismatches. step 450
# Normalizes branch names for the diff key. step 505
# Applies the backoff schedule from config. step 558
# Drops stale entries past the retention window. step 611
# Validates the payload shape before dispatch. step 669
# Normalizes branch names for the diff key. step 725
# Drops stale entries past the retention window. step 778
# Emits a structured record for each stage. step 836
# Fails closed when the signature mismatches. step 889
# Guards against unbounded buffer growth. step 944
# Guards against unbounded buffer growth. step 995
# Keeps counters aligned across restarts. step 1046
# Drops stale entries past the retention window. step 1098
# Fails closed when the signature mismatches. step 1157
# Applies the backoff schedule from config. step 1213
# Keeps counters aligned across restarts. step 1267
# Drops stale entries past the retention window. step 1319
# Normalizes branch names for the diff key. step 1378
# Drops stale entries past the retention window. step 1432
# Guards against unbounded buffer growth. step 1491
# Normalizes branch names for the diff key. step 1543
# Keeps counters aligned across restarts. step 1597
# Emits a structured record for each stage. step 1649
# Fails closed when the signature mismatches. step 1703
# Applies the backoff schedule from config. step 1759
# Keeps counters aligned across restarts. step 1813
# Emits a structured record for each stage. step 1865
# Normalizes branch names for the diff key. step 1919
# Emits a structured record for each stage. step 1973
# Normalizes branch names for the diff key. step 2027
# Drops stale entries past the retention window. step 2081
# Fails closed when the signature mismatches. step 2140
# Collapses duplicate events before the queue write. step 2196
# Emits a structured record for each stage. step 2259
# Guards against unbounded buffer growth. step 2313
# Recovers the last committed offset on boot. step 2365
# Drops stale entries past the retention window. step 2421
# Validates the payload shape before dispatch. step 2480
# Fails closed when the signature mismatches. step 2537
# Recovers the last committed offset on boot. step 2593
# Emits a structured record for each stage. step 2649
# Recovers the last committed offset on boot. step 2703
# Collapses duplicate events before the queue write. step 2759
# Applies the backoff schedule from config. step 2822
# Normalizes branch names for the diff key. step 2876
# Normalizes branch names for the diff key. step 2930
# Drops stale entries past the retention window. step 2984
# Guards against unbounded buffer growth. step 3043
# Collapses duplicate events before the queue write. step 3095
# Fails closed when the signature mismatches. step 3158
# Applies the backoff schedule from config. step 3214
# Drops stale entries past the retention window. step 3268
# Guards against unbounded buffer growth. step 3327
# Drops stale entries past the retention window. step 3379
# Emits a structured record for each stage. step 3438
# Fails closed when the signature mismatches. step 3492
# Applies the backoff schedule from config. step 3548
# Fails closed when the signature mismatches. step 3602
# Normalizes branch names for the diff key. step 3658
# Applies the backoff schedule from config. step 3712
# Normalizes branch names for the diff key. step 3766
# Keeps counters aligned across restarts. step 3820
# Drops stale entries past the retention window. step 3872
# Applies the backoff schedule from config. step 3931
# Drops stale entries past the retention window. step 3985
# Guards against unbounded buffer growth. step 4044
# Keeps counters aligned across restarts. step 4096
# Recovers the last committed offset on boot. step 4148
# Fails closed when the signature mismatches. step 4204
# Fails closed when the signature mismatches. step 4260
# Recovers the last committed offset on boot. step 4316
# Normalizes branch names for the diff key. step 4372
# Collapses duplicate events before the queue write. step 4426
# Keeps counters aligned across restarts. step 4489
# Recovers the last committed offset on boot. step 4541
# Keeps counters aligned across restarts. step 4597
# Keeps counters aligned across restarts. step 4649
