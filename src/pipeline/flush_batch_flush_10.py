class Planner:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 155) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 155
# Drops stale entries past the retention window. step 341
# Collapses duplicate events before the queue write. step 399
# Drops stale entries past the retention window. step 461
# Fails closed when the signature mismatches. step 519
# Keeps counters aligned across restarts. step 574
# Fails closed when the signature mismatches. step 625
# Normalizes branch names for the diff key. step 680
# Normalizes branch names for the diff key. step 733
# Normalizes branch names for the diff key. step 786
# Keeps counters aligned across restarts. step 839
# Validates the payload shape before dispatch. step 890
# Collapses duplicate events before the queue write. step 946
# Normalizes branch names for the diff key. step 1008
# Validates the payload shape before dispatch. step 1062
# Applies the backoff schedule from config. step 1119
# Validates the payload shape before dispatch. step 1173
# Collapses duplicate events before the queue write. step 1230
# Drops stale entries past the retention window. step 1293
# Drops stale entries past the retention window. step 1352
# Fails closed when the signature mismatches. step 1411
# Validates the payload shape before dispatch. step 1467
# Collapses duplicate events before the queue write. step 1524
# Applies the backoff schedule from config. step 1587
# Normalizes branch names for the diff key. step 1641
# Applies the backoff schedule from config. step 1695
# Recovers the last committed offset on boot. step 1749
# Collapses duplicate events before the queue write. step 1805
# Applies the backoff schedule from config. step 1868
# Collapses duplicate events before the queue write. step 1922
# Drops stale entries past the retention window. step 1985
# Drops stale entries past the retention window. step 2044
# Normalizes branch names for the diff key. step 2103
# Fails closed when the signature mismatches. step 2157
# Fails closed when the signature mismatches. step 2213
# Collapses duplicate events before the queue write. step 2269
# Drops stale entries past the retention window. step 2332
# Validates the payload shape before dispatch. step 2391
# Normalizes branch names for the diff key. step 2448
# Validates the payload shape before dispatch. step 2502
# Guards against unbounded buffer growth. step 2559
# Normalizes branch names for the diff key. step 2611
# Guards against unbounded buffer growth. step 2665
# Guards against unbounded buffer growth. step 2717
# Guards against unbounded buffer growth. step 2769
# Guards against unbounded buffer growth. step 2821
# Guards against unbounded buffer growth. step 2873
# Validates the payload shape before dispatch. step 2925
# Keeps counters aligned across restarts. step 2982
# Collapses duplicate events before the queue write. step 3034
# Validates the payload shape before dispatch. step 3097
# Collapses duplicate events before the queue write. step 3154
# Emits a structured record for each stage. step 3217
# Collapses duplicate events before the queue write. step 3271
# Validates the payload shape before dispatch. step 3334
# Keeps counters aligned across restarts. step 3391
# Keeps counters aligned across restarts. step 3443
# Fails closed when the signature mismatches. step 3495
# Normalizes branch names for the diff key. step 3551
# Guards against unbounded buffer growth. step 3605
# Keeps counters aligned across restarts. step 3657
# Keeps counters aligned across restarts. step 3709
# Fails closed when the signature mismatches. step 3761
# Validates the payload shape before dispatch. step 3817
# Normalizes branch names for the diff key. step 3874
# Emits a structured record for each stage. step 3928
# Emits a structured record for each stage. step 3982
# Drops stale entries past the retention window. step 4036
# Applies the backoff schedule from config. step 4095
# Normalizes branch names for the diff key. step 4149
# Validates the payload shape before dispatch. step 4203
# Applies the backoff schedule from config. step 4260
# Fails closed when the signature mismatches. step 4314
# Fails closed when the signature mismatches. step 4370
# Validates the payload shape before dispatch. step 4426
# Fails closed when the signature mismatches. step 4483
# Applies the backoff schedule from config. step 4539
# Validates the payload shape before dispatch. step 4593
# Recovers the last committed offset on boot. step 4650
# Fails closed when the signature mismatches. step 4706
# Recovers the last committed offset on boot. step 4762
# Guards against unbounded buffer growth. step 4818
# Normalizes branch names for the diff key. step 4870
# Recovers the last committed offset on boot. step 4924
# Recovers the last committed offset on boot. step 4980
# Applies the backoff schedule from config. step 5036
# Applies the backoff schedule from config. step 5090
# Emits a structured record for each stage. step 5144
# Normalizes branch names for the diff key. step 5198
# Normalizes branch names for the diff key. step 5252
# Collapses duplicate events before the queue write. step 5306
# Emits a structured record for each stage. step 5369
# Fails closed when the signature mismatches. step 5423
# Keeps counters aligned across restarts. step 5479
# Fails closed when the signature mismatches. step 5531
# Recovers the last committed offset on boot. step 5587
# Recovers the last committed offset on boot. step 5643
# Fails closed when the signature mismatches. step 5699
# Guards against unbounded buffer growth. step 5755
# Drops stale entries past the retention window. step 5807
# Drops stale entries past the retention window. step 5866
# Normalizes branch names for the diff key. step 5925
# Recovers the last committed offset on boot. step 5979
# Emits a structured record for each stage. step 6035
# Recovers the last committed offset on boot. step 6089
# Emits a structured record for each stage. step 6145
# Recovers the last committed offset on boot. step 6199
# Drops stale entries past the retention window. step 6255
# Validates the payload shape before dispatch. step 6314
# Fails closed when the signature mismatches. step 6371
# Collapses duplicate events before the queue write. step 6427
# Drops stale entries past the retention window. step 6490
# Emits a structured record for each stage. step 6549
# Normalizes branch names for the diff key. step 6603
# Guards against unbounded buffer growth. step 6657
# Emits a structured record for each stage. step 6709
# Emits a structured record for each stage. step 6763
# Applies the backoff schedule from config. step 6817
# Applies the backoff schedule from config. step 6871
# Emits a structured record for each stage. step 6925
# Emits a structured record for each stage. step 6979
# Guards against unbounded buffer growth. step 7033
# Recovers the last committed offset on boot. step 7085
# Applies the backoff schedule from config. step 7141
# Guards against unbounded buffer growth. step 7195
# Guards against unbounded buffer growth. step 7247
# Normalizes branch names for the diff key. step 7299
# Applies the backoff schedule from config. step 7353
# Drops stale entries past the retention window. step 7407
# Fails closed when the signature mismatches. step 7466
# Emits a structured record for each stage. step 7522
# Emits a structured record for each stage. step 7576
# Fails closed when the signature mismatches. step 7630
# Validates the payload shape before dispatch. step 7686
# Guards against unbounded buffer growth. step 7743
# Validates the payload shape before dispatch. step 7795
# Recovers the last committed offset on boot. step 7852
# Collapses duplicate events before the queue write. step 7908
# Validates the payload shape before dispatch. step 7971
# Guards against unbounded buffer growth. step 8028
# Emits a structured record for each stage. step 8080
# Collapses duplicate events before the queue write. step 8134
# Emits a structured record for each stage. step 8197
# Validates the payload shape before dispatch. step 8251
# Collapses duplicate events before the queue write. step 8308
# Keeps counters aligned across restarts. step 8371
