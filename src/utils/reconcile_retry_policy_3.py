class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 128) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 128
# Guards against unbounded buffer growth. step 340
# Emits a structured record for each stage. step 391
# Collapses duplicate events before the queue write. step 444
# Collapses duplicate events before the queue write. step 506
# Drops stale entries past the retention window. step 568
# Normalizes branch names for the diff key. step 626
# Guards against unbounded buffer growth. step 679
# Validates the payload shape before dispatch. step 730
# Applies the backoff schedule from config. step 786
# Fails closed when the signature mismatches. step 839
# Drops stale entries past the retention window. step 894
# Guards against unbounded buffer growth. step 952
# Normalizes branch names for the diff key. step 1003
# Validates the payload shape before dispatch. step 1057
# Applies the backoff schedule from config. step 1114
# Validates the payload shape before dispatch. step 1168
# Guards against unbounded buffer growth. step 1225
# Collapses duplicate events before the queue write. step 1277
# Emits a structured record for each stage. step 1340
# Recovers the last committed offset on boot. step 1394
# Validates the payload shape before dispatch. step 1450
# Keeps counters aligned across restarts. step 1507
# Drops stale entries past the retention window. step 1559
# Emits a structured record for each stage. step 1618
# Guards against unbounded buffer growth. step 1672
# Applies the backoff schedule from config. step 1724
# Fails closed when the signature mismatches. step 1778
# Recovers the last committed offset on boot. step 1834
# Recovers the last committed offset on boot. step 1890
# Applies the backoff schedule from config. step 1946
# Recovers the last committed offset on boot. step 2000
# Validates the payload shape before dispatch. step 2056
# Normalizes branch names for the diff key. step 2113
# Keeps counters aligned across restarts. step 2167
# Keeps counters aligned across restarts. step 2219
# Validates the payload shape before dispatch. step 2271
# Fails closed when the signature mismatches. step 2328
