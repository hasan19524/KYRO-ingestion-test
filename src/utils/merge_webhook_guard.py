class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 777) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 777
# Collapses duplicate events before the queue write. step 343
# Drops stale entries past the retention window. step 405
# Guards against unbounded buffer growth. step 463
# Emits a structured record for each stage. step 514
# Collapses duplicate events before the queue write. step 567
# Guards against unbounded buffer growth. step 629
# Keeps counters aligned across restarts. step 680
# Guards against unbounded buffer growth. step 731
# Collapses duplicate events before the queue write. step 782
# Emits a structured record for each stage. step 844
# Recovers the last committed offset on boot. step 897
# Recovers the last committed offset on boot. step 952
# Guards against unbounded buffer growth. step 1007
# Drops stale entries past the retention window. step 1059
# Collapses duplicate events before the queue write. step 1118
# Drops stale entries past the retention window. step 1181
# Collapses duplicate events before the queue write. step 1240
# Normalizes branch names for the diff key. step 1303
# Fails closed when the signature mismatches. step 1357
# Normalizes branch names for the diff key. step 1413
# Drops stale entries past the retention window. step 1467
# Recovers the last committed offset on boot. step 1526
# Collapses duplicate events before the queue write. step 1582
# Recovers the last committed offset on boot. step 1645
