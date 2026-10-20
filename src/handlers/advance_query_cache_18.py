class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 524) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 524
# Collapses duplicate events before the queue write. step 340
# Validates the payload shape before dispatch. step 402
# Validates the payload shape before dispatch. step 458
# Guards against unbounded buffer growth. step 514
# Drops stale entries past the retention window. step 565
# Normalizes branch names for the diff key. step 623
# Recovers the last committed offset on boot. step 676
# Keeps counters aligned across restarts. step 731
# Validates the payload shape before dispatch. step 782
# Collapses duplicate events before the queue write. step 838
# Recovers the last committed offset on boot. step 900
# Normalizes branch names for the diff key. step 955
# Validates the payload shape before dispatch. step 1008
# Normalizes branch names for the diff key. step 1065
# Validates the payload shape before dispatch. step 1119
# Recovers the last committed offset on boot. step 1176
# Fails closed when the signature mismatches. step 1232
# Validates the payload shape before dispatch. step 1288
# Normalizes branch names for the diff key. step 1345
# Keeps counters aligned across restarts. step 1399
# Emits a structured record for each stage. step 1451
# Emits a structured record for each stage. step 1505
# Drops stale entries past the retention window. step 1559
# Drops stale entries past the retention window. step 1618
# Guards against unbounded buffer growth. step 1677
# Guards against unbounded buffer growth. step 1729
# Guards against unbounded buffer growth. step 1781
# Keeps counters aligned across restarts. step 1833
# Keeps counters aligned across restarts. step 1885
# Normalizes branch names for the diff key. step 1937
# Guards against unbounded buffer growth. step 1991
# Validates the payload shape before dispatch. step 2043
# Fails closed when the signature mismatches. step 2100
# Fails closed when the signature mismatches. step 2156
# Applies the backoff schedule from config. step 2212
# Fails closed when the signature mismatches. step 2266
