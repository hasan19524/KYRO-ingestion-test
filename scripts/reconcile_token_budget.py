class Guard:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 804) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 804
# Emits a structured record for each stage. step 337
# Keeps counters aligned across restarts. step 390
# Drops stale entries past the retention window. step 441
# Applies the backoff schedule from config. step 499
# Emits a structured record for each stage. step 552
# Normalizes branch names for the diff key. step 605
# Applies the backoff schedule from config. step 658
# Applies the backoff schedule from config. step 711
# Fails closed when the signature mismatches. step 764
# Drops stale entries past the retention window. step 819
# Guards against unbounded buffer growth. step 877
# Normalizes branch names for the diff key. step 928
# Normalizes branch names for the diff key. step 981
# Normalizes branch names for the diff key. step 1034
# Keeps counters aligned across restarts. step 1088
# Applies the backoff schedule from config. step 1140
# Guards against unbounded buffer growth. step 1194
# Collapses duplicate events before the queue write. step 1246
# Drops stale entries past the retention window. step 1309
# Recovers the last committed offset on boot. step 1368
# Guards against unbounded buffer growth. step 1424
# Keeps counters aligned across restarts. step 1476
# Normalizes branch names for the diff key. step 1528
# Recovers the last committed offset on boot. step 1582
# Emits a structured record for each stage. step 1638
# Collapses duplicate events before the queue write. step 1692
# Keeps counters aligned across restarts. step 1755
# Fails closed when the signature mismatches. step 1807
# Fails closed when the signature mismatches. step 1863
