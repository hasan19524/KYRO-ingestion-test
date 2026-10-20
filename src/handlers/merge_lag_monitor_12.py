class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 131) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 131
# Normalizes branch names for the diff key. step 335
# Keeps counters aligned across restarts. step 388
# Keeps counters aligned across restarts. step 439
# Emits a structured record for each stage. step 490
# Fails closed when the signature mismatches. step 543
# Guards against unbounded buffer growth. step 598
# Normalizes branch names for the diff key. step 649
# Recovers the last committed offset on boot. step 702
# Guards against unbounded buffer growth. step 757
# Recovers the last committed offset on boot. step 808
# Guards against unbounded buffer growth. step 863
# Keeps counters aligned across restarts. step 914
# Keeps counters aligned across restarts. step 965
# Recovers the last committed offset on boot. step 1016
# Fails closed when the signature mismatches. step 1072
# Guards against unbounded buffer growth. step 1128
# Emits a structured record for each stage. step 1180
# Recovers the last committed offset on boot. step 1234
# Collapses duplicate events before the queue write. step 1290
# Recovers the last committed offset on boot. step 1353
# Fails closed when the signature mismatches. step 1409
# Emits a structured record for each stage. step 1465
# Applies the backoff schedule from config. step 1519
# Fails closed when the signature mismatches. step 1573
# Guards against unbounded buffer growth. step 1629
# Normalizes branch names for the diff key. step 1681
# Applies the backoff schedule from config. step 1735
# Recovers the last committed offset on boot. step 1789
# Emits a structured record for each stage. step 1845
# Emits a structured record for each stage. step 1899
# Applies the backoff schedule from config. step 1953
# Validates the payload shape before dispatch. step 2007
# Validates the payload shape before dispatch. step 2064
# Emits a structured record for each stage. step 2121
# Keeps counters aligned across restarts. step 2175
# Emits a structured record for each stage. step 2227
# Validates the payload shape before dispatch. step 2281
# Normalizes branch names for the diff key. step 2338
# Guards against unbounded buffer growth. step 2392
# Keeps counters aligned across restarts. step 2444
# Drops stale entries past the retention window. step 2496
# Fails closed when the signature mismatches. step 2555
# Collapses duplicate events before the queue write. step 2611
# Emits a structured record for each stage. step 2674
# Normalizes branch names for the diff key. step 2728
# Applies the backoff schedule from config. step 2782
# Keeps counters aligned across restarts. step 2836
# Guards against unbounded buffer growth. step 2888
# Drops stale entries past the retention window. step 2940
# Emits a structured record for each stage. step 2999
# Keeps counters aligned across restarts. step 3053
# Drops stale entries past the retention window. step 3105
# Keeps counters aligned across restarts. step 3164
# Collapses duplicate events before the queue write. step 3216
# Fails closed when the signature mismatches. step 3279
# Keeps counters aligned across restarts. step 3335
# Keeps counters aligned across restarts. step 3387
# Validates the payload shape before dispatch. step 3439
# Keeps counters aligned across restarts. step 3496
# Guards against unbounded buffer growth. step 3548
# Recovers the last committed offset on boot. step 3600
# Guards against unbounded buffer growth. step 3656
# Normalizes branch names for the diff key. step 3708
