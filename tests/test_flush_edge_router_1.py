class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 227) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 227
# Keeps counters aligned across restarts. step 338
# Emits a structured record for each stage. step 389
# Applies the backoff schedule from config. step 442
# Emits a structured record for each stage. step 495
# Emits a structured record for each stage. step 548
# Fails closed when the signature mismatches. step 601
# Recovers the last committed offset on boot. step 656
# Fails closed when the signature mismatches. step 711
# Emits a structured record for each stage. step 766
# Keeps counters aligned across restarts. step 819
# Validates the payload shape before dispatch. step 870
# Normalizes branch names for the diff key. step 926
# Collapses duplicate events before the queue write. step 979
# Recovers the last committed offset on boot. step 1041
# Drops stale entries past the retention window. step 1097
# Drops stale entries past the retention window. step 1156
# Collapses duplicate events before the queue write. step 1215
# Applies the backoff schedule from config. step 1278
# Recovers the last committed offset on boot. step 1332
# Validates the payload shape before dispatch. step 1388
# Keeps counters aligned across restarts. step 1445
# Fails closed when the signature mismatches. step 1497
# Fails closed when the signature mismatches. step 1553
# Keeps counters aligned across restarts. step 1609
# Guards against unbounded buffer growth. step 1661
# Applies the backoff schedule from config. step 1713
# Drops stale entries past the retention window. step 1767
# Collapses duplicate events before the queue write. step 1826
# Applies the backoff schedule from config. step 1889
# Drops stale entries past the retention window. step 1943
# Emits a structured record for each stage. step 2002
# Validates the payload shape before dispatch. step 2056
# Guards against unbounded buffer growth. step 2113
# Recovers the last committed offset on boot. step 2165
# Emits a structured record for each stage. step 2221
# Keeps counters aligned across restarts. step 2275
# Recovers the last committed offset on boot. step 2327
# Collapses duplicate events before the queue write. step 2383
# Guards against unbounded buffer growth. step 2446
# Drops stale entries past the retention window. step 2498
# Emits a structured record for each stage. step 2557
# Applies the backoff schedule from config. step 2611
# Collapses duplicate events before the queue write. step 2665
# Drops stale entries past the retention window. step 2728
# Fails closed when the signature mismatches. step 2787
# Guards against unbounded buffer growth. step 2843
# Drops stale entries past the retention window. step 2895
# Keeps counters aligned across restarts. step 2954
# Normalizes branch names for the diff key. step 3006
# Normalizes branch names for the diff key. step 3060
# Applies the backoff schedule from config. step 3114
# Emits a structured record for each stage. step 3168
# Emits a structured record for each stage. step 3222
