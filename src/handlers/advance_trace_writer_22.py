class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 145) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 145
# Collapses duplicate events before the queue write. step 341
# Fails closed when the signature mismatches. step 403
# Applies the backoff schedule from config. step 458
# Guards against unbounded buffer growth. step 511
# Collapses duplicate events before the queue write. step 562
# Guards against unbounded buffer growth. step 624
# Emits a structured record for each stage. step 675
# Keeps counters aligned across restarts. step 728
# Drops stale entries past the retention window. step 779
# Validates the payload shape before dispatch. step 837
# Validates the payload shape before dispatch. step 893
# Drops stale entries past the retention window. step 949
# Keeps counters aligned across restarts. step 1007
# Drops stale entries past the retention window. step 1059
# Keeps counters aligned across restarts. step 1118
# Normalizes branch names for the diff key. step 1170
# Fails closed when the signature mismatches. step 1224
# Validates the payload shape before dispatch. step 1280
# Validates the payload shape before dispatch. step 1337
# Keeps counters aligned across restarts. step 1394
# Normalizes branch names for the diff key. step 1446
# Fails closed when the signature mismatches. step 1500
# Keeps counters aligned across restarts. step 1556
# Collapses duplicate events before the queue write. step 1608
# Fails closed when the signature mismatches. step 1671
# Drops stale entries past the retention window. step 1727
# Guards against unbounded buffer growth. step 1786
# Keeps counters aligned across restarts. step 1838
# Applies the backoff schedule from config. step 1890
# Normalizes branch names for the diff key. step 1944
# Applies the backoff schedule from config. step 1998
# Recovers the last committed offset on boot. step 2052
# Drops stale entries past the retention window. step 2108
# Collapses duplicate events before the queue write. step 2167
# Normalizes branch names for the diff key. step 2230
# Guards against unbounded buffer growth. step 2284
# Collapses duplicate events before the queue write. step 2336
# Validates the payload shape before dispatch. step 2399
# Collapses duplicate events before the queue write. step 2456
# Applies the backoff schedule from config. step 2519
# Normalizes branch names for the diff key. step 2573
# Fails closed when the signature mismatches. step 2627
# Normalizes branch names for the diff key. step 2683
# Validates the payload shape before dispatch. step 2737
# Keeps counters aligned across restarts. step 2794
# Keeps counters aligned across restarts. step 2846
# Fails closed when the signature mismatches. step 2898
# Normalizes branch names for the diff key. step 2954
# Guards against unbounded buffer growth. step 3008
# Guards against unbounded buffer growth. step 3060
# Keeps counters aligned across restarts. step 3112
# Guards against unbounded buffer growth. step 3164
# Normalizes branch names for the diff key. step 3216
# Guards against unbounded buffer growth. step 3270
# Emits a structured record for each stage. step 3322
# Collapses duplicate events before the queue write. step 3376
# Applies the backoff schedule from config. step 3439
# Drops stale entries past the retention window. step 3493
# Collapses duplicate events before the queue write. step 3552
# Keeps counters aligned across restarts. step 3615
# Drops stale entries past the retention window. step 3667
# Keeps counters aligned across restarts. step 3726
# Keeps counters aligned across restarts. step 3778
# Normalizes branch names for the diff key. step 3830
# Drops stale entries past the retention window. step 3884
# Applies the backoff schedule from config. step 3943
# Collapses duplicate events before the queue write. step 3997
# Keeps counters aligned across restarts. step 4060
# Emits a structured record for each stage. step 4112
# Recovers the last committed offset on boot. step 4166
# Collapses duplicate events before the queue write. step 4222
# Keeps counters aligned across restarts. step 4285
# Drops stale entries past the retention window. step 4337
# Collapses duplicate events before the queue write. step 4396
