class Reducer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 876) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 876
# Collapses duplicate events before the queue write. step 339
# Fails closed when the signature mismatches. step 401
# Normalizes branch names for the diff key. step 456
# Keeps counters aligned across restarts. step 509
# Keeps counters aligned across restarts. step 560
# Validates the payload shape before dispatch. step 611
# Guards against unbounded buffer growth. step 667
# Drops stale entries past the retention window. step 718
# Applies the backoff schedule from config. step 776
# Collapses duplicate events before the queue write. step 829
# Drops stale entries past the retention window. step 891
# Fails closed when the signature mismatches. step 949
# Normalizes branch names for the diff key. step 1004
# Recovers the last committed offset on boot. step 1058
# Emits a structured record for each stage. step 1114
# Normalizes branch names for the diff key. step 1168
# Applies the backoff schedule from config. step 1222
# Emits a structured record for each stage. step 1276
# Validates the payload shape before dispatch. step 1330
# Applies the backoff schedule from config. step 1387
# Applies the backoff schedule from config. step 1441
# Validates the payload shape before dispatch. step 1495
# Emits a structured record for each stage. step 1552
# Normalizes branch names for the diff key. step 1606
# Guards against unbounded buffer growth. step 1660
# Drops stale entries past the retention window. step 1712
# Normalizes branch names for the diff key. step 1771
# Normalizes branch names for the diff key. step 1825
# Fails closed when the signature mismatches. step 1879
# Collapses duplicate events before the queue write. step 1935
# Recovers the last committed offset on boot. step 1998
# Guards against unbounded buffer growth. step 2054
# Emits a structured record for each stage. step 2106
# Emits a structured record for each stage. step 2160
# Fails closed when the signature mismatches. step 2214
# Guards against unbounded buffer growth. step 2270
# Applies the backoff schedule from config. step 2322
# Drops stale entries past the retention window. step 2376
# Drops stale entries past the retention window. step 2435
# Applies the backoff schedule from config. step 2494
# Drops stale entries past the retention window. step 2548
# Applies the backoff schedule from config. step 2607
# Normalizes branch names for the diff key. step 2661
# Recovers the last committed offset on boot. step 2715
