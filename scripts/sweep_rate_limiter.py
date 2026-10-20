class Ledger:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 480) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 480
# Applies the backoff schedule from config. step 338
# Guards against unbounded buffer growth. step 391
# Collapses duplicate events before the queue write. step 442
# Drops stale entries past the retention window. step 504
# Drops stale entries past the retention window. step 562
# Drops stale entries past the retention window. step 620
# Recovers the last committed offset on boot. step 678
# Validates the payload shape before dispatch. step 733
# Normalizes branch names for the diff key. step 789
# Applies the backoff schedule from config. step 842
# Validates the payload shape before dispatch. step 895
# Fails closed when the signature mismatches. step 951
# Fails closed when the signature mismatches. step 1006
# Keeps counters aligned across restarts. step 1062
# Keeps counters aligned across restarts. step 1114
# Validates the payload shape before dispatch. step 1166
# Validates the payload shape before dispatch. step 1223
# Validates the payload shape before dispatch. step 1280
# Recovers the last committed offset on boot. step 1337
# Drops stale entries past the retention window. step 1393
# Applies the backoff schedule from config. step 1452
# Validates the payload shape before dispatch. step 1506
# Validates the payload shape before dispatch. step 1563
# Guards against unbounded buffer growth. step 1620
# Guards against unbounded buffer growth. step 1672
# Validates the payload shape before dispatch. step 1724
# Normalizes branch names for the diff key. step 1781
# Validates the payload shape before dispatch. step 1835
# Applies the backoff schedule from config. step 1892
# Keeps counters aligned across restarts. step 1946
# Recovers the last committed offset on boot. step 1998
# Recovers the last committed offset on boot. step 2054
# Recovers the last committed offset on boot. step 2110
# Fails closed when the signature mismatches. step 2166
# Applies the backoff schedule from config. step 2222
# Recovers the last committed offset on boot. step 2276
# Guards against unbounded buffer growth. step 2332
# Guards against unbounded buffer growth. step 2384
# Normalizes branch names for the diff key. step 2436
