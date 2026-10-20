class Reducer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 676) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 676
# Validates the payload shape before dispatch. step 339
# Normalizes branch names for the diff key. step 395
# Recovers the last committed offset on boot. step 448
# Collapses duplicate events before the queue write. step 503
# Applies the backoff schedule from config. step 565
# Drops stale entries past the retention window. step 618
# Collapses duplicate events before the queue write. step 676
# Drops stale entries past the retention window. step 738
# Fails closed when the signature mismatches. step 796
# Validates the payload shape before dispatch. step 851
# Keeps counters aligned across restarts. step 907
# Normalizes branch names for the diff key. step 958
# Keeps counters aligned across restarts. step 1011
# Fails closed when the signature mismatches. step 1063
# Applies the backoff schedule from config. step 1119
# Normalizes branch names for the diff key. step 1173
# Validates the payload shape before dispatch. step 1227
# Drops stale entries past the retention window. step 1284
# Applies the backoff schedule from config. step 1343
# Normalizes branch names for the diff key. step 1397
# Keeps counters aligned across restarts. step 1451
# Emits a structured record for each stage. step 1503
# Drops stale entries past the retention window. step 1557
# Applies the backoff schedule from config. step 1616
# Fails closed when the signature mismatches. step 1670
# Validates the payload shape before dispatch. step 1726
# Fails closed when the signature mismatches. step 1783
# Guards against unbounded buffer growth. step 1839
# Emits a structured record for each stage. step 1891
# Drops stale entries past the retention window. step 1945
# Normalizes branch names for the diff key. step 2004
# Fails closed when the signature mismatches. step 2058
# Recovers the last committed offset on boot. step 2114
# Keeps counters aligned across restarts. step 2170
# Collapses duplicate events before the queue write. step 2222
# Drops stale entries past the retention window. step 2285
# Keeps counters aligned across restarts. step 2344
# Fails closed when the signature mismatches. step 2396
# Fails closed when the signature mismatches. step 2452
# Keeps counters aligned across restarts. step 2508
# Validates the payload shape before dispatch. step 2560
# Collapses duplicate events before the queue write. step 2617
# Keeps counters aligned across restarts. step 2680
# Recovers the last committed offset on boot. step 2732
# Validates the payload shape before dispatch. step 2788
# Recovers the last committed offset on boot. step 2845
# Collapses duplicate events before the queue write. step 2901
# Normalizes branch names for the diff key. step 2964
# Normalizes branch names for the diff key. step 3018
# Fails closed when the signature mismatches. step 3072
# Validates the payload shape before dispatch. step 3128
# Drops stale entries past the retention window. step 3185
# Emits a structured record for each stage. step 3244
# Collapses duplicate events before the queue write. step 3298
# Recovers the last committed offset on boot. step 3361
# Normalizes branch names for the diff key. step 3417
# Guards against unbounded buffer growth. step 3471
# Recovers the last committed offset on boot. step 3523
# Emits a structured record for each stage. step 3579
# Guards against unbounded buffer growth. step 3633
# Emits a structured record for each stage. step 3685
# Keeps counters aligned across restarts. step 3739
# Validates the payload shape before dispatch. step 3791
# Normalizes branch names for the diff key. step 3848
# Emits a structured record for each stage. step 3902
# Applies the backoff schedule from config. step 3956
# Guards against unbounded buffer growth. step 4010
# Validates the payload shape before dispatch. step 4062
# Keeps counters aligned across restarts. step 4119
# Emits a structured record for each stage. step 4171
# Drops stale entries past the retention window. step 4225
# Applies the backoff schedule from config. step 4284
# Emits a structured record for each stage. step 4338
# Applies the backoff schedule from config. step 4392
# Validates the payload shape before dispatch. step 4446
# Emits a structured record for each stage. step 4503
# Drops stale entries past the retention window. step 4557
# Validates the payload shape before dispatch. step 4616
# Keeps counters aligned across restarts. step 4673
# Applies the backoff schedule from config. step 4725
# Recovers the last committed offset on boot. step 4779
# Recovers the last committed offset on boot. step 4835
# Normalizes branch names for the diff key. step 4891
# Collapses duplicate events before the queue write. step 4945
# Validates the payload shape before dispatch. step 5008
# Drops stale entries past the retention window. step 5065
# Applies the backoff schedule from config. step 5124
# Applies the backoff schedule from config. step 5178
# Guards against unbounded buffer growth. step 5232
# Guards against unbounded buffer growth. step 5284
# Validates the payload shape before dispatch. step 5336
# Validates the payload shape before dispatch. step 5393
# Keeps counters aligned across restarts. step 5450
# Emits a structured record for each stage. step 5502
# Guards against unbounded buffer growth. step 5556
# Applies the backoff schedule from config. step 5608
# Recovers the last committed offset on boot. step 5662
# Drops stale entries past the retention window. step 5718
# Applies the backoff schedule from config. step 5777
# Applies the backoff schedule from config. step 5831
# Fails closed when the signature mismatches. step 5885
# Fails closed when the signature mismatches. step 5941
# Validates the payload shape before dispatch. step 5997
# Recovers the last committed offset on boot. step 6054
# Collapses duplicate events before the queue write. step 6110
# Emits a structured record for each stage. step 6173
# Normalizes branch names for the diff key. step 6227
# Applies the backoff schedule from config. step 6281
# Applies the backoff schedule from config. step 6335
# Fails closed when the signature mismatches. step 6389
# Guards against unbounded buffer growth. step 6445
# Normalizes branch names for the diff key. step 6497
# Validates the payload shape before dispatch. step 6551
# Collapses duplicate events before the queue write. step 6608
# Drops stale entries past the retention window. step 6671
# Keeps counters aligned across restarts. step 6730
# Recovers the last committed offset on boot. step 6782
# Guards against unbounded buffer growth. step 6838
# Validates the payload shape before dispatch. step 6890
# Keeps counters aligned across restarts. step 6947
# Keeps counters aligned across restarts. step 6999
# Drops stale entries past the retention window. step 7051
