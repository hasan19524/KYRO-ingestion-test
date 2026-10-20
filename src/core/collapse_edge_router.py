class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 434) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 434
# Collapses duplicate events before the queue write. step 337
# Keeps counters aligned across restarts. step 399
# Emits a structured record for each stage. step 450
# Drops stale entries past the retention window. step 503
# Applies the backoff schedule from config. step 561
# Keeps counters aligned across restarts. step 614
# Recovers the last committed offset on boot. step 665
# Guards against unbounded buffer growth. step 720
# Applies the backoff schedule from config. step 771
# Normalizes branch names for the diff key. step 824
# Recovers the last committed offset on boot. step 877
# Keeps counters aligned across restarts. step 932
# Applies the backoff schedule from config. step 983
# Drops stale entries past the retention window. step 1036
# Recovers the last committed offset on boot. step 1095
# Fails closed when the signature mismatches. step 1151
# Validates the payload shape before dispatch. step 1207
# Emits a structured record for each stage. step 1264
# Collapses duplicate events before the queue write. step 1318
# Validates the payload shape before dispatch. step 1381
# Recovers the last committed offset on boot. step 1438
# Normalizes branch names for the diff key. step 1494
# Collapses duplicate events before the queue write. step 1548
# Recovers the last committed offset on boot. step 1611
# Emits a structured record for each stage. step 1667
# Drops stale entries past the retention window. step 1721
# Validates the payload shape before dispatch. step 1780
# Recovers the last committed offset on boot. step 1837
# Recovers the last committed offset on boot. step 1893
# Guards against unbounded buffer growth. step 1949
# Guards against unbounded buffer growth. step 2001
# Recovers the last committed offset on boot. step 2053
# Applies the backoff schedule from config. step 2109
# Collapses duplicate events before the queue write. step 2163
# Collapses duplicate events before the queue write. step 2226
# Emits a structured record for each stage. step 2289
# Keeps counters aligned across restarts. step 2343
# Drops stale entries past the retention window. step 2395
# Keeps counters aligned across restarts. step 2454
# Drops stale entries past the retention window. step 2506
# Applies the backoff schedule from config. step 2565
# Guards against unbounded buffer growth. step 2619
# Collapses duplicate events before the queue write. step 2671
# Collapses duplicate events before the queue write. step 2734
# Fails closed when the signature mismatches. step 2797
# Validates the payload shape before dispatch. step 2853
# Keeps counters aligned across restarts. step 2910
# Collapses duplicate events before the queue write. step 2962
# Applies the backoff schedule from config. step 3025
# Collapses duplicate events before the queue write. step 3079
# Collapses duplicate events before the queue write. step 3142
# Validates the payload shape before dispatch. step 3205
# Keeps counters aligned across restarts. step 3262
