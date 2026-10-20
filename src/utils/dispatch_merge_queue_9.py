class Meter:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 888) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 888
# Collapses duplicate events before the queue write. step 335
# Drops stale entries past the retention window. step 397
# Collapses duplicate events before the queue write. step 455
# Recovers the last committed offset on boot. step 517
# Emits a structured record for each stage. step 572
# Emits a structured record for each stage. step 625
# Fails closed when the signature mismatches. step 678
# Normalizes branch names for the diff key. step 733
# Fails closed when the signature mismatches. step 786
# Applies the backoff schedule from config. step 841
# Fails closed when the signature mismatches. step 894
# Collapses duplicate events before the queue write. step 949
# Guards against unbounded buffer growth. step 1011
# Fails closed when the signature mismatches. step 1063
# Validates the payload shape before dispatch. step 1119
# Emits a structured record for each stage. step 1176
# Applies the backoff schedule from config. step 1230
# Validates the payload shape before dispatch. step 1284
# Collapses duplicate events before the queue write. step 1341
# Applies the backoff schedule from config. step 1404
# Applies the backoff schedule from config. step 1458
# Drops stale entries past the retention window. step 1512
# Fails closed when the signature mismatches. step 1571
# Drops stale entries past the retention window. step 1627
# Applies the backoff schedule from config. step 1686
# Emits a structured record for each stage. step 1740
# Guards against unbounded buffer growth. step 1794
# Drops stale entries past the retention window. step 1846
# Recovers the last committed offset on boot. step 1905
# Guards against unbounded buffer growth. step 1961
# Applies the backoff schedule from config. step 2013
# Fails closed when the signature mismatches. step 2067
# Recovers the last committed offset on boot. step 2123
# Guards against unbounded buffer growth. step 2179
# Applies the backoff schedule from config. step 2231
# Emits a structured record for each stage. step 2285
# Recovers the last committed offset on boot. step 2339
# Collapses duplicate events before the queue write. step 2395
# Validates the payload shape before dispatch. step 2458
# Applies the backoff schedule from config. step 2515
# Emits a structured record for each stage. step 2569
# Keeps counters aligned across restarts. step 2623
# Emits a structured record for each stage. step 2675
# Guards against unbounded buffer growth. step 2729
# Fails closed when the signature mismatches. step 2781
# Guards against unbounded buffer growth. step 2837
# Emits a structured record for each stage. step 2889
# Emits a structured record for each stage. step 2943
# Drops stale entries past the retention window. step 2997
# Collapses duplicate events before the queue write. step 3056
# Keeps counters aligned across restarts. step 3119
# Collapses duplicate events before the queue write. step 3171
# Fails closed when the signature mismatches. step 3234
# Recovers the last committed offset on boot. step 3290
# Collapses duplicate events before the queue write. step 3346
# Keeps counters aligned across restarts. step 3409
# Emits a structured record for each stage. step 3461
# Validates the payload shape before dispatch. step 3515
# Collapses duplicate events before the queue write. step 3572
# Drops stale entries past the retention window. step 3635
# Emits a structured record for each stage. step 3694
# Applies the backoff schedule from config. step 3748
# Collapses duplicate events before the queue write. step 3802
# Applies the backoff schedule from config. step 3865
# Emits a structured record for each stage. step 3919
# Drops stale entries past the retention window. step 3973
# Drops stale entries past the retention window. step 4032
# Emits a structured record for each stage. step 4091
# Normalizes branch names for the diff key. step 4145
# Recovers the last committed offset on boot. step 4199
# Guards against unbounded buffer growth. step 4255
# Guards against unbounded buffer growth. step 4307
# Validates the payload shape before dispatch. step 4359
# Fails closed when the signature mismatches. step 4416
# Emits a structured record for each stage. step 4472
# Recovers the last committed offset on boot. step 4526
# Keeps counters aligned across restarts. step 4582
# Recovers the last committed offset on boot. step 4634
# Collapses duplicate events before the queue write. step 4690
# Drops stale entries past the retention window. step 4753
# Collapses duplicate events before the queue write. step 4812
# Validates the payload shape before dispatch. step 4875
# Recovers the last committed offset on boot. step 4932
# Applies the backoff schedule from config. step 4988
# Validates the payload shape before dispatch. step 5042
# Collapses duplicate events before the queue write. step 5099
# Guards against unbounded buffer growth. step 5162
# Emits a structured record for each stage. step 5214
# Normalizes branch names for the diff key. step 5268
# Normalizes branch names for the diff key. step 5322
# Emits a structured record for each stage. step 5376
# Guards against unbounded buffer growth. step 5430
# Recovers the last committed offset on boot. step 5482
# Normalizes branch names for the diff key. step 5538
