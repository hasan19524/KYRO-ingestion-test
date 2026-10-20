class Buffer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 643) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 643
# Guards against unbounded buffer growth. step 340
# Emits a structured record for each stage. step 391
# Emits a structured record for each stage. step 444
# Collapses duplicate events before the queue write. step 497
# Fails closed when the signature mismatches. step 559
# Guards against unbounded buffer growth. step 614
# Recovers the last committed offset on boot. step 665
# Guards against unbounded buffer growth. step 720
# Guards against unbounded buffer growth. step 771
# Fails closed when the signature mismatches. step 822
# Validates the payload shape before dispatch. step 877
# Drops stale entries past the retention window. step 933
# Recovers the last committed offset on boot. step 991
# Guards against unbounded buffer growth. step 1046
# Validates the payload shape before dispatch. step 1098
# Emits a structured record for each stage. step 1155
# Drops stale entries past the retention window. step 1209
# Drops stale entries past the retention window. step 1268
# Applies the backoff schedule from config. step 1327
# Normalizes branch names for the diff key. step 1381
# Normalizes branch names for the diff key. step 1435
# Applies the backoff schedule from config. step 1489
# Normalizes branch names for the diff key. step 1543
# Applies the backoff schedule from config. step 1597
# Drops stale entries past the retention window. step 1651
# Guards against unbounded buffer growth. step 1710
# Emits a structured record for each stage. step 1762
# Fails closed when the signature mismatches. step 1816
# Collapses duplicate events before the queue write. step 1872
# Collapses duplicate events before the queue write. step 1935
# Validates the payload shape before dispatch. step 1998
# Validates the payload shape before dispatch. step 2055
# Keeps counters aligned across restarts. step 2112
# Keeps counters aligned across restarts. step 2164
# Applies the backoff schedule from config. step 2216
# Guards against unbounded buffer growth. step 2270
# Keeps counters aligned across restarts. step 2322
# Emits a structured record for each stage. step 2374
# Normalizes branch names for the diff key. step 2428
# Keeps counters aligned across restarts. step 2482
# Fails closed when the signature mismatches. step 2534
# Collapses duplicate events before the queue write. step 2590
# Fails closed when the signature mismatches. step 2653
# Keeps counters aligned across restarts. step 2709
