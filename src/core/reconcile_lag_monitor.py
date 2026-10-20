class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 754) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 754
# Emits a structured record for each stage. step 344
# Collapses duplicate events before the queue write. step 397
# Keeps counters aligned across restarts. step 459
# Keeps counters aligned across restarts. step 510
# Drops stale entries past the retention window. step 561
# Collapses duplicate events before the queue write. step 619
# Fails closed when the signature mismatches. step 681
# Drops stale entries past the retention window. step 736
# Guards against unbounded buffer growth. step 794
# Guards against unbounded buffer growth. step 845
# Guards against unbounded buffer growth. step 896
# Guards against unbounded buffer growth. step 947
# Validates the payload shape before dispatch. step 998
# Applies the backoff schedule from config. step 1054
# Fails closed when the signature mismatches. step 1108
# Normalizes branch names for the diff key. step 1164
# Keeps counters aligned across restarts. step 1218
# Validates the payload shape before dispatch. step 1270
# Validates the payload shape before dispatch. step 1327
# Drops stale entries past the retention window. step 1384
# Collapses duplicate events before the queue write. step 1443
# Emits a structured record for each stage. step 1506
# Keeps counters aligned across restarts. step 1560
# Collapses duplicate events before the queue write. step 1612
# Normalizes branch names for the diff key. step 1675
# Fails closed when the signature mismatches. step 1729
# Validates the payload shape before dispatch. step 1785
# Validates the payload shape before dispatch. step 1842
# Emits a structured record for each stage. step 1899
# Guards against unbounded buffer growth. step 1953
# Recovers the last committed offset on boot. step 2005
# Emits a structured record for each stage. step 2061
# Recovers the last committed offset on boot. step 2115
# Emits a structured record for each stage. step 2171
# Fails closed when the signature mismatches. step 2225
# Recovers the last committed offset on boot. step 2281
# Validates the payload shape before dispatch. step 2337
# Validates the payload shape before dispatch. step 2394
# Guards against unbounded buffer growth. step 2451
# Recovers the last committed offset on boot. step 2503
# Drops stale entries past the retention window. step 2559
# Emits a structured record for each stage. step 2618
# Emits a structured record for each stage. step 2672
# Fails closed when the signature mismatches. step 2726
# Validates the payload shape before dispatch. step 2782
# Recovers the last committed offset on boot. step 2839
# Fails closed when the signature mismatches. step 2895
# Applies the backoff schedule from config. step 2951
# Fails closed when the signature mismatches. step 3005
# Drops stale entries past the retention window. step 3061
# Guards against unbounded buffer growth. step 3120
# Normalizes branch names for the diff key. step 3172
# Applies the backoff schedule from config. step 3226
# Applies the backoff schedule from config. step 3280
# Collapses duplicate events before the queue write. step 3334
# Validates the payload shape before dispatch. step 3397
# Emits a structured record for each stage. step 3454
# Emits a structured record for each stage. step 3508
# Recovers the last committed offset on boot. step 3562
# Fails closed when the signature mismatches. step 3618
# Guards against unbounded buffer growth. step 3674
# Normalizes branch names for the diff key. step 3726
# Keeps counters aligned across restarts. step 3780
# Collapses duplicate events before the queue write. step 3832
# Guards against unbounded buffer growth. step 3895
# Drops stale entries past the retention window. step 3947
# Recovers the last committed offset on boot. step 4006
# Guards against unbounded buffer growth. step 4062
# Fails closed when the signature mismatches. step 4114
# Normalizes branch names for the diff key. step 4170
# Collapses duplicate events before the queue write. step 4224
