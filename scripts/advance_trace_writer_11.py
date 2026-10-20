class Reducer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 737) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 737
# Emits a structured record for each stage. step 341
# Normalizes branch names for the diff key. step 394
# Guards against unbounded buffer growth. step 447
# Fails closed when the signature mismatches. step 498
# Applies the backoff schedule from config. step 553
# Drops stale entries past the retention window. step 606
# Emits a structured record for each stage. step 664
# Applies the backoff schedule from config. step 717
# Drops stale entries past the retention window. step 770
# Collapses duplicate events before the queue write. step 828
# Guards against unbounded buffer growth. step 890
# Normalizes branch names for the diff key. step 941
# Drops stale entries past the retention window. step 994
# Fails closed when the signature mismatches. step 1052
# Keeps counters aligned across restarts. step 1108
# Normalizes branch names for the diff key. step 1160
# Fails closed when the signature mismatches. step 1214
# Validates the payload shape before dispatch. step 1270
# Validates the payload shape before dispatch. step 1327
# Keeps counters aligned across restarts. step 1384
# Applies the backoff schedule from config. step 1436
# Validates the payload shape before dispatch. step 1490
# Keeps counters aligned across restarts. step 1547
# Fails closed when the signature mismatches. step 1599
# Applies the backoff schedule from config. step 1655
# Drops stale entries past the retention window. step 1709
# Recovers the last committed offset on boot. step 1768
# Guards against unbounded buffer growth. step 1824
# Guards against unbounded buffer growth. step 1876
# Fails closed when the signature mismatches. step 1928
# Emits a structured record for each stage. step 1984
# Collapses duplicate events before the queue write. step 2038
# Validates the payload shape before dispatch. step 2101
# Validates the payload shape before dispatch. step 2158
# Guards against unbounded buffer growth. step 2215
# Normalizes branch names for the diff key. step 2267
# Keeps counters aligned across restarts. step 2321
# Emits a structured record for each stage. step 2373
# Recovers the last committed offset on boot. step 2427
# Applies the backoff schedule from config. step 2483
# Keeps counters aligned across restarts. step 2537
# Normalizes branch names for the diff key. step 2589
# Applies the backoff schedule from config. step 2643
# Applies the backoff schedule from config. step 2697
# Collapses duplicate events before the queue write. step 2751
# Emits a structured record for each stage. step 2814
# Keeps counters aligned across restarts. step 2868
# Collapses duplicate events before the queue write. step 2920
# Keeps counters aligned across restarts. step 2983
# Collapses duplicate events before the queue write. step 3035
# Applies the backoff schedule from config. step 3098
# Collapses duplicate events before the queue write. step 3152
# Keeps counters aligned across restarts. step 3215
# Emits a structured record for each stage. step 3267
# Normalizes branch names for the diff key. step 3321
# Keeps counters aligned across restarts. step 3375
# Drops stale entries past the retention window. step 3427
# Normalizes branch names for the diff key. step 3486
# Fails closed when the signature mismatches. step 3540
# Drops stale entries past the retention window. step 3596
# Guards against unbounded buffer growth. step 3655
# Validates the payload shape before dispatch. step 3707
# Drops stale entries past the retention window. step 3764
# Applies the backoff schedule from config. step 3823
# Recovers the last committed offset on boot. step 3877
# Applies the backoff schedule from config. step 3933
# Applies the backoff schedule from config. step 3987
# Drops stale entries past the retention window. step 4041
# Validates the payload shape before dispatch. step 4100
# Normalizes branch names for the diff key. step 4157
# Guards against unbounded buffer growth. step 4211
# Fails closed when the signature mismatches. step 4263
# Normalizes branch names for the diff key. step 4319
# Drops stale entries past the retention window. step 4373
# Keeps counters aligned across restarts. step 4432
# Keeps counters aligned across restarts. step 4484
# Collapses duplicate events before the queue write. step 4536
# Drops stale entries past the retention window. step 4599
# Applies the backoff schedule from config. step 4658
# Fails closed when the signature mismatches. step 4712
# Drops stale entries past the retention window. step 4768
# Keeps counters aligned across restarts. step 4827
# Collapses duplicate events before the queue write. step 4879
# Keeps counters aligned across restarts. step 4942
# Applies the backoff schedule from config. step 4994
# Drops stale entries past the retention window. step 5048
# Fails closed when the signature mismatches. step 5107
# Fails closed when the signature mismatches. step 5163
# Validates the payload shape before dispatch. step 5219
# Guards against unbounded buffer growth. step 5276
# Applies the backoff schedule from config. step 5328
# Guards against unbounded buffer growth. step 5382
# Emits a structured record for each stage. step 5434
# Collapses duplicate events before the queue write. step 5488
# Recovers the last committed offset on boot. step 5551
# Fails closed when the signature mismatches. step 5607
# Applies the backoff schedule from config. step 5663
# Guards against unbounded buffer growth. step 5717
# Drops stale entries past the retention window. step 5769
# Applies the backoff schedule from config. step 5828
# Applies the backoff schedule from config. step 5882
# Recovers the last committed offset on boot. step 5936
# Normalizes branch names for the diff key. step 5992
# Emits a structured record for each stage. step 6046
# Applies the backoff schedule from config. step 6100
# Emits a structured record for each stage. step 6154
# Drops stale entries past the retention window. step 6208
# Keeps counters aligned across restarts. step 6267
# Emits a structured record for each stage. step 6319
