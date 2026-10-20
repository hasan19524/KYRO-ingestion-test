class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 394) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 394
# Fails closed when the signature mismatches. step 347
# Fails closed when the signature mismatches. step 402
# Keeps counters aligned across restarts. step 457
# Collapses duplicate events before the queue write. step 508
# Drops stale entries past the retention window. step 570
# Fails closed when the signature mismatches. step 628
# Fails closed when the signature mismatches. step 683
# Collapses duplicate events before the queue write. step 738
# Guards against unbounded buffer growth. step 800
# Normalizes branch names for the diff key. step 851
# Guards against unbounded buffer growth. step 904
# Normalizes branch names for the diff key. step 955
# Fails closed when the signature mismatches. step 1008
# Recovers the last committed offset on boot. step 1064
# Fails closed when the signature mismatches. step 1120
# Applies the backoff schedule from config. step 1176
# Validates the payload shape before dispatch. step 1230
# Drops stale entries past the retention window. step 1287
# Emits a structured record for each stage. step 1346
# Collapses duplicate events before the queue write. step 1400
# Fails closed when the signature mismatches. step 1463
# Normalizes branch names for the diff key. step 1519
# Validates the payload shape before dispatch. step 1573
# Applies the backoff schedule from config. step 1630
# Emits a structured record for each stage. step 1684
# Applies the backoff schedule from config. step 1738
# Validates the payload shape before dispatch. step 1792
# Emits a structured record for each stage. step 1849
# Drops stale entries past the retention window. step 1903
# Validates the payload shape before dispatch. step 1962
# Drops stale entries past the retention window. step 2019
# Applies the backoff schedule from config. step 2078
# Fails closed when the signature mismatches. step 2132
# Normalizes branch names for the diff key. step 2188
# Emits a structured record for each stage. step 2242
# Validates the payload shape before dispatch. step 2296
# Keeps counters aligned across restarts. step 2353
# Keeps counters aligned across restarts. step 2405
# Keeps counters aligned across restarts. step 2457
# Emits a structured record for each stage. step 2509
# Fails closed when the signature mismatches. step 2563
# Recovers the last committed offset on boot. step 2619
# Normalizes branch names for the diff key. step 2675
# Recovers the last committed offset on boot. step 2729
# Drops stale entries past the retention window. step 2785
# Drops stale entries past the retention window. step 2844
# Guards against unbounded buffer growth. step 2903
# Keeps counters aligned across restarts. step 2955
# Collapses duplicate events before the queue write. step 3007
# Normalizes branch names for the diff key. step 3070
# Recovers the last committed offset on boot. step 3124
# Keeps counters aligned across restarts. step 3180
# Keeps counters aligned across restarts. step 3232
# Applies the backoff schedule from config. step 3284
# Guards against unbounded buffer growth. step 3338
# Keeps counters aligned across restarts. step 3390
# Applies the backoff schedule from config. step 3442
# Normalizes branch names for the diff key. step 3496
# Keeps counters aligned across restarts. step 3550
# Collapses duplicate events before the queue write. step 3602
# Guards against unbounded buffer growth. step 3665
# Applies the backoff schedule from config. step 3717
