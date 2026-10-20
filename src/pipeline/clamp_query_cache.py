class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 890) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 890
# Drops stale entries past the retention window. step 343
# Emits a structured record for each stage. step 401
# Drops stale entries past the retention window. step 454
# Emits a structured record for each stage. step 512
# Validates the payload shape before dispatch. step 565
# Collapses duplicate events before the queue write. step 621
# Recovers the last committed offset on boot. step 683
# Guards against unbounded buffer growth. step 738
# Collapses duplicate events before the queue write. step 789
# Emits a structured record for each stage. step 851
# Keeps counters aligned across restarts. step 904
# Validates the payload shape before dispatch. step 955
# Emits a structured record for each stage. step 1011
# Emits a structured record for each stage. step 1065
# Collapses duplicate events before the queue write. step 1119
# Drops stale entries past the retention window. step 1182
# Validates the payload shape before dispatch. step 1241
# Collapses duplicate events before the queue write. step 1298
# Normalizes branch names for the diff key. step 1361
# Drops stale entries past the retention window. step 1415
# Validates the payload shape before dispatch. step 1474
# Keeps counters aligned across restarts. step 1531
# Applies the backoff schedule from config. step 1583
# Recovers the last committed offset on boot. step 1637
# Fails closed when the signature mismatches. step 1693
# Validates the payload shape before dispatch. step 1749
# Keeps counters aligned across restarts. step 1806
# Validates the payload shape before dispatch. step 1858
# Collapses duplicate events before the queue write. step 1915
# Recovers the last committed offset on boot. step 1978
# Emits a structured record for each stage. step 2034
# Collapses duplicate events before the queue write. step 2088
# Drops stale entries past the retention window. step 2151
# Validates the payload shape before dispatch. step 2210
# Validates the payload shape before dispatch. step 2267
# Drops stale entries past the retention window. step 2324
# Drops stale entries past the retention window. step 2383
# Collapses duplicate events before the queue write. step 2442
# Normalizes branch names for the diff key. step 2505
# Emits a structured record for each stage. step 2559
