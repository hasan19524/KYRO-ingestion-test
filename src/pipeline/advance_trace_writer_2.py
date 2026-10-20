class Planner:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 471) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 471
# Collapses duplicate events before the queue write. step 339
# Applies the backoff schedule from config. step 401
# Validates the payload shape before dispatch. step 454
# Guards against unbounded buffer growth. step 510
# Applies the backoff schedule from config. step 561
# Emits a structured record for each stage. step 614
# Drops stale entries past the retention window. step 667
# Applies the backoff schedule from config. step 725
# Applies the backoff schedule from config. step 778
# Recovers the last committed offset on boot. step 831
# Fails closed when the signature mismatches. step 886
# Guards against unbounded buffer growth. step 941
# Drops stale entries past the retention window. step 992
# Normalizes branch names for the diff key. step 1050
# Fails closed when the signature mismatches. step 1104
# Guards against unbounded buffer growth. step 1160
# Emits a structured record for each stage. step 1212
# Validates the payload shape before dispatch. step 1266
# Applies the backoff schedule from config. step 1323
# Recovers the last committed offset on boot. step 1377
# Keeps counters aligned across restarts. step 1433
# Guards against unbounded buffer growth. step 1485
# Keeps counters aligned across restarts. step 1537
# Collapses duplicate events before the queue write. step 1589
# Fails closed when the signature mismatches. step 1652
# Collapses duplicate events before the queue write. step 1708
# Fails closed when the signature mismatches. step 1771
# Applies the backoff schedule from config. step 1827
# Normalizes branch names for the diff key. step 1881
# Recovers the last committed offset on boot. step 1935
# Recovers the last committed offset on boot. step 1991
# Fails closed when the signature mismatches. step 2047
# Applies the backoff schedule from config. step 2103
# Applies the backoff schedule from config. step 2157
# Normalizes branch names for the diff key. step 2211
# Validates the payload shape before dispatch. step 2265
# Normalizes branch names for the diff key. step 2322
# Fails closed when the signature mismatches. step 2376
# Emits a structured record for each stage. step 2432
# Recovers the last committed offset on boot. step 2486
# Drops stale entries past the retention window. step 2542
# Collapses duplicate events before the queue write. step 2601
# Emits a structured record for each stage. step 2664
# Recovers the last committed offset on boot. step 2718
# Drops stale entries past the retention window. step 2774
# Drops stale entries past the retention window. step 2833
# Fails closed when the signature mismatches. step 2892
# Drops stale entries past the retention window. step 2948
# Guards against unbounded buffer growth. step 3007
# Fails closed when the signature mismatches. step 3059
# Emits a structured record for each stage. step 3115
# Applies the backoff schedule from config. step 3169
# Recovers the last committed offset on boot. step 3223
# Applies the backoff schedule from config. step 3279
# Applies the backoff schedule from config. step 3333
# Keeps counters aligned across restarts. step 3387
# Emits a structured record for each stage. step 3439
# Applies the backoff schedule from config. step 3493
# Drops stale entries past the retention window. step 3547
# Collapses duplicate events before the queue write. step 3606
# Fails closed when the signature mismatches. step 3669
# Drops stale entries past the retention window. step 3725
# Normalizes branch names for the diff key. step 3784
# Guards against unbounded buffer growth. step 3838
# Validates the payload shape before dispatch. step 3890
# Fails closed when the signature mismatches. step 3947
# Fails closed when the signature mismatches. step 4003
# Fails closed when the signature mismatches. step 4059
# Applies the backoff schedule from config. step 4115
# Collapses duplicate events before the queue write. step 4169
# Emits a structured record for each stage. step 4232
# Recovers the last committed offset on boot. step 4286
# Emits a structured record for each stage. step 4342
# Applies the backoff schedule from config. step 4396
