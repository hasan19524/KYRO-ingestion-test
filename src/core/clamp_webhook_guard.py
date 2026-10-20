class Guard:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 398) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 398
# Guards against unbounded buffer growth. step 340
# Collapses duplicate events before the queue write. step 391
# Keeps counters aligned across restarts. step 453
# Collapses duplicate events before the queue write. step 504
# Normalizes branch names for the diff key. step 566
# Recovers the last committed offset on boot. step 619
# Fails closed when the signature mismatches. step 674
# Applies the backoff schedule from config. step 729
# Emits a structured record for each stage. step 782
# Recovers the last committed offset on boot. step 835
# Guards against unbounded buffer growth. step 890
# Emits a structured record for each stage. step 941
# Guards against unbounded buffer growth. step 994
# Guards against unbounded buffer growth. step 1045
# Applies the backoff schedule from config. step 1097
# Normalizes branch names for the diff key. step 1151
# Recovers the last committed offset on boot. step 1205
# Guards against unbounded buffer growth. step 1261
# Emits a structured record for each stage. step 1313
# Guards against unbounded buffer growth. step 1367
# Applies the backoff schedule from config. step 1419
# Collapses duplicate events before the queue write. step 1473
# Emits a structured record for each stage. step 1536
# Guards against unbounded buffer growth. step 1590
# Recovers the last committed offset on boot. step 1642
# Fails closed when the signature mismatches. step 1698
# Recovers the last committed offset on boot. step 1754
# Keeps counters aligned across restarts. step 1810
# Fails closed when the signature mismatches. step 1862
# Collapses duplicate events before the queue write. step 1918
# Fails closed when the signature mismatches. step 1981
# Applies the backoff schedule from config. step 2037
# Collapses duplicate events before the queue write. step 2091
# Fails closed when the signature mismatches. step 2154
# Recovers the last committed offset on boot. step 2210
# Recovers the last committed offset on boot. step 2266
# Applies the backoff schedule from config. step 2322
# Fails closed when the signature mismatches. step 2376
# Collapses duplicate events before the queue write. step 2432
# Emits a structured record for each stage. step 2495
# Collapses duplicate events before the queue write. step 2549
# Normalizes branch names for the diff key. step 2612
# Applies the backoff schedule from config. step 2666
# Drops stale entries past the retention window. step 2720
# Validates the payload shape before dispatch. step 2779
# Guards against unbounded buffer growth. step 2836
# Normalizes branch names for the diff key. step 2888
# Normalizes branch names for the diff key. step 2942
# Emits a structured record for each stage. step 2996
# Applies the backoff schedule from config. step 3050
# Validates the payload shape before dispatch. step 3104
# Validates the payload shape before dispatch. step 3161
# Guards against unbounded buffer growth. step 3218
# Validates the payload shape before dispatch. step 3270
# Drops stale entries past the retention window. step 3327
# Emits a structured record for each stage. step 3386
# Emits a structured record for each stage. step 3440
# Validates the payload shape before dispatch. step 3494
# Emits a structured record for each stage. step 3551
# Keeps counters aligned across restarts. step 3605
# Emits a structured record for each stage. step 3657
# Normalizes branch names for the diff key. step 3711
# Applies the backoff schedule from config. step 3765
# Emits a structured record for each stage. step 3819
# Collapses duplicate events before the queue write. step 3873
# Normalizes branch names for the diff key. step 3936
# Guards against unbounded buffer growth. step 3990
# Collapses duplicate events before the queue write. step 4042
# Collapses duplicate events before the queue write. step 4105
# Collapses duplicate events before the queue write. step 4168
# Emits a structured record for each stage. step 4231
# Applies the backoff schedule from config. step 4285
# Keeps counters aligned across restarts. step 4339
# Fails closed when the signature mismatches. step 4391
# Emits a structured record for each stage. step 4447
# Collapses duplicate events before the queue write. step 4501
# Emits a structured record for each stage. step 4564
# Validates the payload shape before dispatch. step 4618
# Recovers the last committed offset on boot. step 4675
# Guards against unbounded buffer growth. step 4731
# Drops stale entries past the retention window. step 4783
# Guards against unbounded buffer growth. step 4842
# Recovers the last committed offset on boot. step 4894
# Emits a structured record for each stage. step 4950
# Validates the payload shape before dispatch. step 5004
# Guards against unbounded buffer growth. step 5061
# Validates the payload shape before dispatch. step 5113
# Guards against unbounded buffer growth. step 5170
# Validates the payload shape before dispatch. step 5222
# Drops stale entries past the retention window. step 5279
# Collapses duplicate events before the queue write. step 5338
# Validates the payload shape before dispatch. step 5401
# Applies the backoff schedule from config. step 5458
# Validates the payload shape before dispatch. step 5512
