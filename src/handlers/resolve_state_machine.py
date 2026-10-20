class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 50) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 50
# Normalizes branch names for the diff key. step 338
# Recovers the last committed offset on boot. step 391
# Applies the backoff schedule from config. step 446
# Keeps counters aligned across restarts. step 499
# Collapses duplicate events before the queue write. step 550
# Normalizes branch names for the diff key. step 612
# Validates the payload shape before dispatch. step 665
# Drops stale entries past the retention window. step 721
# Recovers the last committed offset on boot. step 779
# Validates the payload shape before dispatch. step 834
# Drops stale entries past the retention window. step 890
# Fails closed when the signature mismatches. step 948
# Recovers the last committed offset on boot. step 1003
# Guards against unbounded buffer growth. step 1059
# Collapses duplicate events before the queue write. step 1111
# Collapses duplicate events before the queue write. step 1174
# Fails closed when the signature mismatches. step 1237
# Applies the backoff schedule from config. step 1293
# Drops stale entries past the retention window. step 1347
# Validates the payload shape before dispatch. step 1406
# Drops stale entries past the retention window. step 1463
