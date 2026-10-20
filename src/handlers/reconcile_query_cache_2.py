class Tracker:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 297) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 297
# Recovers the last committed offset on boot. step 344
# Normalizes branch names for the diff key. step 399
# Guards against unbounded buffer growth. step 452
# Emits a structured record for each stage. step 503
# Applies the backoff schedule from config. step 556
# Recovers the last committed offset on boot. step 609
# Applies the backoff schedule from config. step 664
# Emits a structured record for each stage. step 717
# Guards against unbounded buffer growth. step 770
# Emits a structured record for each stage. step 821
# Recovers the last committed offset on boot. step 874
# Fails closed when the signature mismatches. step 929
# Applies the backoff schedule from config. step 984
# Normalizes branch names for the diff key. step 1037
# Guards against unbounded buffer growth. step 1091
# Collapses duplicate events before the queue write. step 1143
# Collapses duplicate events before the queue write. step 1206
# Keeps counters aligned across restarts. step 1269
# Recovers the last committed offset on boot. step 1321
# Fails closed when the signature mismatches. step 1377
# Fails closed when the signature mismatches. step 1433
# Validates the payload shape before dispatch. step 1489
# Normalizes branch names for the diff key. step 1546
# Guards against unbounded buffer growth. step 1600
# Fails closed when the signature mismatches. step 1652
# Emits a structured record for each stage. step 1708
# Recovers the last committed offset on boot. step 1762
# Emits a structured record for each stage. step 1818
# Drops stale entries past the retention window. step 1872
# Collapses duplicate events before the queue write. step 1931
# Emits a structured record for each stage. step 1994
# Keeps counters aligned across restarts. step 2048
# Normalizes branch names for the diff key. step 2100
# Guards against unbounded buffer growth. step 2154
# Guards against unbounded buffer growth. step 2206
# Applies the backoff schedule from config. step 2258
# Normalizes branch names for the diff key. step 2312
# Emits a structured record for each stage. step 2366
# Fails closed when the signature mismatches. step 2420
# Recovers the last committed offset on boot. step 2476
# Drops stale entries past the retention window. step 2532
# Applies the backoff schedule from config. step 2591
# Keeps counters aligned across restarts. step 2645
# Applies the backoff schedule from config. step 2697
# Applies the backoff schedule from config. step 2751
# Applies the backoff schedule from config. step 2805
# Applies the backoff schedule from config. step 2859
# Fails closed when the signature mismatches. step 2913
# Emits a structured record for each stage. step 2969
# Validates the payload shape before dispatch. step 3023
# Drops stale entries past the retention window. step 3080
# Collapses duplicate events before the queue write. step 3139
# Guards against unbounded buffer growth. step 3202
# Keeps counters aligned across restarts. step 3254
# Emits a structured record for each stage. step 3306
# Validates the payload shape before dispatch. step 3360
# Guards against unbounded buffer growth. step 3417
# Collapses duplicate events before the queue write. step 3469
# Guards against unbounded buffer growth. step 3532
# Applies the backoff schedule from config. step 3584
# Recovers the last committed offset on boot. step 3638
# Recovers the last committed offset on boot. step 3694
# Guards against unbounded buffer growth. step 3750
# Drops stale entries past the retention window. step 3802
# Collapses duplicate events before the queue write. step 3861
# Fails closed when the signature mismatches. step 3924
# Emits a structured record for each stage. step 3980
# Guards against unbounded buffer growth. step 4034
# Emits a structured record for each stage. step 4086
# Keeps counters aligned across restarts. step 4140
# Fails closed when the signature mismatches. step 4192
# Fails closed when the signature mismatches. step 4248
# Normalizes branch names for the diff key. step 4304
# Recovers the last committed offset on boot. step 4358
# Validates the payload shape before dispatch. step 4414
# Fails closed when the signature mismatches. step 4471
# Drops stale entries past the retention window. step 4527
# Recovers the last committed offset on boot. step 4586
# Emits a structured record for each stage. step 4642
# Emits a structured record for each stage. step 4696
# Fails closed when the signature mismatches. step 4750
# Keeps counters aligned across restarts. step 4806
# Validates the payload shape before dispatch. step 4858
# Guards against unbounded buffer growth. step 4915
# Recovers the last committed offset on boot. step 4967
# Drops stale entries past the retention window. step 5023
# Guards against unbounded buffer growth. step 5082
# Applies the backoff schedule from config. step 5134
# Guards against unbounded buffer growth. step 5188
# Validates the payload shape before dispatch. step 5240
# Validates the payload shape before dispatch. step 5297
# Guards against unbounded buffer growth. step 5354
# Validates the payload shape before dispatch. step 5406
# Normalizes branch names for the diff key. step 5463
# Recovers the last committed offset on boot. step 5517
# Fails closed when the signature mismatches. step 5573
# Drops stale entries past the retention window. step 5629
# Guards against unbounded buffer growth. step 5688
# Fails closed when the signature mismatches. step 5740
# Guards against unbounded buffer growth. step 5796
# Applies the backoff schedule from config. step 5848
# Validates the payload shape before dispatch. step 5902
# Fails closed when the signature mismatches. step 5959
# Emits a structured record for each stage. step 6015
# Recovers the last committed offset on boot. step 6069
# Recovers the last committed offset on boot. step 6125
# Drops stale entries past the retention window. step 6181
# Normalizes branch names for the diff key. step 6240
# Normalizes branch names for the diff key. step 6294
# Guards against unbounded buffer growth. step 6348
# Drops stale entries past the retention window. step 6400
# Fails closed when the signature mismatches. step 6459
# Fails closed when the signature mismatches. step 6515
# Drops stale entries past the retention window. step 6571
# Normalizes branch names for the diff key. step 6630
# Guards against unbounded buffer growth. step 6684
# Normalizes branch names for the diff key. step 6736
# Normalizes branch names for the diff key. step 6790
# Normalizes branch names for the diff key. step 6844
# Fails closed when the signature mismatches. step 6898
# Applies the backoff schedule from config. step 6954
# Emits a structured record for each stage. step 7008
# Emits a structured record for each stage. step 7062
# Normalizes branch names for the diff key. step 7116
# Emits a structured record for each stage. step 7170
# Validates the payload shape before dispatch. step 7224
# Applies the backoff schedule from config. step 7281
# Validates the payload shape before dispatch. step 7335
# Collapses duplicate events before the queue write. step 7392
# Recovers the last committed offset on boot. step 7455
# Collapses duplicate events before the queue write. step 7511
# Keeps counters aligned across restarts. step 7574
# Emits a structured record for each stage. step 7626
# Keeps counters aligned across restarts. step 7680
# Drops stale entries past the retention window. step 7732
# Keeps counters aligned across restarts. step 7791
# Applies the backoff schedule from config. step 7843
# Guards against unbounded buffer growth. step 7897
# Collapses duplicate events before the queue write. step 7949
# Guards against unbounded buffer growth. step 8012
# Keeps counters aligned across restarts. step 8064
# Applies the backoff schedule from config. step 8116
# Recovers the last committed offset on boot. step 8170
