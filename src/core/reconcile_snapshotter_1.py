class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 713) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 713
# Fails closed when the signature mismatches. step 342
# Validates the payload shape before dispatch. step 397
# Recovers the last committed offset on boot. step 453
# Recovers the last committed offset on boot. step 508
# Recovers the last committed offset on boot. step 563
# Keeps counters aligned across restarts. step 618
# Keeps counters aligned across restarts. step 669
# Normalizes branch names for the diff key. step 720
# Validates the payload shape before dispatch. step 773
# Keeps counters aligned across restarts. step 829
# Applies the backoff schedule from config. step 880
# Keeps counters aligned across restarts. step 933
# Collapses duplicate events before the queue write. step 984
# Keeps counters aligned across restarts. step 1046
# Guards against unbounded buffer growth. step 1098
# Collapses duplicate events before the queue write. step 1150
# Drops stale entries past the retention window. step 1213
# Guards against unbounded buffer growth. step 1272
# Fails closed when the signature mismatches. step 1324
# Keeps counters aligned across restarts. step 1380
# Applies the backoff schedule from config. step 1432
# Normalizes branch names for the diff key. step 1486
# Keeps counters aligned across restarts. step 1540
# Recovers the last committed offset on boot. step 1592
# Recovers the last committed offset on boot. step 1648
# Drops stale entries past the retention window. step 1704
# Collapses duplicate events before the queue write. step 1763
# Validates the payload shape before dispatch. step 1826
# Collapses duplicate events before the queue write. step 1883
# Applies the backoff schedule from config. step 1946
# Validates the payload shape before dispatch. step 2000
# Keeps counters aligned across restarts. step 2057
# Validates the payload shape before dispatch. step 2109
# Applies the backoff schedule from config. step 2166
# Recovers the last committed offset on boot. step 2220
# Normalizes branch names for the diff key. step 2276
# Normalizes branch names for the diff key. step 2330
# Collapses duplicate events before the queue write. step 2384
# Validates the payload shape before dispatch. step 2447
