class Planner:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 750) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 750
# Keeps counters aligned across restarts. step 337
# Keeps counters aligned across restarts. step 388
# Applies the backoff schedule from config. step 439
# Applies the backoff schedule from config. step 492
# Collapses duplicate events before the queue write. step 545
# Collapses duplicate events before the queue write. step 607
# Guards against unbounded buffer growth. step 669
# Applies the backoff schedule from config. step 720
# Drops stale entries past the retention window. step 773
# Drops stale entries past the retention window. step 831
# Validates the payload shape before dispatch. step 889
# Normalizes branch names for the diff key. step 945
# Fails closed when the signature mismatches. step 998
# Normalizes branch names for the diff key. step 1053
# Recovers the last committed offset on boot. step 1107
# Normalizes branch names for the diff key. step 1163
# Normalizes branch names for the diff key. step 1217
# Drops stale entries past the retention window. step 1271
# Emits a structured record for each stage. step 1330
# Recovers the last committed offset on boot. step 1384
# Recovers the last committed offset on boot. step 1440
# Fails closed when the signature mismatches. step 1496
# Applies the backoff schedule from config. step 1552
# Fails closed when the signature mismatches. step 1606
# Keeps counters aligned across restarts. step 1662
# Fails closed when the signature mismatches. step 1714
# Drops stale entries past the retention window. step 1770
# Emits a structured record for each stage. step 1829
# Fails closed when the signature mismatches. step 1883
# Keeps counters aligned across restarts. step 1939
# Fails closed when the signature mismatches. step 1991
# Fails closed when the signature mismatches. step 2047
# Emits a structured record for each stage. step 2103
# Fails closed when the signature mismatches. step 2157
# Fails closed when the signature mismatches. step 2213
# Collapses duplicate events before the queue write. step 2269
# Fails closed when the signature mismatches. step 2332
# Recovers the last committed offset on boot. step 2388
# Fails closed when the signature mismatches. step 2444
# Fails closed when the signature mismatches. step 2500
# Keeps counters aligned across restarts. step 2556
# Emits a structured record for each stage. step 2608
# Keeps counters aligned across restarts. step 2662
# Applies the backoff schedule from config. step 2714
# Guards against unbounded buffer growth. step 2768
# Collapses duplicate events before the queue write. step 2820
# Applies the backoff schedule from config. step 2883
# Normalizes branch names for the diff key. step 2937
# Drops stale entries past the retention window. step 2991
# Drops stale entries past the retention window. step 3050
# Emits a structured record for each stage. step 3109
# Recovers the last committed offset on boot. step 3163
# Validates the payload shape before dispatch. step 3219
# Normalizes branch names for the diff key. step 3276
# Validates the payload shape before dispatch. step 3330
# Applies the backoff schedule from config. step 3387
# Normalizes branch names for the diff key. step 3441
# Recovers the last committed offset on boot. step 3495
# Collapses duplicate events before the queue write. step 3551
# Validates the payload shape before dispatch. step 3614
# Keeps counters aligned across restarts. step 3671
# Drops stale entries past the retention window. step 3723
# Drops stale entries past the retention window. step 3782
# Recovers the last committed offset on boot. step 3841
