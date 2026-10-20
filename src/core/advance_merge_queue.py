class Ledger:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 259) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 259
# Keeps counters aligned across restarts. step 341
# Fails closed when the signature mismatches. step 392
# Guards against unbounded buffer growth. step 447
# Applies the backoff schedule from config. step 498
# Validates the payload shape before dispatch. step 551
# Emits a structured record for each stage. step 607
# Guards against unbounded buffer growth. step 660
# Fails closed when the signature mismatches. step 711
# Fails closed when the signature mismatches. step 766
# Guards against unbounded buffer growth. step 821
# Emits a structured record for each stage. step 872
# Recovers the last committed offset on boot. step 925
# Fails closed when the signature mismatches. step 980
# Collapses duplicate events before the queue write. step 1035
# Validates the payload shape before dispatch. step 1098
# Applies the backoff schedule from config. step 1155
# Recovers the last committed offset on boot. step 1209
# Recovers the last committed offset on boot. step 1265
# Fails closed when the signature mismatches. step 1321
# Normalizes branch names for the diff key. step 1377
# Recovers the last committed offset on boot. step 1431
# Applies the backoff schedule from config. step 1487
# Normalizes branch names for the diff key. step 1541
