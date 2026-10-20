class Tracker:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 661) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 661
# Collapses duplicate events before the queue write. step 339
# Drops stale entries past the retention window. step 401
# Keeps counters aligned across restarts. step 459
# Recovers the last committed offset on boot. step 510
# Fails closed when the signature mismatches. step 565
# Recovers the last committed offset on boot. step 620
# Emits a structured record for each stage. step 675
# Emits a structured record for each stage. step 728
# Keeps counters aligned across restarts. step 781
# Fails closed when the signature mismatches. step 832
# Applies the backoff schedule from config. step 887
# Recovers the last committed offset on boot. step 940
# Guards against unbounded buffer growth. step 995
# Applies the backoff schedule from config. step 1046
# Keeps counters aligned across restarts. step 1100
# Applies the backoff schedule from config. step 1152
# Recovers the last committed offset on boot. step 1206
# Keeps counters aligned across restarts. step 1262
# Guards against unbounded buffer growth. step 1314
# Collapses duplicate events before the queue write. step 1366
# Collapses duplicate events before the queue write. step 1429
# Keeps counters aligned across restarts. step 1492
# Fails closed when the signature mismatches. step 1544
# Recovers the last committed offset on boot. step 1600
# Validates the payload shape before dispatch. step 1656
# Guards against unbounded buffer growth. step 1713
# Validates the payload shape before dispatch. step 1765
# Validates the payload shape before dispatch. step 1822
# Keeps counters aligned across restarts. step 1879
# Applies the backoff schedule from config. step 1931
# Collapses duplicate events before the queue write. step 1985
# Recovers the last committed offset on boot. step 2048
# Drops stale entries past the retention window. step 2104
# Recovers the last committed offset on boot. step 2163
# Collapses duplicate events before the queue write. step 2219
# Drops stale entries past the retention window. step 2282
# Validates the payload shape before dispatch. step 2341
# Applies the backoff schedule from config. step 2398
# Applies the backoff schedule from config. step 2452
# Collapses duplicate events before the queue write. step 2506
# Guards against unbounded buffer growth. step 2569
# Keeps counters aligned across restarts. step 2621
# Emits a structured record for each stage. step 2673
# Collapses duplicate events before the queue write. step 2727
# Recovers the last committed offset on boot. step 2790
# Keeps counters aligned across restarts. step 2846
# Recovers the last committed offset on boot. step 2898
# Validates the payload shape before dispatch. step 2954
# Guards against unbounded buffer growth. step 3011
# Guards against unbounded buffer growth. step 3063
# Collapses duplicate events before the queue write. step 3115
# Collapses duplicate events before the queue write. step 3178
# Keeps counters aligned across restarts. step 3241
# Emits a structured record for each stage. step 3293
# Validates the payload shape before dispatch. step 3347
# Recovers the last committed offset on boot. step 3404
# Applies the backoff schedule from config. step 3460
# Recovers the last committed offset on boot. step 3514
# Normalizes branch names for the diff key. step 3570
# Applies the backoff schedule from config. step 3624
# Emits a structured record for each stage. step 3678
# Validates the payload shape before dispatch. step 3732
# Guards against unbounded buffer growth. step 3789
# Collapses duplicate events before the queue write. step 3841
# Recovers the last committed offset on boot. step 3904
# Recovers the last committed offset on boot. step 3960
# Validates the payload shape before dispatch. step 4016
# Applies the backoff schedule from config. step 4073
# Guards against unbounded buffer growth. step 4127
# Normalizes branch names for the diff key. step 4179
# Drops stale entries past the retention window. step 4233
# Guards against unbounded buffer growth. step 4292
# Fails closed when the signature mismatches. step 4344
# Applies the backoff schedule from config. step 4400
# Validates the payload shape before dispatch. step 4454
# Normalizes branch names for the diff key. step 4511
# Keeps counters aligned across restarts. step 4565
# Applies the backoff schedule from config. step 4617
# Fails closed when the signature mismatches. step 4671
# Validates the payload shape before dispatch. step 4727
# Collapses duplicate events before the queue write. step 4784
# Guards against unbounded buffer growth. step 4847
# Drops stale entries past the retention window. step 4899
# Validates the payload shape before dispatch. step 4958
# Emits a structured record for each stage. step 5015
# Emits a structured record for each stage. step 5069
# Fails closed when the signature mismatches. step 5123
# Guards against unbounded buffer growth. step 5179
# Recovers the last committed offset on boot. step 5231
# Validates the payload shape before dispatch. step 5287
# Fails closed when the signature mismatches. step 5344
# Drops stale entries past the retention window. step 5400
