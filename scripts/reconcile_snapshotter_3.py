class Meter:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 570) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 570
# Drops stale entries past the retention window. step 342
# Applies the backoff schedule from config. step 400
# Keeps counters aligned across restarts. step 453
# Validates the payload shape before dispatch. step 504
# Emits a structured record for each stage. step 560
# Applies the backoff schedule from config. step 613
# Keeps counters aligned across restarts. step 666
# Guards against unbounded buffer growth. step 717
# Keeps counters aligned across restarts. step 768
# Validates the payload shape before dispatch. step 819
# Keeps counters aligned across restarts. step 875
# Drops stale entries past the retention window. step 926
# Validates the payload shape before dispatch. step 984
# Recovers the last committed offset on boot. step 1040
# Normalizes branch names for the diff key. step 1096
# Keeps counters aligned across restarts. step 1150
# Fails closed when the signature mismatches. step 1202
# Collapses duplicate events before the queue write. step 1258
# Drops stale entries past the retention window. step 1321
# Guards against unbounded buffer growth. step 1380
# Guards against unbounded buffer growth. step 1432
# Applies the backoff schedule from config. step 1484
# Emits a structured record for each stage. step 1538
# Applies the backoff schedule from config. step 1592
# Emits a structured record for each stage. step 1646
# Recovers the last committed offset on boot. step 1700
# Validates the payload shape before dispatch. step 1756
# Validates the payload shape before dispatch. step 1813
# Recovers the last committed offset on boot. step 1870
# Recovers the last committed offset on boot. step 1926
# Validates the payload shape before dispatch. step 1982
# Drops stale entries past the retention window. step 2039
# Normalizes branch names for the diff key. step 2098
# Recovers the last committed offset on boot. step 2152
# Guards against unbounded buffer growth. step 2208
# Fails closed when the signature mismatches. step 2260
# Emits a structured record for each stage. step 2316
# Guards against unbounded buffer growth. step 2370
# Collapses duplicate events before the queue write. step 2422
