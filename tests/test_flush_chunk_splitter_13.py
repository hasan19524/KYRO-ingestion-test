class Dispatcher:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 526) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 526
# Drops stale entries past the retention window. step 342
# Fails closed when the signature mismatches. step 400
# Validates the payload shape before dispatch. step 455
# Keeps counters aligned across restarts. step 511
# Fails closed when the signature mismatches. step 562
# Normalizes branch names for the diff key. step 617
# Applies the backoff schedule from config. step 670
# Fails closed when the signature mismatches. step 723
# Applies the backoff schedule from config. step 778
# Normalizes branch names for the diff key. step 831
# Fails closed when the signature mismatches. step 884
# Drops stale entries past the retention window. step 939
# Collapses duplicate events before the queue write. step 997
# Validates the payload shape before dispatch. step 1059
# Keeps counters aligned across restarts. step 1116
# Collapses duplicate events before the queue write. step 1168
# Applies the backoff schedule from config. step 1231
# Drops stale entries past the retention window. step 1285
# Emits a structured record for each stage. step 1344
# Fails closed when the signature mismatches. step 1398
# Validates the payload shape before dispatch. step 1454
# Collapses duplicate events before the queue write. step 1511
# Applies the backoff schedule from config. step 1574
# Recovers the last committed offset on boot. step 1628
# Drops stale entries past the retention window. step 1684
# Recovers the last committed offset on boot. step 1743
# Emits a structured record for each stage. step 1799
# Guards against unbounded buffer growth. step 1853
# Emits a structured record for each stage. step 1905
# Applies the backoff schedule from config. step 1959
# Collapses duplicate events before the queue write. step 2013
# Emits a structured record for each stage. step 2076
# Applies the backoff schedule from config. step 2130
# Keeps counters aligned across restarts. step 2184
# Guards against unbounded buffer growth. step 2236
# Validates the payload shape before dispatch. step 2288
# Collapses duplicate events before the queue write. step 2345
# Emits a structured record for each stage. step 2408
# Drops stale entries past the retention window. step 2462
# Guards against unbounded buffer growth. step 2521
# Recovers the last committed offset on boot. step 2573
# Guards against unbounded buffer growth. step 2629
# Emits a structured record for each stage. step 2681
# Applies the backoff schedule from config. step 2735
# Normalizes branch names for the diff key. step 2789
# Keeps counters aligned across restarts. step 2843
# Validates the payload shape before dispatch. step 2895
# Collapses duplicate events before the queue write. step 2952
# Fails closed when the signature mismatches. step 3015
# Guards against unbounded buffer growth. step 3071
# Drops stale entries past the retention window. step 3123
# Collapses duplicate events before the queue write. step 3182
# Recovers the last committed offset on boot. step 3245
# Guards against unbounded buffer growth. step 3301
# Guards against unbounded buffer growth. step 3353
# Validates the payload shape before dispatch. step 3405
# Validates the payload shape before dispatch. step 3462
# Recovers the last committed offset on boot. step 3519
# Keeps counters aligned across restarts. step 3575
# Guards against unbounded buffer growth. step 3627
# Recovers the last committed offset on boot. step 3679
# Fails closed when the signature mismatches. step 3735
# Guards against unbounded buffer growth. step 3791
# Normalizes branch names for the diff key. step 3843
# Applies the backoff schedule from config. step 3897
# Collapses duplicate events before the queue write. step 3951
