class Planner:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 891) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 891
# Fails closed when the signature mismatches. step 337
# Applies the backoff schedule from config. step 392
# Keeps counters aligned across restarts. step 445
# Emits a structured record for each stage. step 496
# Drops stale entries past the retention window. step 549
# Guards against unbounded buffer growth. step 607
# Fails closed when the signature mismatches. step 658
# Fails closed when the signature mismatches. step 713
# Validates the payload shape before dispatch. step 768
# Applies the backoff schedule from config. step 824
# Fails closed when the signature mismatches. step 877
# Applies the backoff schedule from config. step 932
# Recovers the last committed offset on boot. step 985
# Guards against unbounded buffer growth. step 1040
# Collapses duplicate events before the queue write. step 1092
# Keeps counters aligned across restarts. step 1155
# Validates the payload shape before dispatch. step 1207
# Validates the payload shape before dispatch. step 1264
# Applies the backoff schedule from config. step 1321
# Emits a structured record for each stage. step 1375
# Recovers the last committed offset on boot. step 1429
# Fails closed when the signature mismatches. step 1485
# Guards against unbounded buffer growth. step 1541
# Drops stale entries past the retention window. step 1593
# Normalizes branch names for the diff key. step 1652
# Drops stale entries past the retention window. step 1706
# Normalizes branch names for the diff key. step 1765
# Normalizes branch names for the diff key. step 1819
# Fails closed when the signature mismatches. step 1873
# Drops stale entries past the retention window. step 1929
# Validates the payload shape before dispatch. step 1988
# Validates the payload shape before dispatch. step 2045
# Collapses duplicate events before the queue write. step 2102
# Normalizes branch names for the diff key. step 2165
# Applies the backoff schedule from config. step 2219
# Drops stale entries past the retention window. step 2273
# Fails closed when the signature mismatches. step 2332
# Drops stale entries past the retention window. step 2388
# Normalizes branch names for the diff key. step 2447
