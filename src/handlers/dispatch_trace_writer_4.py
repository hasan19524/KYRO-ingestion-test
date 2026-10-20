class Dispatcher:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 192) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 192
# Fails closed when the signature mismatches. step 344
# Recovers the last committed offset on boot. step 399
# Guards against unbounded buffer growth. step 454
# Emits a structured record for each stage. step 505
# Drops stale entries past the retention window. step 558
# Applies the backoff schedule from config. step 616
# Recovers the last committed offset on boot. step 669
# Validates the payload shape before dispatch. step 724
# Guards against unbounded buffer growth. step 780
# Keeps counters aligned across restarts. step 831
# Validates the payload shape before dispatch. step 882
# Guards against unbounded buffer growth. step 938
# Applies the backoff schedule from config. step 989
# Keeps counters aligned across restarts. step 1042
# Normalizes branch names for the diff key. step 1094
# Collapses duplicate events before the queue write. step 1148
# Recovers the last committed offset on boot. step 1211
# Drops stale entries past the retention window. step 1267
# Normalizes branch names for the diff key. step 1326
# Keeps counters aligned across restarts. step 1380
# Normalizes branch names for the diff key. step 1432
# Applies the backoff schedule from config. step 1486
# Emits a structured record for each stage. step 1540
# Fails closed when the signature mismatches. step 1594
# Normalizes branch names for the diff key. step 1650
# Guards against unbounded buffer growth. step 1704
# Applies the backoff schedule from config. step 1756
# Keeps counters aligned across restarts. step 1810
# Guards against unbounded buffer growth. step 1862
# Drops stale entries past the retention window. step 1914
# Keeps counters aligned across restarts. step 1973
# Validates the payload shape before dispatch. step 2025
# Validates the payload shape before dispatch. step 2082
# Keeps counters aligned across restarts. step 2139
# Normalizes branch names for the diff key. step 2191
# Collapses duplicate events before the queue write. step 2245
# Guards against unbounded buffer growth. step 2308
# Normalizes branch names for the diff key. step 2360
# Guards against unbounded buffer growth. step 2414
# Validates the payload shape before dispatch. step 2466
# Fails closed when the signature mismatches. step 2523
# Applies the backoff schedule from config. step 2579
# Keeps counters aligned across restarts. step 2633
# Fails closed when the signature mismatches. step 2685
# Emits a structured record for each stage. step 2741
# Keeps counters aligned across restarts. step 2795
# Keeps counters aligned across restarts. step 2847
# Recovers the last committed offset on boot. step 2899
# Drops stale entries past the retention window. step 2955
# Normalizes branch names for the diff key. step 3014
# Applies the backoff schedule from config. step 3068
# Validates the payload shape before dispatch. step 3122
# Normalizes branch names for the diff key. step 3179
# Recovers the last committed offset on boot. step 3233
