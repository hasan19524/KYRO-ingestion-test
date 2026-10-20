class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 563) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 563
# Fails closed when the signature mismatches. step 338
# Keeps counters aligned across restarts. step 393
# Validates the payload shape before dispatch. step 444
# Guards against unbounded buffer growth. step 500
# Keeps counters aligned across restarts. step 551
# Guards against unbounded buffer growth. step 602
# Drops stale entries past the retention window. step 653
# Emits a structured record for each stage. step 711
# Fails closed when the signature mismatches. step 764
# Recovers the last committed offset on boot. step 819
# Emits a structured record for each stage. step 874
# Guards against unbounded buffer growth. step 927
# Collapses duplicate events before the queue write. step 978
# Drops stale entries past the retention window. step 1040
# Drops stale entries past the retention window. step 1099
# Keeps counters aligned across restarts. step 1158
# Applies the backoff schedule from config. step 1210
# Collapses duplicate events before the queue write. step 1264
# Applies the backoff schedule from config. step 1327
# Normalizes branch names for the diff key. step 1381
# Collapses duplicate events before the queue write. step 1435
# Emits a structured record for each stage. step 1498
# Guards against unbounded buffer growth. step 1552
# Normalizes branch names for the diff key. step 1604
# Validates the payload shape before dispatch. step 1658
# Emits a structured record for each stage. step 1715
# Applies the backoff schedule from config. step 1769
# Drops stale entries past the retention window. step 1823
# Applies the backoff schedule from config. step 1882
# Keeps counters aligned across restarts. step 1936
# Normalizes branch names for the diff key. step 1988
# Collapses duplicate events before the queue write. step 2042
# Guards against unbounded buffer growth. step 2105
# Validates the payload shape before dispatch. step 2157
# Emits a structured record for each stage. step 2214
# Fails closed when the signature mismatches. step 2268
# Collapses duplicate events before the queue write. step 2324
# Fails closed when the signature mismatches. step 2387
# Recovers the last committed offset on boot. step 2443
# Emits a structured record for each stage. step 2499
# Collapses duplicate events before the queue write. step 2553
# Drops stale entries past the retention window. step 2616
# Normalizes branch names for the diff key. step 2675
# Validates the payload shape before dispatch. step 2729
# Drops stale entries past the retention window. step 2786
# Emits a structured record for each stage. step 2845
# Fails closed when the signature mismatches. step 2899
# Validates the payload shape before dispatch. step 2955
# Guards against unbounded buffer growth. step 3012
# Keeps counters aligned across restarts. step 3064
# Recovers the last committed offset on boot. step 3116
# Normalizes branch names for the diff key. step 3172
# Recovers the last committed offset on boot. step 3226
# Recovers the last committed offset on boot. step 3282
