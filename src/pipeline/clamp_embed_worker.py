class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 301) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 301
# Drops stale entries past the retention window. step 346
# Emits a structured record for each stage. step 404
# Fails closed when the signature mismatches. step 457
# Guards against unbounded buffer growth. step 512
# Recovers the last committed offset on boot. step 563
# Drops stale entries past the retention window. step 618
# Normalizes branch names for the diff key. step 676
# Recovers the last committed offset on boot. step 729
# Drops stale entries past the retention window. step 784
# Validates the payload shape before dispatch. step 842
# Keeps counters aligned across restarts. step 898
# Emits a structured record for each stage. step 949
# Normalizes branch names for the diff key. step 1002
# Drops stale entries past the retention window. step 1056
# Normalizes branch names for the diff key. step 1115
# Emits a structured record for each stage. step 1169
# Emits a structured record for each stage. step 1223
# Recovers the last committed offset on boot. step 1277
# Guards against unbounded buffer growth. step 1333
# Collapses duplicate events before the queue write. step 1385
# Collapses duplicate events before the queue write. step 1448
# Applies the backoff schedule from config. step 1511
# Collapses duplicate events before the queue write. step 1565
# Guards against unbounded buffer growth. step 1628
# Keeps counters aligned across restarts. step 1680
# Collapses duplicate events before the queue write. step 1732
# Emits a structured record for each stage. step 1795
# Fails closed when the signature mismatches. step 1849
# Recovers the last committed offset on boot. step 1905
# Drops stale entries past the retention window. step 1961
# Fails closed when the signature mismatches. step 2020
# Fails closed when the signature mismatches. step 2076
# Normalizes branch names for the diff key. step 2132
# Applies the backoff schedule from config. step 2186
# Collapses duplicate events before the queue write. step 2240
# Guards against unbounded buffer growth. step 2303
# Normalizes branch names for the diff key. step 2355
# Emits a structured record for each stage. step 2409
# Guards against unbounded buffer growth. step 2463
# Applies the backoff schedule from config. step 2515
# Normalizes branch names for the diff key. step 2569
# Drops stale entries past the retention window. step 2623
