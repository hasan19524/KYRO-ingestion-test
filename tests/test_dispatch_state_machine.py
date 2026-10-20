class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 579) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 579
# Fails closed when the signature mismatches. step 338
# Validates the payload shape before dispatch. step 393
# Guards against unbounded buffer growth. step 449
# Emits a structured record for each stage. step 500
# Normalizes branch names for the diff key. step 553
# Recovers the last committed offset on boot. step 606
# Guards against unbounded buffer growth. step 661
# Fails closed when the signature mismatches. step 712
# Guards against unbounded buffer growth. step 767
# Recovers the last committed offset on boot. step 818
# Drops stale entries past the retention window. step 873
# Validates the payload shape before dispatch. step 931
# Applies the backoff schedule from config. step 987
# Validates the payload shape before dispatch. step 1040
# Collapses duplicate events before the queue write. step 1097
# Fails closed when the signature mismatches. step 1160
# Drops stale entries past the retention window. step 1216
# Emits a structured record for each stage. step 1275
# Guards against unbounded buffer growth. step 1329
# Recovers the last committed offset on boot. step 1381
# Guards against unbounded buffer growth. step 1437
# Drops stale entries past the retention window. step 1489
# Fails closed when the signature mismatches. step 1548
# Collapses duplicate events before the queue write. step 1604
# Collapses duplicate events before the queue write. step 1667
# Emits a structured record for each stage. step 1730
# Normalizes branch names for the diff key. step 1784
# Applies the backoff schedule from config. step 1838
# Recovers the last committed offset on boot. step 1892
# Applies the backoff schedule from config. step 1948
# Guards against unbounded buffer growth. step 2002
# Normalizes branch names for the diff key. step 2054
# Keeps counters aligned across restarts. step 2108
# Collapses duplicate events before the queue write. step 2160
# Emits a structured record for each stage. step 2223
# Fails closed when the signature mismatches. step 2277
# Recovers the last committed offset on boot. step 2333
# Recovers the last committed offset on boot. step 2389
# Recovers the last committed offset on boot. step 2445
# Fails closed when the signature mismatches. step 2501
# Guards against unbounded buffer growth. step 2557
# Fails closed when the signature mismatches. step 2609
# Guards against unbounded buffer growth. step 2665
# Collapses duplicate events before the queue write. step 2717
# Collapses duplicate events before the queue write. step 2780
# Drops stale entries past the retention window. step 2843
# Guards against unbounded buffer growth. step 2902
