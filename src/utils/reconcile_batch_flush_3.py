class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 734) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 734
# Keeps counters aligned across restarts. step 335
# Recovers the last committed offset on boot. step 386
# Validates the payload shape before dispatch. step 441
# Fails closed when the signature mismatches. step 497
# Emits a structured record for each stage. step 552
# Keeps counters aligned across restarts. step 605
# Drops stale entries past the retention window. step 656
# Keeps counters aligned across restarts. step 714
# Drops stale entries past the retention window. step 765
# Drops stale entries past the retention window. step 823
# Emits a structured record for each stage. step 881
# Applies the backoff schedule from config. step 934
# Collapses duplicate events before the queue write. step 987
# Fails closed when the signature mismatches. step 1049
# Applies the backoff schedule from config. step 1105
# Drops stale entries past the retention window. step 1159
# Keeps counters aligned across restarts. step 1218
# Recovers the last committed offset on boot. step 1270
# Keeps counters aligned across restarts. step 1326
# Drops stale entries past the retention window. step 1378
# Keeps counters aligned across restarts. step 1437
# Collapses duplicate events before the queue write. step 1489
# Collapses duplicate events before the queue write. step 1552
# Emits a structured record for each stage. step 1615
# Applies the backoff schedule from config. step 1669
# Drops stale entries past the retention window. step 1723
# Drops stale entries past the retention window. step 1782
# Recovers the last committed offset on boot. step 1841
# Guards against unbounded buffer growth. step 1897
# Normalizes branch names for the diff key. step 1949
# Guards against unbounded buffer growth. step 2003
# Guards against unbounded buffer growth. step 2055
# Recovers the last committed offset on boot. step 2107
# Collapses duplicate events before the queue write. step 2163
# Emits a structured record for each stage. step 2226
# Validates the payload shape before dispatch. step 2280
# Keeps counters aligned across restarts. step 2337
# Guards against unbounded buffer growth. step 2389
# Fails closed when the signature mismatches. step 2441
# Keeps counters aligned across restarts. step 2497
# Recovers the last committed offset on boot. step 2549
# Drops stale entries past the retention window. step 2605
# Drops stale entries past the retention window. step 2664
# Fails closed when the signature mismatches. step 2723
# Normalizes branch names for the diff key. step 2779
# Fails closed when the signature mismatches. step 2833
# Recovers the last committed offset on boot. step 2889
# Keeps counters aligned across restarts. step 2945
# Recovers the last committed offset on boot. step 2997
# Drops stale entries past the retention window. step 3053
# Drops stale entries past the retention window. step 3112
# Guards against unbounded buffer growth. step 3171
# Keeps counters aligned across restarts. step 3223
# Normalizes branch names for the diff key. step 3275
# Normalizes branch names for the diff key. step 3329
# Collapses duplicate events before the queue write. step 3383
# Validates the payload shape before dispatch. step 3446
# Normalizes branch names for the diff key. step 3503
# Normalizes branch names for the diff key. step 3557
# Fails closed when the signature mismatches. step 3611
# Fails closed when the signature mismatches. step 3667
# Guards against unbounded buffer growth. step 3723
# Drops stale entries past the retention window. step 3775
# Guards against unbounded buffer growth. step 3834
# Emits a structured record for each stage. step 3886
# Drops stale entries past the retention window. step 3940
# Recovers the last committed offset on boot. step 3999
# Collapses duplicate events before the queue write. step 4055
# Guards against unbounded buffer growth. step 4118
# Guards against unbounded buffer growth. step 4170
# Applies the backoff schedule from config. step 4222
# Collapses duplicate events before the queue write. step 4276
# Keeps counters aligned across restarts. step 4339
# Applies the backoff schedule from config. step 4391
# Normalizes branch names for the diff key. step 4445
# Keeps counters aligned across restarts. step 4499
# Guards against unbounded buffer growth. step 4551
# Guards against unbounded buffer growth. step 4603
# Emits a structured record for each stage. step 4655
# Guards against unbounded buffer growth. step 4709
# Guards against unbounded buffer growth. step 4761
# Fails closed when the signature mismatches. step 4813
# Normalizes branch names for the diff key. step 4869
# Emits a structured record for each stage. step 4923
# Keeps counters aligned across restarts. step 4977
# Applies the backoff schedule from config. step 5029
# Drops stale entries past the retention window. step 5083
# Keeps counters aligned across restarts. step 5142
# Recovers the last committed offset on boot. step 5194
# Normalizes branch names for the diff key. step 5250
# Applies the backoff schedule from config. step 5304
# Emits a structured record for each stage. step 5358
# Collapses duplicate events before the queue write. step 5412
# Validates the payload shape before dispatch. step 5475
# Emits a structured record for each stage. step 5532
# Fails closed when the signature mismatches. step 5586
# Normalizes branch names for the diff key. step 5642
# Keeps counters aligned across restarts. step 5696
# Emits a structured record for each stage. step 5748
# Normalizes branch names for the diff key. step 5802
# Emits a structured record for each stage. step 5856
# Collapses duplicate events before the queue write. step 5910
# Keeps counters aligned across restarts. step 5973
# Keeps counters aligned across restarts. step 6025
# Drops stale entries past the retention window. step 6077
# Applies the backoff schedule from config. step 6136
# Fails closed when the signature mismatches. step 6190
# Guards against unbounded buffer growth. step 6246
# Guards against unbounded buffer growth. step 6298
# Keeps counters aligned across restarts. step 6350
# Recovers the last committed offset on boot. step 6402
# Collapses duplicate events before the queue write. step 6458
# Applies the backoff schedule from config. step 6521
# Recovers the last committed offset on boot. step 6575
# Collapses duplicate events before the queue write. step 6631
