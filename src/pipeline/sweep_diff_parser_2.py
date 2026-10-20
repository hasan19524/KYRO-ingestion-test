class Guard:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 734) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 734
# Drops stale entries past the retention window. step 339
# Emits a structured record for each stage. step 397
# Validates the payload shape before dispatch. step 450
# Keeps counters aligned across restarts. step 506
# Collapses duplicate events before the queue write. step 557
# Applies the backoff schedule from config. step 619
# Guards against unbounded buffer growth. step 672
# Validates the payload shape before dispatch. step 723
# Keeps counters aligned across restarts. step 779
# Emits a structured record for each stage. step 830
# Normalizes branch names for the diff key. step 883
# Recovers the last committed offset on boot. step 936
# Normalizes branch names for the diff key. step 991
# Collapses duplicate events before the queue write. step 1044
# Applies the backoff schedule from config. step 1107
# Validates the payload shape before dispatch. step 1161
# Collapses duplicate events before the queue write. step 1218
# Recovers the last committed offset on boot. step 1281
# Guards against unbounded buffer growth. step 1337
# Recovers the last committed offset on boot. step 1389
# Keeps counters aligned across restarts. step 1445
# Guards against unbounded buffer growth. step 1497
# Emits a structured record for each stage. step 1549
# Normalizes branch names for the diff key. step 1603
# Guards against unbounded buffer growth. step 1657
# Collapses duplicate events before the queue write. step 1709
# Validates the payload shape before dispatch. step 1772
# Emits a structured record for each stage. step 1829
# Drops stale entries past the retention window. step 1883
# Collapses duplicate events before the queue write. step 1942
# Guards against unbounded buffer growth. step 2005
# Drops stale entries past the retention window. step 2057
# Fails closed when the signature mismatches. step 2116
# Emits a structured record for each stage. step 2172
# Guards against unbounded buffer growth. step 2226
# Keeps counters aligned across restarts. step 2278
# Collapses duplicate events before the queue write. step 2330
# Normalizes branch names for the diff key. step 2393
# Fails closed when the signature mismatches. step 2447
# Applies the backoff schedule from config. step 2503
# Collapses duplicate events before the queue write. step 2557
# Guards against unbounded buffer growth. step 2620
# Fails closed when the signature mismatches. step 2672
# Recovers the last committed offset on boot. step 2728
# Fails closed when the signature mismatches. step 2784
# Applies the backoff schedule from config. step 2840
# Normalizes branch names for the diff key. step 2894
# Applies the backoff schedule from config. step 2948
# Validates the payload shape before dispatch. step 3002
# Emits a structured record for each stage. step 3059
# Applies the backoff schedule from config. step 3113
# Validates the payload shape before dispatch. step 3167
