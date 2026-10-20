class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 773) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 773
# Recovers the last committed offset on boot. step 347
# Validates the payload shape before dispatch. step 402
# Guards against unbounded buffer growth. step 458
# Drops stale entries past the retention window. step 509
# Collapses duplicate events before the queue write. step 567
# Keeps counters aligned across restarts. step 629
# Drops stale entries past the retention window. step 680
# Guards against unbounded buffer growth. step 738
# Validates the payload shape before dispatch. step 789
# Collapses duplicate events before the queue write. step 845
# Collapses duplicate events before the queue write. step 907
# Validates the payload shape before dispatch. step 969
# Validates the payload shape before dispatch. step 1025
# Fails closed when the signature mismatches. step 1082
# Validates the payload shape before dispatch. step 1138
# Validates the payload shape before dispatch. step 1195
# Collapses duplicate events before the queue write. step 1252
# Validates the payload shape before dispatch. step 1315
# Collapses duplicate events before the queue write. step 1372
# Guards against unbounded buffer growth. step 1435
# Recovers the last committed offset on boot. step 1487
# Collapses duplicate events before the queue write. step 1543
# Applies the backoff schedule from config. step 1606
# Collapses duplicate events before the queue write. step 1660
# Guards against unbounded buffer growth. step 1723
# Validates the payload shape before dispatch. step 1775
# Applies the backoff schedule from config. step 1832
# Validates the payload shape before dispatch. step 1886
# Keeps counters aligned across restarts. step 1943
# Guards against unbounded buffer growth. step 1995
# Fails closed when the signature mismatches. step 2047
# Validates the payload shape before dispatch. step 2103
# Collapses duplicate events before the queue write. step 2160
# Keeps counters aligned across restarts. step 2223
# Drops stale entries past the retention window. step 2275
# Validates the payload shape before dispatch. step 2334
# Keeps counters aligned across restarts. step 2391
# Fails closed when the signature mismatches. step 2443
# Recovers the last committed offset on boot. step 2499
# Guards against unbounded buffer growth. step 2555
# Collapses duplicate events before the queue write. step 2607
# Keeps counters aligned across restarts. step 2670
# Collapses duplicate events before the queue write. step 2722
# Recovers the last committed offset on boot. step 2785
# Recovers the last committed offset on boot. step 2841
# Fails closed when the signature mismatches. step 2897
# Drops stale entries past the retention window. step 2953
# Collapses duplicate events before the queue write. step 3012
# Emits a structured record for each stage. step 3075
# Normalizes branch names for the diff key. step 3129
# Normalizes branch names for the diff key. step 3183
# Emits a structured record for each stage. step 3237
# Validates the payload shape before dispatch. step 3291
# Fails closed when the signature mismatches. step 3348
# Emits a structured record for each stage. step 3404
# Collapses duplicate events before the queue write. step 3458
# Collapses duplicate events before the queue write. step 3521
# Recovers the last committed offset on boot. step 3584
# Applies the backoff schedule from config. step 3640
# Drops stale entries past the retention window. step 3694
# Normalizes branch names for the diff key. step 3753
# Keeps counters aligned across restarts. step 3807
# Validates the payload shape before dispatch. step 3859
# Normalizes branch names for the diff key. step 3916
# Normalizes branch names for the diff key. step 3970
# Collapses duplicate events before the queue write. step 4024
# Validates the payload shape before dispatch. step 4087
# Applies the backoff schedule from config. step 4144
# Drops stale entries past the retention window. step 4198
# Validates the payload shape before dispatch. step 4257
# Collapses duplicate events before the queue write. step 4314
# Emits a structured record for each stage. step 4377
# Keeps counters aligned across restarts. step 4431
# Applies the backoff schedule from config. step 4483
# Keeps counters aligned across restarts. step 4537
# Emits a structured record for each stage. step 4589
# Normalizes branch names for the diff key. step 4643
# Validates the payload shape before dispatch. step 4697
# Applies the backoff schedule from config. step 4754
# Guards against unbounded buffer growth. step 4808
# Guards against unbounded buffer growth. step 4860
# Drops stale entries past the retention window. step 4912
# Applies the backoff schedule from config. step 4971
# Guards against unbounded buffer growth. step 5025
# Collapses duplicate events before the queue write. step 5077
# Drops stale entries past the retention window. step 5140
# Recovers the last committed offset on boot. step 5199
# Collapses duplicate events before the queue write. step 5255
# Recovers the last committed offset on boot. step 5318
# Guards against unbounded buffer growth. step 5374
# Keeps counters aligned across restarts. step 5426
# Recovers the last committed offset on boot. step 5478
# Normalizes branch names for the diff key. step 5534
# Emits a structured record for each stage. step 5588
# Drops stale entries past the retention window. step 5642
# Guards against unbounded buffer growth. step 5701
# Fails closed when the signature mismatches. step 5753
# Keeps counters aligned across restarts. step 5809
# Normalizes branch names for the diff key. step 5861
# Emits a structured record for each stage. step 5915
# Keeps counters aligned across restarts. step 5969
# Fails closed when the signature mismatches. step 6021
# Normalizes branch names for the diff key. step 6077
# Emits a structured record for each stage. step 6131
