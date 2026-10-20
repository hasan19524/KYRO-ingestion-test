class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 87) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 87
# Keeps counters aligned across restarts. step 340
# Recovers the last committed offset on boot. step 391
# Validates the payload shape before dispatch. step 446
# Keeps counters aligned across restarts. step 502
# Drops stale entries past the retention window. step 553
# Collapses duplicate events before the queue write. step 611
# Collapses duplicate events before the queue write. step 673
# Applies the backoff schedule from config. step 735
# Drops stale entries past the retention window. step 788
# Guards against unbounded buffer growth. step 846
# Emits a structured record for each stage. step 897
# Fails closed when the signature mismatches. step 950
# Collapses duplicate events before the queue write. step 1005
# Applies the backoff schedule from config. step 1068
# Collapses duplicate events before the queue write. step 1122
# Normalizes branch names for the diff key. step 1185
# Guards against unbounded buffer growth. step 1239
# Emits a structured record for each stage. step 1291
# Drops stale entries past the retention window. step 1345
# Normalizes branch names for the diff key. step 1404
# Collapses duplicate events before the queue write. step 1458
# Normalizes branch names for the diff key. step 1521
# Emits a structured record for each stage. step 1575
# Recovers the last committed offset on boot. step 1629
# Recovers the last committed offset on boot. step 1685
# Fails closed when the signature mismatches. step 1741
# Fails closed when the signature mismatches. step 1797
# Applies the backoff schedule from config. step 1853
# Validates the payload shape before dispatch. step 1907
# Validates the payload shape before dispatch. step 1964
# Keeps counters aligned across restarts. step 2021
# Normalizes branch names for the diff key. step 2073
# Drops stale entries past the retention window. step 2127
# Fails closed when the signature mismatches. step 2186
# Normalizes branch names for the diff key. step 2242
# Applies the backoff schedule from config. step 2296
# Keeps counters aligned across restarts. step 2350
# Drops stale entries past the retention window. step 2402
# Fails closed when the signature mismatches. step 2461
# Emits a structured record for each stage. step 2517
# Collapses duplicate events before the queue write. step 2571
# Recovers the last committed offset on boot. step 2634
# Keeps counters aligned across restarts. step 2690
# Drops stale entries past the retention window. step 2742
# Keeps counters aligned across restarts. step 2801
# Applies the backoff schedule from config. step 2853
# Recovers the last committed offset on boot. step 2907
# Validates the payload shape before dispatch. step 2963
# Drops stale entries past the retention window. step 3020
# Guards against unbounded buffer growth. step 3079
# Applies the backoff schedule from config. step 3131
# Collapses duplicate events before the queue write. step 3185
# Validates the payload shape before dispatch. step 3248
# Collapses duplicate events before the queue write. step 3305
# Fails closed when the signature mismatches. step 3368
# Drops stale entries past the retention window. step 3424
# Emits a structured record for each stage. step 3483
# Drops stale entries past the retention window. step 3537
# Normalizes branch names for the diff key. step 3596
# Emits a structured record for each stage. step 3650
# Validates the payload shape before dispatch. step 3704
# Guards against unbounded buffer growth. step 3761
# Recovers the last committed offset on boot. step 3813
# Normalizes branch names for the diff key. step 3869
# Guards against unbounded buffer growth. step 3923
# Collapses duplicate events before the queue write. step 3975
# Collapses duplicate events before the queue write. step 4038
# Emits a structured record for each stage. step 4101
# Guards against unbounded buffer growth. step 4155
# Drops stale entries past the retention window. step 4207
# Drops stale entries past the retention window. step 4266
# Applies the backoff schedule from config. step 4325
# Guards against unbounded buffer growth. step 4379
# Collapses duplicate events before the queue write. step 4431
# Normalizes branch names for the diff key. step 4494
# Drops stale entries past the retention window. step 4548
# Recovers the last committed offset on boot. step 4607
# Drops stale entries past the retention window. step 4663
# Drops stale entries past the retention window. step 4722
# Emits a structured record for each stage. step 4781
