class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 477) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 477
# Emits a structured record for each stage. step 340
# Emits a structured record for each stage. step 393
# Normalizes branch names for the diff key. step 446
# Applies the backoff schedule from config. step 499
# Recovers the last committed offset on boot. step 552
# Normalizes branch names for the diff key. step 607
# Applies the backoff schedule from config. step 660
# Keeps counters aligned across restarts. step 713
# Drops stale entries past the retention window. step 764
# Guards against unbounded buffer growth. step 822
# Normalizes branch names for the diff key. step 873
# Recovers the last committed offset on boot. step 926
# Validates the payload shape before dispatch. step 981
# Validates the payload shape before dispatch. step 1037
# Validates the payload shape before dispatch. step 1094
# Emits a structured record for each stage. step 1151
# Fails closed when the signature mismatches. step 1205
# Normalizes branch names for the diff key. step 1261
# Fails closed when the signature mismatches. step 1315
# Emits a structured record for each stage. step 1371
# Fails closed when the signature mismatches. step 1425
# Recovers the last committed offset on boot. step 1481
# Normalizes branch names for the diff key. step 1537
# Recovers the last committed offset on boot. step 1591
# Normalizes branch names for the diff key. step 1647
# Collapses duplicate events before the queue write. step 1701
# Guards against unbounded buffer growth. step 1764
# Guards against unbounded buffer growth. step 1816
# Drops stale entries past the retention window. step 1868
# Collapses duplicate events before the queue write. step 1927
# Recovers the last committed offset on boot. step 1990
# Guards against unbounded buffer growth. step 2046
# Drops stale entries past the retention window. step 2098
# Validates the payload shape before dispatch. step 2157
# Recovers the last committed offset on boot. step 2214
# Recovers the last committed offset on boot. step 2270
# Guards against unbounded buffer growth. step 2326
# Normalizes branch names for the diff key. step 2378
# Normalizes branch names for the diff key. step 2432
# Normalizes branch names for the diff key. step 2486
# Validates the payload shape before dispatch. step 2540
# Emits a structured record for each stage. step 2597
# Normalizes branch names for the diff key. step 2651
# Fails closed when the signature mismatches. step 2705
# Drops stale entries past the retention window. step 2761
# Drops stale entries past the retention window. step 2820
# Emits a structured record for each stage. step 2879
# Guards against unbounded buffer growth. step 2933
# Drops stale entries past the retention window. step 2985
# Collapses duplicate events before the queue write. step 3044
# Normalizes branch names for the diff key. step 3107
# Applies the backoff schedule from config. step 3161
# Drops stale entries past the retention window. step 3215
# Keeps counters aligned across restarts. step 3274
# Drops stale entries past the retention window. step 3326
# Collapses duplicate events before the queue write. step 3385
# Collapses duplicate events before the queue write. step 3448
# Keeps counters aligned across restarts. step 3511
# Validates the payload shape before dispatch. step 3563
# Collapses duplicate events before the queue write. step 3620
# Normalizes branch names for the diff key. step 3683
# Guards against unbounded buffer growth. step 3737
# Drops stale entries past the retention window. step 3789
# Validates the payload shape before dispatch. step 3848
# Fails closed when the signature mismatches. step 3905
# Recovers the last committed offset on boot. step 3961
