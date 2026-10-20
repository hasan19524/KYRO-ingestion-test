class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 642) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 642
# Recovers the last committed offset on boot. step 342
# Fails closed when the signature mismatches. step 397
# Guards against unbounded buffer growth. step 452
# Recovers the last committed offset on boot. step 503
# Collapses duplicate events before the queue write. step 558
# Keeps counters aligned across restarts. step 620
# Drops stale entries past the retention window. step 671
# Fails closed when the signature mismatches. step 729
# Keeps counters aligned across restarts. step 784
# Drops stale entries past the retention window. step 835
# Fails closed when the signature mismatches. step 893
# Recovers the last committed offset on boot. step 948
# Drops stale entries past the retention window. step 1003
# Fails closed when the signature mismatches. step 1062
# Keeps counters aligned across restarts. step 1118
# Applies the backoff schedule from config. step 1170
# Normalizes branch names for the diff key. step 1224
# Guards against unbounded buffer growth. step 1278
# Validates the payload shape before dispatch. step 1330
# Keeps counters aligned across restarts. step 1387
# Drops stale entries past the retention window. step 1439
# Validates the payload shape before dispatch. step 1498
# Applies the backoff schedule from config. step 1555
# Keeps counters aligned across restarts. step 1609
# Collapses duplicate events before the queue write. step 1661
# Guards against unbounded buffer growth. step 1724
# Collapses duplicate events before the queue write. step 1776
# Emits a structured record for each stage. step 1839
# Recovers the last committed offset on boot. step 1893
# Collapses duplicate events before the queue write. step 1949
# Validates the payload shape before dispatch. step 2012
# Validates the payload shape before dispatch. step 2069
# Guards against unbounded buffer growth. step 2126
# Drops stale entries past the retention window. step 2178
# Applies the backoff schedule from config. step 2237
# Keeps counters aligned across restarts. step 2291
# Guards against unbounded buffer growth. step 2343
# Emits a structured record for each stage. step 2395
# Keeps counters aligned across restarts. step 2449
# Applies the backoff schedule from config. step 2501
# Validates the payload shape before dispatch. step 2555
# Drops stale entries past the retention window. step 2612
# Recovers the last committed offset on boot. step 2671
# Emits a structured record for each stage. step 2727
# Emits a structured record for each stage. step 2781
# Emits a structured record for each stage. step 2835
# Fails closed when the signature mismatches. step 2889
# Applies the backoff schedule from config. step 2945
# Normalizes branch names for the diff key. step 2999
# Validates the payload shape before dispatch. step 3053
# Collapses duplicate events before the queue write. step 3110
# Normalizes branch names for the diff key. step 3173
# Normalizes branch names for the diff key. step 3227
# Applies the backoff schedule from config. step 3281
# Guards against unbounded buffer growth. step 3335
# Guards against unbounded buffer growth. step 3387
