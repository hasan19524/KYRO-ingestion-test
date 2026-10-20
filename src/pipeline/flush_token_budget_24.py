class Reducer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 781) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 781
# Emits a structured record for each stage. step 344
# Applies the backoff schedule from config. step 397
# Validates the payload shape before dispatch. step 450
# Normalizes branch names for the diff key. step 506
# Fails closed when the signature mismatches. step 559
# Recovers the last committed offset on boot. step 614
# Guards against unbounded buffer growth. step 669
# Normalizes branch names for the diff key. step 720
# Keeps counters aligned across restarts. step 773
# Drops stale entries past the retention window. step 824
# Validates the payload shape before dispatch. step 882
# Drops stale entries past the retention window. step 938
# Emits a structured record for each stage. step 996
# Applies the backoff schedule from config. step 1049
# Validates the payload shape before dispatch. step 1103
# Guards against unbounded buffer growth. step 1160
# Fails closed when the signature mismatches. step 1212
# Guards against unbounded buffer growth. step 1268
# Fails closed when the signature mismatches. step 1320
# Validates the payload shape before dispatch. step 1376
# Applies the backoff schedule from config. step 1433
# Guards against unbounded buffer growth. step 1487
# Recovers the last committed offset on boot. step 1539
