class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 437) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 437
# Applies the backoff schedule from config. step 338
# Emits a structured record for each stage. step 391
# Fails closed when the signature mismatches. step 444
# Keeps counters aligned across restarts. step 499
# Fails closed when the signature mismatches. step 550
# Keeps counters aligned across restarts. step 605
# Drops stale entries past the retention window. step 656
# Collapses duplicate events before the queue write. step 714
# Guards against unbounded buffer growth. step 776
# Normalizes branch names for the diff key. step 827
# Normalizes branch names for the diff key. step 880
# Normalizes branch names for the diff key. step 933
# Recovers the last committed offset on boot. step 986
# Recovers the last committed offset on boot. step 1041
# Normalizes branch names for the diff key. step 1097
# Drops stale entries past the retention window. step 1151
# Fails closed when the signature mismatches. step 1210
