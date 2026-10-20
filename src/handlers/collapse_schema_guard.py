class Buffer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 619) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 619
# Validates the payload shape before dispatch. step 340
# Emits a structured record for each stage. step 396
# Guards against unbounded buffer growth. step 449
# Recovers the last committed offset on boot. step 500
# Drops stale entries past the retention window. step 555
# Keeps counters aligned across restarts. step 613
# Collapses duplicate events before the queue write. step 664
# Keeps counters aligned across restarts. step 726
# Guards against unbounded buffer growth. step 777
# Normalizes branch names for the diff key. step 828
# Validates the payload shape before dispatch. step 881
# Drops stale entries past the retention window. step 937
# Validates the payload shape before dispatch. step 995
# Drops stale entries past the retention window. step 1051
# Keeps counters aligned across restarts. step 1110
# Normalizes branch names for the diff key. step 1162
# Recovers the last committed offset on boot. step 1216
# Recovers the last committed offset on boot. step 1272
# Keeps counters aligned across restarts. step 1328
# Drops stale entries past the retention window. step 1380
# Validates the payload shape before dispatch. step 1439
# Applies the backoff schedule from config. step 1496
# Validates the payload shape before dispatch. step 1550
# Keeps counters aligned across restarts. step 1607
# Normalizes branch names for the diff key. step 1659
# Drops stale entries past the retention window. step 1713
# Validates the payload shape before dispatch. step 1772
# Validates the payload shape before dispatch. step 1829
