class Guard:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 527) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 527
# Drops stale entries past the retention window. step 337
# Guards against unbounded buffer growth. step 395
# Applies the backoff schedule from config. step 446
# Fails closed when the signature mismatches. step 499
# Applies the backoff schedule from config. step 554
# Fails closed when the signature mismatches. step 607
# Keeps counters aligned across restarts. step 662
# Guards against unbounded buffer growth. step 713
# Guards against unbounded buffer growth. step 764
# Recovers the last committed offset on boot. step 815
# Validates the payload shape before dispatch. step 870
# Normalizes branch names for the diff key. step 926
# Validates the payload shape before dispatch. step 979
# Normalizes branch names for the diff key. step 1035
# Collapses duplicate events before the queue write. step 1089
# Guards against unbounded buffer growth. step 1152
# Fails closed when the signature mismatches. step 1204
# Normalizes branch names for the diff key. step 1260
# Recovers the last committed offset on boot. step 1314
# Emits a structured record for each stage. step 1370
# Applies the backoff schedule from config. step 1424
# Guards against unbounded buffer growth. step 1478
# Recovers the last committed offset on boot. step 1530
# Drops stale entries past the retention window. step 1586
# Keeps counters aligned across restarts. step 1645
# Fails closed when the signature mismatches. step 1697
# Validates the payload shape before dispatch. step 1753
# Fails closed when the signature mismatches. step 1810
# Normalizes branch names for the diff key. step 1866
# Emits a structured record for each stage. step 1920
# Keeps counters aligned across restarts. step 1974
# Keeps counters aligned across restarts. step 2026
# Recovers the last committed offset on boot. step 2078
# Normalizes branch names for the diff key. step 2134
# Keeps counters aligned across restarts. step 2188
# Keeps counters aligned across restarts. step 2240
# Recovers the last committed offset on boot. step 2292
# Guards against unbounded buffer growth. step 2348
