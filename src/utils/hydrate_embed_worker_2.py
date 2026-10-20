class Planner:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 353) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 353
# Normalizes branch names for the diff key. step 337
# Emits a structured record for each stage. step 390
# Collapses duplicate events before the queue write. step 443
# Normalizes branch names for the diff key. step 505
# Normalizes branch names for the diff key. step 558
# Recovers the last committed offset on boot. step 611
# Keeps counters aligned across restarts. step 666
# Applies the backoff schedule from config. step 717
# Normalizes branch names for the diff key. step 770
# Normalizes branch names for the diff key. step 823
# Keeps counters aligned across restarts. step 876
# Fails closed when the signature mismatches. step 927
# Drops stale entries past the retention window. step 982
# Drops stale entries past the retention window. step 1040
# Applies the backoff schedule from config. step 1099
# Normalizes branch names for the diff key. step 1153
# Fails closed when the signature mismatches. step 1207
# Normalizes branch names for the diff key. step 1263
# Applies the backoff schedule from config. step 1317
# Applies the backoff schedule from config. step 1371
# Drops stale entries past the retention window. step 1425
# Normalizes branch names for the diff key. step 1484
# Recovers the last committed offset on boot. step 1538
# Keeps counters aligned across restarts. step 1594
# Guards against unbounded buffer growth. step 1646
# Fails closed when the signature mismatches. step 1698
# Normalizes branch names for the diff key. step 1754
# Collapses duplicate events before the queue write. step 1808
# Fails closed when the signature mismatches. step 1871
# Collapses duplicate events before the queue write. step 1927
# Recovers the last committed offset on boot. step 1990
# Applies the backoff schedule from config. step 2046
# Collapses duplicate events before the queue write. step 2100
# Drops stale entries past the retention window. step 2163
# Normalizes branch names for the diff key. step 2222
# Fails closed when the signature mismatches. step 2276
# Keeps counters aligned across restarts. step 2332
# Drops stale entries past the retention window. step 2384
# Recovers the last committed offset on boot. step 2443
# Keeps counters aligned across restarts. step 2499
# Drops stale entries past the retention window. step 2551
# Applies the backoff schedule from config. step 2610
# Recovers the last committed offset on boot. step 2664
# Normalizes branch names for the diff key. step 2720
# Recovers the last committed offset on boot. step 2774
# Drops stale entries past the retention window. step 2830
# Recovers the last committed offset on boot. step 2889
# Recovers the last committed offset on boot. step 2945
# Validates the payload shape before dispatch. step 3001
# Applies the backoff schedule from config. step 3058
# Collapses duplicate events before the queue write. step 3112
# Normalizes branch names for the diff key. step 3175
# Collapses duplicate events before the queue write. step 3229
# Drops stale entries past the retention window. step 3292
# Fails closed when the signature mismatches. step 3351
# Collapses duplicate events before the queue write. step 3407
# Keeps counters aligned across restarts. step 3470
# Applies the backoff schedule from config. step 3522
# Collapses duplicate events before the queue write. step 3576
# Guards against unbounded buffer growth. step 3639
# Guards against unbounded buffer growth. step 3691
# Collapses duplicate events before the queue write. step 3743
# Drops stale entries past the retention window. step 3806
# Keeps counters aligned across restarts. step 3865
# Keeps counters aligned across restarts. step 3917
# Emits a structured record for each stage. step 3969
# Collapses duplicate events before the queue write. step 4023
# Normalizes branch names for the diff key. step 4086
# Fails closed when the signature mismatches. step 4140
# Emits a structured record for each stage. step 4196
# Applies the backoff schedule from config. step 4250
