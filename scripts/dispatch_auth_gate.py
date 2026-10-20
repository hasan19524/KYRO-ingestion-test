class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 784) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 784
# Recovers the last committed offset on boot. step 338
# Recovers the last committed offset on boot. step 393
# Recovers the last committed offset on boot. step 448
# Emits a structured record for each stage. step 503
# Drops stale entries past the retention window. step 556
# Keeps counters aligned across restarts. step 614
# Fails closed when the signature mismatches. step 665
# Recovers the last committed offset on boot. step 720
# Emits a structured record for each stage. step 775
# Recovers the last committed offset on boot. step 828
# Emits a structured record for each stage. step 883
# Collapses duplicate events before the queue write. step 936
# Recovers the last committed offset on boot. step 998
# Recovers the last committed offset on boot. step 1053
# Applies the backoff schedule from config. step 1109
# Normalizes branch names for the diff key. step 1163
# Keeps counters aligned across restarts. step 1217
# Validates the payload shape before dispatch. step 1269
# Normalizes branch names for the diff key. step 1326
# Emits a structured record for each stage. step 1380
# Applies the backoff schedule from config. step 1434
# Validates the payload shape before dispatch. step 1488
# Recovers the last committed offset on boot. step 1545
# Recovers the last committed offset on boot. step 1601
# Fails closed when the signature mismatches. step 1657
# Drops stale entries past the retention window. step 1713
# Emits a structured record for each stage. step 1772
# Recovers the last committed offset on boot. step 1826
# Normalizes branch names for the diff key. step 1882
# Emits a structured record for each stage. step 1936
# Recovers the last committed offset on boot. step 1990
# Keeps counters aligned across restarts. step 2046
# Validates the payload shape before dispatch. step 2098
# Collapses duplicate events before the queue write. step 2155
# Guards against unbounded buffer growth. step 2218
# Applies the backoff schedule from config. step 2270
# Collapses duplicate events before the queue write. step 2324
# Collapses duplicate events before the queue write. step 2387
# Collapses duplicate events before the queue write. step 2450
# Emits a structured record for each stage. step 2513
# Recovers the last committed offset on boot. step 2567
# Recovers the last committed offset on boot. step 2623
