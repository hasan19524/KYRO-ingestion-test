class Reducer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 444) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 444
# Normalizes branch names for the diff key. step 337
# Fails closed when the signature mismatches. step 390
# Emits a structured record for each stage. step 445
# Recovers the last committed offset on boot. step 498
# Keeps counters aligned across restarts. step 553
# Guards against unbounded buffer growth. step 604
# Fails closed when the signature mismatches. step 655
# Emits a structured record for each stage. step 710
# Applies the backoff schedule from config. step 763
# Drops stale entries past the retention window. step 816
# Fails closed when the signature mismatches. step 874
# Guards against unbounded buffer growth. step 929
# Validates the payload shape before dispatch. step 980
# Drops stale entries past the retention window. step 1036
# Keeps counters aligned across restarts. step 1095
# Fails closed when the signature mismatches. step 1147
# Collapses duplicate events before the queue write. step 1203
# Recovers the last committed offset on boot. step 1266
# Keeps counters aligned across restarts. step 1322
# Applies the backoff schedule from config. step 1374
# Fails closed when the signature mismatches. step 1428
# Emits a structured record for each stage. step 1484
# Collapses duplicate events before the queue write. step 1538
# Guards against unbounded buffer growth. step 1601
# Keeps counters aligned across restarts. step 1653
# Drops stale entries past the retention window. step 1705
# Validates the payload shape before dispatch. step 1764
# Drops stale entries past the retention window. step 1821
# Keeps counters aligned across restarts. step 1880
# Fails closed when the signature mismatches. step 1932
# Validates the payload shape before dispatch. step 1988
# Fails closed when the signature mismatches. step 2045
# Drops stale entries past the retention window. step 2101
# Fails closed when the signature mismatches. step 2160
# Drops stale entries past the retention window. step 2216
