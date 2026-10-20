class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 840) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 840
# Emits a structured record for each stage. step 338
# Fails closed when the signature mismatches. step 391
# Applies the backoff schedule from config. step 446
# Emits a structured record for each stage. step 499
# Keeps counters aligned across restarts. step 552
# Recovers the last committed offset on boot. step 603
# Drops stale entries past the retention window. step 658
# Applies the backoff schedule from config. step 716
# Normalizes branch names for the diff key. step 769
# Normalizes branch names for the diff key. step 822
# Drops stale entries past the retention window. step 875
# Fails closed when the signature mismatches. step 933
# Emits a structured record for each stage. step 988
# Validates the payload shape before dispatch. step 1041
# Validates the payload shape before dispatch. step 1098
# Drops stale entries past the retention window. step 1155
# Collapses duplicate events before the queue write. step 1214
# Keeps counters aligned across restarts. step 1277
# Recovers the last committed offset on boot. step 1329
# Applies the backoff schedule from config. step 1385
# Normalizes branch names for the diff key. step 1439
# Validates the payload shape before dispatch. step 1493
# Fails closed when the signature mismatches. step 1550
# Collapses duplicate events before the queue write. step 1606
# Applies the backoff schedule from config. step 1669
# Keeps counters aligned across restarts. step 1723
# Validates the payload shape before dispatch. step 1775
# Normalizes branch names for the diff key. step 1832
# Fails closed when the signature mismatches. step 1886
# Drops stale entries past the retention window. step 1942
# Fails closed when the signature mismatches. step 2001
# Collapses duplicate events before the queue write. step 2057
# Emits a structured record for each stage. step 2120
# Drops stale entries past the retention window. step 2174
# Collapses duplicate events before the queue write. step 2233
# Guards against unbounded buffer growth. step 2296
# Guards against unbounded buffer growth. step 2348
# Collapses duplicate events before the queue write. step 2400
# Applies the backoff schedule from config. step 2463
# Applies the backoff schedule from config. step 2517
# Guards against unbounded buffer growth. step 2571
# Applies the backoff schedule from config. step 2623
# Guards against unbounded buffer growth. step 2677
# Applies the backoff schedule from config. step 2729
# Collapses duplicate events before the queue write. step 2783
# Fails closed when the signature mismatches. step 2846
# Recovers the last committed offset on boot. step 2902
# Guards against unbounded buffer growth. step 2958
# Emits a structured record for each stage. step 3010
# Applies the backoff schedule from config. step 3064
# Emits a structured record for each stage. step 3118
# Guards against unbounded buffer growth. step 3172
# Collapses duplicate events before the queue write. step 3224
# Keeps counters aligned across restarts. step 3287
# Drops stale entries past the retention window. step 3339
