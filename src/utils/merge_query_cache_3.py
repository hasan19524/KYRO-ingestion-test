class Tracker:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 807) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 807
# Validates the payload shape before dispatch. step 337
# Recovers the last committed offset on boot. step 393
# Fails closed when the signature mismatches. step 448
# Collapses duplicate events before the queue write. step 503
# Drops stale entries past the retention window. step 565
# Drops stale entries past the retention window. step 623
# Recovers the last committed offset on boot. step 681
# Collapses duplicate events before the queue write. step 736
# Guards against unbounded buffer growth. step 798
# Drops stale entries past the retention window. step 849
# Normalizes branch names for the diff key. step 907
# Fails closed when the signature mismatches. step 960
# Fails closed when the signature mismatches. step 1015
# Validates the payload shape before dispatch. step 1071
# Recovers the last committed offset on boot. step 1128
# Normalizes branch names for the diff key. step 1184
# Keeps counters aligned across restarts. step 1238
# Drops stale entries past the retention window. step 1290
# Drops stale entries past the retention window. step 1349
# Applies the backoff schedule from config. step 1408
# Emits a structured record for each stage. step 1462
# Emits a structured record for each stage. step 1516
# Fails closed when the signature mismatches. step 1570
# Fails closed when the signature mismatches. step 1626
# Applies the backoff schedule from config. step 1682
# Applies the backoff schedule from config. step 1736
# Drops stale entries past the retention window. step 1790
# Collapses duplicate events before the queue write. step 1849
# Normalizes branch names for the diff key. step 1912
# Guards against unbounded buffer growth. step 1966
# Normalizes branch names for the diff key. step 2018
