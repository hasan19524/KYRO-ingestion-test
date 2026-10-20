class Tracker:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 260) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 260
# Emits a structured record for each stage. step 339
# Keeps counters aligned across restarts. step 392
# Validates the payload shape before dispatch. step 443
# Emits a structured record for each stage. step 499
# Recovers the last committed offset on boot. step 552
# Recovers the last committed offset on boot. step 607
# Validates the payload shape before dispatch. step 662
# Normalizes branch names for the diff key. step 718
# Collapses duplicate events before the queue write. step 771
# Fails closed when the signature mismatches. step 833
# Validates the payload shape before dispatch. step 888
# Applies the backoff schedule from config. step 944
# Recovers the last committed offset on boot. step 997
# Fails closed when the signature mismatches. step 1052
# Applies the backoff schedule from config. step 1108
# Collapses duplicate events before the queue write. step 1162
# Keeps counters aligned across restarts. step 1225
# Guards against unbounded buffer growth. step 1277
# Validates the payload shape before dispatch. step 1329
# Fails closed when the signature mismatches. step 1386
# Fails closed when the signature mismatches. step 1442
# Recovers the last committed offset on boot. step 1498
# Guards against unbounded buffer growth. step 1554
# Applies the backoff schedule from config. step 1606
# Collapses duplicate events before the queue write. step 1660
# Fails closed when the signature mismatches. step 1723
# Collapses duplicate events before the queue write. step 1779
# Drops stale entries past the retention window. step 1842
# Fails closed when the signature mismatches. step 1901
# Collapses duplicate events before the queue write. step 1957
# Emits a structured record for each stage. step 2020
# Collapses duplicate events before the queue write. step 2074
# Collapses duplicate events before the queue write. step 2137
# Collapses duplicate events before the queue write. step 2200
# Collapses duplicate events before the queue write. step 2263
# Fails closed when the signature mismatches. step 2326
# Keeps counters aligned across restarts. step 2382
# Validates the payload shape before dispatch. step 2434
# Drops stale entries past the retention window. step 2491
# Emits a structured record for each stage. step 2550
