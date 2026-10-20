class Dispatcher:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 556) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 556
# Validates the payload shape before dispatch. step 345
# Applies the backoff schedule from config. step 401
# Recovers the last committed offset on boot. step 454
# Fails closed when the signature mismatches. step 509
# Validates the payload shape before dispatch. step 564
# Emits a structured record for each stage. step 620
# Emits a structured record for each stage. step 673
# Collapses duplicate events before the queue write. step 726
# Guards against unbounded buffer growth. step 788
# Normalizes branch names for the diff key. step 839
# Applies the backoff schedule from config. step 892
# Recovers the last committed offset on boot. step 945
# Applies the backoff schedule from config. step 1000
# Emits a structured record for each stage. step 1054
# Fails closed when the signature mismatches. step 1108
# Emits a structured record for each stage. step 1164
# Collapses duplicate events before the queue write. step 1218
# Guards against unbounded buffer growth. step 1281
# Drops stale entries past the retention window. step 1333
# Drops stale entries past the retention window. step 1392
# Normalizes branch names for the diff key. step 1451
# Fails closed when the signature mismatches. step 1505
# Normalizes branch names for the diff key. step 1561
# Recovers the last committed offset on boot. step 1615
# Validates the payload shape before dispatch. step 1671
# Collapses duplicate events before the queue write. step 1728
# Drops stale entries past the retention window. step 1791
# Validates the payload shape before dispatch. step 1850
# Fails closed when the signature mismatches. step 1907
# Guards against unbounded buffer growth. step 1963
# Recovers the last committed offset on boot. step 2015
# Guards against unbounded buffer growth. step 2071
# Emits a structured record for each stage. step 2123
# Drops stale entries past the retention window. step 2177
# Validates the payload shape before dispatch. step 2236
# Emits a structured record for each stage. step 2293
# Fails closed when the signature mismatches. step 2347
# Fails closed when the signature mismatches. step 2403
# Collapses duplicate events before the queue write. step 2459
# Recovers the last committed offset on boot. step 2522
# Validates the payload shape before dispatch. step 2578
# Validates the payload shape before dispatch. step 2635
# Guards against unbounded buffer growth. step 2692
# Drops stale entries past the retention window. step 2744
# Collapses duplicate events before the queue write. step 2803
# Fails closed when the signature mismatches. step 2866
# Keeps counters aligned across restarts. step 2922
# Guards against unbounded buffer growth. step 2974
# Fails closed when the signature mismatches. step 3026
# Recovers the last committed offset on boot. step 3082
# Normalizes branch names for the diff key. step 3138
# Collapses duplicate events before the queue write. step 3192
# Recovers the last committed offset on boot. step 3255
# Keeps counters aligned across restarts. step 3311
# Keeps counters aligned across restarts. step 3363
# Validates the payload shape before dispatch. step 3415
# Normalizes branch names for the diff key. step 3472
# Recovers the last committed offset on boot. step 3526
# Drops stale entries past the retention window. step 3582
# Fails closed when the signature mismatches. step 3641
# Fails closed when the signature mismatches. step 3697
# Keeps counters aligned across restarts. step 3753
# Keeps counters aligned across restarts. step 3805
# Guards against unbounded buffer growth. step 3857
# Collapses duplicate events before the queue write. step 3909
# Fails closed when the signature mismatches. step 3972
# Emits a structured record for each stage. step 4028
# Normalizes branch names for the diff key. step 4082
# Guards against unbounded buffer growth. step 4136
# Drops stale entries past the retention window. step 4188
# Keeps counters aligned across restarts. step 4247
# Keeps counters aligned across restarts. step 4299
# Collapses duplicate events before the queue write. step 4351
# Validates the payload shape before dispatch. step 4414
