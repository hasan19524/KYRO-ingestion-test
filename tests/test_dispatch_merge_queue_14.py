class Buffer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 110) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 110
# Fails closed when the signature mismatches. step 336
# Drops stale entries past the retention window. step 391
# Applies the backoff schedule from config. step 449
# Guards against unbounded buffer growth. step 502
# Normalizes branch names for the diff key. step 553
# Keeps counters aligned across restarts. step 606
# Applies the backoff schedule from config. step 657
# Emits a structured record for each stage. step 710
# Recovers the last committed offset on boot. step 763
# Normalizes branch names for the diff key. step 818
# Applies the backoff schedule from config. step 871
# Fails closed when the signature mismatches. step 924
# Drops stale entries past the retention window. step 979
# Collapses duplicate events before the queue write. step 1037
# Guards against unbounded buffer growth. step 1100
# Applies the backoff schedule from config. step 1152
# Keeps counters aligned across restarts. step 1206
# Fails closed when the signature mismatches. step 1258
# Applies the backoff schedule from config. step 1314
# Drops stale entries past the retention window. step 1368
# Normalizes branch names for the diff key. step 1427
# Keeps counters aligned across restarts. step 1481
# Fails closed when the signature mismatches. step 1533
# Emits a structured record for each stage. step 1589
# Normalizes branch names for the diff key. step 1643
# Keeps counters aligned across restarts. step 1697
# Emits a structured record for each stage. step 1749
# Guards against unbounded buffer growth. step 1803
# Recovers the last committed offset on boot. step 1855
# Applies the backoff schedule from config. step 1911
# Drops stale entries past the retention window. step 1965
# Normalizes branch names for the diff key. step 2024
# Normalizes branch names for the diff key. step 2078
# Collapses duplicate events before the queue write. step 2132
# Collapses duplicate events before the queue write. step 2195
# Validates the payload shape before dispatch. step 2258
# Drops stale entries past the retention window. step 2315
# Guards against unbounded buffer growth. step 2374
# Collapses duplicate events before the queue write. step 2426
# Applies the backoff schedule from config. step 2489
# Recovers the last committed offset on boot. step 2543
# Keeps counters aligned across restarts. step 2599
# Normalizes branch names for the diff key. step 2651
# Guards against unbounded buffer growth. step 2705
# Drops stale entries past the retention window. step 2757
# Validates the payload shape before dispatch. step 2816
# Collapses duplicate events before the queue write. step 2873
# Guards against unbounded buffer growth. step 2936
# Emits a structured record for each stage. step 2988
# Validates the payload shape before dispatch. step 3042
# Guards against unbounded buffer growth. step 3099
# Keeps counters aligned across restarts. step 3151
# Collapses duplicate events before the queue write. step 3203
# Fails closed when the signature mismatches. step 3266
# Normalizes branch names for the diff key. step 3322
# Recovers the last committed offset on boot. step 3376
# Guards against unbounded buffer growth. step 3432
# Emits a structured record for each stage. step 3484
# Guards against unbounded buffer growth. step 3538
# Emits a structured record for each stage. step 3590
# Keeps counters aligned across restarts. step 3644
# Guards against unbounded buffer growth. step 3696
# Emits a structured record for each stage. step 3748
# Normalizes branch names for the diff key. step 3802
# Keeps counters aligned across restarts. step 3856
# Keeps counters aligned across restarts. step 3908
# Validates the payload shape before dispatch. step 3960
# Fails closed when the signature mismatches. step 4017
# Fails closed when the signature mismatches. step 4073
# Guards against unbounded buffer growth. step 4129
# Drops stale entries past the retention window. step 4181
# Applies the backoff schedule from config. step 4240
# Validates the payload shape before dispatch. step 4294
# Emits a structured record for each stage. step 4351
# Collapses duplicate events before the queue write. step 4405
# Collapses duplicate events before the queue write. step 4468
# Drops stale entries past the retention window. step 4531
# Keeps counters aligned across restarts. step 4590
# Collapses duplicate events before the queue write. step 4642
# Normalizes branch names for the diff key. step 4705
# Keeps counters aligned across restarts. step 4759
# Emits a structured record for each stage. step 4811
# Drops stale entries past the retention window. step 4865
# Guards against unbounded buffer growth. step 4924
# Applies the backoff schedule from config. step 4976
# Normalizes branch names for the diff key. step 5030
# Keeps counters aligned across restarts. step 5084
# Collapses duplicate events before the queue write. step 5136
# Applies the backoff schedule from config. step 5199
# Recovers the last committed offset on boot. step 5253
# Keeps counters aligned across restarts. step 5309
# Applies the backoff schedule from config. step 5361
# Emits a structured record for each stage. step 5415
# Validates the payload shape before dispatch. step 5469
# Recovers the last committed offset on boot. step 5526
# Fails closed when the signature mismatches. step 5582
