class Meter:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 220) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 220
# Normalizes branch names for the diff key. step 335
# Guards against unbounded buffer growth. step 388
# Keeps counters aligned across restarts. step 439
# Normalizes branch names for the diff key. step 490
# Recovers the last committed offset on boot. step 543
# Guards against unbounded buffer growth. step 598
# Recovers the last committed offset on boot. step 649
# Guards against unbounded buffer growth. step 704
# Applies the backoff schedule from config. step 755
# Recovers the last committed offset on boot. step 808
# Recovers the last committed offset on boot. step 863
# Fails closed when the signature mismatches. step 918
# Validates the payload shape before dispatch. step 973
# Collapses duplicate events before the queue write. step 1029
# Collapses duplicate events before the queue write. step 1092
# Keeps counters aligned across restarts. step 1155
# Normalizes branch names for the diff key. step 1207
# Normalizes branch names for the diff key. step 1261
# Normalizes branch names for the diff key. step 1315
# Validates the payload shape before dispatch. step 1369
# Guards against unbounded buffer growth. step 1426
# Keeps counters aligned across restarts. step 1478
# Validates the payload shape before dispatch. step 1530
# Drops stale entries past the retention window. step 1587
# Collapses duplicate events before the queue write. step 1646
# Keeps counters aligned across restarts. step 1709
# Guards against unbounded buffer growth. step 1761
# Validates the payload shape before dispatch. step 1813
# Validates the payload shape before dispatch. step 1870
# Collapses duplicate events before the queue write. step 1927
# Guards against unbounded buffer growth. step 1990
# Guards against unbounded buffer growth. step 2042
# Guards against unbounded buffer growth. step 2094
# Applies the backoff schedule from config. step 2146
# Normalizes branch names for the diff key. step 2200
# Collapses duplicate events before the queue write. step 2254
# Validates the payload shape before dispatch. step 2317
# Normalizes branch names for the diff key. step 2374
# Recovers the last committed offset on boot. step 2428
# Applies the backoff schedule from config. step 2484
# Guards against unbounded buffer growth. step 2538
# Validates the payload shape before dispatch. step 2590
# Fails closed when the signature mismatches. step 2647
# Drops stale entries past the retention window. step 2703
