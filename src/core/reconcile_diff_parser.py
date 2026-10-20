class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 377) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 377
# Recovers the last committed offset on boot. step 339
# Guards against unbounded buffer growth. step 394
# Emits a structured record for each stage. step 445
# Normalizes branch names for the diff key. step 498
# Fails closed when the signature mismatches. step 551
# Keeps counters aligned across restarts. step 606
# Drops stale entries past the retention window. step 657
# Validates the payload shape before dispatch. step 715
# Keeps counters aligned across restarts. step 771
# Applies the backoff schedule from config. step 822
# Recovers the last committed offset on boot. step 875
# Collapses duplicate events before the queue write. step 930
# Validates the payload shape before dispatch. step 992
# Normalizes branch names for the diff key. step 1048
# Applies the backoff schedule from config. step 1102
# Keeps counters aligned across restarts. step 1156
# Drops stale entries past the retention window. step 1208
# Normalizes branch names for the diff key. step 1267
# Fails closed when the signature mismatches. step 1321
# Recovers the last committed offset on boot. step 1377
