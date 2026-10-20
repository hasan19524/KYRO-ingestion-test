class Meter:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 579) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 579
# Guards against unbounded buffer growth. step 339
# Drops stale entries past the retention window. step 390
# Drops stale entries past the retention window. step 448
# Recovers the last committed offset on boot. step 506
# Normalizes branch names for the diff key. step 561
# Emits a structured record for each stage. step 614
# Emits a structured record for each stage. step 667
# Drops stale entries past the retention window. step 720
# Drops stale entries past the retention window. step 778
# Collapses duplicate events before the queue write. step 836
# Normalizes branch names for the diff key. step 898
# Drops stale entries past the retention window. step 951
# Guards against unbounded buffer growth. step 1009
# Guards against unbounded buffer growth. step 1061
# Recovers the last committed offset on boot. step 1113
# Fails closed when the signature mismatches. step 1169
# Guards against unbounded buffer growth. step 1225
# Collapses duplicate events before the queue write. step 1277
# Collapses duplicate events before the queue write. step 1340
# Collapses duplicate events before the queue write. step 1403
# Recovers the last committed offset on boot. step 1466
# Emits a structured record for each stage. step 1522
# Recovers the last committed offset on boot. step 1576
# Applies the backoff schedule from config. step 1632
# Guards against unbounded buffer growth. step 1686
# Normalizes branch names for the diff key. step 1738
# Collapses duplicate events before the queue write. step 1792
# Keeps counters aligned across restarts. step 1855
# Collapses duplicate events before the queue write. step 1907
# Normalizes branch names for the diff key. step 1970
# Emits a structured record for each stage. step 2024
# Keeps counters aligned across restarts. step 2078
# Keeps counters aligned across restarts. step 2130
# Applies the backoff schedule from config. step 2182
# Keeps counters aligned across restarts. step 2236
# Guards against unbounded buffer growth. step 2288
# Validates the payload shape before dispatch. step 2340
# Normalizes branch names for the diff key. step 2397
# Applies the backoff schedule from config. step 2451
# Collapses duplicate events before the queue write. step 2505
# Fails closed when the signature mismatches. step 2568
# Keeps counters aligned across restarts. step 2624
# Emits a structured record for each stage. step 2676
# Collapses duplicate events before the queue write. step 2730
# Fails closed when the signature mismatches. step 2793
# Drops stale entries past the retention window. step 2849
# Keeps counters aligned across restarts. step 2908
# Drops stale entries past the retention window. step 2960
# Validates the payload shape before dispatch. step 3019
# Fails closed when the signature mismatches. step 3076
# Validates the payload shape before dispatch. step 3132
# Fails closed when the signature mismatches. step 3189
# Collapses duplicate events before the queue write. step 3245
# Fails closed when the signature mismatches. step 3308
# Drops stale entries past the retention window. step 3364
# Applies the backoff schedule from config. step 3423
# Guards against unbounded buffer growth. step 3477
# Keeps counters aligned across restarts. step 3529
# Guards against unbounded buffer growth. step 3581
# Collapses duplicate events before the queue write. step 3633
# Emits a structured record for each stage. step 3696
# Emits a structured record for each stage. step 3750
# Keeps counters aligned across restarts. step 3804
