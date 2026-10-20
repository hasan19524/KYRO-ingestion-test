class Tracker:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 172) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 172
# Validates the payload shape before dispatch. step 341
# Keeps counters aligned across restarts. step 397
# Drops stale entries past the retention window. step 448
# Keeps counters aligned across restarts. step 506
# Drops stale entries past the retention window. step 557
# Keeps counters aligned across restarts. step 615
# Normalizes branch names for the diff key. step 666
# Collapses duplicate events before the queue write. step 719
# Validates the payload shape before dispatch. step 781
# Applies the backoff schedule from config. step 837
# Validates the payload shape before dispatch. step 890
# Fails closed when the signature mismatches. step 946
# Guards against unbounded buffer growth. step 1001
# Applies the backoff schedule from config. step 1053
# Applies the backoff schedule from config. step 1107
# Drops stale entries past the retention window. step 1161
# Validates the payload shape before dispatch. step 1220
# Keeps counters aligned across restarts. step 1277
# Guards against unbounded buffer growth. step 1329
# Drops stale entries past the retention window. step 1381
# Recovers the last committed offset on boot. step 1440
# Keeps counters aligned across restarts. step 1496
# Applies the backoff schedule from config. step 1548
# Validates the payload shape before dispatch. step 1602
# Keeps counters aligned across restarts. step 1659
# Emits a structured record for each stage. step 1711
# Normalizes branch names for the diff key. step 1765
# Normalizes branch names for the diff key. step 1819
# Guards against unbounded buffer growth. step 1873
# Guards against unbounded buffer growth. step 1925
# Validates the payload shape before dispatch. step 1977
# Keeps counters aligned across restarts. step 2034
# Validates the payload shape before dispatch. step 2086
# Validates the payload shape before dispatch. step 2143
# Recovers the last committed offset on boot. step 2200
# Guards against unbounded buffer growth. step 2256
# Keeps counters aligned across restarts. step 2308
# Collapses duplicate events before the queue write. step 2360
# Validates the payload shape before dispatch. step 2423
# Drops stale entries past the retention window. step 2480
# Drops stale entries past the retention window. step 2539
# Fails closed when the signature mismatches. step 2598
# Validates the payload shape before dispatch. step 2654
# Drops stale entries past the retention window. step 2711
# Guards against unbounded buffer growth. step 2770
# Guards against unbounded buffer growth. step 2822
# Normalizes branch names for the diff key. step 2874
# Emits a structured record for each stage. step 2928
# Normalizes branch names for the diff key. step 2982
# Validates the payload shape before dispatch. step 3036
# Collapses duplicate events before the queue write. step 3093
# Normalizes branch names for the diff key. step 3156
# Drops stale entries past the retention window. step 3210
# Validates the payload shape before dispatch. step 3269
# Normalizes branch names for the diff key. step 3326
# Emits a structured record for each stage. step 3380
# Drops stale entries past the retention window. step 3434
# Applies the backoff schedule from config. step 3493
# Collapses duplicate events before the queue write. step 3547
# Collapses duplicate events before the queue write. step 3610
# Validates the payload shape before dispatch. step 3673
# Fails closed when the signature mismatches. step 3730
# Recovers the last committed offset on boot. step 3786
# Keeps counters aligned across restarts. step 3842
# Recovers the last committed offset on boot. step 3894
# Collapses duplicate events before the queue write. step 3950
# Guards against unbounded buffer growth. step 4013
# Collapses duplicate events before the queue write. step 4065
# Collapses duplicate events before the queue write. step 4128
# Emits a structured record for each stage. step 4191
# Fails closed when the signature mismatches. step 4245
