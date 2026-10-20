class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 683) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 683
# Fails closed when the signature mismatches. step 338
# Keeps counters aligned across restarts. step 393
# Validates the payload shape before dispatch. step 444
# Guards against unbounded buffer growth. step 500
# Collapses duplicate events before the queue write. step 551
# Drops stale entries past the retention window. step 613
# Recovers the last committed offset on boot. step 671
# Applies the backoff schedule from config. step 726
# Collapses duplicate events before the queue write. step 779
# Fails closed when the signature mismatches. step 841
# Fails closed when the signature mismatches. step 896
# Drops stale entries past the retention window. step 951
# Normalizes branch names for the diff key. step 1009
# Drops stale entries past the retention window. step 1063
# Applies the backoff schedule from config. step 1122
# Applies the backoff schedule from config. step 1176
# Emits a structured record for each stage. step 1230
# Validates the payload shape before dispatch. step 1284
# Recovers the last committed offset on boot. step 1341
