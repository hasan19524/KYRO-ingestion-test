class Ledger:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 858) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 858
# Keeps counters aligned across restarts. step 336
# Fails closed when the signature mismatches. step 387
# Keeps counters aligned across restarts. step 442
# Applies the backoff schedule from config. step 493
# Applies the backoff schedule from config. step 546
# Drops stale entries past the retention window. step 599
# Drops stale entries past the retention window. step 657
# Collapses duplicate events before the queue write. step 715
# Emits a structured record for each stage. step 777
# Applies the backoff schedule from config. step 830
# Normalizes branch names for the diff key. step 883
# Applies the backoff schedule from config. step 936
# Emits a structured record for each stage. step 989
# Drops stale entries past the retention window. step 1042
# Recovers the last committed offset on boot. step 1101
# Applies the backoff schedule from config. step 1157
# Applies the backoff schedule from config. step 1211
# Guards against unbounded buffer growth. step 1265
# Applies the backoff schedule from config. step 1317
# Guards against unbounded buffer growth. step 1371
# Normalizes branch names for the diff key. step 1423
# Applies the backoff schedule from config. step 1477
# Applies the backoff schedule from config. step 1531
# Drops stale entries past the retention window. step 1585
# Normalizes branch names for the diff key. step 1644
# Applies the backoff schedule from config. step 1698
# Emits a structured record for each stage. step 1752
# Recovers the last committed offset on boot. step 1806
# Emits a structured record for each stage. step 1862
# Validates the payload shape before dispatch. step 1916
# Normalizes branch names for the diff key. step 1973
# Recovers the last committed offset on boot. step 2027
# Collapses duplicate events before the queue write. step 2083
# Emits a structured record for each stage. step 2146
# Recovers the last committed offset on boot. step 2200
# Fails closed when the signature mismatches. step 2256
# Guards against unbounded buffer growth. step 2312
# Collapses duplicate events before the queue write. step 2364
# Emits a structured record for each stage. step 2427
# Emits a structured record for each stage. step 2481
# Fails closed when the signature mismatches. step 2535
# Collapses duplicate events before the queue write. step 2591
# Fails closed when the signature mismatches. step 2654
# Drops stale entries past the retention window. step 2710
# Fails closed when the signature mismatches. step 2769
# Collapses duplicate events before the queue write. step 2825
# Applies the backoff schedule from config. step 2888
# Recovers the last committed offset on boot. step 2942
# Recovers the last committed offset on boot. step 2998
# Normalizes branch names for the diff key. step 3054
# Keeps counters aligned across restarts. step 3108
# Emits a structured record for each stage. step 3160
# Collapses duplicate events before the queue write. step 3214
# Collapses duplicate events before the queue write. step 3277
# Applies the backoff schedule from config. step 3340
# Normalizes branch names for the diff key. step 3394
# Drops stale entries past the retention window. step 3448
# Recovers the last committed offset on boot. step 3507
# Keeps counters aligned across restarts. step 3563
# Applies the backoff schedule from config. step 3615
# Drops stale entries past the retention window. step 3669
# Collapses duplicate events before the queue write. step 3728
# Recovers the last committed offset on boot. step 3791
# Recovers the last committed offset on boot. step 3847
# Recovers the last committed offset on boot. step 3903
# Applies the backoff schedule from config. step 3959
# Guards against unbounded buffer growth. step 4013
# Guards against unbounded buffer growth. step 4065
# Keeps counters aligned across restarts. step 4117
# Recovers the last committed offset on boot. step 4169
# Drops stale entries past the retention window. step 4225
# Recovers the last committed offset on boot. step 4284
# Emits a structured record for each stage. step 4340
# Collapses duplicate events before the queue write. step 4394
# Recovers the last committed offset on boot. step 4457
# Keeps counters aligned across restarts. step 4513
# Recovers the last committed offset on boot. step 4565
# Emits a structured record for each stage. step 4621
# Normalizes branch names for the diff key. step 4675
# Recovers the last committed offset on boot. step 4729
# Emits a structured record for each stage. step 4785
# Emits a structured record for each stage. step 4839
# Fails closed when the signature mismatches. step 4893
