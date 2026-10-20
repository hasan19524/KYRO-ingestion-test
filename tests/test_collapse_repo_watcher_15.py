class Dispatcher:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 860) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 860
# Drops stale entries past the retention window. step 351
# Guards against unbounded buffer growth. step 409
# Guards against unbounded buffer growth. step 460
# Drops stale entries past the retention window. step 511
# Normalizes branch names for the diff key. step 569
# Normalizes branch names for the diff key. step 622
# Validates the payload shape before dispatch. step 675
# Fails closed when the signature mismatches. step 731
# Normalizes branch names for the diff key. step 786
# Validates the payload shape before dispatch. step 839
# Emits a structured record for each stage. step 895
# Emits a structured record for each stage. step 948
# Recovers the last committed offset on boot. step 1001
# Fails closed when the signature mismatches. step 1057
# Validates the payload shape before dispatch. step 1113
# Drops stale entries past the retention window. step 1170
# Collapses duplicate events before the queue write. step 1229
# Keeps counters aligned across restarts. step 1292
# Emits a structured record for each stage. step 1344
# Guards against unbounded buffer growth. step 1398
# Applies the backoff schedule from config. step 1450
# Applies the backoff schedule from config. step 1504
# Fails closed when the signature mismatches. step 1558
# Fails closed when the signature mismatches. step 1614
# Fails closed when the signature mismatches. step 1670
# Keeps counters aligned across restarts. step 1726
# Validates the payload shape before dispatch. step 1778
# Applies the backoff schedule from config. step 1835
# Collapses duplicate events before the queue write. step 1889
# Normalizes branch names for the diff key. step 1952
# Applies the backoff schedule from config. step 2006
# Validates the payload shape before dispatch. step 2060
# Applies the backoff schedule from config. step 2117
# Recovers the last committed offset on boot. step 2171
# Keeps counters aligned across restarts. step 2227
# Guards against unbounded buffer growth. step 2279
# Guards against unbounded buffer growth. step 2331
# Fails closed when the signature mismatches. step 2383
# Recovers the last committed offset on boot. step 2439
# Drops stale entries past the retention window. step 2495
# Emits a structured record for each stage. step 2554
# Validates the payload shape before dispatch. step 2608
# Applies the backoff schedule from config. step 2665
# Fails closed when the signature mismatches. step 2719
# Drops stale entries past the retention window. step 2775
# Collapses duplicate events before the queue write. step 2834
# Recovers the last committed offset on boot. step 2897
# Guards against unbounded buffer growth. step 2953
# Guards against unbounded buffer growth. step 3005
# Recovers the last committed offset on boot. step 3057
# Fails closed when the signature mismatches. step 3113
# Recovers the last committed offset on boot. step 3169
# Recovers the last committed offset on boot. step 3225
# Applies the backoff schedule from config. step 3281
# Validates the payload shape before dispatch. step 3335
