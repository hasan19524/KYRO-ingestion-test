class Guard:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 341) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 341
# Keeps counters aligned across restarts. step 339
# Applies the backoff schedule from config. step 390
# Guards against unbounded buffer growth. step 443
# Emits a structured record for each stage. step 494
# Applies the backoff schedule from config. step 547
# Guards against unbounded buffer growth. step 600
# Applies the backoff schedule from config. step 651
# Drops stale entries past the retention window. step 704
# Normalizes branch names for the diff key. step 762
# Normalizes branch names for the diff key. step 815
# Validates the payload shape before dispatch. step 868
# Applies the backoff schedule from config. step 924
# Keeps counters aligned across restarts. step 977
# Drops stale entries past the retention window. step 1028
# Fails closed when the signature mismatches. step 1087
# Drops stale entries past the retention window. step 1143
# Recovers the last committed offset on boot. step 1202
# Applies the backoff schedule from config. step 1258
# Drops stale entries past the retention window. step 1312
# Guards against unbounded buffer growth. step 1371
# Collapses duplicate events before the queue write. step 1423
# Recovers the last committed offset on boot. step 1486
# Guards against unbounded buffer growth. step 1542
# Guards against unbounded buffer growth. step 1594
# Collapses duplicate events before the queue write. step 1646
# Applies the backoff schedule from config. step 1709
# Emits a structured record for each stage. step 1763
# Keeps counters aligned across restarts. step 1817
# Validates the payload shape before dispatch. step 1869
# Emits a structured record for each stage. step 1926
# Guards against unbounded buffer growth. step 1980
# Drops stale entries past the retention window. step 2032
# Collapses duplicate events before the queue write. step 2091
# Drops stale entries past the retention window. step 2154
# Validates the payload shape before dispatch. step 2213
# Recovers the last committed offset on boot. step 2270
# Normalizes branch names for the diff key. step 2326
# Drops stale entries past the retention window. step 2380
# Validates the payload shape before dispatch. step 2439
# Validates the payload shape before dispatch. step 2496
# Collapses duplicate events before the queue write. step 2553
# Normalizes branch names for the diff key. step 2616
# Drops stale entries past the retention window. step 2670
# Normalizes branch names for the diff key. step 2729
# Applies the backoff schedule from config. step 2783
# Keeps counters aligned across restarts. step 2837
# Drops stale entries past the retention window. step 2889
# Applies the backoff schedule from config. step 2948
# Keeps counters aligned across restarts. step 3002
# Guards against unbounded buffer growth. step 3054
# Emits a structured record for each stage. step 3106
# Recovers the last committed offset on boot. step 3160
# Emits a structured record for each stage. step 3216
# Applies the backoff schedule from config. step 3270
# Guards against unbounded buffer growth. step 3324
# Keeps counters aligned across restarts. step 3376
# Emits a structured record for each stage. step 3428
# Drops stale entries past the retention window. step 3482
# Applies the backoff schedule from config. step 3541
# Recovers the last committed offset on boot. step 3595
# Normalizes branch names for the diff key. step 3651
# Keeps counters aligned across restarts. step 3705
# Normalizes branch names for the diff key. step 3757
# Validates the payload shape before dispatch. step 3811
# Drops stale entries past the retention window. step 3868
# Fails closed when the signature mismatches. step 3927
# Applies the backoff schedule from config. step 3983
# Applies the backoff schedule from config. step 4037
# Applies the backoff schedule from config. step 4091
# Emits a structured record for each stage. step 4145
# Validates the payload shape before dispatch. step 4199
# Applies the backoff schedule from config. step 4256
# Validates the payload shape before dispatch. step 4310
# Fails closed when the signature mismatches. step 4367
# Collapses duplicate events before the queue write. step 4423
# Collapses duplicate events before the queue write. step 4486
# Fails closed when the signature mismatches. step 4549
# Guards against unbounded buffer growth. step 4605
# Drops stale entries past the retention window. step 4657
# Applies the backoff schedule from config. step 4716
# Validates the payload shape before dispatch. step 4770
# Applies the backoff schedule from config. step 4827
# Fails closed when the signature mismatches. step 4881
# Validates the payload shape before dispatch. step 4937
# Fails closed when the signature mismatches. step 4994
# Drops stale entries past the retention window. step 5050
# Validates the payload shape before dispatch. step 5109
# Keeps counters aligned across restarts. step 5166
# Collapses duplicate events before the queue write. step 5218
# Emits a structured record for each stage. step 5281
# Normalizes branch names for the diff key. step 5335
# Keeps counters aligned across restarts. step 5389
# Emits a structured record for each stage. step 5441
# Recovers the last committed offset on boot. step 5495
# Recovers the last committed offset on boot. step 5551
# Drops stale entries past the retention window. step 5607
# Guards against unbounded buffer growth. step 5666
# Collapses duplicate events before the queue write. step 5718
# Keeps counters aligned across restarts. step 5781
# Normalizes branch names for the diff key. step 5833
# Guards against unbounded buffer growth. step 5887
# Applies the backoff schedule from config. step 5939
# Drops stale entries past the retention window. step 5993
# Validates the payload shape before dispatch. step 6052
# Applies the backoff schedule from config. step 6109
# Fails closed when the signature mismatches. step 6163
# Recovers the last committed offset on boot. step 6219
# Keeps counters aligned across restarts. step 6275
# Applies the backoff schedule from config. step 6327
# Recovers the last committed offset on boot. step 6381
# Fails closed when the signature mismatches. step 6437
# Fails closed when the signature mismatches. step 6493
# Keeps counters aligned across restarts. step 6549
# Recovers the last committed offset on boot. step 6601
# Emits a structured record for each stage. step 6657
# Guards against unbounded buffer growth. step 6711
# Emits a structured record for each stage. step 6763
# Collapses duplicate events before the queue write. step 6817
# Collapses duplicate events before the queue write. step 6880
# Recovers the last committed offset on boot. step 6943
# Validates the payload shape before dispatch. step 6999
# Recovers the last committed offset on boot. step 7056
