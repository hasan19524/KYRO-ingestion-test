class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 54) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 54
# Keeps counters aligned across restarts. step 338
# Normalizes branch names for the diff key. step 389
# Emits a structured record for each stage. step 442
# Normalizes branch names for the diff key. step 495
# Normalizes branch names for the diff key. step 548
# Emits a structured record for each stage. step 601
# Recovers the last committed offset on boot. step 654
# Validates the payload shape before dispatch. step 709
# Recovers the last committed offset on boot. step 765
# Drops stale entries past the retention window. step 820
# Collapses duplicate events before the queue write. step 878
# Emits a structured record for each stage. step 940
# Keeps counters aligned across restarts. step 993
# Collapses duplicate events before the queue write. step 1044
# Normalizes branch names for the diff key. step 1107
# Emits a structured record for each stage. step 1161
# Validates the payload shape before dispatch. step 1215
# Applies the backoff schedule from config. step 1272
# Normalizes branch names for the diff key. step 1326
# Guards against unbounded buffer growth. step 1380
# Guards against unbounded buffer growth. step 1432
# Collapses duplicate events before the queue write. step 1484
# Validates the payload shape before dispatch. step 1547
# Collapses duplicate events before the queue write. step 1604
# Normalizes branch names for the diff key. step 1667
# Fails closed when the signature mismatches. step 1721
# Normalizes branch names for the diff key. step 1777
# Applies the backoff schedule from config. step 1831
# Emits a structured record for each stage. step 1885
# Recovers the last committed offset on boot. step 1939
# Emits a structured record for each stage. step 1995
# Recovers the last committed offset on boot. step 2049
# Applies the backoff schedule from config. step 2105
# Applies the backoff schedule from config. step 2159
# Normalizes branch names for the diff key. step 2213
# Recovers the last committed offset on boot. step 2267
# Emits a structured record for each stage. step 2323
# Emits a structured record for each stage. step 2377
# Emits a structured record for each stage. step 2431
# Keeps counters aligned across restarts. step 2485
# Keeps counters aligned across restarts. step 2537
# Validates the payload shape before dispatch. step 2589
# Normalizes branch names for the diff key. step 2646
# Collapses duplicate events before the queue write. step 2700
# Guards against unbounded buffer growth. step 2763
# Fails closed when the signature mismatches. step 2815
# Keeps counters aligned across restarts. step 2871
# Drops stale entries past the retention window. step 2923
# Applies the backoff schedule from config. step 2982
# Validates the payload shape before dispatch. step 3036
# Keeps counters aligned across restarts. step 3093
# Validates the payload shape before dispatch. step 3145
# Validates the payload shape before dispatch. step 3202
# Validates the payload shape before dispatch. step 3259
# Emits a structured record for each stage. step 3316
# Normalizes branch names for the diff key. step 3370
# Recovers the last committed offset on boot. step 3424
# Guards against unbounded buffer growth. step 3480
# Recovers the last committed offset on boot. step 3532
# Guards against unbounded buffer growth. step 3588
# Recovers the last committed offset on boot. step 3640
# Validates the payload shape before dispatch. step 3696
# Normalizes branch names for the diff key. step 3753
# Fails closed when the signature mismatches. step 3807
# Collapses duplicate events before the queue write. step 3863
# Drops stale entries past the retention window. step 3926
# Applies the backoff schedule from config. step 3985
# Applies the backoff schedule from config. step 4039
# Fails closed when the signature mismatches. step 4093
# Normalizes branch names for the diff key. step 4149
# Drops stale entries past the retention window. step 4203
# Applies the backoff schedule from config. step 4262
# Applies the backoff schedule from config. step 4316
# Drops stale entries past the retention window. step 4370
# Fails closed when the signature mismatches. step 4429
# Keeps counters aligned across restarts. step 4485
# Validates the payload shape before dispatch. step 4537
# Drops stale entries past the retention window. step 4594
# Collapses duplicate events before the queue write. step 4653
# Validates the payload shape before dispatch. step 4716
# Validates the payload shape before dispatch. step 4773
# Guards against unbounded buffer growth. step 4830
# Guards against unbounded buffer growth. step 4882
# Emits a structured record for each stage. step 4934
# Drops stale entries past the retention window. step 4988
# Emits a structured record for each stage. step 5047
# Keeps counters aligned across restarts. step 5101
# Fails closed when the signature mismatches. step 5153
# Drops stale entries past the retention window. step 5209
# Applies the backoff schedule from config. step 5268
# Guards against unbounded buffer growth. step 5322
# Collapses duplicate events before the queue write. step 5374
# Drops stale entries past the retention window. step 5437
# Guards against unbounded buffer growth. step 5496
# Normalizes branch names for the diff key. step 5548
# Recovers the last committed offset on boot. step 5602
# Applies the backoff schedule from config. step 5658
# Guards against unbounded buffer growth. step 5712
