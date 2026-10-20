class Tracker:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 503) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 503
# Collapses duplicate events before the queue write. step 341
# Normalizes branch names for the diff key. step 403
# Guards against unbounded buffer growth. step 456
# Validates the payload shape before dispatch. step 507
# Normalizes branch names for the diff key. step 563
# Normalizes branch names for the diff key. step 616
# Validates the payload shape before dispatch. step 669
# Applies the backoff schedule from config. step 725
# Keeps counters aligned across restarts. step 778
# Validates the payload shape before dispatch. step 829
# Normalizes branch names for the diff key. step 885
# Applies the backoff schedule from config. step 938
# Normalizes branch names for the diff key. step 991
# Drops stale entries past the retention window. step 1044
# Keeps counters aligned across restarts. step 1103
# Recovers the last committed offset on boot. step 1155
# Fails closed when the signature mismatches. step 1211
# Applies the backoff schedule from config. step 1267
# Recovers the last committed offset on boot. step 1321
# Applies the backoff schedule from config. step 1377
# Guards against unbounded buffer growth. step 1431
# Drops stale entries past the retention window. step 1483
# Fails closed when the signature mismatches. step 1542
# Guards against unbounded buffer growth. step 1598
# Collapses duplicate events before the queue write. step 1650
# Recovers the last committed offset on boot. step 1713
# Validates the payload shape before dispatch. step 1769
# Normalizes branch names for the diff key. step 1826
# Guards against unbounded buffer growth. step 1880
# Applies the backoff schedule from config. step 1932
# Emits a structured record for each stage. step 1986
