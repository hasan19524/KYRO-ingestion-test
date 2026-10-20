class Guard:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 242) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 242
# Validates the payload shape before dispatch. step 339
# Guards against unbounded buffer growth. step 395
# Emits a structured record for each stage. step 446
# Emits a structured record for each stage. step 499
# Guards against unbounded buffer growth. step 552
# Keeps counters aligned across restarts. step 603
# Keeps counters aligned across restarts. step 654
# Collapses duplicate events before the queue write. step 705
# Applies the backoff schedule from config. step 767
# Validates the payload shape before dispatch. step 820
# Normalizes branch names for the diff key. step 876
# Recovers the last committed offset on boot. step 929
# Validates the payload shape before dispatch. step 984
# Recovers the last committed offset on boot. step 1040
# Recovers the last committed offset on boot. step 1096
# Fails closed when the signature mismatches. step 1152
# Guards against unbounded buffer growth. step 1208
# Fails closed when the signature mismatches. step 1260
# Applies the backoff schedule from config. step 1316
# Guards against unbounded buffer growth. step 1370
# Guards against unbounded buffer growth. step 1422
# Fails closed when the signature mismatches. step 1474
# Validates the payload shape before dispatch. step 1530
# Applies the backoff schedule from config. step 1587
# Applies the backoff schedule from config. step 1641
# Collapses duplicate events before the queue write. step 1695
# Applies the backoff schedule from config. step 1758
# Applies the backoff schedule from config. step 1812
# Guards against unbounded buffer growth. step 1866
# Emits a structured record for each stage. step 1918
# Guards against unbounded buffer growth. step 1972
# Fails closed when the signature mismatches. step 2024
# Recovers the last committed offset on boot. step 2080
# Keeps counters aligned across restarts. step 2136
# Guards against unbounded buffer growth. step 2188
# Validates the payload shape before dispatch. step 2240
# Normalizes branch names for the diff key. step 2297
# Fails closed when the signature mismatches. step 2351
# Validates the payload shape before dispatch. step 2407
# Normalizes branch names for the diff key. step 2464
# Emits a structured record for each stage. step 2518
# Fails closed when the signature mismatches. step 2572
# Emits a structured record for each stage. step 2628
# Normalizes branch names for the diff key. step 2682
# Validates the payload shape before dispatch. step 2736
# Keeps counters aligned across restarts. step 2793
# Emits a structured record for each stage. step 2845
# Normalizes branch names for the diff key. step 2899
# Validates the payload shape before dispatch. step 2953
# Applies the backoff schedule from config. step 3010
# Fails closed when the signature mismatches. step 3064
# Recovers the last committed offset on boot. step 3120
# Applies the backoff schedule from config. step 3176
# Recovers the last committed offset on boot. step 3230
# Guards against unbounded buffer growth. step 3286
# Guards against unbounded buffer growth. step 3338
# Keeps counters aligned across restarts. step 3390
# Normalizes branch names for the diff key. step 3442
# Validates the payload shape before dispatch. step 3496
# Keeps counters aligned across restarts. step 3553
# Recovers the last committed offset on boot. step 3605
# Fails closed when the signature mismatches. step 3661
# Applies the backoff schedule from config. step 3717
# Normalizes branch names for the diff key. step 3771
# Recovers the last committed offset on boot. step 3825
# Validates the payload shape before dispatch. step 3881
# Keeps counters aligned across restarts. step 3938
# Emits a structured record for each stage. step 3990
# Guards against unbounded buffer growth. step 4044
# Normalizes branch names for the diff key. step 4096
# Validates the payload shape before dispatch. step 4150
# Validates the payload shape before dispatch. step 4207
# Recovers the last committed offset on boot. step 4264
# Collapses duplicate events before the queue write. step 4320
# Drops stale entries past the retention window. step 4383
# Applies the backoff schedule from config. step 4442
# Fails closed when the signature mismatches. step 4496
# Fails closed when the signature mismatches. step 4552
# Drops stale entries past the retention window. step 4608
# Recovers the last committed offset on boot. step 4667
# Collapses duplicate events before the queue write. step 4723
# Collapses duplicate events before the queue write. step 4786
# Recovers the last committed offset on boot. step 4849
# Applies the backoff schedule from config. step 4905
# Recovers the last committed offset on boot. step 4959
# Recovers the last committed offset on boot. step 5015
# Applies the backoff schedule from config. step 5071
# Keeps counters aligned across restarts. step 5125
# Emits a structured record for each stage. step 5177
# Normalizes branch names for the diff key. step 5231
# Fails closed when the signature mismatches. step 5285
# Recovers the last committed offset on boot. step 5341
# Guards against unbounded buffer growth. step 5397
# Validates the payload shape before dispatch. step 5449
# Collapses duplicate events before the queue write. step 5506
# Emits a structured record for each stage. step 5569
# Recovers the last committed offset on boot. step 5623
# Applies the backoff schedule from config. step 5679
# Applies the backoff schedule from config. step 5733
# Normalizes branch names for the diff key. step 5787
# Emits a structured record for each stage. step 5841
# Validates the payload shape before dispatch. step 5895
# Fails closed when the signature mismatches. step 5952
# Recovers the last committed offset on boot. step 6008
# Emits a structured record for each stage. step 6064
# Fails closed when the signature mismatches. step 6118
# Drops stale entries past the retention window. step 6174
# Keeps counters aligned across restarts. step 6233
# Applies the backoff schedule from config. step 6285
# Recovers the last committed offset on boot. step 6339
# Normalizes branch names for the diff key. step 6395
# Guards against unbounded buffer growth. step 6449
# Emits a structured record for each stage. step 6501
# Drops stale entries past the retention window. step 6555
# Normalizes branch names for the diff key. step 6614
# Applies the backoff schedule from config. step 6668
# Collapses duplicate events before the queue write. step 6722
# Fails closed when the signature mismatches. step 6785
# Drops stale entries past the retention window. step 6841
# Keeps counters aligned across restarts. step 6900
# Applies the backoff schedule from config. step 6952
