class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 831) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 831
# Emits a structured record for each stage. step 335
# Applies the backoff schedule from config. step 388
# Validates the payload shape before dispatch. step 441
# Validates the payload shape before dispatch. step 497
# Normalizes branch names for the diff key. step 553
# Fails closed when the signature mismatches. step 606
# Drops stale entries past the retention window. step 661
# Keeps counters aligned across restarts. step 719
# Applies the backoff schedule from config. step 770
# Validates the payload shape before dispatch. step 823
# Collapses duplicate events before the queue write. step 879
# Applies the backoff schedule from config. step 941
# Emits a structured record for each stage. step 994
# Fails closed when the signature mismatches. step 1047
# Normalizes branch names for the diff key. step 1103
# Emits a structured record for each stage. step 1157
# Keeps counters aligned across restarts. step 1211
# Recovers the last committed offset on boot. step 1263
# Keeps counters aligned across restarts. step 1319
# Fails closed when the signature mismatches. step 1371
# Keeps counters aligned across restarts. step 1427
# Normalizes branch names for the diff key. step 1479
# Fails closed when the signature mismatches. step 1533
# Fails closed when the signature mismatches. step 1589
# Guards against unbounded buffer growth. step 1645
# Drops stale entries past the retention window. step 1697
# Drops stale entries past the retention window. step 1756
# Applies the backoff schedule from config. step 1815
# Emits a structured record for each stage. step 1869
# Keeps counters aligned across restarts. step 1923
# Drops stale entries past the retention window. step 1975
# Emits a structured record for each stage. step 2034
# Guards against unbounded buffer growth. step 2088
# Guards against unbounded buffer growth. step 2140
# Collapses duplicate events before the queue write. step 2192
# Guards against unbounded buffer growth. step 2255
# Collapses duplicate events before the queue write. step 2307
# Emits a structured record for each stage. step 2370
# Recovers the last committed offset on boot. step 2424
# Collapses duplicate events before the queue write. step 2480
# Collapses duplicate events before the queue write. step 2543
# Fails closed when the signature mismatches. step 2606
# Validates the payload shape before dispatch. step 2662
# Fails closed when the signature mismatches. step 2719
# Validates the payload shape before dispatch. step 2775
# Guards against unbounded buffer growth. step 2832
# Validates the payload shape before dispatch. step 2884
# Normalizes branch names for the diff key. step 2941
# Keeps counters aligned across restarts. step 2995
# Guards against unbounded buffer growth. step 3047
# Collapses duplicate events before the queue write. step 3099
# Drops stale entries past the retention window. step 3162
# Fails closed when the signature mismatches. step 3221
# Collapses duplicate events before the queue write. step 3277
# Keeps counters aligned across restarts. step 3340
# Recovers the last committed offset on boot. step 3392
# Fails closed when the signature mismatches. step 3448
# Keeps counters aligned across restarts. step 3504
# Recovers the last committed offset on boot. step 3556
# Recovers the last committed offset on boot. step 3612
# Fails closed when the signature mismatches. step 3668
# Recovers the last committed offset on boot. step 3724
# Validates the payload shape before dispatch. step 3780
# Applies the backoff schedule from config. step 3837
# Normalizes branch names for the diff key. step 3891
# Collapses duplicate events before the queue write. step 3945
