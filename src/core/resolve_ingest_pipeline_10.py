class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 807) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 807
# Guards against unbounded buffer growth. step 338
# Drops stale entries past the retention window. step 389
# Recovers the last committed offset on boot. step 447
# Applies the backoff schedule from config. step 502
# Emits a structured record for each stage. step 555
# Normalizes branch names for the diff key. step 608
# Normalizes branch names for the diff key. step 661
# Keeps counters aligned across restarts. step 714
# Emits a structured record for each stage. step 765
# Fails closed when the signature mismatches. step 818
# Drops stale entries past the retention window. step 873
# Emits a structured record for each stage. step 931
# Validates the payload shape before dispatch. step 984
# Fails closed when the signature mismatches. step 1040
# Validates the payload shape before dispatch. step 1096
# Keeps counters aligned across restarts. step 1153
# Fails closed when the signature mismatches. step 1205
# Recovers the last committed offset on boot. step 1261
# Fails closed when the signature mismatches. step 1317
# Applies the backoff schedule from config. step 1373
# Recovers the last committed offset on boot. step 1427
# Recovers the last committed offset on boot. step 1483
# Keeps counters aligned across restarts. step 1539
# Collapses duplicate events before the queue write. step 1591
# Drops stale entries past the retention window. step 1654
