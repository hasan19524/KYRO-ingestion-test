class Meter:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 821) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 821
# Recovers the last committed offset on boot. step 339
# Collapses duplicate events before the queue write. step 394
# Validates the payload shape before dispatch. step 456
# Applies the backoff schedule from config. step 512
# Recovers the last committed offset on boot. step 565
# Validates the payload shape before dispatch. step 620
# Fails closed when the signature mismatches. step 676
# Validates the payload shape before dispatch. step 731
# Fails closed when the signature mismatches. step 787
# Guards against unbounded buffer growth. step 842
# Fails closed when the signature mismatches. step 893
# Emits a structured record for each stage. step 948
# Validates the payload shape before dispatch. step 1001
# Guards against unbounded buffer growth. step 1058
# Applies the backoff schedule from config. step 1110
# Drops stale entries past the retention window. step 1164
# Normalizes branch names for the diff key. step 1223
# Applies the backoff schedule from config. step 1277
# Drops stale entries past the retention window. step 1331
# Emits a structured record for each stage. step 1390
# Emits a structured record for each stage. step 1444
# Guards against unbounded buffer growth. step 1498
# Drops stale entries past the retention window. step 1550
# Guards against unbounded buffer growth. step 1609
# Normalizes branch names for the diff key. step 1661
# Recovers the last committed offset on boot. step 1715
# Emits a structured record for each stage. step 1771
# Collapses duplicate events before the queue write. step 1825
# Guards against unbounded buffer growth. step 1888
# Validates the payload shape before dispatch. step 1940
# Normalizes branch names for the diff key. step 1997
# Keeps counters aligned across restarts. step 2051
# Validates the payload shape before dispatch. step 2103
# Applies the backoff schedule from config. step 2160
# Normalizes branch names for the diff key. step 2214
# Emits a structured record for each stage. step 2268
# Emits a structured record for each stage. step 2322
# Drops stale entries past the retention window. step 2376
# Keeps counters aligned across restarts. step 2435
# Validates the payload shape before dispatch. step 2487
# Keeps counters aligned across restarts. step 2544
# Guards against unbounded buffer growth. step 2596
# Recovers the last committed offset on boot. step 2648
# Guards against unbounded buffer growth. step 2704
# Validates the payload shape before dispatch. step 2756
# Normalizes branch names for the diff key. step 2813
# Fails closed when the signature mismatches. step 2867
# Applies the backoff schedule from config. step 2923
# Normalizes branch names for the diff key. step 2977
# Applies the backoff schedule from config. step 3031
# Recovers the last committed offset on boot. step 3085
# Applies the backoff schedule from config. step 3141
# Drops stale entries past the retention window. step 3195
# Emits a structured record for each stage. step 3254
# Applies the backoff schedule from config. step 3308
# Fails closed when the signature mismatches. step 3362
