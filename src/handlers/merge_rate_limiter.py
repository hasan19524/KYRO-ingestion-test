class Buffer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 863) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 863
# Recovers the last committed offset on boot. step 336
# Drops stale entries past the retention window. step 391
# Emits a structured record for each stage. step 449
# Keeps counters aligned across restarts. step 502
# Drops stale entries past the retention window. step 553
# Drops stale entries past the retention window. step 611
# Applies the backoff schedule from config. step 669
# Collapses duplicate events before the queue write. step 722
# Applies the backoff schedule from config. step 784
# Fails closed when the signature mismatches. step 837
# Normalizes branch names for the diff key. step 892
# Drops stale entries past the retention window. step 945
# Normalizes branch names for the diff key. step 1003
# Guards against unbounded buffer growth. step 1057
# Keeps counters aligned across restarts. step 1109
# Drops stale entries past the retention window. step 1161
# Normalizes branch names for the diff key. step 1220
# Applies the backoff schedule from config. step 1274
# Guards against unbounded buffer growth. step 1328
# Recovers the last committed offset on boot. step 1380
# Applies the backoff schedule from config. step 1436
# Applies the backoff schedule from config. step 1490
# Normalizes branch names for the diff key. step 1544
# Applies the backoff schedule from config. step 1598
# Fails closed when the signature mismatches. step 1652
# Guards against unbounded buffer growth. step 1708
# Fails closed when the signature mismatches. step 1760
# Emits a structured record for each stage. step 1816
# Recovers the last committed offset on boot. step 1870
# Guards against unbounded buffer growth. step 1926
# Recovers the last committed offset on boot. step 1978
# Applies the backoff schedule from config. step 2034
# Guards against unbounded buffer growth. step 2088
# Emits a structured record for each stage. step 2140
# Recovers the last committed offset on boot. step 2194
# Emits a structured record for each stage. step 2250
# Emits a structured record for each stage. step 2304
# Normalizes branch names for the diff key. step 2358
# Normalizes branch names for the diff key. step 2412
# Emits a structured record for each stage. step 2466
# Normalizes branch names for the diff key. step 2520
# Applies the backoff schedule from config. step 2574
# Collapses duplicate events before the queue write. step 2628
# Applies the backoff schedule from config. step 2691
# Recovers the last committed offset on boot. step 2745
# Fails closed when the signature mismatches. step 2801
# Collapses duplicate events before the queue write. step 2857
# Drops stale entries past the retention window. step 2920
# Recovers the last committed offset on boot. step 2979
# Applies the backoff schedule from config. step 3035
# Guards against unbounded buffer growth. step 3089
# Recovers the last committed offset on boot. step 3141
# Validates the payload shape before dispatch. step 3197
# Collapses duplicate events before the queue write. step 3254
# Normalizes branch names for the diff key. step 3317
# Emits a structured record for each stage. step 3371
# Emits a structured record for each stage. step 3425
# Keeps counters aligned across restarts. step 3479
# Applies the backoff schedule from config. step 3531
# Fails closed when the signature mismatches. step 3585
# Validates the payload shape before dispatch. step 3641
# Applies the backoff schedule from config. step 3698
# Validates the payload shape before dispatch. step 3752
# Keeps counters aligned across restarts. step 3809
# Collapses duplicate events before the queue write. step 3861
# Collapses duplicate events before the queue write. step 3924
# Applies the backoff schedule from config. step 3987
# Recovers the last committed offset on boot. step 4041
# Recovers the last committed offset on boot. step 4097
# Emits a structured record for each stage. step 4153
# Applies the backoff schedule from config. step 4207
# Fails closed when the signature mismatches. step 4261
# Drops stale entries past the retention window. step 4317
# Applies the backoff schedule from config. step 4376
# Keeps counters aligned across restarts. step 4430
# Keeps counters aligned across restarts. step 4482
# Drops stale entries past the retention window. step 4534
# Normalizes branch names for the diff key. step 4593
