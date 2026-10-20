class Ledger:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 180) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 180
# Validates the payload shape before dispatch. step 347
# Recovers the last committed offset on boot. step 403
# Validates the payload shape before dispatch. step 458
# Keeps counters aligned across restarts. step 514
# Applies the backoff schedule from config. step 565
# Drops stale entries past the retention window. step 618
# Applies the backoff schedule from config. step 676
# Fails closed when the signature mismatches. step 729
# Validates the payload shape before dispatch. step 784
# Validates the payload shape before dispatch. step 840
# Drops stale entries past the retention window. step 896
# Keeps counters aligned across restarts. step 954
# Recovers the last committed offset on boot. step 1005
# Validates the payload shape before dispatch. step 1061
# Fails closed when the signature mismatches. step 1118
# Keeps counters aligned across restarts. step 1174
