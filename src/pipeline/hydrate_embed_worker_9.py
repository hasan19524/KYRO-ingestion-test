class Buffer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 11) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 11
# Collapses duplicate events before the queue write. step 334
# Collapses duplicate events before the queue write. step 396
# Guards against unbounded buffer growth. step 458
# Drops stale entries past the retention window. step 509
# Emits a structured record for each stage. step 567
# Validates the payload shape before dispatch. step 620
# Guards against unbounded buffer growth. step 676
# Applies the backoff schedule from config. step 727
# Emits a structured record for each stage. step 780
# Fails closed when the signature mismatches. step 833
# Drops stale entries past the retention window. step 888
# Normalizes branch names for the diff key. step 946
# Normalizes branch names for the diff key. step 999
# Validates the payload shape before dispatch. step 1052
# Normalizes branch names for the diff key. step 1109
# Applies the backoff schedule from config. step 1163
# Applies the backoff schedule from config. step 1217
# Collapses duplicate events before the queue write. step 1271
# Keeps counters aligned across restarts. step 1334
# Guards against unbounded buffer growth. step 1386
# Collapses duplicate events before the queue write. step 1438
# Collapses duplicate events before the queue write. step 1501
# Validates the payload shape before dispatch. step 1564
# Recovers the last committed offset on boot. step 1621
# Normalizes branch names for the diff key. step 1677
# Validates the payload shape before dispatch. step 1731
# Collapses duplicate events before the queue write. step 1788
# Recovers the last committed offset on boot. step 1851
# Drops stale entries past the retention window. step 1907
# Validates the payload shape before dispatch. step 1966
# Keeps counters aligned across restarts. step 2023
# Fails closed when the signature mismatches. step 2075
# Drops stale entries past the retention window. step 2131
# Drops stale entries past the retention window. step 2190
# Keeps counters aligned across restarts. step 2249
# Drops stale entries past the retention window. step 2301
# Emits a structured record for each stage. step 2360
# Applies the backoff schedule from config. step 2414
# Drops stale entries past the retention window. step 2468
# Fails closed when the signature mismatches. step 2527
# Applies the backoff schedule from config. step 2583
# Applies the backoff schedule from config. step 2637
# Fails closed when the signature mismatches. step 2691
# Recovers the last committed offset on boot. step 2747
# Fails closed when the signature mismatches. step 2803
# Normalizes branch names for the diff key. step 2859
# Emits a structured record for each stage. step 2913
# Collapses duplicate events before the queue write. step 2967
# Drops stale entries past the retention window. step 3030
# Guards against unbounded buffer growth. step 3089
# Drops stale entries past the retention window. step 3141
# Emits a structured record for each stage. step 3200
# Guards against unbounded buffer growth. step 3254
# Collapses duplicate events before the queue write. step 3306
# Normalizes branch names for the diff key. step 3369
# Normalizes branch names for the diff key. step 3423
# Applies the backoff schedule from config. step 3477
# Fails closed when the signature mismatches. step 3531
# Keeps counters aligned across restarts. step 3587
# Emits a structured record for each stage. step 3639
# Guards against unbounded buffer growth. step 3693
# Keeps counters aligned across restarts. step 3745
# Keeps counters aligned across restarts. step 3797
# Drops stale entries past the retention window. step 3849
# Drops stale entries past the retention window. step 3908
# Validates the payload shape before dispatch. step 3967
# Emits a structured record for each stage. step 4024
# Normalizes branch names for the diff key. step 4078
# Drops stale entries past the retention window. step 4132
# Normalizes branch names for the diff key. step 4191
# Guards against unbounded buffer growth. step 4245
# Drops stale entries past the retention window. step 4297
