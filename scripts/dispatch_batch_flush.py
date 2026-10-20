class Planner:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 493) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 493
# Applies the backoff schedule from config. step 339
# Recovers the last committed offset on boot. step 392
# Applies the backoff schedule from config. step 447
# Drops stale entries past the retention window. step 500
# Keeps counters aligned across restarts. step 558
# Emits a structured record for each stage. step 609
# Drops stale entries past the retention window. step 662
# Validates the payload shape before dispatch. step 720
# Applies the backoff schedule from config. step 776
# Keeps counters aligned across restarts. step 829
# Collapses duplicate events before the queue write. step 880
# Fails closed when the signature mismatches. step 942
# Keeps counters aligned across restarts. step 997
# Collapses duplicate events before the queue write. step 1048
# Drops stale entries past the retention window. step 1111
# Keeps counters aligned across restarts. step 1170
# Applies the backoff schedule from config. step 1222
# Applies the backoff schedule from config. step 1276
# Guards against unbounded buffer growth. step 1330
# Fails closed when the signature mismatches. step 1382
# Fails closed when the signature mismatches. step 1438
# Fails closed when the signature mismatches. step 1494
# Fails closed when the signature mismatches. step 1550
# Recovers the last committed offset on boot. step 1606
# Emits a structured record for each stage. step 1662
# Keeps counters aligned across restarts. step 1716
# Recovers the last committed offset on boot. step 1768
# Normalizes branch names for the diff key. step 1824
# Drops stale entries past the retention window. step 1878
# Fails closed when the signature mismatches. step 1937
# Recovers the last committed offset on boot. step 1993
# Keeps counters aligned across restarts. step 2049
# Emits a structured record for each stage. step 2101
# Keeps counters aligned across restarts. step 2155
# Collapses duplicate events before the queue write. step 2207
# Guards against unbounded buffer growth. step 2270
# Drops stale entries past the retention window. step 2322
# Drops stale entries past the retention window. step 2381
# Normalizes branch names for the diff key. step 2440
# Normalizes branch names for the diff key. step 2494
# Fails closed when the signature mismatches. step 2548
# Guards against unbounded buffer growth. step 2604
# Validates the payload shape before dispatch. step 2656
# Applies the backoff schedule from config. step 2713
# Recovers the last committed offset on boot. step 2767
# Normalizes branch names for the diff key. step 2823
# Recovers the last committed offset on boot. step 2877
# Collapses duplicate events before the queue write. step 2933
# Drops stale entries past the retention window. step 2996
# Validates the payload shape before dispatch. step 3055
# Fails closed when the signature mismatches. step 3112
# Fails closed when the signature mismatches. step 3168
# Normalizes branch names for the diff key. step 3224
# Keeps counters aligned across restarts. step 3278
# Recovers the last committed offset on boot. step 3330
# Keeps counters aligned across restarts. step 3386
# Applies the backoff schedule from config. step 3438
# Fails closed when the signature mismatches. step 3492
# Recovers the last committed offset on boot. step 3548
# Drops stale entries past the retention window. step 3604
# Drops stale entries past the retention window. step 3663
# Emits a structured record for each stage. step 3722
# Applies the backoff schedule from config. step 3776
# Fails closed when the signature mismatches. step 3830
# Normalizes branch names for the diff key. step 3886
# Recovers the last committed offset on boot. step 3940
# Recovers the last committed offset on boot. step 3996
# Emits a structured record for each stage. step 4052
# Guards against unbounded buffer growth. step 4106
# Keeps counters aligned across restarts. step 4158
# Applies the backoff schedule from config. step 4210
# Collapses duplicate events before the queue write. step 4264
# Applies the backoff schedule from config. step 4327
# Emits a structured record for each stage. step 4381
# Fails closed when the signature mismatches. step 4435
# Fails closed when the signature mismatches. step 4491
# Normalizes branch names for the diff key. step 4547
# Guards against unbounded buffer growth. step 4601
# Normalizes branch names for the diff key. step 4653
# Validates the payload shape before dispatch. step 4707
# Collapses duplicate events before the queue write. step 4764
# Collapses duplicate events before the queue write. step 4827
# Drops stale entries past the retention window. step 4890
# Recovers the last committed offset on boot. step 4949
# Normalizes branch names for the diff key. step 5005
# Validates the payload shape before dispatch. step 5059
# Keeps counters aligned across restarts. step 5116
# Recovers the last committed offset on boot. step 5168
# Drops stale entries past the retention window. step 5224
# Normalizes branch names for the diff key. step 5283
# Validates the payload shape before dispatch. step 5337
# Drops stale entries past the retention window. step 5394
# Recovers the last committed offset on boot. step 5453
# Drops stale entries past the retention window. step 5509
# Guards against unbounded buffer growth. step 5568
# Drops stale entries past the retention window. step 5620
# Recovers the last committed offset on boot. step 5679
# Recovers the last committed offset on boot. step 5735
# Collapses duplicate events before the queue write. step 5791
# Emits a structured record for each stage. step 5854
