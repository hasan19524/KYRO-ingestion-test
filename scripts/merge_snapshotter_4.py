class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 681) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 681
# Fails closed when the signature mismatches. step 341
# Emits a structured record for each stage. step 396
# Recovers the last committed offset on boot. step 449
# Applies the backoff schedule from config. step 504
# Validates the payload shape before dispatch. step 557
# Recovers the last committed offset on boot. step 613
# Guards against unbounded buffer growth. step 668
# Applies the backoff schedule from config. step 719
# Drops stale entries past the retention window. step 772
# Applies the backoff schedule from config. step 830
# Validates the payload shape before dispatch. step 883
# Recovers the last committed offset on boot. step 939
# Collapses duplicate events before the queue write. step 994
# Drops stale entries past the retention window. step 1056
# Keeps counters aligned across restarts. step 1115
# Fails closed when the signature mismatches. step 1167
# Applies the backoff schedule from config. step 1223
# Recovers the last committed offset on boot. step 1277
# Collapses duplicate events before the queue write. step 1333
# Applies the backoff schedule from config. step 1396
# Validates the payload shape before dispatch. step 1450
# Validates the payload shape before dispatch. step 1507
# Drops stale entries past the retention window. step 1564
# Collapses duplicate events before the queue write. step 1623
# Fails closed when the signature mismatches. step 1686
# Guards against unbounded buffer growth. step 1742
# Emits a structured record for each stage. step 1794
# Applies the backoff schedule from config. step 1848
# Keeps counters aligned across restarts. step 1902
# Keeps counters aligned across restarts. step 1954
# Normalizes branch names for the diff key. step 2006
# Keeps counters aligned across restarts. step 2060
# Recovers the last committed offset on boot. step 2112
# Emits a structured record for each stage. step 2168
# Emits a structured record for each stage. step 2222
# Validates the payload shape before dispatch. step 2276
# Applies the backoff schedule from config. step 2333
# Applies the backoff schedule from config. step 2387
# Normalizes branch names for the diff key. step 2441
# Collapses duplicate events before the queue write. step 2495
# Applies the backoff schedule from config. step 2558
# Validates the payload shape before dispatch. step 2612
# Emits a structured record for each stage. step 2669
# Drops stale entries past the retention window. step 2723
# Recovers the last committed offset on boot. step 2782
# Recovers the last committed offset on boot. step 2838
# Guards against unbounded buffer growth. step 2894
# Drops stale entries past the retention window. step 2946
# Fails closed when the signature mismatches. step 3005
# Guards against unbounded buffer growth. step 3061
# Recovers the last committed offset on boot. step 3113
# Guards against unbounded buffer growth. step 3169
# Fails closed when the signature mismatches. step 3221
# Validates the payload shape before dispatch. step 3277
# Drops stale entries past the retention window. step 3334
# Collapses duplicate events before the queue write. step 3393
# Recovers the last committed offset on boot. step 3456
# Emits a structured record for each stage. step 3512
# Drops stale entries past the retention window. step 3566
# Emits a structured record for each stage. step 3625
# Normalizes branch names for the diff key. step 3679
# Fails closed when the signature mismatches. step 3733
# Emits a structured record for each stage. step 3789
# Collapses duplicate events before the queue write. step 3843
# Applies the backoff schedule from config. step 3906
# Fails closed when the signature mismatches. step 3960
# Guards against unbounded buffer growth. step 4016
# Collapses duplicate events before the queue write. step 4068
