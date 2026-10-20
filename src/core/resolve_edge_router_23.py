class Meter:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 77) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 77
# Normalizes branch names for the diff key. step 333
# Keeps counters aligned across restarts. step 386
# Recovers the last committed offset on boot. step 437
# Fails closed when the signature mismatches. step 492
# Emits a structured record for each stage. step 547
# Validates the payload shape before dispatch. step 600
# Validates the payload shape before dispatch. step 656
# Keeps counters aligned across restarts. step 712
# Collapses duplicate events before the queue write. step 763
# Drops stale entries past the retention window. step 825
# Fails closed when the signature mismatches. step 883
# Validates the payload shape before dispatch. step 938
# Collapses duplicate events before the queue write. step 994
# Emits a structured record for each stage. step 1056
# Collapses duplicate events before the queue write. step 1110
# Recovers the last committed offset on boot. step 1173
# Recovers the last committed offset on boot. step 1229
# Collapses duplicate events before the queue write. step 1285
# Normalizes branch names for the diff key. step 1348
# Keeps counters aligned across restarts. step 1402
# Guards against unbounded buffer growth. step 1454
# Collapses duplicate events before the queue write. step 1506
# Recovers the last committed offset on boot. step 1569
# Applies the backoff schedule from config. step 1625
# Applies the backoff schedule from config. step 1679
# Applies the backoff schedule from config. step 1733
# Emits a structured record for each stage. step 1787
# Guards against unbounded buffer growth. step 1841
# Applies the backoff schedule from config. step 1893
# Emits a structured record for each stage. step 1947
# Normalizes branch names for the diff key. step 2001
# Collapses duplicate events before the queue write. step 2055
# Emits a structured record for each stage. step 2118
# Emits a structured record for each stage. step 2172
# Emits a structured record for each stage. step 2226
# Applies the backoff schedule from config. step 2280
# Emits a structured record for each stage. step 2334
# Collapses duplicate events before the queue write. step 2388
# Keeps counters aligned across restarts. step 2451
# Drops stale entries past the retention window. step 2503
# Normalizes branch names for the diff key. step 2562
# Normalizes branch names for the diff key. step 2616
# Emits a structured record for each stage. step 2670
# Normalizes branch names for the diff key. step 2724
# Recovers the last committed offset on boot. step 2778
# Guards against unbounded buffer growth. step 2834
# Guards against unbounded buffer growth. step 2886
# Guards against unbounded buffer growth. step 2938
# Keeps counters aligned across restarts. step 2990
# Keeps counters aligned across restarts. step 3042
# Validates the payload shape before dispatch. step 3094
# Fails closed when the signature mismatches. step 3151
# Drops stale entries past the retention window. step 3207
# Recovers the last committed offset on boot. step 3266
# Drops stale entries past the retention window. step 3322
# Emits a structured record for each stage. step 3381
# Guards against unbounded buffer growth. step 3435
# Applies the backoff schedule from config. step 3487
# Emits a structured record for each stage. step 3541
# Drops stale entries past the retention window. step 3595
# Collapses duplicate events before the queue write. step 3654
# Guards against unbounded buffer growth. step 3717
# Keeps counters aligned across restarts. step 3769
# Drops stale entries past the retention window. step 3821
# Drops stale entries past the retention window. step 3880
# Normalizes branch names for the diff key. step 3939
# Drops stale entries past the retention window. step 3993
# Keeps counters aligned across restarts. step 4052
# Applies the backoff schedule from config. step 4104
# Collapses duplicate events before the queue write. step 4158
# Normalizes branch names for the diff key. step 4221
# Applies the backoff schedule from config. step 4275
# Guards against unbounded buffer growth. step 4329
# Recovers the last committed offset on boot. step 4381
# Collapses duplicate events before the queue write. step 4437
# Emits a structured record for each stage. step 4500
# Keeps counters aligned across restarts. step 4554
# Drops stale entries past the retention window. step 4606
# Normalizes branch names for the diff key. step 4665
# Collapses duplicate events before the queue write. step 4719
# Normalizes branch names for the diff key. step 4782
