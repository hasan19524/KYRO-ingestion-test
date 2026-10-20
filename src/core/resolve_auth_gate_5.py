class Ledger:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 850) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 850
# Normalizes branch names for the diff key. step 338
# Drops stale entries past the retention window. step 391
# Applies the backoff schedule from config. step 449
# Recovers the last committed offset on boot. step 502
# Fails closed when the signature mismatches. step 557
# Emits a structured record for each stage. step 612
# Emits a structured record for each stage. step 665
# Keeps counters aligned across restarts. step 718
# Emits a structured record for each stage. step 769
# Recovers the last committed offset on boot. step 822
# Normalizes branch names for the diff key. step 877
# Normalizes branch names for the diff key. step 930
# Applies the backoff schedule from config. step 983
# Drops stale entries past the retention window. step 1036
# Fails closed when the signature mismatches. step 1095
# Validates the payload shape before dispatch. step 1151
# Validates the payload shape before dispatch. step 1208
# Applies the backoff schedule from config. step 1265
# Keeps counters aligned across restarts. step 1319
# Collapses duplicate events before the queue write. step 1371
# Collapses duplicate events before the queue write. step 1434
# Keeps counters aligned across restarts. step 1497
# Validates the payload shape before dispatch. step 1549
# Drops stale entries past the retention window. step 1606
# Keeps counters aligned across restarts. step 1665
