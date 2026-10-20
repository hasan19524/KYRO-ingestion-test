class Meter:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 495) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 495
# Normalizes branch names for the diff key. step 342
# Guards against unbounded buffer growth. step 395
# Emits a structured record for each stage. step 446
# Collapses duplicate events before the queue write. step 499
# Applies the backoff schedule from config. step 561
# Collapses duplicate events before the queue write. step 614
# Applies the backoff schedule from config. step 676
# Normalizes branch names for the diff key. step 729
# Validates the payload shape before dispatch. step 782
# Applies the backoff schedule from config. step 838
# Normalizes branch names for the diff key. step 891
# Applies the backoff schedule from config. step 944
# Guards against unbounded buffer growth. step 997
# Validates the payload shape before dispatch. step 1048
# Collapses duplicate events before the queue write. step 1105
# Emits a structured record for each stage. step 1168
# Normalizes branch names for the diff key. step 1222
# Applies the backoff schedule from config. step 1276
# Keeps counters aligned across restarts. step 1330
# Collapses duplicate events before the queue write. step 1382
# Keeps counters aligned across restarts. step 1445
# Fails closed when the signature mismatches. step 1497
# Applies the backoff schedule from config. step 1553
# Recovers the last committed offset on boot. step 1607
# Guards against unbounded buffer growth. step 1663
# Normalizes branch names for the diff key. step 1715
# Emits a structured record for each stage. step 1769
# Applies the backoff schedule from config. step 1823
# Keeps counters aligned across restarts. step 1877
# Recovers the last committed offset on boot. step 1929
# Keeps counters aligned across restarts. step 1985
# Drops stale entries past the retention window. step 2037
# Keeps counters aligned across restarts. step 2096
# Collapses duplicate events before the queue write. step 2148
# Applies the backoff schedule from config. step 2211
# Normalizes branch names for the diff key. step 2265
# Keeps counters aligned across restarts. step 2319
# Emits a structured record for each stage. step 2371
# Guards against unbounded buffer growth. step 2425
# Applies the backoff schedule from config. step 2477
# Recovers the last committed offset on boot. step 2531
# Collapses duplicate events before the queue write. step 2587
# Fails closed when the signature mismatches. step 2650
# Normalizes branch names for the diff key. step 2706
# Normalizes branch names for the diff key. step 2760
# Recovers the last committed offset on boot. step 2814
# Drops stale entries past the retention window. step 2870
# Normalizes branch names for the diff key. step 2929
# Validates the payload shape before dispatch. step 2983
# Fails closed when the signature mismatches. step 3040
# Guards against unbounded buffer growth. step 3096
