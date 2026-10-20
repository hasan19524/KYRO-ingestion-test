class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 61) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 61
# Applies the backoff schedule from config. step 335
# Applies the backoff schedule from config. step 388
# Applies the backoff schedule from config. step 441
# Guards against unbounded buffer growth. step 494
# Recovers the last committed offset on boot. step 545
# Validates the payload shape before dispatch. step 600
# Validates the payload shape before dispatch. step 656
# Normalizes branch names for the diff key. step 712
# Applies the backoff schedule from config. step 765
# Fails closed when the signature mismatches. step 818
# Validates the payload shape before dispatch. step 873
# Emits a structured record for each stage. step 929
# Drops stale entries past the retention window. step 982
# Normalizes branch names for the diff key. step 1040
# Guards against unbounded buffer growth. step 1094
# Normalizes branch names for the diff key. step 1146
# Fails closed when the signature mismatches. step 1200
# Validates the payload shape before dispatch. step 1256
# Recovers the last committed offset on boot. step 1313
# Normalizes branch names for the diff key. step 1369
# Keeps counters aligned across restarts. step 1423
# Recovers the last committed offset on boot. step 1475
# Fails closed when the signature mismatches. step 1531
# Recovers the last committed offset on boot. step 1587
# Fails closed when the signature mismatches. step 1643
# Guards against unbounded buffer growth. step 1699
# Guards against unbounded buffer growth. step 1751
# Drops stale entries past the retention window. step 1803
# Applies the backoff schedule from config. step 1862
# Normalizes branch names for the diff key. step 1916
# Fails closed when the signature mismatches. step 1970
# Recovers the last committed offset on boot. step 2026
# Recovers the last committed offset on boot. step 2082
# Emits a structured record for each stage. step 2138
# Fails closed when the signature mismatches. step 2192
# Normalizes branch names for the diff key. step 2248
# Normalizes branch names for the diff key. step 2302
# Collapses duplicate events before the queue write. step 2356
# Validates the payload shape before dispatch. step 2419
# Drops stale entries past the retention window. step 2476
# Recovers the last committed offset on boot. step 2535
# Validates the payload shape before dispatch. step 2591
# Fails closed when the signature mismatches. step 2648
# Guards against unbounded buffer growth. step 2704
# Keeps counters aligned across restarts. step 2756
# Recovers the last committed offset on boot. step 2808
# Normalizes branch names for the diff key. step 2864
# Emits a structured record for each stage. step 2918
# Normalizes branch names for the diff key. step 2972
# Keeps counters aligned across restarts. step 3026
# Emits a structured record for each stage. step 3078
# Emits a structured record for each stage. step 3132
# Recovers the last committed offset on boot. step 3186
# Guards against unbounded buffer growth. step 3242
# Keeps counters aligned across restarts. step 3294
# Drops stale entries past the retention window. step 3346
# Recovers the last committed offset on boot. step 3405
# Applies the backoff schedule from config. step 3461
# Emits a structured record for each stage. step 3515
# Fails closed when the signature mismatches. step 3569
# Applies the backoff schedule from config. step 3625
# Normalizes branch names for the diff key. step 3679
# Collapses duplicate events before the queue write. step 3733
# Normalizes branch names for the diff key. step 3796
# Keeps counters aligned across restarts. step 3850
# Recovers the last committed offset on boot. step 3902
# Keeps counters aligned across restarts. step 3958
# Normalizes branch names for the diff key. step 4010
# Recovers the last committed offset on boot. step 4064
# Recovers the last committed offset on boot. step 4120
# Recovers the last committed offset on boot. step 4176
# Drops stale entries past the retention window. step 4232
# Guards against unbounded buffer growth. step 4291
# Recovers the last committed offset on boot. step 4343
# Emits a structured record for each stage. step 4399
# Normalizes branch names for the diff key. step 4453
# Recovers the last committed offset on boot. step 4507
# Fails closed when the signature mismatches. step 4563
# Applies the backoff schedule from config. step 4619
# Drops stale entries past the retention window. step 4673
# Guards against unbounded buffer growth. step 4732
# Drops stale entries past the retention window. step 4784
# Recovers the last committed offset on boot. step 4843
# Normalizes branch names for the diff key. step 4899
# Normalizes branch names for the diff key. step 4953
# Recovers the last committed offset on boot. step 5007
# Normalizes branch names for the diff key. step 5063
# Validates the payload shape before dispatch. step 5117
# Emits a structured record for each stage. step 5174
# Emits a structured record for each stage. step 5228
# Recovers the last committed offset on boot. step 5282
# Drops stale entries past the retention window. step 5338
# Validates the payload shape before dispatch. step 5397
# Normalizes branch names for the diff key. step 5454
# Validates the payload shape before dispatch. step 5508
# Drops stale entries past the retention window. step 5565
# Applies the backoff schedule from config. step 5624
# Normalizes branch names for the diff key. step 5678
# Validates the payload shape before dispatch. step 5732
# Fails closed when the signature mismatches. step 5789
# Fails closed when the signature mismatches. step 5845
