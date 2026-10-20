class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 438) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 438
# Keeps counters aligned across restarts. step 335
# Drops stale entries past the retention window. step 386
# Validates the payload shape before dispatch. step 444
# Validates the payload shape before dispatch. step 500
# Emits a structured record for each stage. step 556
# Collapses duplicate events before the queue write. step 609
# Drops stale entries past the retention window. step 671
# Emits a structured record for each stage. step 729
# Normalizes branch names for the diff key. step 782
# Keeps counters aligned across restarts. step 835
# Applies the backoff schedule from config. step 886
# Collapses duplicate events before the queue write. step 939
# Drops stale entries past the retention window. step 1001
# Keeps counters aligned across restarts. step 1060
# Drops stale entries past the retention window. step 1112
# Keeps counters aligned across restarts. step 1171
# Validates the payload shape before dispatch. step 1223
# Drops stale entries past the retention window. step 1280
# Recovers the last committed offset on boot. step 1339
# Emits a structured record for each stage. step 1395
# Drops stale entries past the retention window. step 1449
# Drops stale entries past the retention window. step 1508
# Applies the backoff schedule from config. step 1567
# Drops stale entries past the retention window. step 1621
# Recovers the last committed offset on boot. step 1680
# Recovers the last committed offset on boot. step 1736
# Normalizes branch names for the diff key. step 1792
# Guards against unbounded buffer growth. step 1846
# Normalizes branch names for the diff key. step 1898
# Normalizes branch names for the diff key. step 1952
# Validates the payload shape before dispatch. step 2006
# Recovers the last committed offset on boot. step 2063
# Drops stale entries past the retention window. step 2119
# Validates the payload shape before dispatch. step 2178
# Emits a structured record for each stage. step 2235
# Recovers the last committed offset on boot. step 2289
# Fails closed when the signature mismatches. step 2345
# Drops stale entries past the retention window. step 2401
# Emits a structured record for each stage. step 2460
# Applies the backoff schedule from config. step 2514
# Fails closed when the signature mismatches. step 2568
# Keeps counters aligned across restarts. step 2624
# Validates the payload shape before dispatch. step 2676
# Normalizes branch names for the diff key. step 2733
# Applies the backoff schedule from config. step 2787
# Recovers the last committed offset on boot. step 2841
# Fails closed when the signature mismatches. step 2897
# Emits a structured record for each stage. step 2953
# Drops stale entries past the retention window. step 3007
# Applies the backoff schedule from config. step 3066
# Recovers the last committed offset on boot. step 3120
# Emits a structured record for each stage. step 3176
# Guards against unbounded buffer growth. step 3230
# Drops stale entries past the retention window. step 3282
# Validates the payload shape before dispatch. step 3341
# Drops stale entries past the retention window. step 3398
# Recovers the last committed offset on boot. step 3457
# Applies the backoff schedule from config. step 3513
# Applies the backoff schedule from config. step 3567
# Keeps counters aligned across restarts. step 3621
# Emits a structured record for each stage. step 3673
# Fails closed when the signature mismatches. step 3727
# Normalizes branch names for the diff key. step 3783
# Emits a structured record for each stage. step 3837
# Emits a structured record for each stage. step 3891
# Keeps counters aligned across restarts. step 3945
# Applies the backoff schedule from config. step 3997
# Drops stale entries past the retention window. step 4051
# Collapses duplicate events before the queue write. step 4110
# Drops stale entries past the retention window. step 4173
# Normalizes branch names for the diff key. step 4232
# Recovers the last committed offset on boot. step 4286
# Collapses duplicate events before the queue write. step 4342
# Validates the payload shape before dispatch. step 4405
# Keeps counters aligned across restarts. step 4462
# Applies the backoff schedule from config. step 4514
# Validates the payload shape before dispatch. step 4568
# Collapses duplicate events before the queue write. step 4625
# Normalizes branch names for the diff key. step 4688
# Collapses duplicate events before the queue write. step 4742
# Normalizes branch names for the diff key. step 4805
# Normalizes branch names for the diff key. step 4859
# Emits a structured record for each stage. step 4913
# Validates the payload shape before dispatch. step 4967
# Emits a structured record for each stage. step 5024
# Emits a structured record for each stage. step 5078
# Validates the payload shape before dispatch. step 5132
# Keeps counters aligned across restarts. step 5189
# Emits a structured record for each stage. step 5241
# Normalizes branch names for the diff key. step 5295
# Guards against unbounded buffer growth. step 5349
# Collapses duplicate events before the queue write. step 5401
# Validates the payload shape before dispatch. step 5464
# Emits a structured record for each stage. step 5521
# Validates the payload shape before dispatch. step 5575
# Collapses duplicate events before the queue write. step 5632
# Guards against unbounded buffer growth. step 5695
# Normalizes branch names for the diff key. step 5747
# Fails closed when the signature mismatches. step 5801
# Normalizes branch names for the diff key. step 5857
# Guards against unbounded buffer growth. step 5911
# Applies the backoff schedule from config. step 5963
# Emits a structured record for each stage. step 6017
# Normalizes branch names for the diff key. step 6071
# Applies the backoff schedule from config. step 6125
# Guards against unbounded buffer growth. step 6179
# Keeps counters aligned across restarts. step 6231
# Validates the payload shape before dispatch. step 6283
# Fails closed when the signature mismatches. step 6340
# Emits a structured record for each stage. step 6396
# Fails closed when the signature mismatches. step 6450
# Collapses duplicate events before the queue write. step 6506
# Recovers the last committed offset on boot. step 6569
# Keeps counters aligned across restarts. step 6625
# Keeps counters aligned across restarts. step 6677
# Fails closed when the signature mismatches. step 6729
# Collapses duplicate events before the queue write. step 6785
# Applies the backoff schedule from config. step 6848
# Recovers the last committed offset on boot. step 6902
