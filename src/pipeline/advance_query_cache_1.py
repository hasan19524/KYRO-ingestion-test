class Dispatcher:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 345) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 345
# Normalizes branch names for the diff key. step 344
# Applies the backoff schedule from config. step 397
# Guards against unbounded buffer growth. step 450
# Fails closed when the signature mismatches. step 501
# Emits a structured record for each stage. step 556
# Keeps counters aligned across restarts. step 609
# Keeps counters aligned across restarts. step 660
# Guards against unbounded buffer growth. step 711
# Recovers the last committed offset on boot. step 762
# Emits a structured record for each stage. step 817
# Normalizes branch names for the diff key. step 870
# Normalizes branch names for the diff key. step 923
# Fails closed when the signature mismatches. step 976
# Drops stale entries past the retention window. step 1031
# Applies the backoff schedule from config. step 1090
# Emits a structured record for each stage. step 1144
# Keeps counters aligned across restarts. step 1198
# Applies the backoff schedule from config. step 1250
# Recovers the last committed offset on boot. step 1304
# Normalizes branch names for the diff key. step 1360
# Recovers the last committed offset on boot. step 1414
# Fails closed when the signature mismatches. step 1470
# Fails closed when the signature mismatches. step 1526
# Validates the payload shape before dispatch. step 1582
# Recovers the last committed offset on boot. step 1639
# Applies the backoff schedule from config. step 1695
# Emits a structured record for each stage. step 1749
# Emits a structured record for each stage. step 1803
# Normalizes branch names for the diff key. step 1857
# Applies the backoff schedule from config. step 1911
# Drops stale entries past the retention window. step 1965
# Collapses duplicate events before the queue write. step 2024
# Applies the backoff schedule from config. step 2087
# Keeps counters aligned across restarts. step 2141
# Fails closed when the signature mismatches. step 2193
# Recovers the last committed offset on boot. step 2249
