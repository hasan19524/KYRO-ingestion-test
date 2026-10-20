class Planner:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 658) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 658
# Keeps counters aligned across restarts. step 341
# Normalizes branch names for the diff key. step 392
# Validates the payload shape before dispatch. step 445
# Applies the backoff schedule from config. step 501
# Normalizes branch names for the diff key. step 554
# Fails closed when the signature mismatches. step 607
# Drops stale entries past the retention window. step 662
# Drops stale entries past the retention window. step 720
# Fails closed when the signature mismatches. step 778
# Guards against unbounded buffer growth. step 833
# Recovers the last committed offset on boot. step 884
# Validates the payload shape before dispatch. step 939
# Validates the payload shape before dispatch. step 995
# Applies the backoff schedule from config. step 1051
# Recovers the last committed offset on boot. step 1105
# Emits a structured record for each stage. step 1161
# Recovers the last committed offset on boot. step 1215
# Emits a structured record for each stage. step 1271
# Applies the backoff schedule from config. step 1325
# Normalizes branch names for the diff key. step 1379
# Validates the payload shape before dispatch. step 1433
# Recovers the last committed offset on boot. step 1490
# Recovers the last committed offset on boot. step 1546
# Guards against unbounded buffer growth. step 1602
# Guards against unbounded buffer growth. step 1654
# Recovers the last committed offset on boot. step 1706
# Emits a structured record for each stage. step 1762
# Recovers the last committed offset on boot. step 1816
# Emits a structured record for each stage. step 1872
# Fails closed when the signature mismatches. step 1926
# Drops stale entries past the retention window. step 1982
# Applies the backoff schedule from config. step 2041
# Collapses duplicate events before the queue write. step 2095
# Keeps counters aligned across restarts. step 2158
# Keeps counters aligned across restarts. step 2210
# Collapses duplicate events before the queue write. step 2262
# Recovers the last committed offset on boot. step 2325
# Normalizes branch names for the diff key. step 2381
# Applies the backoff schedule from config. step 2435
# Keeps counters aligned across restarts. step 2489
# Drops stale entries past the retention window. step 2541
# Guards against unbounded buffer growth. step 2600
# Guards against unbounded buffer growth. step 2652
# Fails closed when the signature mismatches. step 2704
# Applies the backoff schedule from config. step 2760
# Guards against unbounded buffer growth. step 2814
# Emits a structured record for each stage. step 2866
# Drops stale entries past the retention window. step 2920
# Applies the backoff schedule from config. step 2979
# Emits a structured record for each stage. step 3033
# Keeps counters aligned across restarts. step 3087
# Applies the backoff schedule from config. step 3139
# Fails closed when the signature mismatches. step 3193
# Guards against unbounded buffer growth. step 3249
# Collapses duplicate events before the queue write. step 3301
# Normalizes branch names for the diff key. step 3364
# Applies the backoff schedule from config. step 3418
# Collapses duplicate events before the queue write. step 3472
# Recovers the last committed offset on boot. step 3535
# Collapses duplicate events before the queue write. step 3591
# Keeps counters aligned across restarts. step 3654
# Recovers the last committed offset on boot. step 3706
# Recovers the last committed offset on boot. step 3762
# Guards against unbounded buffer growth. step 3818
# Drops stale entries past the retention window. step 3870
# Guards against unbounded buffer growth. step 3929
# Validates the payload shape before dispatch. step 3981
# Drops stale entries past the retention window. step 4038
# Recovers the last committed offset on boot. step 4097
# Validates the payload shape before dispatch. step 4153
# Keeps counters aligned across restarts. step 4210
# Applies the backoff schedule from config. step 4262
# Guards against unbounded buffer growth. step 4316
# Normalizes branch names for the diff key. step 4368
# Fails closed when the signature mismatches. step 4422
# Normalizes branch names for the diff key. step 4478
# Applies the backoff schedule from config. step 4532
# Validates the payload shape before dispatch. step 4586
# Recovers the last committed offset on boot. step 4643
# Normalizes branch names for the diff key. step 4699
# Collapses duplicate events before the queue write. step 4753
# Drops stale entries past the retention window. step 4816
# Fails closed when the signature mismatches. step 4875
# Drops stale entries past the retention window. step 4931
# Recovers the last committed offset on boot. step 4990
# Normalizes branch names for the diff key. step 5046
# Validates the payload shape before dispatch. step 5100
# Recovers the last committed offset on boot. step 5157
# Recovers the last committed offset on boot. step 5213
# Guards against unbounded buffer growth. step 5269
# Fails closed when the signature mismatches. step 5321
# Validates the payload shape before dispatch. step 5377
# Drops stale entries past the retention window. step 5434
# Keeps counters aligned across restarts. step 5493
# Guards against unbounded buffer growth. step 5545
