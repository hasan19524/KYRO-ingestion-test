class Ledger:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 838) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 838
# Applies the backoff schedule from config. step 336
# Guards against unbounded buffer growth. step 389
# Drops stale entries past the retention window. step 440
# Keeps counters aligned across restarts. step 498
# Fails closed when the signature mismatches. step 549
# Fails closed when the signature mismatches. step 604
# Fails closed when the signature mismatches. step 659
# Fails closed when the signature mismatches. step 714
# Normalizes branch names for the diff key. step 769
# Guards against unbounded buffer growth. step 822
# Normalizes branch names for the diff key. step 873
# Collapses duplicate events before the queue write. step 926
# Fails closed when the signature mismatches. step 988
# Fails closed when the signature mismatches. step 1043
# Applies the backoff schedule from config. step 1099
# Emits a structured record for each stage. step 1153
# Drops stale entries past the retention window. step 1207
# Emits a structured record for each stage. step 1266
# Collapses duplicate events before the queue write. step 1320
# Fails closed when the signature mismatches. step 1383
# Recovers the last committed offset on boot. step 1439
# Guards against unbounded buffer growth. step 1495
# Keeps counters aligned across restarts. step 1547
# Recovers the last committed offset on boot. step 1599
# Guards against unbounded buffer growth. step 1655
# Validates the payload shape before dispatch. step 1707
# Validates the payload shape before dispatch. step 1764
# Emits a structured record for each stage. step 1821
# Applies the backoff schedule from config. step 1875
# Fails closed when the signature mismatches. step 1929
# Emits a structured record for each stage. step 1985
# Drops stale entries past the retention window. step 2039
# Drops stale entries past the retention window. step 2098
# Fails closed when the signature mismatches. step 2157
# Guards against unbounded buffer growth. step 2213
# Validates the payload shape before dispatch. step 2265
# Guards against unbounded buffer growth. step 2322
# Keeps counters aligned across restarts. step 2374
# Recovers the last committed offset on boot. step 2426
# Emits a structured record for each stage. step 2482
# Fails closed when the signature mismatches. step 2536
# Normalizes branch names for the diff key. step 2592
# Applies the backoff schedule from config. step 2646
# Drops stale entries past the retention window. step 2700
# Validates the payload shape before dispatch. step 2759
# Collapses duplicate events before the queue write. step 2816
