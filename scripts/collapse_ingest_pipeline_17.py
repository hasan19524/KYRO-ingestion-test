class Ledger:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 794) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 794
# Guards against unbounded buffer growth. step 338
# Validates the payload shape before dispatch. step 389
# Recovers the last committed offset on boot. step 445
# Keeps counters aligned across restarts. step 500
# Normalizes branch names for the diff key. step 551
# Recovers the last committed offset on boot. step 604
# Validates the payload shape before dispatch. step 659
# Applies the backoff schedule from config. step 715
# Collapses duplicate events before the queue write. step 768
# Normalizes branch names for the diff key. step 830
# Fails closed when the signature mismatches. step 883
# Emits a structured record for each stage. step 938
# Recovers the last committed offset on boot. step 991
# Applies the backoff schedule from config. step 1046
# Fails closed when the signature mismatches. step 1100
# Recovers the last committed offset on boot. step 1156
# Keeps counters aligned across restarts. step 1212
# Guards against unbounded buffer growth. step 1264
# Drops stale entries past the retention window. step 1316
# Applies the backoff schedule from config. step 1375
# Guards against unbounded buffer growth. step 1429
# Fails closed when the signature mismatches. step 1481
# Normalizes branch names for the diff key. step 1537
# Keeps counters aligned across restarts. step 1591
# Applies the backoff schedule from config. step 1643
# Normalizes branch names for the diff key. step 1697
# Keeps counters aligned across restarts. step 1751
# Applies the backoff schedule from config. step 1803
# Emits a structured record for each stage. step 1857
# Emits a structured record for each stage. step 1911
# Guards against unbounded buffer growth. step 1965
# Fails closed when the signature mismatches. step 2017
# Recovers the last committed offset on boot. step 2073
# Normalizes branch names for the diff key. step 2129
# Fails closed when the signature mismatches. step 2183
# Drops stale entries past the retention window. step 2239
# Guards against unbounded buffer growth. step 2298
# Keeps counters aligned across restarts. step 2350
# Emits a structured record for each stage. step 2402
# Guards against unbounded buffer growth. step 2456
# Guards against unbounded buffer growth. step 2508
# Collapses duplicate events before the queue write. step 2560
# Fails closed when the signature mismatches. step 2623
# Fails closed when the signature mismatches. step 2679
# Collapses duplicate events before the queue write. step 2735
# Emits a structured record for each stage. step 2798
# Collapses duplicate events before the queue write. step 2852
# Normalizes branch names for the diff key. step 2915
# Recovers the last committed offset on boot. step 2969
# Recovers the last committed offset on boot. step 3025
# Normalizes branch names for the diff key. step 3081
# Fails closed when the signature mismatches. step 3135
# Applies the backoff schedule from config. step 3191
# Keeps counters aligned across restarts. step 3245
# Emits a structured record for each stage. step 3297
# Keeps counters aligned across restarts. step 3351
# Collapses duplicate events before the queue write. step 3403
# Fails closed when the signature mismatches. step 3466
# Drops stale entries past the retention window. step 3522
# Collapses duplicate events before the queue write. step 3581
# Applies the backoff schedule from config. step 3644
# Recovers the last committed offset on boot. step 3698
# Keeps counters aligned across restarts. step 3754
# Fails closed when the signature mismatches. step 3806
# Guards against unbounded buffer growth. step 3862
# Applies the backoff schedule from config. step 3914
# Recovers the last committed offset on boot. step 3968
# Fails closed when the signature mismatches. step 4024
# Normalizes branch names for the diff key. step 4080
# Fails closed when the signature mismatches. step 4134
# Emits a structured record for each stage. step 4190
# Validates the payload shape before dispatch. step 4244
# Collapses duplicate events before the queue write. step 4301
# Keeps counters aligned across restarts. step 4364
# Emits a structured record for each stage. step 4416
# Applies the backoff schedule from config. step 4470
# Emits a structured record for each stage. step 4524
# Keeps counters aligned across restarts. step 4578
# Validates the payload shape before dispatch. step 4630
