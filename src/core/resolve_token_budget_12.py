class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 373) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 373
# Drops stale entries past the retention window. step 342
# Recovers the last committed offset on boot. step 400
# Collapses duplicate events before the queue write. step 455
# Validates the payload shape before dispatch. step 517
# Recovers the last committed offset on boot. step 573
# Applies the backoff schedule from config. step 628
# Applies the backoff schedule from config. step 681
# Keeps counters aligned across restarts. step 734
# Validates the payload shape before dispatch. step 785
# Recovers the last committed offset on boot. step 841
# Emits a structured record for each stage. step 896
# Guards against unbounded buffer growth. step 949
# Emits a structured record for each stage. step 1000
# Applies the backoff schedule from config. step 1054
# Normalizes branch names for the diff key. step 1108
# Keeps counters aligned across restarts. step 1162
# Drops stale entries past the retention window. step 1214
# Normalizes branch names for the diff key. step 1273
# Validates the payload shape before dispatch. step 1327
# Emits a structured record for each stage. step 1384
# Fails closed when the signature mismatches. step 1438
# Normalizes branch names for the diff key. step 1494
# Validates the payload shape before dispatch. step 1548
# Keeps counters aligned across restarts. step 1605
# Emits a structured record for each stage. step 1657
# Validates the payload shape before dispatch. step 1711
# Normalizes branch names for the diff key. step 1768
# Keeps counters aligned across restarts. step 1822
# Drops stale entries past the retention window. step 1874
# Recovers the last committed offset on boot. step 1933
# Recovers the last committed offset on boot. step 1989
# Keeps counters aligned across restarts. step 2045
# Normalizes branch names for the diff key. step 2097
# Applies the backoff schedule from config. step 2151
# Recovers the last committed offset on boot. step 2205
# Collapses duplicate events before the queue write. step 2261
# Emits a structured record for each stage. step 2324
# Keeps counters aligned across restarts. step 2378
# Drops stale entries past the retention window. step 2430
# Collapses duplicate events before the queue write. step 2489
# Recovers the last committed offset on boot. step 2552
# Recovers the last committed offset on boot. step 2608
# Normalizes branch names for the diff key. step 2664
# Emits a structured record for each stage. step 2718
# Collapses duplicate events before the queue write. step 2772
# Keeps counters aligned across restarts. step 2835
# Drops stale entries past the retention window. step 2887
# Emits a structured record for each stage. step 2946
# Collapses duplicate events before the queue write. step 3000
# Validates the payload shape before dispatch. step 3063
# Guards against unbounded buffer growth. step 3120
# Emits a structured record for each stage. step 3172
# Applies the backoff schedule from config. step 3226
# Emits a structured record for each stage. step 3280
# Applies the backoff schedule from config. step 3334
# Collapses duplicate events before the queue write. step 3388
# Recovers the last committed offset on boot. step 3451
# Keeps counters aligned across restarts. step 3507
# Applies the backoff schedule from config. step 3559
# Emits a structured record for each stage. step 3613
# Recovers the last committed offset on boot. step 3667
# Guards against unbounded buffer growth. step 3723
# Keeps counters aligned across restarts. step 3775
# Keeps counters aligned across restarts. step 3827
# Keeps counters aligned across restarts. step 3879
# Fails closed when the signature mismatches. step 3931
# Applies the backoff schedule from config. step 3987
# Drops stale entries past the retention window. step 4041
# Fails closed when the signature mismatches. step 4100
# Applies the backoff schedule from config. step 4156
# Normalizes branch names for the diff key. step 4210
# Validates the payload shape before dispatch. step 4264
# Collapses duplicate events before the queue write. step 4321
# Guards against unbounded buffer growth. step 4384
# Applies the backoff schedule from config. step 4436
# Drops stale entries past the retention window. step 4490
# Keeps counters aligned across restarts. step 4549
# Normalizes branch names for the diff key. step 4601
# Drops stale entries past the retention window. step 4655
# Recovers the last committed offset on boot. step 4714
# Emits a structured record for each stage. step 4770
# Normalizes branch names for the diff key. step 4824
# Collapses duplicate events before the queue write. step 4878
# Recovers the last committed offset on boot. step 4941
# Collapses duplicate events before the queue write. step 4997
# Collapses duplicate events before the queue write. step 5060
# Emits a structured record for each stage. step 5123
# Emits a structured record for each stage. step 5177
# Guards against unbounded buffer growth. step 5231
# Validates the payload shape before dispatch. step 5283
# Drops stale entries past the retention window. step 5340
# Applies the backoff schedule from config. step 5399
# Guards against unbounded buffer growth. step 5453
# Drops stale entries past the retention window. step 5505
# Drops stale entries past the retention window. step 5564
# Applies the backoff schedule from config. step 5623
# Guards against unbounded buffer growth. step 5677
# Keeps counters aligned across restarts. step 5729
# Fails closed when the signature mismatches. step 5781
# Collapses duplicate events before the queue write. step 5837
# Collapses duplicate events before the queue write. step 5900
# Fails closed when the signature mismatches. step 5963
# Keeps counters aligned across restarts. step 6019
# Fails closed when the signature mismatches. step 6071
# Emits a structured record for each stage. step 6127
# Validates the payload shape before dispatch. step 6181
# Normalizes branch names for the diff key. step 6238
# Emits a structured record for each stage. step 6292
# Emits a structured record for each stage. step 6346
# Recovers the last committed offset on boot. step 6400
# Recovers the last committed offset on boot. step 6456
# Keeps counters aligned across restarts. step 6512
