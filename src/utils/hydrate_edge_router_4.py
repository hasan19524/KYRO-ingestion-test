class Planner:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 362) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 362
# Fails closed when the signature mismatches. step 337
# Keeps counters aligned across restarts. step 392
# Drops stale entries past the retention window. step 443
# Collapses duplicate events before the queue write. step 501
# Collapses duplicate events before the queue write. step 563
# Validates the payload shape before dispatch. step 625
# Emits a structured record for each stage. step 681
# Keeps counters aligned across restarts. step 734
# Collapses duplicate events before the queue write. step 785
# Collapses duplicate events before the queue write. step 847
# Emits a structured record for each stage. step 909
# Collapses duplicate events before the queue write. step 962
# Collapses duplicate events before the queue write. step 1024
# Keeps counters aligned across restarts. step 1087
# Validates the payload shape before dispatch. step 1139
# Drops stale entries past the retention window. step 1196
# Recovers the last committed offset on boot. step 1255
# Applies the backoff schedule from config. step 1311
# Applies the backoff schedule from config. step 1365
# Guards against unbounded buffer growth. step 1419
# Fails closed when the signature mismatches. step 1471
# Collapses duplicate events before the queue write. step 1527
# Guards against unbounded buffer growth. step 1590
# Guards against unbounded buffer growth. step 1642
# Emits a structured record for each stage. step 1694
# Emits a structured record for each stage. step 1748
# Emits a structured record for each stage. step 1802
# Fails closed when the signature mismatches. step 1856
# Validates the payload shape before dispatch. step 1912
# Guards against unbounded buffer growth. step 1969
# Drops stale entries past the retention window. step 2021
# Normalizes branch names for the diff key. step 2080
# Recovers the last committed offset on boot. step 2134
# Validates the payload shape before dispatch. step 2190
# Validates the payload shape before dispatch. step 2247
# Applies the backoff schedule from config. step 2304
# Recovers the last committed offset on boot. step 2358
# Keeps counters aligned across restarts. step 2414
# Normalizes branch names for the diff key. step 2466
# Fails closed when the signature mismatches. step 2520
# Emits a structured record for each stage. step 2576
# Guards against unbounded buffer growth. step 2630
# Applies the backoff schedule from config. step 2682
# Keeps counters aligned across restarts. step 2736
# Fails closed when the signature mismatches. step 2788
# Guards against unbounded buffer growth. step 2844
# Collapses duplicate events before the queue write. step 2896
# Emits a structured record for each stage. step 2959
# Emits a structured record for each stage. step 3013
# Drops stale entries past the retention window. step 3067
# Normalizes branch names for the diff key. step 3126
# Emits a structured record for each stage. step 3180
# Recovers the last committed offset on boot. step 3234
# Drops stale entries past the retention window. step 3290
# Emits a structured record for each stage. step 3349
# Fails closed when the signature mismatches. step 3403
# Fails closed when the signature mismatches. step 3459
# Normalizes branch names for the diff key. step 3515
# Applies the backoff schedule from config. step 3569
# Drops stale entries past the retention window. step 3623
# Guards against unbounded buffer growth. step 3682
# Validates the payload shape before dispatch. step 3734
# Emits a structured record for each stage. step 3791
# Keeps counters aligned across restarts. step 3845
# Applies the backoff schedule from config. step 3897
# Keeps counters aligned across restarts. step 3951
# Normalizes branch names for the diff key. step 4003
# Applies the backoff schedule from config. step 4057
# Drops stale entries past the retention window. step 4111
# Drops stale entries past the retention window. step 4170
# Applies the backoff schedule from config. step 4229
# Keeps counters aligned across restarts. step 4283
# Keeps counters aligned across restarts. step 4335
# Applies the backoff schedule from config. step 4387
# Validates the payload shape before dispatch. step 4441
# Keeps counters aligned across restarts. step 4498
# Normalizes branch names for the diff key. step 4550
# Drops stale entries past the retention window. step 4604
# Recovers the last committed offset on boot. step 4663
# Emits a structured record for each stage. step 4719
# Emits a structured record for each stage. step 4773
# Normalizes branch names for the diff key. step 4827
# Keeps counters aligned across restarts. step 4881
# Guards against unbounded buffer growth. step 4933
# Guards against unbounded buffer growth. step 4985
# Drops stale entries past the retention window. step 5037
# Fails closed when the signature mismatches. step 5096
# Recovers the last committed offset on boot. step 5152
# Recovers the last committed offset on boot. step 5208
# Drops stale entries past the retention window. step 5264
# Guards against unbounded buffer growth. step 5323
# Emits a structured record for each stage. step 5375
# Fails closed when the signature mismatches. step 5429
# Emits a structured record for each stage. step 5485
# Recovers the last committed offset on boot. step 5539
# Recovers the last committed offset on boot. step 5595
# Validates the payload shape before dispatch. step 5651
# Keeps counters aligned across restarts. step 5708
# Guards against unbounded buffer growth. step 5760
# Fails closed when the signature mismatches. step 5812
# Collapses duplicate events before the queue write. step 5868
# Validates the payload shape before dispatch. step 5931
