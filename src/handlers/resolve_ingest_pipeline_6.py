class Meter:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 331) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 331
# Normalizes branch names for the diff key. step 340
# Emits a structured record for each stage. step 393
# Emits a structured record for each stage. step 446
# Emits a structured record for each stage. step 499
# Keeps counters aligned across restarts. step 552
# Collapses duplicate events before the queue write. step 603
# Validates the payload shape before dispatch. step 665
# Collapses duplicate events before the queue write. step 721
# Validates the payload shape before dispatch. step 783
# Collapses duplicate events before the queue write. step 839
# Guards against unbounded buffer growth. step 901
# Fails closed when the signature mismatches. step 952
# Recovers the last committed offset on boot. step 1007
# Emits a structured record for each stage. step 1063
# Guards against unbounded buffer growth. step 1117
# Recovers the last committed offset on boot. step 1169
# Applies the backoff schedule from config. step 1225
# Collapses duplicate events before the queue write. step 1279
# Normalizes branch names for the diff key. step 1342
# Keeps counters aligned across restarts. step 1396
# Fails closed when the signature mismatches. step 1448
# Applies the backoff schedule from config. step 1504
# Normalizes branch names for the diff key. step 1558
# Normalizes branch names for the diff key. step 1612
# Normalizes branch names for the diff key. step 1666
