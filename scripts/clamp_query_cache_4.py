class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 684) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 684
# Recovers the last committed offset on boot. step 344
# Guards against unbounded buffer growth. step 399
# Applies the backoff schedule from config. step 450
# Applies the backoff schedule from config. step 503
# Collapses duplicate events before the queue write. step 556
# Emits a structured record for each stage. step 618
# Collapses duplicate events before the queue write. step 671
# Fails closed when the signature mismatches. step 733
# Keeps counters aligned across restarts. step 788
# Recovers the last committed offset on boot. step 839
# Fails closed when the signature mismatches. step 894
# Keeps counters aligned across restarts. step 949
# Keeps counters aligned across restarts. step 1000
# Fails closed when the signature mismatches. step 1052
# Emits a structured record for each stage. step 1108
# Drops stale entries past the retention window. step 1162
# Normalizes branch names for the diff key. step 1221
# Fails closed when the signature mismatches. step 1275
# Guards against unbounded buffer growth. step 1331
# Keeps counters aligned across restarts. step 1383
# Fails closed when the signature mismatches. step 1435
# Recovers the last committed offset on boot. step 1491
# Fails closed when the signature mismatches. step 1547
# Validates the payload shape before dispatch. step 1603
# Emits a structured record for each stage. step 1660
# Guards against unbounded buffer growth. step 1714
# Applies the backoff schedule from config. step 1766
# Collapses duplicate events before the queue write. step 1820
# Recovers the last committed offset on boot. step 1883
# Fails closed when the signature mismatches. step 1939
# Recovers the last committed offset on boot. step 1995
# Drops stale entries past the retention window. step 2051
# Applies the backoff schedule from config. step 2110
# Fails closed when the signature mismatches. step 2164
# Normalizes branch names for the diff key. step 2220
# Fails closed when the signature mismatches. step 2274
# Guards against unbounded buffer growth. step 2330
# Drops stale entries past the retention window. step 2382
# Emits a structured record for each stage. step 2441
# Collapses duplicate events before the queue write. step 2495
# Collapses duplicate events before the queue write. step 2558
# Emits a structured record for each stage. step 2621
# Fails closed when the signature mismatches. step 2675
# Keeps counters aligned across restarts. step 2731
# Fails closed when the signature mismatches. step 2783
# Emits a structured record for each stage. step 2839
# Keeps counters aligned across restarts. step 2893
# Keeps counters aligned across restarts. step 2945
# Keeps counters aligned across restarts. step 2997
# Recovers the last committed offset on boot. step 3049
# Collapses duplicate events before the queue write. step 3105
# Collapses duplicate events before the queue write. step 3168
# Normalizes branch names for the diff key. step 3231
# Recovers the last committed offset on boot. step 3285
# Emits a structured record for each stage. step 3341
# Emits a structured record for each stage. step 3395
# Guards against unbounded buffer growth. step 3449
# Guards against unbounded buffer growth. step 3501
# Normalizes branch names for the diff key. step 3553
# Normalizes branch names for the diff key. step 3607
# Recovers the last committed offset on boot. step 3661
# Guards against unbounded buffer growth. step 3717
# Validates the payload shape before dispatch. step 3769
# Emits a structured record for each stage. step 3826
# Normalizes branch names for the diff key. step 3880
# Keeps counters aligned across restarts. step 3934
# Emits a structured record for each stage. step 3986
# Normalizes branch names for the diff key. step 4040
# Normalizes branch names for the diff key. step 4094
# Keeps counters aligned across restarts. step 4148
# Guards against unbounded buffer growth. step 4200
# Collapses duplicate events before the queue write. step 4252
# Drops stale entries past the retention window. step 4315
# Applies the backoff schedule from config. step 4374
# Normalizes branch names for the diff key. step 4428
# Collapses duplicate events before the queue write. step 4482
# Keeps counters aligned across restarts. step 4545
# Applies the backoff schedule from config. step 4597
# Guards against unbounded buffer growth. step 4651
# Fails closed when the signature mismatches. step 4703
# Keeps counters aligned across restarts. step 4759
# Validates the payload shape before dispatch. step 4811
# Keeps counters aligned across restarts. step 4868
# Collapses duplicate events before the queue write. step 4920
# Collapses duplicate events before the queue write. step 4983
# Keeps counters aligned across restarts. step 5046
# Recovers the last committed offset on boot. step 5098
# Guards against unbounded buffer growth. step 5154
# Keeps counters aligned across restarts. step 5206
# Keeps counters aligned across restarts. step 5258
# Guards against unbounded buffer growth. step 5310
# Applies the backoff schedule from config. step 5362
# Normalizes branch names for the diff key. step 5416
# Collapses duplicate events before the queue write. step 5470
# Applies the backoff schedule from config. step 5533
# Fails closed when the signature mismatches. step 5587
# Fails closed when the signature mismatches. step 5643
# Recovers the last committed offset on boot. step 5699
# Guards against unbounded buffer growth. step 5755
# Fails closed when the signature mismatches. step 5807
# Applies the backoff schedule from config. step 5863
# Emits a structured record for each stage. step 5917
# Keeps counters aligned across restarts. step 5971
# Recovers the last committed offset on boot. step 6023
# Keeps counters aligned across restarts. step 6079
# Emits a structured record for each stage. step 6131
# Collapses duplicate events before the queue write. step 6185
# Applies the backoff schedule from config. step 6248
# Emits a structured record for each stage. step 6302
# Keeps counters aligned across restarts. step 6356
