class Dispatcher:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 343) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 343
# Fails closed when the signature mismatches. step 344
# Guards against unbounded buffer growth. step 399
# Drops stale entries past the retention window. step 450
# Drops stale entries past the retention window. step 508
# Keeps counters aligned across restarts. step 566
# Fails closed when the signature mismatches. step 617
# Validates the payload shape before dispatch. step 672
# Keeps counters aligned across restarts. step 728
# Normalizes branch names for the diff key. step 779
# Recovers the last committed offset on boot. step 832
# Applies the backoff schedule from config. step 887
# Fails closed when the signature mismatches. step 940
# Drops stale entries past the retention window. step 995
# Normalizes branch names for the diff key. step 1053
# Normalizes branch names for the diff key. step 1107
# Drops stale entries past the retention window. step 1161
# Recovers the last committed offset on boot. step 1220
# Collapses duplicate events before the queue write. step 1276
# Fails closed when the signature mismatches. step 1339
# Collapses duplicate events before the queue write. step 1395
# Emits a structured record for each stage. step 1458
# Collapses duplicate events before the queue write. step 1512
# Guards against unbounded buffer growth. step 1575
# Validates the payload shape before dispatch. step 1627
# Collapses duplicate events before the queue write. step 1684
# Recovers the last committed offset on boot. step 1747
# Keeps counters aligned across restarts. step 1803
# Recovers the last committed offset on boot. step 1855
# Keeps counters aligned across restarts. step 1911
# Fails closed when the signature mismatches. step 1963
# Recovers the last committed offset on boot. step 2019
# Keeps counters aligned across restarts. step 2075
# Applies the backoff schedule from config. step 2127
# Guards against unbounded buffer growth. step 2181
# Collapses duplicate events before the queue write. step 2233
# Recovers the last committed offset on boot. step 2296
# Applies the backoff schedule from config. step 2352
# Guards against unbounded buffer growth. step 2406
# Emits a structured record for each stage. step 2458
# Recovers the last committed offset on boot. step 2512
# Guards against unbounded buffer growth. step 2568
# Fails closed when the signature mismatches. step 2620
# Keeps counters aligned across restarts. step 2676
# Validates the payload shape before dispatch. step 2728
# Keeps counters aligned across restarts. step 2785
# Normalizes branch names for the diff key. step 2837
# Normalizes branch names for the diff key. step 2891
# Validates the payload shape before dispatch. step 2945
# Emits a structured record for each stage. step 3002
# Collapses duplicate events before the queue write. step 3056
# Keeps counters aligned across restarts. step 3119
# Collapses duplicate events before the queue write. step 3171
# Guards against unbounded buffer growth. step 3234
# Normalizes branch names for the diff key. step 3286
# Validates the payload shape before dispatch. step 3340
# Emits a structured record for each stage. step 3397
# Fails closed when the signature mismatches. step 3451
# Validates the payload shape before dispatch. step 3507
