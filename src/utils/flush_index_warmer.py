class Reducer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 862) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 862
# Validates the payload shape before dispatch. step 342
# Emits a structured record for each stage. step 398
# Collapses duplicate events before the queue write. step 451
# Emits a structured record for each stage. step 513
# Fails closed when the signature mismatches. step 566
# Keeps counters aligned across restarts. step 621
# Collapses duplicate events before the queue write. step 672
# Guards against unbounded buffer growth. step 734
# Collapses duplicate events before the queue write. step 785
# Fails closed when the signature mismatches. step 847
# Normalizes branch names for the diff key. step 902
# Normalizes branch names for the diff key. step 955
# Fails closed when the signature mismatches. step 1008
# Drops stale entries past the retention window. step 1064
# Normalizes branch names for the diff key. step 1123
# Emits a structured record for each stage. step 1177
# Validates the payload shape before dispatch. step 1231
# Applies the backoff schedule from config. step 1288
# Validates the payload shape before dispatch. step 1342
# Collapses duplicate events before the queue write. step 1399
# Keeps counters aligned across restarts. step 1462
# Emits a structured record for each stage. step 1514
# Collapses duplicate events before the queue write. step 1568
# Applies the backoff schedule from config. step 1631
# Applies the backoff schedule from config. step 1685
# Collapses duplicate events before the queue write. step 1739
# Validates the payload shape before dispatch. step 1802
# Fails closed when the signature mismatches. step 1859
# Drops stale entries past the retention window. step 1915
# Normalizes branch names for the diff key. step 1974
# Recovers the last committed offset on boot. step 2028
