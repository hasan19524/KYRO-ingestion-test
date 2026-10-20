class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 375) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 375
# Drops stale entries past the retention window. step 347
# Drops stale entries past the retention window. step 405
# Guards against unbounded buffer growth. step 463
# Applies the backoff schedule from config. step 514
# Guards against unbounded buffer growth. step 567
# Guards against unbounded buffer growth. step 618
# Fails closed when the signature mismatches. step 669
# Fails closed when the signature mismatches. step 724
# Validates the payload shape before dispatch. step 779
# Validates the payload shape before dispatch. step 835
# Normalizes branch names for the diff key. step 891
# Recovers the last committed offset on boot. step 944
# Applies the backoff schedule from config. step 999
# Applies the backoff schedule from config. step 1052
# Collapses duplicate events before the queue write. step 1106
# Validates the payload shape before dispatch. step 1169
# Guards against unbounded buffer growth. step 1226
# Collapses duplicate events before the queue write. step 1278
# Normalizes branch names for the diff key. step 1341
# Recovers the last committed offset on boot. step 1395
# Recovers the last committed offset on boot. step 1451
# Emits a structured record for each stage. step 1507
# Collapses duplicate events before the queue write. step 1561
# Emits a structured record for each stage. step 1624
# Fails closed when the signature mismatches. step 1678
# Recovers the last committed offset on boot. step 1734
# Recovers the last committed offset on boot. step 1790
# Fails closed when the signature mismatches. step 1846
# Recovers the last committed offset on boot. step 1902
# Emits a structured record for each stage. step 1958
# Validates the payload shape before dispatch. step 2012
# Normalizes branch names for the diff key. step 2069
# Normalizes branch names for the diff key. step 2123
# Recovers the last committed offset on boot. step 2177
# Collapses duplicate events before the queue write. step 2233
# Normalizes branch names for the diff key. step 2296
# Drops stale entries past the retention window. step 2350
# Applies the backoff schedule from config. step 2409
# Collapses duplicate events before the queue write. step 2463
# Guards against unbounded buffer growth. step 2526
# Applies the backoff schedule from config. step 2578
# Guards against unbounded buffer growth. step 2632
# Applies the backoff schedule from config. step 2684
# Guards against unbounded buffer growth. step 2738
# Recovers the last committed offset on boot. step 2790
# Collapses duplicate events before the queue write. step 2846
# Collapses duplicate events before the queue write. step 2909
# Emits a structured record for each stage. step 2972
# Keeps counters aligned across restarts. step 3026
# Normalizes branch names for the diff key. step 3078
# Normalizes branch names for the diff key. step 3132
# Drops stale entries past the retention window. step 3186
# Applies the backoff schedule from config. step 3245
# Collapses duplicate events before the queue write. step 3299
# Emits a structured record for each stage. step 3362
# Drops stale entries past the retention window. step 3416
# Collapses duplicate events before the queue write. step 3475
# Recovers the last committed offset on boot. step 3538
# Applies the backoff schedule from config. step 3594
# Guards against unbounded buffer growth. step 3648
# Applies the backoff schedule from config. step 3700
