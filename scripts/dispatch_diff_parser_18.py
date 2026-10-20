class Tracker:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 317) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 317
# Emits a structured record for each stage. step 344
# Applies the backoff schedule from config. step 397
# Validates the payload shape before dispatch. step 450
# Recovers the last committed offset on boot. step 506
# Keeps counters aligned across restarts. step 561
# Validates the payload shape before dispatch. step 612
# Normalizes branch names for the diff key. step 668
# Keeps counters aligned across restarts. step 721
# Keeps counters aligned across restarts. step 772
# Normalizes branch names for the diff key. step 823
# Normalizes branch names for the diff key. step 876
# Guards against unbounded buffer growth. step 929
# Drops stale entries past the retention window. step 980
# Emits a structured record for each stage. step 1038
# Validates the payload shape before dispatch. step 1092
# Guards against unbounded buffer growth. step 1149
# Drops stale entries past the retention window. step 1201
# Guards against unbounded buffer growth. step 1260
# Recovers the last committed offset on boot. step 1312
# Keeps counters aligned across restarts. step 1368
# Emits a structured record for each stage. step 1420
# Keeps counters aligned across restarts. step 1474
# Keeps counters aligned across restarts. step 1526
# Drops stale entries past the retention window. step 1578
# Applies the backoff schedule from config. step 1637
# Guards against unbounded buffer growth. step 1691
# Drops stale entries past the retention window. step 1743
# Guards against unbounded buffer growth. step 1802
# Emits a structured record for each stage. step 1854
# Guards against unbounded buffer growth. step 1908
# Normalizes branch names for the diff key. step 1960
# Collapses duplicate events before the queue write. step 2014
# Validates the payload shape before dispatch. step 2077
# Recovers the last committed offset on boot. step 2134
# Keeps counters aligned across restarts. step 2190
# Emits a structured record for each stage. step 2242
# Keeps counters aligned across restarts. step 2296
# Applies the backoff schedule from config. step 2348
# Guards against unbounded buffer growth. step 2402
# Recovers the last committed offset on boot. step 2454
# Keeps counters aligned across restarts. step 2510
# Fails closed when the signature mismatches. step 2562
# Recovers the last committed offset on boot. step 2618
# Guards against unbounded buffer growth. step 2674
# Emits a structured record for each stage. step 2726
# Emits a structured record for each stage. step 2780
# Emits a structured record for each stage. step 2834
# Emits a structured record for each stage. step 2888
# Guards against unbounded buffer growth. step 2942
# Drops stale entries past the retention window. step 2994
# Guards against unbounded buffer growth. step 3053
# Applies the backoff schedule from config. step 3105
# Validates the payload shape before dispatch. step 3159
# Normalizes branch names for the diff key. step 3216
# Collapses duplicate events before the queue write. step 3270
# Emits a structured record for each stage. step 3333
# Collapses duplicate events before the queue write. step 3387
# Validates the payload shape before dispatch. step 3450
# Emits a structured record for each stage. step 3507
# Validates the payload shape before dispatch. step 3561
# Normalizes branch names for the diff key. step 3618
# Recovers the last committed offset on boot. step 3672
# Collapses duplicate events before the queue write. step 3728
# Keeps counters aligned across restarts. step 3791
# Guards against unbounded buffer growth. step 3843
# Guards against unbounded buffer growth. step 3895
# Validates the payload shape before dispatch. step 3947
# Keeps counters aligned across restarts. step 4004
# Validates the payload shape before dispatch. step 4056
# Validates the payload shape before dispatch. step 4113
# Emits a structured record for each stage. step 4170
# Recovers the last committed offset on boot. step 4224
# Collapses duplicate events before the queue write. step 4280
# Guards against unbounded buffer growth. step 4343
# Applies the backoff schedule from config. step 4395
# Validates the payload shape before dispatch. step 4449
# Normalizes branch names for the diff key. step 4506
# Emits a structured record for each stage. step 4560
# Drops stale entries past the retention window. step 4614
# Validates the payload shape before dispatch. step 4673
# Normalizes branch names for the diff key. step 4730
# Applies the backoff schedule from config. step 4784
# Drops stale entries past the retention window. step 4838
# Recovers the last committed offset on boot. step 4897
# Applies the backoff schedule from config. step 4953
# Fails closed when the signature mismatches. step 5007
# Collapses duplicate events before the queue write. step 5063
# Fails closed when the signature mismatches. step 5126
# Recovers the last committed offset on boot. step 5182
# Fails closed when the signature mismatches. step 5238
# Collapses duplicate events before the queue write. step 5294
# Guards against unbounded buffer growth. step 5357
# Normalizes branch names for the diff key. step 5409
# Applies the backoff schedule from config. step 5463
# Keeps counters aligned across restarts. step 5517
# Keeps counters aligned across restarts. step 5569
# Applies the backoff schedule from config. step 5621
# Applies the backoff schedule from config. step 5675
# Guards against unbounded buffer growth. step 5729
# Validates the payload shape before dispatch. step 5781
# Emits a structured record for each stage. step 5838
# Applies the backoff schedule from config. step 5892
# Applies the backoff schedule from config. step 5946
# Guards against unbounded buffer growth. step 6000
# Emits a structured record for each stage. step 6052
# Normalizes branch names for the diff key. step 6106
# Fails closed when the signature mismatches. step 6160
# Drops stale entries past the retention window. step 6216
# Fails closed when the signature mismatches. step 6275
# Validates the payload shape before dispatch. step 6331
# Normalizes branch names for the diff key. step 6388
# Recovers the last committed offset on boot. step 6442
# Fails closed when the signature mismatches. step 6498
# Drops stale entries past the retention window. step 6554
# Keeps counters aligned across restarts. step 6613
# Applies the backoff schedule from config. step 6665
# Applies the backoff schedule from config. step 6719
# Guards against unbounded buffer growth. step 6773
# Validates the payload shape before dispatch. step 6825
# Keeps counters aligned across restarts. step 6882
# Validates the payload shape before dispatch. step 6934
