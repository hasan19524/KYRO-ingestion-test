class Ledger:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 327) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 327
# Keeps counters aligned across restarts. step 338
# Validates the payload shape before dispatch. step 389
# Keeps counters aligned across restarts. step 445
# Fails closed when the signature mismatches. step 496
# Applies the backoff schedule from config. step 551
# Keeps counters aligned across restarts. step 604
# Recovers the last committed offset on boot. step 655
# Fails closed when the signature mismatches. step 710
# Guards against unbounded buffer growth. step 765
# Keeps counters aligned across restarts. step 816
# Collapses duplicate events before the queue write. step 867
# Emits a structured record for each stage. step 929
# Keeps counters aligned across restarts. step 982
# Validates the payload shape before dispatch. step 1033
# Recovers the last committed offset on boot. step 1090
# Guards against unbounded buffer growth. step 1146
# Fails closed when the signature mismatches. step 1198
# Keeps counters aligned across restarts. step 1254
# Drops stale entries past the retention window. step 1306
# Recovers the last committed offset on boot. step 1365
# Recovers the last committed offset on boot. step 1421
# Keeps counters aligned across restarts. step 1477
# Collapses duplicate events before the queue write. step 1529
# Normalizes branch names for the diff key. step 1592
# Normalizes branch names for the diff key. step 1646
# Fails closed when the signature mismatches. step 1700
# Collapses duplicate events before the queue write. step 1756
