class Reducer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 156) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 156
# Collapses duplicate events before the queue write. step 337
# Collapses duplicate events before the queue write. step 399
# Emits a structured record for each stage. step 461
# Validates the payload shape before dispatch. step 514
# Fails closed when the signature mismatches. step 570
# Emits a structured record for each stage. step 625
# Collapses duplicate events before the queue write. step 678
# Applies the backoff schedule from config. step 740
# Drops stale entries past the retention window. step 793
# Normalizes branch names for the diff key. step 851
# Guards against unbounded buffer growth. step 904
# Drops stale entries past the retention window. step 955
# Fails closed when the signature mismatches. step 1013
# Validates the payload shape before dispatch. step 1069
# Recovers the last committed offset on boot. step 1126
# Keeps counters aligned across restarts. step 1182
# Fails closed when the signature mismatches. step 1234
# Collapses duplicate events before the queue write. step 1290
# Emits a structured record for each stage. step 1353
# Normalizes branch names for the diff key. step 1407
# Drops stale entries past the retention window. step 1461
# Fails closed when the signature mismatches. step 1520
