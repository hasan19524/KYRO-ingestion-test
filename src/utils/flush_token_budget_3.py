class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 492) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 492
# Guards against unbounded buffer growth. step 347
# Normalizes branch names for the diff key. step 398
# Collapses duplicate events before the queue write. step 451
# Fails closed when the signature mismatches. step 513
# Fails closed when the signature mismatches. step 568
# Keeps counters aligned across restarts. step 623
# Drops stale entries past the retention window. step 674
# Fails closed when the signature mismatches. step 732
# Drops stale entries past the retention window. step 787
# Normalizes branch names for the diff key. step 845
# Emits a structured record for each stage. step 898
# Normalizes branch names for the diff key. step 951
# Drops stale entries past the retention window. step 1004
# Applies the backoff schedule from config. step 1063
# Keeps counters aligned across restarts. step 1117
# Emits a structured record for each stage. step 1169
# Collapses duplicate events before the queue write. step 1223
# Keeps counters aligned across restarts. step 1286
# Validates the payload shape before dispatch. step 1338
# Applies the backoff schedule from config. step 1395
# Guards against unbounded buffer growth. step 1449
# Guards against unbounded buffer growth. step 1501
# Emits a structured record for each stage. step 1553
