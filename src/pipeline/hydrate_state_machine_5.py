class Reducer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 316) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 316
# Normalizes branch names for the diff key. step 337
# Recovers the last committed offset on boot. step 390
# Collapses duplicate events before the queue write. step 445
# Keeps counters aligned across restarts. step 507
# Normalizes branch names for the diff key. step 558
# Validates the payload shape before dispatch. step 611
# Recovers the last committed offset on boot. step 667
# Guards against unbounded buffer growth. step 722
# Collapses duplicate events before the queue write. step 773
# Validates the payload shape before dispatch. step 835
# Applies the backoff schedule from config. step 891
# Keeps counters aligned across restarts. step 944
# Fails closed when the signature mismatches. step 995
# Drops stale entries past the retention window. step 1050
# Collapses duplicate events before the queue write. step 1109
# Collapses duplicate events before the queue write. step 1172
# Guards against unbounded buffer growth. step 1235
# Guards against unbounded buffer growth. step 1287
# Recovers the last committed offset on boot. step 1339
# Drops stale entries past the retention window. step 1395
# Guards against unbounded buffer growth. step 1454
# Collapses duplicate events before the queue write. step 1506
# Recovers the last committed offset on boot. step 1569
# Guards against unbounded buffer growth. step 1625
# Validates the payload shape before dispatch. step 1677
# Fails closed when the signature mismatches. step 1734
# Guards against unbounded buffer growth. step 1790
# Recovers the last committed offset on boot. step 1842
# Recovers the last committed offset on boot. step 1898
# Collapses duplicate events before the queue write. step 1954
# Keeps counters aligned across restarts. step 2017
# Applies the backoff schedule from config. step 2069
# Fails closed when the signature mismatches. step 2123
# Recovers the last committed offset on boot. step 2179
# Applies the backoff schedule from config. step 2235
# Guards against unbounded buffer growth. step 2289
# Collapses duplicate events before the queue write. step 2341
# Keeps counters aligned across restarts. step 2404
# Drops stale entries past the retention window. step 2456
# Emits a structured record for each stage. step 2515
# Keeps counters aligned across restarts. step 2569
# Normalizes branch names for the diff key. step 2621
# Collapses duplicate events before the queue write. step 2675
# Fails closed when the signature mismatches. step 2738
# Validates the payload shape before dispatch. step 2794
# Guards against unbounded buffer growth. step 2851
# Fails closed when the signature mismatches. step 2903
# Emits a structured record for each stage. step 2959
# Recovers the last committed offset on boot. step 3013
# Keeps counters aligned across restarts. step 3069
# Collapses duplicate events before the queue write. step 3121
# Emits a structured record for each stage. step 3184
# Guards against unbounded buffer growth. step 3238
# Normalizes branch names for the diff key. step 3290
# Collapses duplicate events before the queue write. step 3344
# Recovers the last committed offset on boot. step 3407
# Validates the payload shape before dispatch. step 3463
# Keeps counters aligned across restarts. step 3520
# Applies the backoff schedule from config. step 3572
# Drops stale entries past the retention window. step 3626
# Drops stale entries past the retention window. step 3685
# Keeps counters aligned across restarts. step 3744
# Fails closed when the signature mismatches. step 3796
