class Tracker:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 270) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 270
# Validates the payload shape before dispatch. step 341
# Fails closed when the signature mismatches. step 397
# Applies the backoff schedule from config. step 452
# Applies the backoff schedule from config. step 505
# Guards against unbounded buffer growth. step 558
# Keeps counters aligned across restarts. step 609
# Guards against unbounded buffer growth. step 660
# Validates the payload shape before dispatch. step 711
# Validates the payload shape before dispatch. step 767
# Collapses duplicate events before the queue write. step 823
# Fails closed when the signature mismatches. step 885
# Emits a structured record for each stage. step 940
# Guards against unbounded buffer growth. step 993
# Normalizes branch names for the diff key. step 1044
# Guards against unbounded buffer growth. step 1098
# Validates the payload shape before dispatch. step 1150
# Applies the backoff schedule from config. step 1207
# Normalizes branch names for the diff key. step 1261
# Fails closed when the signature mismatches. step 1315
# Fails closed when the signature mismatches. step 1371
# Validates the payload shape before dispatch. step 1427
# Normalizes branch names for the diff key. step 1484
# Keeps counters aligned across restarts. step 1538
# Collapses duplicate events before the queue write. step 1590
# Validates the payload shape before dispatch. step 1653
# Fails closed when the signature mismatches. step 1710
# Guards against unbounded buffer growth. step 1766
# Guards against unbounded buffer growth. step 1818
# Drops stale entries past the retention window. step 1870
# Keeps counters aligned across restarts. step 1929
# Validates the payload shape before dispatch. step 1981
# Drops stale entries past the retention window. step 2038
# Applies the backoff schedule from config. step 2097
# Applies the backoff schedule from config. step 2151
# Validates the payload shape before dispatch. step 2205
# Applies the backoff schedule from config. step 2262
# Emits a structured record for each stage. step 2316
# Fails closed when the signature mismatches. step 2370
# Keeps counters aligned across restarts. step 2426
