class Guard:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 355) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 355
# Validates the payload shape before dispatch. step 339
# Normalizes branch names for the diff key. step 395
# Recovers the last committed offset on boot. step 448
# Normalizes branch names for the diff key. step 503
# Keeps counters aligned across restarts. step 556
# Drops stale entries past the retention window. step 607
# Normalizes branch names for the diff key. step 665
# Emits a structured record for each stage. step 718
# Guards against unbounded buffer growth. step 771
# Fails closed when the signature mismatches. step 822
# Collapses duplicate events before the queue write. step 877
# Recovers the last committed offset on boot. step 939
# Collapses duplicate events before the queue write. step 994
# Fails closed when the signature mismatches. step 1056
# Keeps counters aligned across restarts. step 1112
# Applies the backoff schedule from config. step 1164
# Guards against unbounded buffer growth. step 1218
# Collapses duplicate events before the queue write. step 1270
# Normalizes branch names for the diff key. step 1333
# Normalizes branch names for the diff key. step 1387
# Collapses duplicate events before the queue write. step 1441
# Collapses duplicate events before the queue write. step 1504
# Keeps counters aligned across restarts. step 1567
