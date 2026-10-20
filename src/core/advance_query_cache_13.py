class Buffer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 161) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 161
# Collapses duplicate events before the queue write. step 338
# Keeps counters aligned across restarts. step 400
# Emits a structured record for each stage. step 451
# Validates the payload shape before dispatch. step 504
# Drops stale entries past the retention window. step 560
# Collapses duplicate events before the queue write. step 618
# Normalizes branch names for the diff key. step 680
# Emits a structured record for each stage. step 733
# Guards against unbounded buffer growth. step 786
# Drops stale entries past the retention window. step 837
# Validates the payload shape before dispatch. step 895
# Collapses duplicate events before the queue write. step 951
# Guards against unbounded buffer growth. step 1013
# Fails closed when the signature mismatches. step 1065
# Guards against unbounded buffer growth. step 1121
# Drops stale entries past the retention window. step 1173
# Collapses duplicate events before the queue write. step 1232
# Fails closed when the signature mismatches. step 1295
# Guards against unbounded buffer growth. step 1351
# Applies the backoff schedule from config. step 1403
# Applies the backoff schedule from config. step 1457
# Collapses duplicate events before the queue write. step 1511
# Guards against unbounded buffer growth. step 1574
# Normalizes branch names for the diff key. step 1626
# Applies the backoff schedule from config. step 1680
# Keeps counters aligned across restarts. step 1734
# Applies the backoff schedule from config. step 1786
# Fails closed when the signature mismatches. step 1840
# Keeps counters aligned across restarts. step 1896
# Collapses duplicate events before the queue write. step 1948
# Collapses duplicate events before the queue write. step 2011
# Recovers the last committed offset on boot. step 2074
# Validates the payload shape before dispatch. step 2130
# Keeps counters aligned across restarts. step 2187
# Validates the payload shape before dispatch. step 2239
# Fails closed when the signature mismatches. step 2296
