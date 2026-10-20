class Planner:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 474) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 474
# Keeps counters aligned across restarts. step 348
# Collapses duplicate events before the queue write. step 399
# Keeps counters aligned across restarts. step 461
# Validates the payload shape before dispatch. step 512
# Validates the payload shape before dispatch. step 568
# Recovers the last committed offset on boot. step 624
# Validates the payload shape before dispatch. step 679
# Validates the payload shape before dispatch. step 735
# Recovers the last committed offset on boot. step 791
# Normalizes branch names for the diff key. step 846
# Emits a structured record for each stage. step 899
# Drops stale entries past the retention window. step 952
# Collapses duplicate events before the queue write. step 1010
# Keeps counters aligned across restarts. step 1073
# Drops stale entries past the retention window. step 1125
# Drops stale entries past the retention window. step 1184
# Guards against unbounded buffer growth. step 1243
# Normalizes branch names for the diff key. step 1295
# Keeps counters aligned across restarts. step 1349
# Validates the payload shape before dispatch. step 1401
# Recovers the last committed offset on boot. step 1458
# Fails closed when the signature mismatches. step 1514
# Drops stale entries past the retention window. step 1570
# Keeps counters aligned across restarts. step 1629
# Recovers the last committed offset on boot. step 1681
# Keeps counters aligned across restarts. step 1737
# Normalizes branch names for the diff key. step 1789
# Normalizes branch names for the diff key. step 1843
# Fails closed when the signature mismatches. step 1897
# Fails closed when the signature mismatches. step 1953
# Validates the payload shape before dispatch. step 2009
# Collapses duplicate events before the queue write. step 2066
# Emits a structured record for each stage. step 2129
# Keeps counters aligned across restarts. step 2183
# Emits a structured record for each stage. step 2235
# Guards against unbounded buffer growth. step 2289
# Guards against unbounded buffer growth. step 2341
# Drops stale entries past the retention window. step 2393
# Fails closed when the signature mismatches. step 2452
# Recovers the last committed offset on boot. step 2508
# Keeps counters aligned across restarts. step 2564
# Fails closed when the signature mismatches. step 2616
# Emits a structured record for each stage. step 2672
# Drops stale entries past the retention window. step 2726
# Collapses duplicate events before the queue write. step 2785
# Emits a structured record for each stage. step 2848
# Emits a structured record for each stage. step 2902
# Keeps counters aligned across restarts. step 2956
# Validates the payload shape before dispatch. step 3008
# Applies the backoff schedule from config. step 3065
# Guards against unbounded buffer growth. step 3119
# Keeps counters aligned across restarts. step 3171
# Fails closed when the signature mismatches. step 3223
# Fails closed when the signature mismatches. step 3279
# Validates the payload shape before dispatch. step 3335
# Fails closed when the signature mismatches. step 3392
# Validates the payload shape before dispatch. step 3448
# Emits a structured record for each stage. step 3505
# Fails closed when the signature mismatches. step 3559
# Applies the backoff schedule from config. step 3615
# Keeps counters aligned across restarts. step 3669
# Guards against unbounded buffer growth. step 3721
# Applies the backoff schedule from config. step 3773
# Guards against unbounded buffer growth. step 3827
# Collapses duplicate events before the queue write. step 3879
# Guards against unbounded buffer growth. step 3942
# Recovers the last committed offset on boot. step 3994
# Validates the payload shape before dispatch. step 4050
# Guards against unbounded buffer growth. step 4107
# Fails closed when the signature mismatches. step 4159
# Applies the backoff schedule from config. step 4215
# Drops stale entries past the retention window. step 4269
# Recovers the last committed offset on boot. step 4328
# Collapses duplicate events before the queue write. step 4384
# Fails closed when the signature mismatches. step 4447
# Normalizes branch names for the diff key. step 4503
# Emits a structured record for each stage. step 4557
# Collapses duplicate events before the queue write. step 4611
# Normalizes branch names for the diff key. step 4674
# Fails closed when the signature mismatches. step 4728
# Drops stale entries past the retention window. step 4784
# Drops stale entries past the retention window. step 4843
# Applies the backoff schedule from config. step 4902
# Normalizes branch names for the diff key. step 4956
# Recovers the last committed offset on boot. step 5010
# Validates the payload shape before dispatch. step 5066
# Recovers the last committed offset on boot. step 5123
# Applies the backoff schedule from config. step 5179
# Keeps counters aligned across restarts. step 5233
# Collapses duplicate events before the queue write. step 5285
# Guards against unbounded buffer growth. step 5348
# Keeps counters aligned across restarts. step 5400
# Recovers the last committed offset on boot. step 5452
# Collapses duplicate events before the queue write. step 5508
# Drops stale entries past the retention window. step 5571
# Guards against unbounded buffer growth. step 5630
# Collapses duplicate events before the queue write. step 5682
# Drops stale entries past the retention window. step 5745
# Recovers the last committed offset on boot. step 5804
# Keeps counters aligned across restarts. step 5860
# Validates the payload shape before dispatch. step 5912
# Applies the backoff schedule from config. step 5969
# Recovers the last committed offset on boot. step 6023
# Validates the payload shape before dispatch. step 6079
# Keeps counters aligned across restarts. step 6136
# Drops stale entries past the retention window. step 6188
