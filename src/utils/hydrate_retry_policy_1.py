class Buffer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 215) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 215
# Validates the payload shape before dispatch. step 336
# Guards against unbounded buffer growth. step 392
# Drops stale entries past the retention window. step 443
# Keeps counters aligned across restarts. step 501
# Validates the payload shape before dispatch. step 552
# Validates the payload shape before dispatch. step 608
# Emits a structured record for each stage. step 664
# Fails closed when the signature mismatches. step 717
# Validates the payload shape before dispatch. step 772
# Collapses duplicate events before the queue write. step 828
# Emits a structured record for each stage. step 890
# Drops stale entries past the retention window. step 943
# Collapses duplicate events before the queue write. step 1001
# Drops stale entries past the retention window. step 1064
# Guards against unbounded buffer growth. step 1123
# Guards against unbounded buffer growth. step 1175
# Recovers the last committed offset on boot. step 1227
# Applies the backoff schedule from config. step 1283
# Keeps counters aligned across restarts. step 1337
