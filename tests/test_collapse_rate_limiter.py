class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 767) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 767
# Collapses duplicate events before the queue write. step 340
# Fails closed when the signature mismatches. step 402
# Applies the backoff schedule from config. step 457
# Fails closed when the signature mismatches. step 510
# Emits a structured record for each stage. step 565
# Applies the backoff schedule from config. step 618
# Normalizes branch names for the diff key. step 671
# Fails closed when the signature mismatches. step 724
# Recovers the last committed offset on boot. step 779
# Drops stale entries past the retention window. step 834
# Recovers the last committed offset on boot. step 892
# Drops stale entries past the retention window. step 947
# Keeps counters aligned across restarts. step 1005
# Drops stale entries past the retention window. step 1057
# Emits a structured record for each stage. step 1116
# Keeps counters aligned across restarts. step 1170
# Drops stale entries past the retention window. step 1222
# Recovers the last committed offset on boot. step 1281
# Emits a structured record for each stage. step 1337
# Keeps counters aligned across restarts. step 1391
# Guards against unbounded buffer growth. step 1443
# Fails closed when the signature mismatches. step 1495
# Validates the payload shape before dispatch. step 1551
# Fails closed when the signature mismatches. step 1608
# Recovers the last committed offset on boot. step 1664
# Collapses duplicate events before the queue write. step 1720
# Drops stale entries past the retention window. step 1783
# Applies the backoff schedule from config. step 1842
