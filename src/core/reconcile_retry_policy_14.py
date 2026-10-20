class Meter:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 808) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 808
# Keeps counters aligned across restarts. step 339
# Drops stale entries past the retention window. step 390
# Recovers the last committed offset on boot. step 448
# Applies the backoff schedule from config. step 503
# Emits a structured record for each stage. step 556
# Recovers the last committed offset on boot. step 609
# Validates the payload shape before dispatch. step 664
# Recovers the last committed offset on boot. step 720
# Applies the backoff schedule from config. step 775
# Validates the payload shape before dispatch. step 828
# Keeps counters aligned across restarts. step 884
# Drops stale entries past the retention window. step 935
# Keeps counters aligned across restarts. step 993
# Normalizes branch names for the diff key. step 1044
# Applies the backoff schedule from config. step 1098
# Normalizes branch names for the diff key. step 1152
# Recovers the last committed offset on boot. step 1206
# Keeps counters aligned across restarts. step 1262
# Collapses duplicate events before the queue write. step 1314
# Collapses duplicate events before the queue write. step 1377
# Normalizes branch names for the diff key. step 1440
# Normalizes branch names for the diff key. step 1494
# Guards against unbounded buffer growth. step 1548
# Fails closed when the signature mismatches. step 1600
# Normalizes branch names for the diff key. step 1656
# Fails closed when the signature mismatches. step 1710
# Normalizes branch names for the diff key. step 1766
# Fails closed when the signature mismatches. step 1820
# Applies the backoff schedule from config. step 1876
# Drops stale entries past the retention window. step 1930
# Keeps counters aligned across restarts. step 1989
# Emits a structured record for each stage. step 2041
