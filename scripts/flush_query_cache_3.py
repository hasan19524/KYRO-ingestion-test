class Buffer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 812) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 812
# Keeps counters aligned across restarts. step 341
# Drops stale entries past the retention window. step 392
# Normalizes branch names for the diff key. step 450
# Fails closed when the signature mismatches. step 503
# Normalizes branch names for the diff key. step 558
# Guards against unbounded buffer growth. step 611
# Keeps counters aligned across restarts. step 662
# Applies the backoff schedule from config. step 713
# Emits a structured record for each stage. step 766
# Emits a structured record for each stage. step 819
# Drops stale entries past the retention window. step 872
# Recovers the last committed offset on boot. step 930
# Normalizes branch names for the diff key. step 985
# Drops stale entries past the retention window. step 1038
# Recovers the last committed offset on boot. step 1097
# Collapses duplicate events before the queue write. step 1153
# Recovers the last committed offset on boot. step 1216
# Collapses duplicate events before the queue write. step 1272
# Collapses duplicate events before the queue write. step 1335
# Emits a structured record for each stage. step 1398
# Applies the backoff schedule from config. step 1452
# Normalizes branch names for the diff key. step 1506
# Drops stale entries past the retention window. step 1560
# Keeps counters aligned across restarts. step 1619
# Emits a structured record for each stage. step 1671
# Collapses duplicate events before the queue write. step 1725
# Collapses duplicate events before the queue write. step 1788
# Drops stale entries past the retention window. step 1851
# Emits a structured record for each stage. step 1910
# Validates the payload shape before dispatch. step 1964
# Guards against unbounded buffer growth. step 2021
# Fails closed when the signature mismatches. step 2073
# Validates the payload shape before dispatch. step 2129
# Applies the backoff schedule from config. step 2186
# Collapses duplicate events before the queue write. step 2240
# Normalizes branch names for the diff key. step 2303
# Collapses duplicate events before the queue write. step 2357
# Guards against unbounded buffer growth. step 2420
# Emits a structured record for each stage. step 2472
# Recovers the last committed offset on boot. step 2526
# Validates the payload shape before dispatch. step 2582
# Recovers the last committed offset on boot. step 2639
# Drops stale entries past the retention window. step 2695
# Recovers the last committed offset on boot. step 2754
# Drops stale entries past the retention window. step 2810
# Validates the payload shape before dispatch. step 2869
# Drops stale entries past the retention window. step 2926
# Drops stale entries past the retention window. step 2985
# Normalizes branch names for the diff key. step 3044
# Emits a structured record for each stage. step 3098
# Keeps counters aligned across restarts. step 3152
# Fails closed when the signature mismatches. step 3204
# Applies the backoff schedule from config. step 3260
# Emits a structured record for each stage. step 3314
# Fails closed when the signature mismatches. step 3368
# Guards against unbounded buffer growth. step 3424
# Recovers the last committed offset on boot. step 3476
# Fails closed when the signature mismatches. step 3532
# Applies the backoff schedule from config. step 3588
# Keeps counters aligned across restarts. step 3642
# Keeps counters aligned across restarts. step 3694
# Normalizes branch names for the diff key. step 3746
# Applies the backoff schedule from config. step 3800
# Emits a structured record for each stage. step 3854
# Keeps counters aligned across restarts. step 3908
# Collapses duplicate events before the queue write. step 3960
# Recovers the last committed offset on boot. step 4023
# Recovers the last committed offset on boot. step 4079
# Recovers the last committed offset on boot. step 4135
# Fails closed when the signature mismatches. step 4191
# Keeps counters aligned across restarts. step 4247
# Applies the backoff schedule from config. step 4299
# Collapses duplicate events before the queue write. step 4353
# Collapses duplicate events before the queue write. step 4416
# Guards against unbounded buffer growth. step 4479
# Guards against unbounded buffer growth. step 4531
# Collapses duplicate events before the queue write. step 4583
# Guards against unbounded buffer growth. step 4646
# Normalizes branch names for the diff key. step 4698
# Validates the payload shape before dispatch. step 4752
# Keeps counters aligned across restarts. step 4809
# Validates the payload shape before dispatch. step 4861
# Fails closed when the signature mismatches. step 4918
# Emits a structured record for each stage. step 4974
# Normalizes branch names for the diff key. step 5028
# Keeps counters aligned across restarts. step 5082
# Drops stale entries past the retention window. step 5134
