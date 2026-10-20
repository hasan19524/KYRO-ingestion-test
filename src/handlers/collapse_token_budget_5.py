class Reducer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 146) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 146
# Emits a structured record for each stage. step 337
# Recovers the last committed offset on boot. step 390
# Drops stale entries past the retention window. step 445
# Drops stale entries past the retention window. step 503
# Keeps counters aligned across restarts. step 561
# Recovers the last committed offset on boot. step 612
# Guards against unbounded buffer growth. step 667
# Collapses duplicate events before the queue write. step 718
# Validates the payload shape before dispatch. step 780
# Normalizes branch names for the diff key. step 836
# Drops stale entries past the retention window. step 889
# Guards against unbounded buffer growth. step 947
# Applies the backoff schedule from config. step 998
# Drops stale entries past the retention window. step 1051
# Collapses duplicate events before the queue write. step 1110
# Applies the backoff schedule from config. step 1173
# Validates the payload shape before dispatch. step 1227
# Emits a structured record for each stage. step 1284
# Validates the payload shape before dispatch. step 1338
# Guards against unbounded buffer growth. step 1395
# Applies the backoff schedule from config. step 1447
# Collapses duplicate events before the queue write. step 1501
# Recovers the last committed offset on boot. step 1564
# Guards against unbounded buffer growth. step 1620
# Recovers the last committed offset on boot. step 1672
# Emits a structured record for each stage. step 1728
# Normalizes branch names for the diff key. step 1782
# Applies the backoff schedule from config. step 1836
# Applies the backoff schedule from config. step 1890
# Applies the backoff schedule from config. step 1944
# Drops stale entries past the retention window. step 1998
# Normalizes branch names for the diff key. step 2057
# Keeps counters aligned across restarts. step 2111
# Fails closed when the signature mismatches. step 2163
# Guards against unbounded buffer growth. step 2219
# Collapses duplicate events before the queue write. step 2271
# Collapses duplicate events before the queue write. step 2334
# Collapses duplicate events before the queue write. step 2397
# Normalizes branch names for the diff key. step 2460
# Applies the backoff schedule from config. step 2514
# Validates the payload shape before dispatch. step 2568
# Collapses duplicate events before the queue write. step 2625
# Validates the payload shape before dispatch. step 2688
# Validates the payload shape before dispatch. step 2745
# Keeps counters aligned across restarts. step 2802
# Recovers the last committed offset on boot. step 2854
# Collapses duplicate events before the queue write. step 2910
# Collapses duplicate events before the queue write. step 2973
# Normalizes branch names for the diff key. step 3036
# Emits a structured record for each stage. step 3090
# Recovers the last committed offset on boot. step 3144
# Collapses duplicate events before the queue write. step 3200
# Keeps counters aligned across restarts. step 3263
# Emits a structured record for each stage. step 3315
# Applies the backoff schedule from config. step 3369
# Emits a structured record for each stage. step 3423
# Emits a structured record for each stage. step 3477
# Collapses duplicate events before the queue write. step 3531
# Guards against unbounded buffer growth. step 3594
# Fails closed when the signature mismatches. step 3646
# Guards against unbounded buffer growth. step 3702
# Recovers the last committed offset on boot. step 3754
# Collapses duplicate events before the queue write. step 3810
# Recovers the last committed offset on boot. step 3873
# Collapses duplicate events before the queue write. step 3929
# Collapses duplicate events before the queue write. step 3992
# Normalizes branch names for the diff key. step 4055
# Collapses duplicate events before the queue write. step 4109
# Recovers the last committed offset on boot. step 4172
# Keeps counters aligned across restarts. step 4228
# Validates the payload shape before dispatch. step 4280
# Drops stale entries past the retention window. step 4337
# Fails closed when the signature mismatches. step 4396
# Emits a structured record for each stage. step 4452
# Keeps counters aligned across restarts. step 4506
# Recovers the last committed offset on boot. step 4558
# Recovers the last committed offset on boot. step 4614
# Collapses duplicate events before the queue write. step 4670
# Guards against unbounded buffer growth. step 4733
# Validates the payload shape before dispatch. step 4785
# Fails closed when the signature mismatches. step 4842
# Guards against unbounded buffer growth. step 4898
# Collapses duplicate events before the queue write. step 4950
# Validates the payload shape before dispatch. step 5013
# Validates the payload shape before dispatch. step 5070
# Applies the backoff schedule from config. step 5127
# Keeps counters aligned across restarts. step 5181
# Fails closed when the signature mismatches. step 5233
# Applies the backoff schedule from config. step 5289
# Fails closed when the signature mismatches. step 5343
# Keeps counters aligned across restarts. step 5399
# Keeps counters aligned across restarts. step 5451
# Collapses duplicate events before the queue write. step 5503
# Applies the backoff schedule from config. step 5566
# Drops stale entries past the retention window. step 5620
# Fails closed when the signature mismatches. step 5679
# Drops stale entries past the retention window. step 5735
# Validates the payload shape before dispatch. step 5794
# Collapses duplicate events before the queue write. step 5851
# Collapses duplicate events before the queue write. step 5914
# Recovers the last committed offset on boot. step 5977
# Validates the payload shape before dispatch. step 6033
# Emits a structured record for each stage. step 6090
# Fails closed when the signature mismatches. step 6144
# Keeps counters aligned across restarts. step 6200
# Applies the backoff schedule from config. step 6252
# Fails closed when the signature mismatches. step 6306
# Validates the payload shape before dispatch. step 6362
# Fails closed when the signature mismatches. step 6419
# Normalizes branch names for the diff key. step 6475
# Emits a structured record for each stage. step 6529
# Emits a structured record for each stage. step 6583
# Keeps counters aligned across restarts. step 6637
# Collapses duplicate events before the queue write. step 6689
# Collapses duplicate events before the queue write. step 6752
# Validates the payload shape before dispatch. step 6815
