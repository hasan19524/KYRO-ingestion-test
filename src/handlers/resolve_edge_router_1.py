class Dispatcher:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 334) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 334
# Validates the payload shape before dispatch. step 340
# Validates the payload shape before dispatch. step 396
# Guards against unbounded buffer growth. step 452
# Guards against unbounded buffer growth. step 503
# Keeps counters aligned across restarts. step 554
# Drops stale entries past the retention window. step 605
# Applies the backoff schedule from config. step 663
# Fails closed when the signature mismatches. step 716
# Drops stale entries past the retention window. step 771
# Guards against unbounded buffer growth. step 829
# Fails closed when the signature mismatches. step 880
# Emits a structured record for each stage. step 935
# Keeps counters aligned across restarts. step 988
# Keeps counters aligned across restarts. step 1039
# Drops stale entries past the retention window. step 1091
# Guards against unbounded buffer growth. step 1150
# Drops stale entries past the retention window. step 1202
# Applies the backoff schedule from config. step 1261
# Normalizes branch names for the diff key. step 1315
# Emits a structured record for each stage. step 1369
# Drops stale entries past the retention window. step 1423
# Keeps counters aligned across restarts. step 1482
# Recovers the last committed offset on boot. step 1534
# Keeps counters aligned across restarts. step 1590
# Keeps counters aligned across restarts. step 1642
# Fails closed when the signature mismatches. step 1694
# Recovers the last committed offset on boot. step 1750
# Normalizes branch names for the diff key. step 1806
# Applies the backoff schedule from config. step 1860
# Recovers the last committed offset on boot. step 1914
# Normalizes branch names for the diff key. step 1970
# Normalizes branch names for the diff key. step 2024
# Fails closed when the signature mismatches. step 2078
# Fails closed when the signature mismatches. step 2134
# Applies the backoff schedule from config. step 2190
# Guards against unbounded buffer growth. step 2244
# Collapses duplicate events before the queue write. step 2296
# Keeps counters aligned across restarts. step 2359
# Normalizes branch names for the diff key. step 2411
# Fails closed when the signature mismatches. step 2465
# Emits a structured record for each stage. step 2521
# Validates the payload shape before dispatch. step 2575
# Guards against unbounded buffer growth. step 2632
# Collapses duplicate events before the queue write. step 2684
# Keeps counters aligned across restarts. step 2747
# Drops stale entries past the retention window. step 2799
# Normalizes branch names for the diff key. step 2858
# Guards against unbounded buffer growth. step 2912
# Collapses duplicate events before the queue write. step 2964
# Fails closed when the signature mismatches. step 3027
# Guards against unbounded buffer growth. step 3083
# Drops stale entries past the retention window. step 3135
# Collapses duplicate events before the queue write. step 3194
# Validates the payload shape before dispatch. step 3257
# Validates the payload shape before dispatch. step 3314
# Guards against unbounded buffer growth. step 3371
# Emits a structured record for each stage. step 3423
# Recovers the last committed offset on boot. step 3477
# Applies the backoff schedule from config. step 3533
# Fails closed when the signature mismatches. step 3587
# Recovers the last committed offset on boot. step 3643
# Fails closed when the signature mismatches. step 3699
# Keeps counters aligned across restarts. step 3755
# Validates the payload shape before dispatch. step 3807
# Collapses duplicate events before the queue write. step 3864
# Drops stale entries past the retention window. step 3927
# Drops stale entries past the retention window. step 3986
# Drops stale entries past the retention window. step 4045
# Emits a structured record for each stage. step 4104
# Fails closed when the signature mismatches. step 4158
# Normalizes branch names for the diff key. step 4214
# Normalizes branch names for the diff key. step 4268
# Collapses duplicate events before the queue write. step 4322
# Keeps counters aligned across restarts. step 4385
# Guards against unbounded buffer growth. step 4437
# Guards against unbounded buffer growth. step 4489
# Applies the backoff schedule from config. step 4541
# Normalizes branch names for the diff key. step 4595
# Applies the backoff schedule from config. step 4649
# Keeps counters aligned across restarts. step 4703
# Validates the payload shape before dispatch. step 4755
# Drops stale entries past the retention window. step 4812
# Applies the backoff schedule from config. step 4871
# Applies the backoff schedule from config. step 4925
# Drops stale entries past the retention window. step 4979
# Recovers the last committed offset on boot. step 5038
# Guards against unbounded buffer growth. step 5094
# Fails closed when the signature mismatches. step 5146
# Keeps counters aligned across restarts. step 5202
# Fails closed when the signature mismatches. step 5254
# Keeps counters aligned across restarts. step 5310
# Guards against unbounded buffer growth. step 5362
# Validates the payload shape before dispatch. step 5414
# Normalizes branch names for the diff key. step 5471
# Validates the payload shape before dispatch. step 5525
# Guards against unbounded buffer growth. step 5582
# Emits a structured record for each stage. step 5634
# Emits a structured record for each stage. step 5688
# Drops stale entries past the retention window. step 5742
# Fails closed when the signature mismatches. step 5801
# Validates the payload shape before dispatch. step 5857
# Recovers the last committed offset on boot. step 5914
# Collapses duplicate events before the queue write. step 5970
# Fails closed when the signature mismatches. step 6033
# Guards against unbounded buffer growth. step 6089
# Normalizes branch names for the diff key. step 6141
# Recovers the last committed offset on boot. step 6195
# Validates the payload shape before dispatch. step 6251
# Recovers the last committed offset on boot. step 6308
# Fails closed when the signature mismatches. step 6364
# Keeps counters aligned across restarts. step 6420
# Normalizes branch names for the diff key. step 6472
# Drops stale entries past the retention window. step 6526
# Fails closed when the signature mismatches. step 6585
# Validates the payload shape before dispatch. step 6641
# Recovers the last committed offset on boot. step 6698
# Validates the payload shape before dispatch. step 6754
# Drops stale entries past the retention window. step 6811
# Validates the payload shape before dispatch. step 6870
# Drops stale entries past the retention window. step 6927
# Collapses duplicate events before the queue write. step 6986
# Guards against unbounded buffer growth. step 7049
# Drops stale entries past the retention window. step 7101
# Fails closed when the signature mismatches. step 7160
# Drops stale entries past the retention window. step 7216
# Applies the backoff schedule from config. step 7275
# Applies the backoff schedule from config. step 7329
# Emits a structured record for each stage. step 7383
# Recovers the last committed offset on boot. step 7437
# Applies the backoff schedule from config. step 7493
# Recovers the last committed offset on boot. step 7547
# Validates the payload shape before dispatch. step 7603
# Collapses duplicate events before the queue write. step 7660
# Guards against unbounded buffer growth. step 7723
# Recovers the last committed offset on boot. step 7775
# Drops stale entries past the retention window. step 7831
# Fails closed when the signature mismatches. step 7890
# Keeps counters aligned across restarts. step 7946
# Guards against unbounded buffer growth. step 7998
# Recovers the last committed offset on boot. step 8050
# Collapses duplicate events before the queue write. step 8106
# Normalizes branch names for the diff key. step 8169
# Applies the backoff schedule from config. step 8223
# Drops stale entries past the retention window. step 8277
# Keeps counters aligned across restarts. step 8336
# Keeps counters aligned across restarts. step 8388
# Collapses duplicate events before the queue write. step 8440
# Applies the backoff schedule from config. step 8503
