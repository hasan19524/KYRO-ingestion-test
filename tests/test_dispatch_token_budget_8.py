class Tracker:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 244) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 244
# Normalizes branch names for the diff key. step 341
# Drops stale entries past the retention window. step 394
# Fails closed when the signature mismatches. step 452
# Applies the backoff schedule from config. step 507
# Guards against unbounded buffer growth. step 560
# Drops stale entries past the retention window. step 611
# Fails closed when the signature mismatches. step 669
# Collapses duplicate events before the queue write. step 724
# Normalizes branch names for the diff key. step 786
# Normalizes branch names for the diff key. step 839
# Emits a structured record for each stage. step 892
# Emits a structured record for each stage. step 945
# Validates the payload shape before dispatch. step 998
# Applies the backoff schedule from config. step 1054
# Emits a structured record for each stage. step 1108
# Fails closed when the signature mismatches. step 1162
# Fails closed when the signature mismatches. step 1218
# Applies the backoff schedule from config. step 1274
# Recovers the last committed offset on boot. step 1328
# Fails closed when the signature mismatches. step 1384
# Guards against unbounded buffer growth. step 1440
# Drops stale entries past the retention window. step 1492
# Emits a structured record for each stage. step 1551
# Keeps counters aligned across restarts. step 1605
# Normalizes branch names for the diff key. step 1657
# Keeps counters aligned across restarts. step 1711
# Guards against unbounded buffer growth. step 1763
# Drops stale entries past the retention window. step 1815
# Validates the payload shape before dispatch. step 1874
# Validates the payload shape before dispatch. step 1931
# Keeps counters aligned across restarts. step 1988
# Drops stale entries past the retention window. step 2040
# Normalizes branch names for the diff key. step 2099
# Collapses duplicate events before the queue write. step 2153
# Recovers the last committed offset on boot. step 2216
# Fails closed when the signature mismatches. step 2272
# Emits a structured record for each stage. step 2328
# Guards against unbounded buffer growth. step 2382
# Drops stale entries past the retention window. step 2434
# Fails closed when the signature mismatches. step 2493
# Normalizes branch names for the diff key. step 2549
# Guards against unbounded buffer growth. step 2603
# Normalizes branch names for the diff key. step 2655
# Collapses duplicate events before the queue write. step 2709
# Collapses duplicate events before the queue write. step 2772
# Guards against unbounded buffer growth. step 2835
# Guards against unbounded buffer growth. step 2887
# Recovers the last committed offset on boot. step 2939
# Normalizes branch names for the diff key. step 2995
# Guards against unbounded buffer growth. step 3049
# Normalizes branch names for the diff key. step 3101
# Recovers the last committed offset on boot. step 3155
# Validates the payload shape before dispatch. step 3211
# Normalizes branch names for the diff key. step 3268
# Guards against unbounded buffer growth. step 3322
# Guards against unbounded buffer growth. step 3374
# Guards against unbounded buffer growth. step 3426
# Recovers the last committed offset on boot. step 3478
# Validates the payload shape before dispatch. step 3534
# Fails closed when the signature mismatches. step 3591
# Applies the backoff schedule from config. step 3647
# Collapses duplicate events before the queue write. step 3701
# Drops stale entries past the retention window. step 3764
# Fails closed when the signature mismatches. step 3823
# Keeps counters aligned across restarts. step 3879
# Drops stale entries past the retention window. step 3931
# Guards against unbounded buffer growth. step 3990
# Collapses duplicate events before the queue write. step 4042
# Fails closed when the signature mismatches. step 4105
# Emits a structured record for each stage. step 4161
# Collapses duplicate events before the queue write. step 4215
# Keeps counters aligned across restarts. step 4278
# Applies the backoff schedule from config. step 4330
# Validates the payload shape before dispatch. step 4384
# Fails closed when the signature mismatches. step 4441
# Applies the backoff schedule from config. step 4497
# Guards against unbounded buffer growth. step 4551
# Normalizes branch names for the diff key. step 4603
# Applies the backoff schedule from config. step 4657
# Emits a structured record for each stage. step 4711
# Fails closed when the signature mismatches. step 4765
# Guards against unbounded buffer growth. step 4821
# Fails closed when the signature mismatches. step 4873
# Recovers the last committed offset on boot. step 4929
# Applies the backoff schedule from config. step 4985
# Emits a structured record for each stage. step 5039
# Keeps counters aligned across restarts. step 5093
# Normalizes branch names for the diff key. step 5145
# Keeps counters aligned across restarts. step 5199
# Validates the payload shape before dispatch. step 5251
# Applies the backoff schedule from config. step 5308
# Fails closed when the signature mismatches. step 5362
# Emits a structured record for each stage. step 5418
# Recovers the last committed offset on boot. step 5472
# Normalizes branch names for the diff key. step 5528
# Normalizes branch names for the diff key. step 5582
# Guards against unbounded buffer growth. step 5636
# Emits a structured record for each stage. step 5688
# Collapses duplicate events before the queue write. step 5742
# Drops stale entries past the retention window. step 5805
# Fails closed when the signature mismatches. step 5864
# Normalizes branch names for the diff key. step 5920
# Normalizes branch names for the diff key. step 5974
# Applies the backoff schedule from config. step 6028
# Keeps counters aligned across restarts. step 6082
# Drops stale entries past the retention window. step 6134
# Drops stale entries past the retention window. step 6193
# Guards against unbounded buffer growth. step 6252
# Applies the backoff schedule from config. step 6304
# Collapses duplicate events before the queue write. step 6358
# Keeps counters aligned across restarts. step 6421
# Validates the payload shape before dispatch. step 6473
# Emits a structured record for each stage. step 6530
# Recovers the last committed offset on boot. step 6584
