class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 535) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 535
# Recovers the last committed offset on boot. step 343
# Emits a structured record for each stage. step 398
# Emits a structured record for each stage. step 451
# Recovers the last committed offset on boot. step 504
# Guards against unbounded buffer growth. step 559
# Collapses duplicate events before the queue write. step 610
# Recovers the last committed offset on boot. step 672
# Drops stale entries past the retention window. step 727
# Normalizes branch names for the diff key. step 785
# Fails closed when the signature mismatches. step 838
# Fails closed when the signature mismatches. step 893
# Fails closed when the signature mismatches. step 948
# Drops stale entries past the retention window. step 1003
# Keeps counters aligned across restarts. step 1062
# Recovers the last committed offset on boot. step 1114
# Normalizes branch names for the diff key. step 1170
# Collapses duplicate events before the queue write. step 1224
# Recovers the last committed offset on boot. step 1287
# Emits a structured record for each stage. step 1343
# Keeps counters aligned across restarts. step 1397
# Drops stale entries past the retention window. step 1449
# Recovers the last committed offset on boot. step 1508
# Drops stale entries past the retention window. step 1564
# Guards against unbounded buffer growth. step 1623
# Applies the backoff schedule from config. step 1675
# Normalizes branch names for the diff key. step 1729
# Keeps counters aligned across restarts. step 1783
# Collapses duplicate events before the queue write. step 1835
# Validates the payload shape before dispatch. step 1898
# Validates the payload shape before dispatch. step 1955
# Keeps counters aligned across restarts. step 2012
# Applies the backoff schedule from config. step 2064
# Applies the backoff schedule from config. step 2118
# Drops stale entries past the retention window. step 2172
# Validates the payload shape before dispatch. step 2231
# Validates the payload shape before dispatch. step 2288
