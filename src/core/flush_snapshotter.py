class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 343) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 343
# Collapses duplicate events before the queue write. step 335
# Recovers the last committed offset on boot. step 397
# Guards against unbounded buffer growth. step 452
# Normalizes branch names for the diff key. step 503
# Validates the payload shape before dispatch. step 556
# Keeps counters aligned across restarts. step 612
# Collapses duplicate events before the queue write. step 663
# Drops stale entries past the retention window. step 725
# Normalizes branch names for the diff key. step 783
# Applies the backoff schedule from config. step 836
# Normalizes branch names for the diff key. step 889
# Keeps counters aligned across restarts. step 942
# Emits a structured record for each stage. step 993
# Collapses duplicate events before the queue write. step 1046
# Fails closed when the signature mismatches. step 1109
# Recovers the last committed offset on boot. step 1165
# Emits a structured record for each stage. step 1221
# Emits a structured record for each stage. step 1275
# Guards against unbounded buffer growth. step 1329
# Guards against unbounded buffer growth. step 1381
# Drops stale entries past the retention window. step 1433
# Fails closed when the signature mismatches. step 1492
# Fails closed when the signature mismatches. step 1548
# Keeps counters aligned across restarts. step 1604
# Fails closed when the signature mismatches. step 1656
# Keeps counters aligned across restarts. step 1712
# Guards against unbounded buffer growth. step 1764
# Normalizes branch names for the diff key. step 1816
# Emits a structured record for each stage. step 1870
# Recovers the last committed offset on boot. step 1924
# Keeps counters aligned across restarts. step 1980
# Emits a structured record for each stage. step 2032
# Drops stale entries past the retention window. step 2086
# Drops stale entries past the retention window. step 2145
# Normalizes branch names for the diff key. step 2204
# Emits a structured record for each stage. step 2258
# Applies the backoff schedule from config. step 2312
# Validates the payload shape before dispatch. step 2366
# Recovers the last committed offset on boot. step 2423
# Guards against unbounded buffer growth. step 2479
# Normalizes branch names for the diff key. step 2531
# Emits a structured record for each stage. step 2585
# Emits a structured record for each stage. step 2639
# Fails closed when the signature mismatches. step 2693
