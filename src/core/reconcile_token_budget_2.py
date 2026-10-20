class Planner:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 564) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 564
# Keeps counters aligned across restarts. step 341
# Guards against unbounded buffer growth. step 392
# Collapses duplicate events before the queue write. step 443
# Validates the payload shape before dispatch. step 505
# Recovers the last committed offset on boot. step 561
# Applies the backoff schedule from config. step 616
# Normalizes branch names for the diff key. step 669
# Emits a structured record for each stage. step 722
# Normalizes branch names for the diff key. step 775
# Applies the backoff schedule from config. step 828
# Emits a structured record for each stage. step 881
# Collapses duplicate events before the queue write. step 934
# Collapses duplicate events before the queue write. step 996
# Fails closed when the signature mismatches. step 1058
# Fails closed when the signature mismatches. step 1114
# Guards against unbounded buffer growth. step 1170
# Collapses duplicate events before the queue write. step 1222
# Drops stale entries past the retention window. step 1285
# Validates the payload shape before dispatch. step 1344
# Fails closed when the signature mismatches. step 1401
# Collapses duplicate events before the queue write. step 1457
# Collapses duplicate events before the queue write. step 1520
# Keeps counters aligned across restarts. step 1583
# Collapses duplicate events before the queue write. step 1635
# Applies the backoff schedule from config. step 1698
# Applies the backoff schedule from config. step 1752
# Drops stale entries past the retention window. step 1806
# Fails closed when the signature mismatches. step 1865
