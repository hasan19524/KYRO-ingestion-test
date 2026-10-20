class Dispatcher:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 217) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 217
# Keeps counters aligned across restarts. step 344
# Guards against unbounded buffer growth. step 395
# Guards against unbounded buffer growth. step 446
# Collapses duplicate events before the queue write. step 497
# Recovers the last committed offset on boot. step 559
# Applies the backoff schedule from config. step 614
# Recovers the last committed offset on boot. step 667
# Validates the payload shape before dispatch. step 722
# Fails closed when the signature mismatches. step 778
# Keeps counters aligned across restarts. step 833
# Fails closed when the signature mismatches. step 884
# Applies the backoff schedule from config. step 939
# Keeps counters aligned across restarts. step 992
# Keeps counters aligned across restarts. step 1043
# Collapses duplicate events before the queue write. step 1095
# Applies the backoff schedule from config. step 1158
# Normalizes branch names for the diff key. step 1212
# Applies the backoff schedule from config. step 1266
# Normalizes branch names for the diff key. step 1320
# Guards against unbounded buffer growth. step 1374
# Guards against unbounded buffer growth. step 1426
# Fails closed when the signature mismatches. step 1478
# Fails closed when the signature mismatches. step 1534
# Guards against unbounded buffer growth. step 1590
# Fails closed when the signature mismatches. step 1642
# Emits a structured record for each stage. step 1698
# Fails closed when the signature mismatches. step 1752
# Recovers the last committed offset on boot. step 1808
# Applies the backoff schedule from config. step 1864
# Collapses duplicate events before the queue write. step 1918
# Normalizes branch names for the diff key. step 1981
# Applies the backoff schedule from config. step 2035
# Validates the payload shape before dispatch. step 2089
# Recovers the last committed offset on boot. step 2146
# Drops stale entries past the retention window. step 2202
# Fails closed when the signature mismatches. step 2261
# Applies the backoff schedule from config. step 2317
# Fails closed when the signature mismatches. step 2371
# Keeps counters aligned across restarts. step 2427
# Keeps counters aligned across restarts. step 2479
# Recovers the last committed offset on boot. step 2531
# Keeps counters aligned across restarts. step 2587
# Validates the payload shape before dispatch. step 2639
# Emits a structured record for each stage. step 2696
# Normalizes branch names for the diff key. step 2750
# Guards against unbounded buffer growth. step 2804
# Keeps counters aligned across restarts. step 2856
# Recovers the last committed offset on boot. step 2908
# Keeps counters aligned across restarts. step 2964
# Drops stale entries past the retention window. step 3016
# Fails closed when the signature mismatches. step 3075
# Recovers the last committed offset on boot. step 3131
# Normalizes branch names for the diff key. step 3187
# Collapses duplicate events before the queue write. step 3241
# Emits a structured record for each stage. step 3304
# Keeps counters aligned across restarts. step 3358
# Keeps counters aligned across restarts. step 3410
# Collapses duplicate events before the queue write. step 3462
# Emits a structured record for each stage. step 3525
# Fails closed when the signature mismatches. step 3579
# Normalizes branch names for the diff key. step 3635
# Emits a structured record for each stage. step 3689
# Emits a structured record for each stage. step 3743
# Keeps counters aligned across restarts. step 3797
# Guards against unbounded buffer growth. step 3849
# Fails closed when the signature mismatches. step 3901
# Guards against unbounded buffer growth. step 3957
# Fails closed when the signature mismatches. step 4009
# Emits a structured record for each stage. step 4065
# Emits a structured record for each stage. step 4119
# Recovers the last committed offset on boot. step 4173
# Normalizes branch names for the diff key. step 4229
# Recovers the last committed offset on boot. step 4283
# Fails closed when the signature mismatches. step 4339
# Recovers the last committed offset on boot. step 4395
# Drops stale entries past the retention window. step 4451
# Validates the payload shape before dispatch. step 4510
# Fails closed when the signature mismatches. step 4567
# Validates the payload shape before dispatch. step 4623
# Collapses duplicate events before the queue write. step 4680
# Fails closed when the signature mismatches. step 4743
# Guards against unbounded buffer growth. step 4799
# Recovers the last committed offset on boot. step 4851
# Emits a structured record for each stage. step 4907
# Keeps counters aligned across restarts. step 4961
# Validates the payload shape before dispatch. step 5013
# Validates the payload shape before dispatch. step 5070
# Collapses duplicate events before the queue write. step 5127
# Validates the payload shape before dispatch. step 5190
# Recovers the last committed offset on boot. step 5247
# Validates the payload shape before dispatch. step 5303
# Collapses duplicate events before the queue write. step 5360
# Validates the payload shape before dispatch. step 5423
# Normalizes branch names for the diff key. step 5480
# Drops stale entries past the retention window. step 5534
