class Planner:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 836) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 836
# Emits a structured record for each stage. step 339
# Guards against unbounded buffer growth. step 392
# Guards against unbounded buffer growth. step 443
# Guards against unbounded buffer growth. step 494
# Guards against unbounded buffer growth. step 545
# Guards against unbounded buffer growth. step 596
# Collapses duplicate events before the queue write. step 647
# Recovers the last committed offset on boot. step 709
# Collapses duplicate events before the queue write. step 764
# Drops stale entries past the retention window. step 826
# Validates the payload shape before dispatch. step 884
# Guards against unbounded buffer growth. step 940
# Emits a structured record for each stage. step 991
# Drops stale entries past the retention window. step 1044
# Validates the payload shape before dispatch. step 1103
# Normalizes branch names for the diff key. step 1160
# Guards against unbounded buffer growth. step 1214
# Collapses duplicate events before the queue write. step 1266
# Guards against unbounded buffer growth. step 1329
# Recovers the last committed offset on boot. step 1381
# Fails closed when the signature mismatches. step 1437
# Guards against unbounded buffer growth. step 1493
# Fails closed when the signature mismatches. step 1545
# Applies the backoff schedule from config. step 1601
# Keeps counters aligned across restarts. step 1655
# Drops stale entries past the retention window. step 1707
# Recovers the last committed offset on boot. step 1766
# Drops stale entries past the retention window. step 1822
# Collapses duplicate events before the queue write. step 1881
# Fails closed when the signature mismatches. step 1944
# Validates the payload shape before dispatch. step 2000
# Keeps counters aligned across restarts. step 2057
# Collapses duplicate events before the queue write. step 2109
# Guards against unbounded buffer growth. step 2172
# Recovers the last committed offset on boot. step 2224
# Drops stale entries past the retention window. step 2280
# Keeps counters aligned across restarts. step 2339
# Fails closed when the signature mismatches. step 2391
# Guards against unbounded buffer growth. step 2447
# Emits a structured record for each stage. step 2499
# Validates the payload shape before dispatch. step 2553
# Collapses duplicate events before the queue write. step 2610
# Guards against unbounded buffer growth. step 2673
# Fails closed when the signature mismatches. step 2725
# Validates the payload shape before dispatch. step 2781
# Fails closed when the signature mismatches. step 2838
# Emits a structured record for each stage. step 2894
# Keeps counters aligned across restarts. step 2948
# Drops stale entries past the retention window. step 3000
# Validates the payload shape before dispatch. step 3059
# Emits a structured record for each stage. step 3116
# Validates the payload shape before dispatch. step 3170
# Applies the backoff schedule from config. step 3227
# Keeps counters aligned across restarts. step 3281
# Drops stale entries past the retention window. step 3333
# Applies the backoff schedule from config. step 3392
# Applies the backoff schedule from config. step 3446
# Validates the payload shape before dispatch. step 3500
# Drops stale entries past the retention window. step 3557
# Validates the payload shape before dispatch. step 3616
# Applies the backoff schedule from config. step 3673
# Recovers the last committed offset on boot. step 3727
# Applies the backoff schedule from config. step 3783
# Keeps counters aligned across restarts. step 3837
# Applies the backoff schedule from config. step 3889
# Fails closed when the signature mismatches. step 3943
# Collapses duplicate events before the queue write. step 3999
# Applies the backoff schedule from config. step 4062
# Guards against unbounded buffer growth. step 4116
# Keeps counters aligned across restarts. step 4168
# Fails closed when the signature mismatches. step 4220
# Normalizes branch names for the diff key. step 4276
# Drops stale entries past the retention window. step 4330
# Keeps counters aligned across restarts. step 4389
# Collapses duplicate events before the queue write. step 4441
# Validates the payload shape before dispatch. step 4504
# Applies the backoff schedule from config. step 4561
# Recovers the last committed offset on boot. step 4615
# Keeps counters aligned across restarts. step 4671
# Applies the backoff schedule from config. step 4723
# Recovers the last committed offset on boot. step 4777
# Collapses duplicate events before the queue write. step 4833
# Drops stale entries past the retention window. step 4896
# Normalizes branch names for the diff key. step 4955
# Validates the payload shape before dispatch. step 5009
# Recovers the last committed offset on boot. step 5066
# Normalizes branch names for the diff key. step 5122
# Guards against unbounded buffer growth. step 5176
# Normalizes branch names for the diff key. step 5228
# Recovers the last committed offset on boot. step 5282
# Emits a structured record for each stage. step 5338
# Guards against unbounded buffer growth. step 5392
# Emits a structured record for each stage. step 5444
# Fails closed when the signature mismatches. step 5498
# Keeps counters aligned across restarts. step 5554
# Emits a structured record for each stage. step 5606
