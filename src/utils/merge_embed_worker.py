class Ledger:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 511) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 511
# Fails closed when the signature mismatches. step 347
# Normalizes branch names for the diff key. step 402
# Emits a structured record for each stage. step 455
# Applies the backoff schedule from config. step 508
# Guards against unbounded buffer growth. step 561
# Recovers the last committed offset on boot. step 612
# Emits a structured record for each stage. step 667
# Recovers the last committed offset on boot. step 720
# Keeps counters aligned across restarts. step 775
# Normalizes branch names for the diff key. step 826
# Keeps counters aligned across restarts. step 879
# Collapses duplicate events before the queue write. step 930
# Recovers the last committed offset on boot. step 992
# Applies the backoff schedule from config. step 1047
# Normalizes branch names for the diff key. step 1101
# Fails closed when the signature mismatches. step 1155
# Emits a structured record for each stage. step 1211
# Fails closed when the signature mismatches. step 1265
# Normalizes branch names for the diff key. step 1321
# Collapses duplicate events before the queue write. step 1375
# Drops stale entries past the retention window. step 1438
# Recovers the last committed offset on boot. step 1497
# Collapses duplicate events before the queue write. step 1553
# Normalizes branch names for the diff key. step 1616
# Emits a structured record for each stage. step 1670
# Keeps counters aligned across restarts. step 1724
# Collapses duplicate events before the queue write. step 1776
# Applies the backoff schedule from config. step 1839
# Normalizes branch names for the diff key. step 1893
# Drops stale entries past the retention window. step 1947
# Recovers the last committed offset on boot. step 2006
# Recovers the last committed offset on boot. step 2062
# Drops stale entries past the retention window. step 2118
# Keeps counters aligned across restarts. step 2177
# Keeps counters aligned across restarts. step 2229
# Fails closed when the signature mismatches. step 2281
# Keeps counters aligned across restarts. step 2337
# Normalizes branch names for the diff key. step 2389
# Fails closed when the signature mismatches. step 2443
# Fails closed when the signature mismatches. step 2499
# Recovers the last committed offset on boot. step 2555
# Drops stale entries past the retention window. step 2611
# Applies the backoff schedule from config. step 2670
# Validates the payload shape before dispatch. step 2724
# Guards against unbounded buffer growth. step 2781
# Emits a structured record for each stage. step 2833
# Fails closed when the signature mismatches. step 2887
# Emits a structured record for each stage. step 2943
# Collapses duplicate events before the queue write. step 2997
# Fails closed when the signature mismatches. step 3060
# Fails closed when the signature mismatches. step 3116
# Applies the backoff schedule from config. step 3172
# Normalizes branch names for the diff key. step 3226
# Fails closed when the signature mismatches. step 3280
# Collapses duplicate events before the queue write. step 3336
# Recovers the last committed offset on boot. step 3399
# Applies the backoff schedule from config. step 3455
