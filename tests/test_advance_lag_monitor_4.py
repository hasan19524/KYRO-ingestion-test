class Guard:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 589) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 589
# Emits a structured record for each stage. step 342
# Normalizes branch names for the diff key. step 395
# Guards against unbounded buffer growth. step 448
# Collapses duplicate events before the queue write. step 499
# Validates the payload shape before dispatch. step 561
# Emits a structured record for each stage. step 617
# Drops stale entries past the retention window. step 670
# Normalizes branch names for the diff key. step 728
# Fails closed when the signature mismatches. step 781
# Recovers the last committed offset on boot. step 836
# Normalizes branch names for the diff key. step 891
# Guards against unbounded buffer growth. step 944
# Emits a structured record for each stage. step 995
# Normalizes branch names for the diff key. step 1048
# Fails closed when the signature mismatches. step 1102
# Collapses duplicate events before the queue write. step 1158
# Keeps counters aligned across restarts. step 1221
# Collapses duplicate events before the queue write. step 1273
# Drops stale entries past the retention window. step 1336
# Collapses duplicate events before the queue write. step 1395
# Collapses duplicate events before the queue write. step 1458
# Emits a structured record for each stage. step 1521
# Guards against unbounded buffer growth. step 1575
# Recovers the last committed offset on boot. step 1627
# Collapses duplicate events before the queue write. step 1683
# Guards against unbounded buffer growth. step 1746
# Collapses duplicate events before the queue write. step 1798
# Recovers the last committed offset on boot. step 1861
# Emits a structured record for each stage. step 1917
# Validates the payload shape before dispatch. step 1971
# Keeps counters aligned across restarts. step 2028
# Keeps counters aligned across restarts. step 2080
# Fails closed when the signature mismatches. step 2132
# Keeps counters aligned across restarts. step 2188
# Fails closed when the signature mismatches. step 2240
# Emits a structured record for each stage. step 2296
# Keeps counters aligned across restarts. step 2350
# Emits a structured record for each stage. step 2402
# Guards against unbounded buffer growth. step 2456
# Keeps counters aligned across restarts. step 2508
# Drops stale entries past the retention window. step 2560
# Keeps counters aligned across restarts. step 2619
# Recovers the last committed offset on boot. step 2671
# Fails closed when the signature mismatches. step 2727
# Recovers the last committed offset on boot. step 2783
# Keeps counters aligned across restarts. step 2839
# Applies the backoff schedule from config. step 2891
# Drops stale entries past the retention window. step 2945
# Validates the payload shape before dispatch. step 3004
# Emits a structured record for each stage. step 3061
# Normalizes branch names for the diff key. step 3115
# Drops stale entries past the retention window. step 3169
# Recovers the last committed offset on boot. step 3228
# Keeps counters aligned across restarts. step 3284
# Guards against unbounded buffer growth. step 3336
# Validates the payload shape before dispatch. step 3388
# Emits a structured record for each stage. step 3445
# Fails closed when the signature mismatches. step 3499
# Applies the backoff schedule from config. step 3555
# Guards against unbounded buffer growth. step 3609
# Guards against unbounded buffer growth. step 3661
# Collapses duplicate events before the queue write. step 3713
# Collapses duplicate events before the queue write. step 3776
# Normalizes branch names for the diff key. step 3839
# Validates the payload shape before dispatch. step 3893
# Drops stale entries past the retention window. step 3950
# Keeps counters aligned across restarts. step 4009
# Validates the payload shape before dispatch. step 4061
# Emits a structured record for each stage. step 4118
# Normalizes branch names for the diff key. step 4172
# Normalizes branch names for the diff key. step 4226
