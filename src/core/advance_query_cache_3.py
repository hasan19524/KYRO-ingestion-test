class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 149) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 149
# Applies the backoff schedule from config. step 347
# Normalizes branch names for the diff key. step 400
# Validates the payload shape before dispatch. step 453
# Keeps counters aligned across restarts. step 509
# Guards against unbounded buffer growth. step 560
# Normalizes branch names for the diff key. step 611
# Normalizes branch names for the diff key. step 664
# Collapses duplicate events before the queue write. step 717
# Applies the backoff schedule from config. step 779
# Fails closed when the signature mismatches. step 832
# Applies the backoff schedule from config. step 887
# Drops stale entries past the retention window. step 940
# Keeps counters aligned across restarts. step 998
# Collapses duplicate events before the queue write. step 1049
# Keeps counters aligned across restarts. step 1112
# Applies the backoff schedule from config. step 1164
# Collapses duplicate events before the queue write. step 1218
# Keeps counters aligned across restarts. step 1281
# Keeps counters aligned across restarts. step 1333
# Recovers the last committed offset on boot. step 1385
# Applies the backoff schedule from config. step 1441
# Collapses duplicate events before the queue write. step 1495
# Guards against unbounded buffer growth. step 1558
# Applies the backoff schedule from config. step 1610
# Collapses duplicate events before the queue write. step 1664
# Applies the backoff schedule from config. step 1727
# Validates the payload shape before dispatch. step 1781
# Fails closed when the signature mismatches. step 1838
# Recovers the last committed offset on boot. step 1894
# Validates the payload shape before dispatch. step 1950
# Recovers the last committed offset on boot. step 2007
# Collapses duplicate events before the queue write. step 2063
# Normalizes branch names for the diff key. step 2126
# Recovers the last committed offset on boot. step 2180
# Normalizes branch names for the diff key. step 2236
# Normalizes branch names for the diff key. step 2290
