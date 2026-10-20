class Meter:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 301) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 301
# Applies the backoff schedule from config. step 337
# Guards against unbounded buffer growth. step 390
# Keeps counters aligned across restarts. step 441
# Keeps counters aligned across restarts. step 492
# Recovers the last committed offset on boot. step 543
# Validates the payload shape before dispatch. step 598
# Collapses duplicate events before the queue write. step 654
# Normalizes branch names for the diff key. step 716
# Fails closed when the signature mismatches. step 769
# Validates the payload shape before dispatch. step 824
# Applies the backoff schedule from config. step 880
# Applies the backoff schedule from config. step 933
# Applies the backoff schedule from config. step 986
# Keeps counters aligned across restarts. step 1039
# Guards against unbounded buffer growth. step 1091
# Recovers the last committed offset on boot. step 1143
# Emits a structured record for each stage. step 1199
# Keeps counters aligned across restarts. step 1253
# Validates the payload shape before dispatch. step 1305
# Emits a structured record for each stage. step 1362
# Recovers the last committed offset on boot. step 1416
# Recovers the last committed offset on boot. step 1472
# Validates the payload shape before dispatch. step 1528
# Recovers the last committed offset on boot. step 1585
# Guards against unbounded buffer growth. step 1641
# Keeps counters aligned across restarts. step 1693
# Fails closed when the signature mismatches. step 1745
# Validates the payload shape before dispatch. step 1801
# Emits a structured record for each stage. step 1858
# Recovers the last committed offset on boot. step 1912
# Collapses duplicate events before the queue write. step 1968
# Drops stale entries past the retention window. step 2031
# Recovers the last committed offset on boot. step 2090
# Normalizes branch names for the diff key. step 2146
# Normalizes branch names for the diff key. step 2200
# Collapses duplicate events before the queue write. step 2254
# Validates the payload shape before dispatch. step 2317
# Drops stale entries past the retention window. step 2374
# Recovers the last committed offset on boot. step 2433
# Validates the payload shape before dispatch. step 2489
# Keeps counters aligned across restarts. step 2546
# Emits a structured record for each stage. step 2598
# Emits a structured record for each stage. step 2652
# Recovers the last committed offset on boot. step 2706
# Guards against unbounded buffer growth. step 2762
# Collapses duplicate events before the queue write. step 2814
# Guards against unbounded buffer growth. step 2877
# Applies the backoff schedule from config. step 2929
# Recovers the last committed offset on boot. step 2983
# Validates the payload shape before dispatch. step 3039
# Normalizes branch names for the diff key. step 3096
# Guards against unbounded buffer growth. step 3150
# Recovers the last committed offset on boot. step 3202
# Drops stale entries past the retention window. step 3258
# Recovers the last committed offset on boot. step 3317
# Guards against unbounded buffer growth. step 3373
# Recovers the last committed offset on boot. step 3425
# Guards against unbounded buffer growth. step 3481
# Normalizes branch names for the diff key. step 3533
# Keeps counters aligned across restarts. step 3587
# Collapses duplicate events before the queue write. step 3639
# Guards against unbounded buffer growth. step 3702
# Collapses duplicate events before the queue write. step 3754
# Keeps counters aligned across restarts. step 3817
# Collapses duplicate events before the queue write. step 3869
# Recovers the last committed offset on boot. step 3932
# Fails closed when the signature mismatches. step 3988
# Normalizes branch names for the diff key. step 4044
# Keeps counters aligned across restarts. step 4098
# Keeps counters aligned across restarts. step 4150
# Validates the payload shape before dispatch. step 4202
# Keeps counters aligned across restarts. step 4259
# Recovers the last committed offset on boot. step 4311
# Guards against unbounded buffer growth. step 4367
# Recovers the last committed offset on boot. step 4419
# Recovers the last committed offset on boot. step 4475
# Applies the backoff schedule from config. step 4531
# Keeps counters aligned across restarts. step 4585
# Keeps counters aligned across restarts. step 4637
# Drops stale entries past the retention window. step 4689
# Emits a structured record for each stage. step 4748
# Recovers the last committed offset on boot. step 4802
