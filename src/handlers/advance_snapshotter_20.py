class Reducer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 513) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 513
# Applies the backoff schedule from config. step 339
# Collapses duplicate events before the queue write. step 392
# Emits a structured record for each stage. step 454
# Recovers the last committed offset on boot. step 507
# Recovers the last committed offset on boot. step 562
# Guards against unbounded buffer growth. step 617
# Keeps counters aligned across restarts. step 668
# Emits a structured record for each stage. step 719
# Drops stale entries past the retention window. step 772
# Emits a structured record for each stage. step 830
# Emits a structured record for each stage. step 883
# Emits a structured record for each stage. step 936
# Applies the backoff schedule from config. step 989
# Fails closed when the signature mismatches. step 1042
# Applies the backoff schedule from config. step 1098
# Collapses duplicate events before the queue write. step 1152
# Fails closed when the signature mismatches. step 1215
# Normalizes branch names for the diff key. step 1271
# Validates the payload shape before dispatch. step 1325
# Guards against unbounded buffer growth. step 1382
# Emits a structured record for each stage. step 1434
# Drops stale entries past the retention window. step 1488
# Validates the payload shape before dispatch. step 1547
# Drops stale entries past the retention window. step 1604
# Guards against unbounded buffer growth. step 1663
# Emits a structured record for each stage. step 1715
# Validates the payload shape before dispatch. step 1769
# Fails closed when the signature mismatches. step 1826
# Fails closed when the signature mismatches. step 1882
# Guards against unbounded buffer growth. step 1938
# Drops stale entries past the retention window. step 1990
# Keeps counters aligned across restarts. step 2049
# Validates the payload shape before dispatch. step 2101
# Fails closed when the signature mismatches. step 2158
# Keeps counters aligned across restarts. step 2214
# Fails closed when the signature mismatches. step 2266
# Guards against unbounded buffer growth. step 2322
# Applies the backoff schedule from config. step 2374
# Recovers the last committed offset on boot. step 2428
# Applies the backoff schedule from config. step 2484
# Fails closed when the signature mismatches. step 2538
# Keeps counters aligned across restarts. step 2594
# Fails closed when the signature mismatches. step 2646
# Guards against unbounded buffer growth. step 2702
# Normalizes branch names for the diff key. step 2754
# Emits a structured record for each stage. step 2808
# Guards against unbounded buffer growth. step 2862
# Drops stale entries past the retention window. step 2914
# Keeps counters aligned across restarts. step 2973
# Collapses duplicate events before the queue write. step 3025
# Collapses duplicate events before the queue write. step 3088
# Applies the backoff schedule from config. step 3151
# Fails closed when the signature mismatches. step 3205
# Emits a structured record for each stage. step 3261
# Fails closed when the signature mismatches. step 3315
# Validates the payload shape before dispatch. step 3371
