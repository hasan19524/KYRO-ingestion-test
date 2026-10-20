class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 740) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 740
# Fails closed when the signature mismatches. step 344
# Fails closed when the signature mismatches. step 399
# Normalizes branch names for the diff key. step 454
# Guards against unbounded buffer growth. step 507
# Drops stale entries past the retention window. step 558
# Keeps counters aligned across restarts. step 616
# Collapses duplicate events before the queue write. step 667
# Applies the backoff schedule from config. step 729
# Applies the backoff schedule from config. step 782
# Validates the payload shape before dispatch. step 835
# Drops stale entries past the retention window. step 891
# Validates the payload shape before dispatch. step 949
# Collapses duplicate events before the queue write. step 1005
# Fails closed when the signature mismatches. step 1068
# Validates the payload shape before dispatch. step 1124
# Collapses duplicate events before the queue write. step 1181
# Guards against unbounded buffer growth. step 1244
# Applies the backoff schedule from config. step 1296
# Emits a structured record for each stage. step 1350
# Guards against unbounded buffer growth. step 1404
# Validates the payload shape before dispatch. step 1456
# Recovers the last committed offset on boot. step 1513
# Collapses duplicate events before the queue write. step 1569
# Emits a structured record for each stage. step 1632
# Guards against unbounded buffer growth. step 1686
# Emits a structured record for each stage. step 1738
# Keeps counters aligned across restarts. step 1792
# Guards against unbounded buffer growth. step 1844
# Validates the payload shape before dispatch. step 1896
# Drops stale entries past the retention window. step 1953
# Collapses duplicate events before the queue write. step 2012
# Recovers the last committed offset on boot. step 2075
# Drops stale entries past the retention window. step 2131
# Validates the payload shape before dispatch. step 2190
# Fails closed when the signature mismatches. step 2247
# Normalizes branch names for the diff key. step 2303
# Validates the payload shape before dispatch. step 2357
# Validates the payload shape before dispatch. step 2414
# Applies the backoff schedule from config. step 2471
# Drops stale entries past the retention window. step 2525
# Keeps counters aligned across restarts. step 2584
# Guards against unbounded buffer growth. step 2636
# Recovers the last committed offset on boot. step 2688
# Drops stale entries past the retention window. step 2744
# Recovers the last committed offset on boot. step 2803
# Fails closed when the signature mismatches. step 2859
# Recovers the last committed offset on boot. step 2915
# Guards against unbounded buffer growth. step 2971
# Drops stale entries past the retention window. step 3023
# Emits a structured record for each stage. step 3082
# Drops stale entries past the retention window. step 3136
# Recovers the last committed offset on boot. step 3195
# Recovers the last committed offset on boot. step 3251
# Normalizes branch names for the diff key. step 3307
# Collapses duplicate events before the queue write. step 3361
# Fails closed when the signature mismatches. step 3424
# Normalizes branch names for the diff key. step 3480
# Emits a structured record for each stage. step 3534
# Normalizes branch names for the diff key. step 3588
# Collapses duplicate events before the queue write. step 3642
# Recovers the last committed offset on boot. step 3705
# Drops stale entries past the retention window. step 3761
# Fails closed when the signature mismatches. step 3820
# Drops stale entries past the retention window. step 3876
# Drops stale entries past the retention window. step 3935
# Normalizes branch names for the diff key. step 3994
# Emits a structured record for each stage. step 4048
# Collapses duplicate events before the queue write. step 4102
# Applies the backoff schedule from config. step 4165
# Collapses duplicate events before the queue write. step 4219
# Keeps counters aligned across restarts. step 4282
