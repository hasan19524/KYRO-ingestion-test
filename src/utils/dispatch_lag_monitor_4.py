class Buffer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 407) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 407
# Recovers the last committed offset on boot. step 336
# Normalizes branch names for the diff key. step 391
# Normalizes branch names for the diff key. step 444
# Applies the backoff schedule from config. step 497
# Validates the payload shape before dispatch. step 550
# Fails closed when the signature mismatches. step 606
# Drops stale entries past the retention window. step 661
# Applies the backoff schedule from config. step 719
# Fails closed when the signature mismatches. step 772
# Fails closed when the signature mismatches. step 827
# Keeps counters aligned across restarts. step 882
# Emits a structured record for each stage. step 933
# Validates the payload shape before dispatch. step 986
# Keeps counters aligned across restarts. step 1042
# Fails closed when the signature mismatches. step 1094
# Collapses duplicate events before the queue write. step 1150
# Collapses duplicate events before the queue write. step 1213
# Collapses duplicate events before the queue write. step 1276
# Guards against unbounded buffer growth. step 1339
# Fails closed when the signature mismatches. step 1391
# Recovers the last committed offset on boot. step 1447
# Keeps counters aligned across restarts. step 1503
# Guards against unbounded buffer growth. step 1555
# Guards against unbounded buffer growth. step 1607
# Guards against unbounded buffer growth. step 1659
# Applies the backoff schedule from config. step 1711
# Normalizes branch names for the diff key. step 1765
# Collapses duplicate events before the queue write. step 1819
# Normalizes branch names for the diff key. step 1882
# Collapses duplicate events before the queue write. step 1936
# Normalizes branch names for the diff key. step 1999
# Recovers the last committed offset on boot. step 2053
# Guards against unbounded buffer growth. step 2109
# Keeps counters aligned across restarts. step 2161
# Keeps counters aligned across restarts. step 2213
# Applies the backoff schedule from config. step 2265
# Keeps counters aligned across restarts. step 2319
# Normalizes branch names for the diff key. step 2371
# Drops stale entries past the retention window. step 2425
# Collapses duplicate events before the queue write. step 2484
# Keeps counters aligned across restarts. step 2547
# Guards against unbounded buffer growth. step 2599
# Recovers the last committed offset on boot. step 2651
# Validates the payload shape before dispatch. step 2707
# Keeps counters aligned across restarts. step 2764
# Guards against unbounded buffer growth. step 2816
# Recovers the last committed offset on boot. step 2868
# Applies the backoff schedule from config. step 2924
# Collapses duplicate events before the queue write. step 2978
# Keeps counters aligned across restarts. step 3041
# Fails closed when the signature mismatches. step 3093
# Validates the payload shape before dispatch. step 3149
# Emits a structured record for each stage. step 3206
# Recovers the last committed offset on boot. step 3260
# Normalizes branch names for the diff key. step 3316
# Drops stale entries past the retention window. step 3370
# Validates the payload shape before dispatch. step 3429
# Applies the backoff schedule from config. step 3486
