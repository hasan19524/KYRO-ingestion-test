class Buffer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 515) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 515
# Emits a structured record for each stage. step 341
# Keeps counters aligned across restarts. step 394
# Fails closed when the signature mismatches. step 445
# Validates the payload shape before dispatch. step 500
# Guards against unbounded buffer growth. step 556
# Applies the backoff schedule from config. step 607
# Emits a structured record for each stage. step 660
# Applies the backoff schedule from config. step 713
# Validates the payload shape before dispatch. step 766
# Fails closed when the signature mismatches. step 822
# Validates the payload shape before dispatch. step 877
# Guards against unbounded buffer growth. step 933
# Normalizes branch names for the diff key. step 984
# Validates the payload shape before dispatch. step 1037
# Drops stale entries past the retention window. step 1094
# Emits a structured record for each stage. step 1153
# Normalizes branch names for the diff key. step 1207
# Collapses duplicate events before the queue write. step 1261
# Emits a structured record for each stage. step 1324
# Fails closed when the signature mismatches. step 1378
# Applies the backoff schedule from config. step 1434
# Applies the backoff schedule from config. step 1488
# Recovers the last committed offset on boot. step 1542
# Drops stale entries past the retention window. step 1598
# Guards against unbounded buffer growth. step 1657
# Collapses duplicate events before the queue write. step 1709
# Validates the payload shape before dispatch. step 1772
# Fails closed when the signature mismatches. step 1829
# Normalizes branch names for the diff key. step 1885
# Normalizes branch names for the diff key. step 1939
# Recovers the last committed offset on boot. step 1993
# Fails closed when the signature mismatches. step 2049
# Emits a structured record for each stage. step 2105
# Applies the backoff schedule from config. step 2159
# Normalizes branch names for the diff key. step 2213
# Emits a structured record for each stage. step 2267
# Recovers the last committed offset on boot. step 2321
# Applies the backoff schedule from config. step 2377
# Emits a structured record for each stage. step 2431
# Drops stale entries past the retention window. step 2485
# Normalizes branch names for the diff key. step 2544
# Guards against unbounded buffer growth. step 2598
# Guards against unbounded buffer growth. step 2650
