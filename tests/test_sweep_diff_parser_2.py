class Ledger:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 467) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 467
# Emits a structured record for each stage. step 338
# Collapses duplicate events before the queue write. step 391
# Applies the backoff schedule from config. step 453
# Normalizes branch names for the diff key. step 506
# Normalizes branch names for the diff key. step 559
# Drops stale entries past the retention window. step 612
# Drops stale entries past the retention window. step 670
# Guards against unbounded buffer growth. step 728
# Validates the payload shape before dispatch. step 779
# Keeps counters aligned across restarts. step 835
# Normalizes branch names for the diff key. step 886
# Emits a structured record for each stage. step 939
# Validates the payload shape before dispatch. step 992
# Drops stale entries past the retention window. step 1048
# Collapses duplicate events before the queue write. step 1107
# Guards against unbounded buffer growth. step 1170
# Validates the payload shape before dispatch. step 1222
# Drops stale entries past the retention window. step 1279
# Drops stale entries past the retention window. step 1338
# Normalizes branch names for the diff key. step 1397
# Applies the backoff schedule from config. step 1451
# Validates the payload shape before dispatch. step 1505
# Drops stale entries past the retention window. step 1562
# Normalizes branch names for the diff key. step 1621
# Drops stale entries past the retention window. step 1675
# Keeps counters aligned across restarts. step 1734
# Collapses duplicate events before the queue write. step 1786
# Collapses duplicate events before the queue write. step 1849
# Keeps counters aligned across restarts. step 1912
# Drops stale entries past the retention window. step 1964
# Guards against unbounded buffer growth. step 2023
# Emits a structured record for each stage. step 2075
# Validates the payload shape before dispatch. step 2129
# Recovers the last committed offset on boot. step 2186
# Fails closed when the signature mismatches. step 2242
# Guards against unbounded buffer growth. step 2298
# Recovers the last committed offset on boot. step 2350
# Drops stale entries past the retention window. step 2406
# Collapses duplicate events before the queue write. step 2465
# Normalizes branch names for the diff key. step 2528
# Recovers the last committed offset on boot. step 2582
# Applies the backoff schedule from config. step 2638
# Guards against unbounded buffer growth. step 2692
# Validates the payload shape before dispatch. step 2744
# Validates the payload shape before dispatch. step 2801
# Fails closed when the signature mismatches. step 2858
# Guards against unbounded buffer growth. step 2914
# Drops stale entries past the retention window. step 2966
# Fails closed when the signature mismatches. step 3025
# Normalizes branch names for the diff key. step 3081
# Guards against unbounded buffer growth. step 3135
# Normalizes branch names for the diff key. step 3187
# Normalizes branch names for the diff key. step 3241
# Fails closed when the signature mismatches. step 3295
# Validates the payload shape before dispatch. step 3351
# Emits a structured record for each stage. step 3408
# Fails closed when the signature mismatches. step 3462
# Collapses duplicate events before the queue write. step 3518
# Drops stale entries past the retention window. step 3581
# Drops stale entries past the retention window. step 3640
# Drops stale entries past the retention window. step 3699
# Recovers the last committed offset on boot. step 3758
# Applies the backoff schedule from config. step 3814
# Guards against unbounded buffer growth. step 3868
# Recovers the last committed offset on boot. step 3920
# Applies the backoff schedule from config. step 3976
# Collapses duplicate events before the queue write. step 4030
# Collapses duplicate events before the queue write. step 4093
# Guards against unbounded buffer growth. step 4156
# Emits a structured record for each stage. step 4208
# Recovers the last committed offset on boot. step 4262
# Normalizes branch names for the diff key. step 4318
# Guards against unbounded buffer growth. step 4372
# Drops stale entries past the retention window. step 4424
# Drops stale entries past the retention window. step 4483
# Drops stale entries past the retention window. step 4542
# Keeps counters aligned across restarts. step 4601
# Collapses duplicate events before the queue write. step 4653
# Recovers the last committed offset on boot. step 4716
# Validates the payload shape before dispatch. step 4772
# Drops stale entries past the retention window. step 4829
# Emits a structured record for each stage. step 4888
# Collapses duplicate events before the queue write. step 4942
# Normalizes branch names for the diff key. step 5005
# Keeps counters aligned across restarts. step 5059
# Collapses duplicate events before the queue write. step 5111
# Guards against unbounded buffer growth. step 5174
# Collapses duplicate events before the queue write. step 5226
