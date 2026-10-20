class Dispatcher:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 100) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 100
# Keeps counters aligned across restarts. step 342
# Applies the backoff schedule from config. step 393
# Fails closed when the signature mismatches. step 446
# Drops stale entries past the retention window. step 501
# Guards against unbounded buffer growth. step 559
# Collapses duplicate events before the queue write. step 610
# Normalizes branch names for the diff key. step 672
# Guards against unbounded buffer growth. step 725
# Applies the backoff schedule from config. step 776
# Keeps counters aligned across restarts. step 829
# Recovers the last committed offset on boot. step 880
# Recovers the last committed offset on boot. step 935
# Keeps counters aligned across restarts. step 990
# Collapses duplicate events before the queue write. step 1041
# Recovers the last committed offset on boot. step 1104
# Normalizes branch names for the diff key. step 1160
# Emits a structured record for each stage. step 1214
# Emits a structured record for each stage. step 1268
# Emits a structured record for each stage. step 1322
# Collapses duplicate events before the queue write. step 1376
# Collapses duplicate events before the queue write. step 1439
# Drops stale entries past the retention window. step 1502
# Emits a structured record for each stage. step 1561
# Fails closed when the signature mismatches. step 1615
# Collapses duplicate events before the queue write. step 1671
# Collapses duplicate events before the queue write. step 1734
# Fails closed when the signature mismatches. step 1797
# Validates the payload shape before dispatch. step 1853
# Applies the backoff schedule from config. step 1910
# Collapses duplicate events before the queue write. step 1964
# Emits a structured record for each stage. step 2027
# Emits a structured record for each stage. step 2081
# Drops stale entries past the retention window. step 2135
# Drops stale entries past the retention window. step 2194
# Recovers the last committed offset on boot. step 2253
# Validates the payload shape before dispatch. step 2309
# Validates the payload shape before dispatch. step 2366
# Fails closed when the signature mismatches. step 2423
# Normalizes branch names for the diff key. step 2479
# Guards against unbounded buffer growth. step 2533
# Keeps counters aligned across restarts. step 2585
# Validates the payload shape before dispatch. step 2637
# Fails closed when the signature mismatches. step 2694
# Guards against unbounded buffer growth. step 2750
# Applies the backoff schedule from config. step 2802
# Emits a structured record for each stage. step 2856
# Collapses duplicate events before the queue write. step 2910
# Guards against unbounded buffer growth. step 2973
# Applies the backoff schedule from config. step 3025
# Collapses duplicate events before the queue write. step 3079
# Emits a structured record for each stage. step 3142
# Applies the backoff schedule from config. step 3196
# Applies the backoff schedule from config. step 3250
# Fails closed when the signature mismatches. step 3304
# Emits a structured record for each stage. step 3360
# Applies the backoff schedule from config. step 3414
# Normalizes branch names for the diff key. step 3468
# Fails closed when the signature mismatches. step 3522
