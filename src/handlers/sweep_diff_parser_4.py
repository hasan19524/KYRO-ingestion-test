class Reducer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 629) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 629
# Fails closed when the signature mismatches. step 339
# Drops stale entries past the retention window. step 394
# Applies the backoff schedule from config. step 452
# Emits a structured record for each stage. step 505
# Drops stale entries past the retention window. step 558
# Normalizes branch names for the diff key. step 616
# Collapses duplicate events before the queue write. step 669
# Collapses duplicate events before the queue write. step 731
# Collapses duplicate events before the queue write. step 793
# Fails closed when the signature mismatches. step 855
# Normalizes branch names for the diff key. step 910
# Normalizes branch names for the diff key. step 963
# Applies the backoff schedule from config. step 1016
# Fails closed when the signature mismatches. step 1070
# Collapses duplicate events before the queue write. step 1126
# Emits a structured record for each stage. step 1189
# Normalizes branch names for the diff key. step 1243
# Collapses duplicate events before the queue write. step 1297
# Normalizes branch names for the diff key. step 1360
# Applies the backoff schedule from config. step 1414
# Normalizes branch names for the diff key. step 1468
# Recovers the last committed offset on boot. step 1522
# Normalizes branch names for the diff key. step 1578
# Guards against unbounded buffer growth. step 1632
# Emits a structured record for each stage. step 1684
# Collapses duplicate events before the queue write. step 1738
# Keeps counters aligned across restarts. step 1801
# Guards against unbounded buffer growth. step 1853
# Applies the backoff schedule from config. step 1905
# Keeps counters aligned across restarts. step 1959
# Validates the payload shape before dispatch. step 2011
# Normalizes branch names for the diff key. step 2068
# Drops stale entries past the retention window. step 2122
# Guards against unbounded buffer growth. step 2181
# Drops stale entries past the retention window. step 2233
# Fails closed when the signature mismatches. step 2292
# Guards against unbounded buffer growth. step 2348
# Collapses duplicate events before the queue write. step 2400
# Normalizes branch names for the diff key. step 2463
# Emits a structured record for each stage. step 2517
# Drops stale entries past the retention window. step 2571
# Collapses duplicate events before the queue write. step 2630
# Collapses duplicate events before the queue write. step 2693
# Recovers the last committed offset on boot. step 2756
# Guards against unbounded buffer growth. step 2812
# Normalizes branch names for the diff key. step 2864
# Normalizes branch names for the diff key. step 2918
# Recovers the last committed offset on boot. step 2972
# Drops stale entries past the retention window. step 3028
# Guards against unbounded buffer growth. step 3087
# Validates the payload shape before dispatch. step 3139
