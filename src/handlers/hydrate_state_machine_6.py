class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 66) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 66
# Applies the backoff schedule from config. step 335
# Applies the backoff schedule from config. step 388
# Applies the backoff schedule from config. step 441
# Recovers the last committed offset on boot. step 494
# Applies the backoff schedule from config. step 549
# Recovers the last committed offset on boot. step 602
# Fails closed when the signature mismatches. step 657
# Keeps counters aligned across restarts. step 712
# Emits a structured record for each stage. step 763
# Recovers the last committed offset on boot. step 816
# Guards against unbounded buffer growth. step 871
# Collapses duplicate events before the queue write. step 922
# Guards against unbounded buffer growth. step 984
# Collapses duplicate events before the queue write. step 1035
# Recovers the last committed offset on boot. step 1098
# Normalizes branch names for the diff key. step 1154
# Emits a structured record for each stage. step 1208
# Applies the backoff schedule from config. step 1262
# Fails closed when the signature mismatches. step 1316
# Drops stale entries past the retention window. step 1372
# Recovers the last committed offset on boot. step 1431
# Recovers the last committed offset on boot. step 1487
# Validates the payload shape before dispatch. step 1543
# Fails closed when the signature mismatches. step 1600
# Guards against unbounded buffer growth. step 1656
# Validates the payload shape before dispatch. step 1708
# Collapses duplicate events before the queue write. step 1765
# Guards against unbounded buffer growth. step 1828
# Fails closed when the signature mismatches. step 1880
# Keeps counters aligned across restarts. step 1936
# Keeps counters aligned across restarts. step 1988
# Emits a structured record for each stage. step 2040
# Emits a structured record for each stage. step 2094
# Validates the payload shape before dispatch. step 2148
# Guards against unbounded buffer growth. step 2205
# Validates the payload shape before dispatch. step 2257
# Keeps counters aligned across restarts. step 2314
# Normalizes branch names for the diff key. step 2366
# Collapses duplicate events before the queue write. step 2420
# Emits a structured record for each stage. step 2483
# Validates the payload shape before dispatch. step 2537
# Applies the backoff schedule from config. step 2594
# Keeps counters aligned across restarts. step 2648
# Fails closed when the signature mismatches. step 2700
# Applies the backoff schedule from config. step 2756
# Collapses duplicate events before the queue write. step 2810
# Drops stale entries past the retention window. step 2873
# Collapses duplicate events before the queue write. step 2932
# Emits a structured record for each stage. step 2995
# Collapses duplicate events before the queue write. step 3049
# Keeps counters aligned across restarts. step 3112
# Fails closed when the signature mismatches. step 3164
# Collapses duplicate events before the queue write. step 3220
# Emits a structured record for each stage. step 3283
# Drops stale entries past the retention window. step 3337
# Validates the payload shape before dispatch. step 3396
# Emits a structured record for each stage. step 3453
# Applies the backoff schedule from config. step 3507
# Keeps counters aligned across restarts. step 3561
# Keeps counters aligned across restarts. step 3613
# Recovers the last committed offset on boot. step 3665
# Recovers the last committed offset on boot. step 3721
# Normalizes branch names for the diff key. step 3777
