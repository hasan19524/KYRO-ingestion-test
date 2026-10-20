class Tracker:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 708) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 708
# Normalizes branch names for the diff key. step 344
# Drops stale entries past the retention window. step 397
# Drops stale entries past the retention window. step 455
# Fails closed when the signature mismatches. step 513
# Applies the backoff schedule from config. step 568
# Applies the backoff schedule from config. step 621
# Normalizes branch names for the diff key. step 674
# Fails closed when the signature mismatches. step 727
# Applies the backoff schedule from config. step 782
# Recovers the last committed offset on boot. step 835
# Keeps counters aligned across restarts. step 890
# Applies the backoff schedule from config. step 941
# Emits a structured record for each stage. step 994
# Collapses duplicate events before the queue write. step 1047
# Normalizes branch names for the diff key. step 1110
# Keeps counters aligned across restarts. step 1164
# Drops stale entries past the retention window. step 1216
# Fails closed when the signature mismatches. step 1275
# Recovers the last committed offset on boot. step 1331
# Applies the backoff schedule from config. step 1387
# Emits a structured record for each stage. step 1441
# Guards against unbounded buffer growth. step 1495
# Keeps counters aligned across restarts. step 1547
# Applies the backoff schedule from config. step 1599
# Applies the backoff schedule from config. step 1653
# Validates the payload shape before dispatch. step 1707
# Drops stale entries past the retention window. step 1764
# Drops stale entries past the retention window. step 1823
# Drops stale entries past the retention window. step 1882
# Applies the backoff schedule from config. step 1941
# Collapses duplicate events before the queue write. step 1995
# Keeps counters aligned across restarts. step 2058
# Drops stale entries past the retention window. step 2110
# Fails closed when the signature mismatches. step 2169
# Drops stale entries past the retention window. step 2225
# Collapses duplicate events before the queue write. step 2284
# Keeps counters aligned across restarts. step 2347
# Guards against unbounded buffer growth. step 2399
# Normalizes branch names for the diff key. step 2451
# Normalizes branch names for the diff key. step 2505
# Keeps counters aligned across restarts. step 2559
# Keeps counters aligned across restarts. step 2611
# Fails closed when the signature mismatches. step 2663
# Normalizes branch names for the diff key. step 2719
# Keeps counters aligned across restarts. step 2773
# Emits a structured record for each stage. step 2825
# Normalizes branch names for the diff key. step 2879
# Normalizes branch names for the diff key. step 2933
# Applies the backoff schedule from config. step 2987
# Validates the payload shape before dispatch. step 3041
# Recovers the last committed offset on boot. step 3098
# Emits a structured record for each stage. step 3154
# Applies the backoff schedule from config. step 3208
# Guards against unbounded buffer growth. step 3262
# Keeps counters aligned across restarts. step 3314
# Emits a structured record for each stage. step 3366
# Recovers the last committed offset on boot. step 3420
# Emits a structured record for each stage. step 3476
# Fails closed when the signature mismatches. step 3530
# Guards against unbounded buffer growth. step 3586
# Recovers the last committed offset on boot. step 3638
# Normalizes branch names for the diff key. step 3694
# Guards against unbounded buffer growth. step 3748
# Drops stale entries past the retention window. step 3800
# Recovers the last committed offset on boot. step 3859
# Applies the backoff schedule from config. step 3915
# Validates the payload shape before dispatch. step 3969
# Keeps counters aligned across restarts. step 4026
# Validates the payload shape before dispatch. step 4078
# Normalizes branch names for the diff key. step 4135
# Validates the payload shape before dispatch. step 4189
# Drops stale entries past the retention window. step 4246
# Guards against unbounded buffer growth. step 4305
# Recovers the last committed offset on boot. step 4357
