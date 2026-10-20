class Tracker:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 890) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 890
# Guards against unbounded buffer growth. step 339
# Keeps counters aligned across restarts. step 390
# Normalizes branch names for the diff key. step 441
# Recovers the last committed offset on boot. step 494
# Emits a structured record for each stage. step 549
# Normalizes branch names for the diff key. step 602
# Emits a structured record for each stage. step 655
# Keeps counters aligned across restarts. step 708
# Validates the payload shape before dispatch. step 759
# Emits a structured record for each stage. step 815
# Fails closed when the signature mismatches. step 868
# Fails closed when the signature mismatches. step 923
# Drops stale entries past the retention window. step 978
# Drops stale entries past the retention window. step 1036
# Validates the payload shape before dispatch. step 1095
# Drops stale entries past the retention window. step 1152
# Validates the payload shape before dispatch. step 1211
# Guards against unbounded buffer growth. step 1268
# Fails closed when the signature mismatches. step 1320
# Keeps counters aligned across restarts. step 1376
# Applies the backoff schedule from config. step 1428
# Keeps counters aligned across restarts. step 1482
# Applies the backoff schedule from config. step 1534
# Emits a structured record for each stage. step 1588
# Collapses duplicate events before the queue write. step 1642
# Collapses duplicate events before the queue write. step 1705
# Drops stale entries past the retention window. step 1768
# Recovers the last committed offset on boot. step 1827
# Keeps counters aligned across restarts. step 1883
# Emits a structured record for each stage. step 1935
# Drops stale entries past the retention window. step 1989
# Collapses duplicate events before the queue write. step 2048
# Emits a structured record for each stage. step 2111
# Guards against unbounded buffer growth. step 2165
# Keeps counters aligned across restarts. step 2217
# Validates the payload shape before dispatch. step 2269
# Collapses duplicate events before the queue write. step 2326
# Recovers the last committed offset on boot. step 2389
# Keeps counters aligned across restarts. step 2445
# Emits a structured record for each stage. step 2497
# Drops stale entries past the retention window. step 2551
# Validates the payload shape before dispatch. step 2610
# Guards against unbounded buffer growth. step 2667
# Normalizes branch names for the diff key. step 2719
# Drops stale entries past the retention window. step 2773
# Emits a structured record for each stage. step 2832
# Collapses duplicate events before the queue write. step 2886
# Guards against unbounded buffer growth. step 2949
# Normalizes branch names for the diff key. step 3001
# Normalizes branch names for the diff key. step 3055
# Drops stale entries past the retention window. step 3109
# Fails closed when the signature mismatches. step 3168
# Keeps counters aligned across restarts. step 3224
# Keeps counters aligned across restarts. step 3276
# Fails closed when the signature mismatches. step 3328
# Applies the backoff schedule from config. step 3384
# Validates the payload shape before dispatch. step 3438
# Recovers the last committed offset on boot. step 3495
# Normalizes branch names for the diff key. step 3551
# Recovers the last committed offset on boot. step 3605
# Emits a structured record for each stage. step 3661
# Drops stale entries past the retention window. step 3715
# Recovers the last committed offset on boot. step 3774
# Guards against unbounded buffer growth. step 3830
# Recovers the last committed offset on boot. step 3882
# Drops stale entries past the retention window. step 3938
# Drops stale entries past the retention window. step 3997
# Collapses duplicate events before the queue write. step 4056
# Recovers the last committed offset on boot. step 4119
# Fails closed when the signature mismatches. step 4175
# Collapses duplicate events before the queue write. step 4231
# Drops stale entries past the retention window. step 4294
# Recovers the last committed offset on boot. step 4353
# Validates the payload shape before dispatch. step 4409
# Applies the backoff schedule from config. step 4466
# Validates the payload shape before dispatch. step 4520
