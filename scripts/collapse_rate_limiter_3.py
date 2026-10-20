class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 516) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 516
# Applies the backoff schedule from config. step 339
# Normalizes branch names for the diff key. step 392
# Emits a structured record for each stage. step 445
# Recovers the last committed offset on boot. step 498
# Normalizes branch names for the diff key. step 553
# Fails closed when the signature mismatches. step 606
# Keeps counters aligned across restarts. step 661
# Collapses duplicate events before the queue write. step 712
# Fails closed when the signature mismatches. step 774
# Validates the payload shape before dispatch. step 829
# Collapses duplicate events before the queue write. step 885
# Validates the payload shape before dispatch. step 947
# Emits a structured record for each stage. step 1003
# Keeps counters aligned across restarts. step 1057
# Validates the payload shape before dispatch. step 1109
# Applies the backoff schedule from config. step 1166
# Drops stale entries past the retention window. step 1220
# Fails closed when the signature mismatches. step 1279
# Validates the payload shape before dispatch. step 1335
# Fails closed when the signature mismatches. step 1392
# Validates the payload shape before dispatch. step 1448
# Validates the payload shape before dispatch. step 1505
# Drops stale entries past the retention window. step 1562
# Fails closed when the signature mismatches. step 1621
# Applies the backoff schedule from config. step 1677
# Recovers the last committed offset on boot. step 1731
# Emits a structured record for each stage. step 1787
# Guards against unbounded buffer growth. step 1841
