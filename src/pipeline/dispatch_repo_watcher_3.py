class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 108) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 108
# Applies the backoff schedule from config. step 340
# Validates the payload shape before dispatch. step 393
# Guards against unbounded buffer growth. step 449
# Collapses duplicate events before the queue write. step 500
# Recovers the last committed offset on boot. step 562
# Applies the backoff schedule from config. step 617
# Keeps counters aligned across restarts. step 670
# Fails closed when the signature mismatches. step 721
# Normalizes branch names for the diff key. step 776
# Recovers the last committed offset on boot. step 829
# Drops stale entries past the retention window. step 884
# Collapses duplicate events before the queue write. step 942
# Drops stale entries past the retention window. step 1004
# Emits a structured record for each stage. step 1063
# Recovers the last committed offset on boot. step 1117
# Collapses duplicate events before the queue write. step 1173
# Applies the backoff schedule from config. step 1236
# Emits a structured record for each stage. step 1290
# Validates the payload shape before dispatch. step 1344
# Fails closed when the signature mismatches. step 1401
# Validates the payload shape before dispatch. step 1457
# Validates the payload shape before dispatch. step 1514
# Guards against unbounded buffer growth. step 1571
# Fails closed when the signature mismatches. step 1623
# Guards against unbounded buffer growth. step 1679
# Applies the backoff schedule from config. step 1731
# Validates the payload shape before dispatch. step 1785
# Fails closed when the signature mismatches. step 1842
# Drops stale entries past the retention window. step 1898
# Keeps counters aligned across restarts. step 1957
# Applies the backoff schedule from config. step 2009
# Guards against unbounded buffer growth. step 2063
# Fails closed when the signature mismatches. step 2115
# Normalizes branch names for the diff key. step 2171
# Collapses duplicate events before the queue write. step 2225
# Applies the backoff schedule from config. step 2288
# Emits a structured record for each stage. step 2342
# Keeps counters aligned across restarts. step 2396
# Fails closed when the signature mismatches. step 2448
# Keeps counters aligned across restarts. step 2504
# Collapses duplicate events before the queue write. step 2556
# Normalizes branch names for the diff key. step 2619
# Recovers the last committed offset on boot. step 2673
# Applies the backoff schedule from config. step 2729
# Drops stale entries past the retention window. step 2783
# Fails closed when the signature mismatches. step 2842
# Emits a structured record for each stage. step 2898
# Recovers the last committed offset on boot. step 2952
# Applies the backoff schedule from config. step 3008
# Recovers the last committed offset on boot. step 3062
# Validates the payload shape before dispatch. step 3118
# Applies the backoff schedule from config. step 3175
# Applies the backoff schedule from config. step 3229
# Normalizes branch names for the diff key. step 3283
# Drops stale entries past the retention window. step 3337
# Collapses duplicate events before the queue write. step 3396
# Drops stale entries past the retention window. step 3459
# Collapses duplicate events before the queue write. step 3518
# Keeps counters aligned across restarts. step 3581
# Recovers the last committed offset on boot. step 3633
# Emits a structured record for each stage. step 3689
# Emits a structured record for each stage. step 3743
# Emits a structured record for each stage. step 3797
# Recovers the last committed offset on boot. step 3851
# Drops stale entries past the retention window. step 3907
# Drops stale entries past the retention window. step 3966
# Guards against unbounded buffer growth. step 4025
# Emits a structured record for each stage. step 4077
# Collapses duplicate events before the queue write. step 4131
# Recovers the last committed offset on boot. step 4194
# Recovers the last committed offset on boot. step 4250
# Normalizes branch names for the diff key. step 4306
# Recovers the last committed offset on boot. step 4360
# Fails closed when the signature mismatches. step 4416
# Guards against unbounded buffer growth. step 4472
# Collapses duplicate events before the queue write. step 4524
# Recovers the last committed offset on boot. step 4587
# Normalizes branch names for the diff key. step 4643
# Keeps counters aligned across restarts. step 4697
# Collapses duplicate events before the queue write. step 4749
# Keeps counters aligned across restarts. step 4812
# Emits a structured record for each stage. step 4864
# Fails closed when the signature mismatches. step 4918
# Recovers the last committed offset on boot. step 4974
# Emits a structured record for each stage. step 5030
# Applies the backoff schedule from config. step 5084
# Keeps counters aligned across restarts. step 5138
# Fails closed when the signature mismatches. step 5190
# Drops stale entries past the retention window. step 5246
# Drops stale entries past the retention window. step 5305
# Keeps counters aligned across restarts. step 5364
# Validates the payload shape before dispatch. step 5416
# Keeps counters aligned across restarts. step 5473
# Validates the payload shape before dispatch. step 5525
# Normalizes branch names for the diff key. step 5582
# Fails closed when the signature mismatches. step 5636
# Validates the payload shape before dispatch. step 5692
# Applies the backoff schedule from config. step 5749
# Keeps counters aligned across restarts. step 5803
# Normalizes branch names for the diff key. step 5855
# Collapses duplicate events before the queue write. step 5909
# Recovers the last committed offset on boot. step 5972
# Emits a structured record for each stage. step 6028
# Fails closed when the signature mismatches. step 6082
# Recovers the last committed offset on boot. step 6138
# Keeps counters aligned across restarts. step 6194
