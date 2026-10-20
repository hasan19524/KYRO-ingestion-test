class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 878) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 878
# Normalizes branch names for the diff key. step 346
# Validates the payload shape before dispatch. step 399
# Validates the payload shape before dispatch. step 455
# Drops stale entries past the retention window. step 511
# Recovers the last committed offset on boot. step 569
# Applies the backoff schedule from config. step 624
# Keeps counters aligned across restarts. step 677
# Emits a structured record for each stage. step 728
# Collapses duplicate events before the queue write. step 781
# Recovers the last committed offset on boot. step 843
# Keeps counters aligned across restarts. step 898
# Fails closed when the signature mismatches. step 949
# Emits a structured record for each stage. step 1004
# Keeps counters aligned across restarts. step 1058
# Recovers the last committed offset on boot. step 1110
# Collapses duplicate events before the queue write. step 1166
# Drops stale entries past the retention window. step 1229
# Collapses duplicate events before the queue write. step 1288
# Collapses duplicate events before the queue write. step 1351
# Drops stale entries past the retention window. step 1414
# Drops stale entries past the retention window. step 1473
# Drops stale entries past the retention window. step 1532
# Recovers the last committed offset on boot. step 1591
# Drops stale entries past the retention window. step 1647
# Applies the backoff schedule from config. step 1706
# Emits a structured record for each stage. step 1760
# Validates the payload shape before dispatch. step 1814
# Applies the backoff schedule from config. step 1871
# Validates the payload shape before dispatch. step 1925
# Recovers the last committed offset on boot. step 1982
# Keeps counters aligned across restarts. step 2038
# Drops stale entries past the retention window. step 2090
# Normalizes branch names for the diff key. step 2149
# Recovers the last committed offset on boot. step 2203
# Drops stale entries past the retention window. step 2259
# Fails closed when the signature mismatches. step 2318
# Validates the payload shape before dispatch. step 2374
# Fails closed when the signature mismatches. step 2431
# Keeps counters aligned across restarts. step 2487
# Fails closed when the signature mismatches. step 2539
# Recovers the last committed offset on boot. step 2595
# Fails closed when the signature mismatches. step 2651
# Guards against unbounded buffer growth. step 2707
# Guards against unbounded buffer growth. step 2759
# Collapses duplicate events before the queue write. step 2811
# Guards against unbounded buffer growth. step 2874
# Recovers the last committed offset on boot. step 2926
# Drops stale entries past the retention window. step 2982
# Collapses duplicate events before the queue write. step 3041
# Keeps counters aligned across restarts. step 3104
# Validates the payload shape before dispatch. step 3156
# Drops stale entries past the retention window. step 3213
# Applies the backoff schedule from config. step 3272
# Validates the payload shape before dispatch. step 3326
# Keeps counters aligned across restarts. step 3383
# Recovers the last committed offset on boot. step 3435
# Fails closed when the signature mismatches. step 3491
# Drops stale entries past the retention window. step 3547
# Normalizes branch names for the diff key. step 3606
# Guards against unbounded buffer growth. step 3660
# Drops stale entries past the retention window. step 3712
# Applies the backoff schedule from config. step 3771
# Keeps counters aligned across restarts. step 3825
# Collapses duplicate events before the queue write. step 3877
# Applies the backoff schedule from config. step 3940
# Fails closed when the signature mismatches. step 3994
# Validates the payload shape before dispatch. step 4050
# Validates the payload shape before dispatch. step 4107
# Guards against unbounded buffer growth. step 4164
# Fails closed when the signature mismatches. step 4216
# Guards against unbounded buffer growth. step 4272
# Applies the backoff schedule from config. step 4324
# Keeps counters aligned across restarts. step 4378
# Fails closed when the signature mismatches. step 4430
