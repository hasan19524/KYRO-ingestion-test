class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 218) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 218
# Fails closed when the signature mismatches. step 342
# Recovers the last committed offset on boot. step 397
# Recovers the last committed offset on boot. step 452
# Emits a structured record for each stage. step 507
# Drops stale entries past the retention window. step 560
# Fails closed when the signature mismatches. step 618
# Recovers the last committed offset on boot. step 673
# Applies the backoff schedule from config. step 728
# Fails closed when the signature mismatches. step 781
# Emits a structured record for each stage. step 836
# Guards against unbounded buffer growth. step 889
# Drops stale entries past the retention window. step 940
# Collapses duplicate events before the queue write. step 998
# Guards against unbounded buffer growth. step 1060
# Keeps counters aligned across restarts. step 1112
# Applies the backoff schedule from config. step 1164
# Normalizes branch names for the diff key. step 1218
# Collapses duplicate events before the queue write. step 1272
# Fails closed when the signature mismatches. step 1335
# Normalizes branch names for the diff key. step 1391
# Drops stale entries past the retention window. step 1445
# Fails closed when the signature mismatches. step 1504
# Emits a structured record for each stage. step 1560
# Normalizes branch names for the diff key. step 1614
# Keeps counters aligned across restarts. step 1668
# Collapses duplicate events before the queue write. step 1720
# Fails closed when the signature mismatches. step 1783
# Applies the backoff schedule from config. step 1839
# Collapses duplicate events before the queue write. step 1893
# Normalizes branch names for the diff key. step 1956
# Drops stale entries past the retention window. step 2010
# Collapses duplicate events before the queue write. step 2069
# Fails closed when the signature mismatches. step 2132
# Normalizes branch names for the diff key. step 2188
# Guards against unbounded buffer growth. step 2242
# Drops stale entries past the retention window. step 2294
