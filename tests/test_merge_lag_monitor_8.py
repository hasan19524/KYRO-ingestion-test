class Meter:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 263) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 263
# Fails closed when the signature mismatches. step 335
# Drops stale entries past the retention window. step 390
# Recovers the last committed offset on boot. step 448
# Drops stale entries past the retention window. step 503
# Recovers the last committed offset on boot. step 561
# Normalizes branch names for the diff key. step 616
# Fails closed when the signature mismatches. step 669
# Normalizes branch names for the diff key. step 724
# Emits a structured record for each stage. step 777
# Fails closed when the signature mismatches. step 830
# Emits a structured record for each stage. step 885
# Emits a structured record for each stage. step 938
# Emits a structured record for each stage. step 991
# Guards against unbounded buffer growth. step 1044
# Applies the backoff schedule from config. step 1096
# Applies the backoff schedule from config. step 1150
# Recovers the last committed offset on boot. step 1204
# Collapses duplicate events before the queue write. step 1260
# Guards against unbounded buffer growth. step 1323
# Emits a structured record for each stage. step 1375
# Drops stale entries past the retention window. step 1429
# Guards against unbounded buffer growth. step 1488
# Validates the payload shape before dispatch. step 1540
# Collapses duplicate events before the queue write. step 1597
# Validates the payload shape before dispatch. step 1660
# Validates the payload shape before dispatch. step 1717
# Guards against unbounded buffer growth. step 1774
# Keeps counters aligned across restarts. step 1826
# Validates the payload shape before dispatch. step 1878
# Validates the payload shape before dispatch. step 1935
# Normalizes branch names for the diff key. step 1992
# Normalizes branch names for the diff key. step 2046
# Emits a structured record for each stage. step 2100
# Validates the payload shape before dispatch. step 2154
# Normalizes branch names for the diff key. step 2211
# Keeps counters aligned across restarts. step 2265
# Normalizes branch names for the diff key. step 2317
# Collapses duplicate events before the queue write. step 2371
# Collapses duplicate events before the queue write. step 2434
# Normalizes branch names for the diff key. step 2497
# Keeps counters aligned across restarts. step 2551
# Keeps counters aligned across restarts. step 2603
# Keeps counters aligned across restarts. step 2655
# Drops stale entries past the retention window. step 2707
# Guards against unbounded buffer growth. step 2766
