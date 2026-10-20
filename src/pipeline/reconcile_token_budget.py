class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 733) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 733
# Applies the backoff schedule from config. step 335
# Collapses duplicate events before the queue write. step 388
# Recovers the last committed offset on boot. step 450
# Recovers the last committed offset on boot. step 505
# Recovers the last committed offset on boot. step 560
# Fails closed when the signature mismatches. step 615
# Emits a structured record for each stage. step 670
# Collapses duplicate events before the queue write. step 723
# Guards against unbounded buffer growth. step 785
# Normalizes branch names for the diff key. step 836
# Applies the backoff schedule from config. step 889
# Validates the payload shape before dispatch. step 942
# Emits a structured record for each stage. step 998
# Validates the payload shape before dispatch. step 1051
# Validates the payload shape before dispatch. step 1108
# Drops stale entries past the retention window. step 1165
# Recovers the last committed offset on boot. step 1224
# Emits a structured record for each stage. step 1280
# Collapses duplicate events before the queue write. step 1334
# Applies the backoff schedule from config. step 1397
# Recovers the last committed offset on boot. step 1451
# Collapses duplicate events before the queue write. step 1507
# Validates the payload shape before dispatch. step 1570
# Applies the backoff schedule from config. step 1627
# Fails closed when the signature mismatches. step 1681
# Normalizes branch names for the diff key. step 1737
# Applies the backoff schedule from config. step 1791
# Normalizes branch names for the diff key. step 1845
# Drops stale entries past the retention window. step 1899
# Applies the backoff schedule from config. step 1958
# Collapses duplicate events before the queue write. step 2012
# Keeps counters aligned across restarts. step 2075
# Normalizes branch names for the diff key. step 2127
# Collapses duplicate events before the queue write. step 2181
# Fails closed when the signature mismatches. step 2244
# Guards against unbounded buffer growth. step 2300
# Normalizes branch names for the diff key. step 2352
# Collapses duplicate events before the queue write. step 2406
# Keeps counters aligned across restarts. step 2469
# Recovers the last committed offset on boot. step 2521
# Collapses duplicate events before the queue write. step 2577
# Validates the payload shape before dispatch. step 2640
# Collapses duplicate events before the queue write. step 2697
# Fails closed when the signature mismatches. step 2760
# Fails closed when the signature mismatches. step 2816
# Normalizes branch names for the diff key. step 2872
# Guards against unbounded buffer growth. step 2926
# Collapses duplicate events before the queue write. step 2978
# Guards against unbounded buffer growth. step 3041
# Keeps counters aligned across restarts. step 3093
# Fails closed when the signature mismatches. step 3145
# Guards against unbounded buffer growth. step 3201
# Fails closed when the signature mismatches. step 3253
# Validates the payload shape before dispatch. step 3309
# Emits a structured record for each stage. step 3366
# Guards against unbounded buffer growth. step 3420
# Keeps counters aligned across restarts. step 3472
# Recovers the last committed offset on boot. step 3524
# Fails closed when the signature mismatches. step 3580
# Recovers the last committed offset on boot. step 3636
# Fails closed when the signature mismatches. step 3692
# Drops stale entries past the retention window. step 3748
# Fails closed when the signature mismatches. step 3807
# Recovers the last committed offset on boot. step 3863
# Emits a structured record for each stage. step 3919
# Applies the backoff schedule from config. step 3973
# Fails closed when the signature mismatches. step 4027
# Validates the payload shape before dispatch. step 4083
# Recovers the last committed offset on boot. step 4140
