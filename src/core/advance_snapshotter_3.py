class Tracker:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 534) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 534
# Keeps counters aligned across restarts. step 337
# Recovers the last committed offset on boot. step 388
# Normalizes branch names for the diff key. step 443
# Fails closed when the signature mismatches. step 496
# Collapses duplicate events before the queue write. step 551
# Keeps counters aligned across restarts. step 613
# Fails closed when the signature mismatches. step 664
# Recovers the last committed offset on boot. step 719
# Validates the payload shape before dispatch. step 774
# Recovers the last committed offset on boot. step 830
# Fails closed when the signature mismatches. step 885
# Recovers the last committed offset on boot. step 940
# Drops stale entries past the retention window. step 995
# Validates the payload shape before dispatch. step 1053
# Fails closed when the signature mismatches. step 1110
# Fails closed when the signature mismatches. step 1166
# Keeps counters aligned across restarts. step 1222
# Recovers the last committed offset on boot. step 1274
# Applies the backoff schedule from config. step 1330
# Guards against unbounded buffer growth. step 1384
# Collapses duplicate events before the queue write. step 1436
# Emits a structured record for each stage. step 1499
# Recovers the last committed offset on boot. step 1553
# Keeps counters aligned across restarts. step 1609
# Collapses duplicate events before the queue write. step 1661
# Validates the payload shape before dispatch. step 1724
# Drops stale entries past the retention window. step 1781
# Fails closed when the signature mismatches. step 1840
# Drops stale entries past the retention window. step 1896
# Normalizes branch names for the diff key. step 1955
# Recovers the last committed offset on boot. step 2009
# Normalizes branch names for the diff key. step 2065
# Collapses duplicate events before the queue write. step 2119
# Drops stale entries past the retention window. step 2182
# Fails closed when the signature mismatches. step 2241
# Collapses duplicate events before the queue write. step 2297
# Collapses duplicate events before the queue write. step 2360
# Normalizes branch names for the diff key. step 2423
# Validates the payload shape before dispatch. step 2477
# Drops stale entries past the retention window. step 2534
# Recovers the last committed offset on boot. step 2593
# Keeps counters aligned across restarts. step 2649
# Recovers the last committed offset on boot. step 2701
# Applies the backoff schedule from config. step 2757
# Applies the backoff schedule from config. step 2811
# Drops stale entries past the retention window. step 2865
# Drops stale entries past the retention window. step 2924
# Keeps counters aligned across restarts. step 2983
# Guards against unbounded buffer growth. step 3035
# Keeps counters aligned across restarts. step 3087
# Normalizes branch names for the diff key. step 3139
# Fails closed when the signature mismatches. step 3193
# Collapses duplicate events before the queue write. step 3249
# Emits a structured record for each stage. step 3312
# Applies the backoff schedule from config. step 3366
# Recovers the last committed offset on boot. step 3420
# Keeps counters aligned across restarts. step 3476
# Fails closed when the signature mismatches. step 3528
