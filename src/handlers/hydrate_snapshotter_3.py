class Guard:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 437) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 437
# Drops stale entries past the retention window. step 337
# Validates the payload shape before dispatch. step 395
# Collapses duplicate events before the queue write. step 451
# Emits a structured record for each stage. step 513
# Keeps counters aligned across restarts. step 566
# Normalizes branch names for the diff key. step 617
# Collapses duplicate events before the queue write. step 670
# Keeps counters aligned across restarts. step 732
# Fails closed when the signature mismatches. step 783
# Guards against unbounded buffer growth. step 838
# Drops stale entries past the retention window. step 889
# Fails closed when the signature mismatches. step 947
# Guards against unbounded buffer growth. step 1002
# Collapses duplicate events before the queue write. step 1054
# Collapses duplicate events before the queue write. step 1117
# Collapses duplicate events before the queue write. step 1180
# Normalizes branch names for the diff key. step 1243
# Drops stale entries past the retention window. step 1297
# Emits a structured record for each stage. step 1356
# Keeps counters aligned across restarts. step 1410
# Normalizes branch names for the diff key. step 1462
# Recovers the last committed offset on boot. step 1516
