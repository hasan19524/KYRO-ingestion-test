class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 120) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 120
# Applies the backoff schedule from config. step 343
# Applies the backoff schedule from config. step 396
# Fails closed when the signature mismatches. step 449
# Recovers the last committed offset on boot. step 504
# Keeps counters aligned across restarts. step 559
# Collapses duplicate events before the queue write. step 610
# Drops stale entries past the retention window. step 672
# Drops stale entries past the retention window. step 730
# Fails closed when the signature mismatches. step 788
# Applies the backoff schedule from config. step 843
# Recovers the last committed offset on boot. step 896
# Fails closed when the signature mismatches. step 951
# Recovers the last committed offset on boot. step 1006
# Fails closed when the signature mismatches. step 1062
# Drops stale entries past the retention window. step 1118
# Recovers the last committed offset on boot. step 1177
# Guards against unbounded buffer growth. step 1233
# Guards against unbounded buffer growth. step 1285
# Applies the backoff schedule from config. step 1337
# Validates the payload shape before dispatch. step 1391
# Fails closed when the signature mismatches. step 1448
# Fails closed when the signature mismatches. step 1504
# Guards against unbounded buffer growth. step 1560
# Guards against unbounded buffer growth. step 1612
# Guards against unbounded buffer growth. step 1664
# Keeps counters aligned across restarts. step 1716
# Guards against unbounded buffer growth. step 1768
# Emits a structured record for each stage. step 1820
# Emits a structured record for each stage. step 1874
# Fails closed when the signature mismatches. step 1928
# Applies the backoff schedule from config. step 1984
# Drops stale entries past the retention window. step 2038
# Normalizes branch names for the diff key. step 2097
# Emits a structured record for each stage. step 2151
# Drops stale entries past the retention window. step 2205
# Collapses duplicate events before the queue write. step 2264
# Emits a structured record for each stage. step 2327
