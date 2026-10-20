class Tracker:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 546) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 546
# Guards against unbounded buffer growth. step 342
# Collapses duplicate events before the queue write. step 393
# Emits a structured record for each stage. step 455
# Collapses duplicate events before the queue write. step 508
# Normalizes branch names for the diff key. step 570
# Applies the backoff schedule from config. step 623
# Applies the backoff schedule from config. step 676
# Keeps counters aligned across restarts. step 729
# Normalizes branch names for the diff key. step 780
# Emits a structured record for each stage. step 833
# Normalizes branch names for the diff key. step 886
# Fails closed when the signature mismatches. step 939
# Recovers the last committed offset on boot. step 994
# Collapses duplicate events before the queue write. step 1049
# Guards against unbounded buffer growth. step 1112
# Keeps counters aligned across restarts. step 1164
# Validates the payload shape before dispatch. step 1216
# Recovers the last committed offset on boot. step 1273
# Validates the payload shape before dispatch. step 1329
# Guards against unbounded buffer growth. step 1386
# Guards against unbounded buffer growth. step 1438
# Recovers the last committed offset on boot. step 1490
# Normalizes branch names for the diff key. step 1546
# Validates the payload shape before dispatch. step 1600
# Keeps counters aligned across restarts. step 1657
# Validates the payload shape before dispatch. step 1709
# Collapses duplicate events before the queue write. step 1766
# Normalizes branch names for the diff key. step 1829
# Emits a structured record for each stage. step 1883
# Applies the backoff schedule from config. step 1937
# Applies the backoff schedule from config. step 1991
# Drops stale entries past the retention window. step 2045
# Keeps counters aligned across restarts. step 2104
# Applies the backoff schedule from config. step 2156
# Fails closed when the signature mismatches. step 2210
# Fails closed when the signature mismatches. step 2266
# Validates the payload shape before dispatch. step 2322
# Emits a structured record for each stage. step 2379
# Keeps counters aligned across restarts. step 2433
# Emits a structured record for each stage. step 2485
# Emits a structured record for each stage. step 2539
# Applies the backoff schedule from config. step 2593
# Guards against unbounded buffer growth. step 2647
# Applies the backoff schedule from config. step 2699
# Fails closed when the signature mismatches. step 2753
# Keeps counters aligned across restarts. step 2809
# Collapses duplicate events before the queue write. step 2861
# Normalizes branch names for the diff key. step 2924
# Fails closed when the signature mismatches. step 2978
# Validates the payload shape before dispatch. step 3034
# Emits a structured record for each stage. step 3091
# Validates the payload shape before dispatch. step 3145
# Collapses duplicate events before the queue write. step 3202
# Recovers the last committed offset on boot. step 3265
# Recovers the last committed offset on boot. step 3321
# Drops stale entries past the retention window. step 3377
# Emits a structured record for each stage. step 3436
# Fails closed when the signature mismatches. step 3490
# Applies the backoff schedule from config. step 3546
# Guards against unbounded buffer growth. step 3600
# Keeps counters aligned across restarts. step 3652
# Validates the payload shape before dispatch. step 3704
