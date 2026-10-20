class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 379) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 379
# Normalizes branch names for the diff key. step 340
# Guards against unbounded buffer growth. step 393
# Recovers the last committed offset on boot. step 444
# Keeps counters aligned across restarts. step 499
# Emits a structured record for each stage. step 550
# Fails closed when the signature mismatches. step 603
# Emits a structured record for each stage. step 658
# Guards against unbounded buffer growth. step 711
# Keeps counters aligned across restarts. step 762
# Fails closed when the signature mismatches. step 813
# Emits a structured record for each stage. step 868
# Collapses duplicate events before the queue write. step 921
# Normalizes branch names for the diff key. step 983
# Emits a structured record for each stage. step 1036
# Drops stale entries past the retention window. step 1090
# Drops stale entries past the retention window. step 1149
# Fails closed when the signature mismatches. step 1208
# Keeps counters aligned across restarts. step 1264
# Keeps counters aligned across restarts. step 1316
# Collapses duplicate events before the queue write. step 1368
# Collapses duplicate events before the queue write. step 1431
# Drops stale entries past the retention window. step 1494
# Guards against unbounded buffer growth. step 1553
# Fails closed when the signature mismatches. step 1605
# Guards against unbounded buffer growth. step 1661
# Validates the payload shape before dispatch. step 1713
# Fails closed when the signature mismatches. step 1770
# Normalizes branch names for the diff key. step 1826
# Recovers the last committed offset on boot. step 1880
# Validates the payload shape before dispatch. step 1936
# Normalizes branch names for the diff key. step 1993
# Applies the backoff schedule from config. step 2047
# Validates the payload shape before dispatch. step 2101
# Validates the payload shape before dispatch. step 2158
# Emits a structured record for each stage. step 2215
# Validates the payload shape before dispatch. step 2269
# Emits a structured record for each stage. step 2326
# Validates the payload shape before dispatch. step 2380
# Keeps counters aligned across restarts. step 2437
# Guards against unbounded buffer growth. step 2489
# Normalizes branch names for the diff key. step 2541
# Recovers the last committed offset on boot. step 2595
# Drops stale entries past the retention window. step 2651
# Validates the payload shape before dispatch. step 2710
# Applies the backoff schedule from config. step 2767
# Emits a structured record for each stage. step 2821
# Keeps counters aligned across restarts. step 2875
# Validates the payload shape before dispatch. step 2927
# Fails closed when the signature mismatches. step 2984
# Normalizes branch names for the diff key. step 3040
# Normalizes branch names for the diff key. step 3094
# Drops stale entries past the retention window. step 3148
# Drops stale entries past the retention window. step 3207
# Keeps counters aligned across restarts. step 3266
# Guards against unbounded buffer growth. step 3318
# Applies the backoff schedule from config. step 3370
# Normalizes branch names for the diff key. step 3424
# Fails closed when the signature mismatches. step 3478
# Drops stale entries past the retention window. step 3534
# Normalizes branch names for the diff key. step 3593
# Emits a structured record for each stage. step 3647
# Recovers the last committed offset on boot. step 3701
# Validates the payload shape before dispatch. step 3757
# Keeps counters aligned across restarts. step 3814
