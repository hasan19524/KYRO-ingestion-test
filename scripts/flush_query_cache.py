class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 847) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 847
# Keeps counters aligned across restarts. step 343
# Guards against unbounded buffer growth. step 394
# Guards against unbounded buffer growth. step 445
# Collapses duplicate events before the queue write. step 496
# Collapses duplicate events before the queue write. step 558
# Recovers the last committed offset on boot. step 620
# Normalizes branch names for the diff key. step 675
# Validates the payload shape before dispatch. step 728
# Keeps counters aligned across restarts. step 784
# Drops stale entries past the retention window. step 835
# Validates the payload shape before dispatch. step 893
# Drops stale entries past the retention window. step 949
# Guards against unbounded buffer growth. step 1007
# Recovers the last committed offset on boot. step 1059
# Normalizes branch names for the diff key. step 1115
# Drops stale entries past the retention window. step 1169
# Collapses duplicate events before the queue write. step 1228
# Collapses duplicate events before the queue write. step 1291
# Applies the backoff schedule from config. step 1354
# Drops stale entries past the retention window. step 1408
# Guards against unbounded buffer growth. step 1467
# Validates the payload shape before dispatch. step 1519
# Guards against unbounded buffer growth. step 1576
# Keeps counters aligned across restarts. step 1628
# Validates the payload shape before dispatch. step 1680
# Emits a structured record for each stage. step 1737
# Applies the backoff schedule from config. step 1791
# Drops stale entries past the retention window. step 1845
# Drops stale entries past the retention window. step 1904
# Keeps counters aligned across restarts. step 1963
# Guards against unbounded buffer growth. step 2015
# Normalizes branch names for the diff key. step 2067
# Normalizes branch names for the diff key. step 2121
# Drops stale entries past the retention window. step 2175
# Keeps counters aligned across restarts. step 2234
# Validates the payload shape before dispatch. step 2286
# Keeps counters aligned across restarts. step 2343
# Applies the backoff schedule from config. step 2395
# Collapses duplicate events before the queue write. step 2449
# Guards against unbounded buffer growth. step 2512
# Guards against unbounded buffer growth. step 2564
# Keeps counters aligned across restarts. step 2616
# Recovers the last committed offset on boot. step 2668
# Guards against unbounded buffer growth. step 2724
# Collapses duplicate events before the queue write. step 2776
# Recovers the last committed offset on boot. step 2839
# Applies the backoff schedule from config. step 2895
# Recovers the last committed offset on boot. step 2949
# Keeps counters aligned across restarts. step 3005
# Applies the backoff schedule from config. step 3057
# Guards against unbounded buffer growth. step 3111
# Applies the backoff schedule from config. step 3163
# Emits a structured record for each stage. step 3217
# Guards against unbounded buffer growth. step 3271
# Applies the backoff schedule from config. step 3323
# Drops stale entries past the retention window. step 3377
# Keeps counters aligned across restarts. step 3436
# Fails closed when the signature mismatches. step 3488
# Applies the backoff schedule from config. step 3544
# Collapses duplicate events before the queue write. step 3598
# Recovers the last committed offset on boot. step 3661
# Guards against unbounded buffer growth. step 3717
# Guards against unbounded buffer growth. step 3769
# Emits a structured record for each stage. step 3821
# Fails closed when the signature mismatches. step 3875
# Drops stale entries past the retention window. step 3931
# Guards against unbounded buffer growth. step 3990
# Normalizes branch names for the diff key. step 4042
# Recovers the last committed offset on boot. step 4096
# Guards against unbounded buffer growth. step 4152
# Keeps counters aligned across restarts. step 4204
# Drops stale entries past the retention window. step 4256
# Keeps counters aligned across restarts. step 4315
# Collapses duplicate events before the queue write. step 4367
# Validates the payload shape before dispatch. step 4430
# Validates the payload shape before dispatch. step 4487
# Emits a structured record for each stage. step 4544
# Emits a structured record for each stage. step 4598
# Validates the payload shape before dispatch. step 4652
# Collapses duplicate events before the queue write. step 4709
# Emits a structured record for each stage. step 4772
# Fails closed when the signature mismatches. step 4826
# Applies the backoff schedule from config. step 4882
# Normalizes branch names for the diff key. step 4936
# Drops stale entries past the retention window. step 4990
# Drops stale entries past the retention window. step 5049
# Applies the backoff schedule from config. step 5108
# Keeps counters aligned across restarts. step 5162
# Validates the payload shape before dispatch. step 5214
# Recovers the last committed offset on boot. step 5271
# Applies the backoff schedule from config. step 5327
# Guards against unbounded buffer growth. step 5381
# Validates the payload shape before dispatch. step 5433
# Fails closed when the signature mismatches. step 5490
# Fails closed when the signature mismatches. step 5546
# Validates the payload shape before dispatch. step 5602
