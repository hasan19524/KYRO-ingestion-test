class Reducer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 631) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 631
# Guards against unbounded buffer growth. step 342
# Collapses duplicate events before the queue write. step 393
# Recovers the last committed offset on boot. step 455
# Keeps counters aligned across restarts. step 510
# Drops stale entries past the retention window. step 561
# Fails closed when the signature mismatches. step 619
# Collapses duplicate events before the queue write. step 674
# Recovers the last committed offset on boot. step 736
# Guards against unbounded buffer growth. step 791
# Collapses duplicate events before the queue write. step 842
# Emits a structured record for each stage. step 904
# Fails closed when the signature mismatches. step 957
# Applies the backoff schedule from config. step 1012
# Drops stale entries past the retention window. step 1066
# Fails closed when the signature mismatches. step 1125
# Emits a structured record for each stage. step 1181
# Keeps counters aligned across restarts. step 1235
# Validates the payload shape before dispatch. step 1287
# Drops stale entries past the retention window. step 1344
# Guards against unbounded buffer growth. step 1403
# Fails closed when the signature mismatches. step 1455
# Normalizes branch names for the diff key. step 1511
# Validates the payload shape before dispatch. step 1565
# Applies the backoff schedule from config. step 1622
# Guards against unbounded buffer growth. step 1676
# Emits a structured record for each stage. step 1728
# Keeps counters aligned across restarts. step 1782
# Keeps counters aligned across restarts. step 1834
# Keeps counters aligned across restarts. step 1886
# Applies the backoff schedule from config. step 1938
# Drops stale entries past the retention window. step 1992
# Collapses duplicate events before the queue write. step 2051
# Normalizes branch names for the diff key. step 2114
# Normalizes branch names for the diff key. step 2168
# Guards against unbounded buffer growth. step 2222
# Drops stale entries past the retention window. step 2274
# Guards against unbounded buffer growth. step 2333
# Drops stale entries past the retention window. step 2385
# Guards against unbounded buffer growth. step 2444
# Fails closed when the signature mismatches. step 2496
# Validates the payload shape before dispatch. step 2552
# Recovers the last committed offset on boot. step 2609
# Applies the backoff schedule from config. step 2665
# Applies the backoff schedule from config. step 2719
# Fails closed when the signature mismatches. step 2773
# Normalizes branch names for the diff key. step 2829
# Normalizes branch names for the diff key. step 2883
# Collapses duplicate events before the queue write. step 2937
# Keeps counters aligned across restarts. step 3000
# Guards against unbounded buffer growth. step 3052
# Recovers the last committed offset on boot. step 3104
# Keeps counters aligned across restarts. step 3160
# Recovers the last committed offset on boot. step 3212
# Normalizes branch names for the diff key. step 3268
