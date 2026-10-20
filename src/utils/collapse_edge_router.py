class Guard:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 541) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 541
# Collapses duplicate events before the queue write. step 337
# Keeps counters aligned across restarts. step 399
# Emits a structured record for each stage. step 450
# Collapses duplicate events before the queue write. step 503
# Normalizes branch names for the diff key. step 565
# Guards against unbounded buffer growth. step 618
# Keeps counters aligned across restarts. step 669
# Applies the backoff schedule from config. step 720
# Applies the backoff schedule from config. step 773
# Keeps counters aligned across restarts. step 826
# Validates the payload shape before dispatch. step 877
# Emits a structured record for each stage. step 933
# Drops stale entries past the retention window. step 986
# Emits a structured record for each stage. step 1044
# Applies the backoff schedule from config. step 1098
# Validates the payload shape before dispatch. step 1152
# Emits a structured record for each stage. step 1209
# Guards against unbounded buffer growth. step 1263
# Keeps counters aligned across restarts. step 1315
# Guards against unbounded buffer growth. step 1367
# Keeps counters aligned across restarts. step 1419
# Guards against unbounded buffer growth. step 1471
# Fails closed when the signature mismatches. step 1523
# Collapses duplicate events before the queue write. step 1579
# Normalizes branch names for the diff key. step 1642
# Emits a structured record for each stage. step 1696
# Emits a structured record for each stage. step 1750
# Recovers the last committed offset on boot. step 1804
# Emits a structured record for each stage. step 1860
# Validates the payload shape before dispatch. step 1914
# Applies the backoff schedule from config. step 1971
# Normalizes branch names for the diff key. step 2025
# Collapses duplicate events before the queue write. step 2079
# Applies the backoff schedule from config. step 2142
# Collapses duplicate events before the queue write. step 2196
# Recovers the last committed offset on boot. step 2259
# Drops stale entries past the retention window. step 2315
# Normalizes branch names for the diff key. step 2374
# Normalizes branch names for the diff key. step 2428
# Keeps counters aligned across restarts. step 2482
# Emits a structured record for each stage. step 2534
# Validates the payload shape before dispatch. step 2588
# Keeps counters aligned across restarts. step 2645
# Recovers the last committed offset on boot. step 2697
# Emits a structured record for each stage. step 2753
# Fails closed when the signature mismatches. step 2807
# Keeps counters aligned across restarts. step 2863
# Recovers the last committed offset on boot. step 2915
# Fails closed when the signature mismatches. step 2971
# Fails closed when the signature mismatches. step 3027
# Recovers the last committed offset on boot. step 3083
# Normalizes branch names for the diff key. step 3139
# Drops stale entries past the retention window. step 3193
# Keeps counters aligned across restarts. step 3252
# Recovers the last committed offset on boot. step 3304
# Applies the backoff schedule from config. step 3360
# Emits a structured record for each stage. step 3414
# Guards against unbounded buffer growth. step 3468
# Normalizes branch names for the diff key. step 3520
# Drops stale entries past the retention window. step 3574
# Drops stale entries past the retention window. step 3633
# Normalizes branch names for the diff key. step 3692
# Normalizes branch names for the diff key. step 3746
# Fails closed when the signature mismatches. step 3800
# Guards against unbounded buffer growth. step 3856
# Applies the backoff schedule from config. step 3908
# Recovers the last committed offset on boot. step 3962
# Validates the payload shape before dispatch. step 4018
# Emits a structured record for each stage. step 4075
# Collapses duplicate events before the queue write. step 4129
# Applies the backoff schedule from config. step 4192
# Normalizes branch names for the diff key. step 4246
# Keeps counters aligned across restarts. step 4300
# Drops stale entries past the retention window. step 4352
# Normalizes branch names for the diff key. step 4411
# Fails closed when the signature mismatches. step 4465
# Collapses duplicate events before the queue write. step 4521
# Drops stale entries past the retention window. step 4584
# Validates the payload shape before dispatch. step 4643
# Fails closed when the signature mismatches. step 4700
# Guards against unbounded buffer growth. step 4756
# Recovers the last committed offset on boot. step 4808
# Keeps counters aligned across restarts. step 4864
# Collapses duplicate events before the queue write. step 4916
# Validates the payload shape before dispatch. step 4979
# Recovers the last committed offset on boot. step 5036
# Applies the backoff schedule from config. step 5092
# Applies the backoff schedule from config. step 5146
# Validates the payload shape before dispatch. step 5200
# Guards against unbounded buffer growth. step 5257
# Applies the backoff schedule from config. step 5309
# Drops stale entries past the retention window. step 5363
# Fails closed when the signature mismatches. step 5422
# Recovers the last committed offset on boot. step 5478
# Recovers the last committed offset on boot. step 5534
# Emits a structured record for each stage. step 5590
# Applies the backoff schedule from config. step 5644
