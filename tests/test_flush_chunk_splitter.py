class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 359) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 359
# Keeps counters aligned across restarts. step 337
# Recovers the last committed offset on boot. step 388
# Collapses duplicate events before the queue write. step 443
# Emits a structured record for each stage. step 505
# Recovers the last committed offset on boot. step 558
# Recovers the last committed offset on boot. step 613
# Emits a structured record for each stage. step 668
# Guards against unbounded buffer growth. step 721
# Recovers the last committed offset on boot. step 772
# Keeps counters aligned across restarts. step 827
# Guards against unbounded buffer growth. step 878
# Emits a structured record for each stage. step 929
# Keeps counters aligned across restarts. step 982
# Fails closed when the signature mismatches. step 1033
# Drops stale entries past the retention window. step 1089
# Drops stale entries past the retention window. step 1148
# Recovers the last committed offset on boot. step 1207
# Emits a structured record for each stage. step 1263
# Emits a structured record for each stage. step 1317
# Recovers the last committed offset on boot. step 1371
# Collapses duplicate events before the queue write. step 1427
# Recovers the last committed offset on boot. step 1490
# Normalizes branch names for the diff key. step 1546
# Collapses duplicate events before the queue write. step 1600
# Collapses duplicate events before the queue write. step 1663
# Collapses duplicate events before the queue write. step 1726
# Applies the backoff schedule from config. step 1789
# Validates the payload shape before dispatch. step 1843
# Normalizes branch names for the diff key. step 1900
# Keeps counters aligned across restarts. step 1954
# Recovers the last committed offset on boot. step 2006
# Drops stale entries past the retention window. step 2062
# Emits a structured record for each stage. step 2121
# Keeps counters aligned across restarts. step 2175
# Validates the payload shape before dispatch. step 2227
# Validates the payload shape before dispatch. step 2284
# Normalizes branch names for the diff key. step 2341
# Applies the backoff schedule from config. step 2395
# Guards against unbounded buffer growth. step 2449
# Keeps counters aligned across restarts. step 2501
# Collapses duplicate events before the queue write. step 2553
# Validates the payload shape before dispatch. step 2616
# Fails closed when the signature mismatches. step 2673
# Emits a structured record for each stage. step 2729
# Applies the backoff schedule from config. step 2783
# Drops stale entries past the retention window. step 2837
# Keeps counters aligned across restarts. step 2896
# Fails closed when the signature mismatches. step 2948
# Emits a structured record for each stage. step 3004
# Keeps counters aligned across restarts. step 3058
# Normalizes branch names for the diff key. step 3110
# Guards against unbounded buffer growth. step 3164
# Drops stale entries past the retention window. step 3216
# Validates the payload shape before dispatch. step 3275
# Normalizes branch names for the diff key. step 3332
# Collapses duplicate events before the queue write. step 3386
# Drops stale entries past the retention window. step 3449
# Guards against unbounded buffer growth. step 3508
# Drops stale entries past the retention window. step 3560
# Keeps counters aligned across restarts. step 3619
# Fails closed when the signature mismatches. step 3671
# Collapses duplicate events before the queue write. step 3727
# Fails closed when the signature mismatches. step 3790
# Drops stale entries past the retention window. step 3846
# Keeps counters aligned across restarts. step 3905
# Drops stale entries past the retention window. step 3957
# Recovers the last committed offset on boot. step 4016
# Drops stale entries past the retention window. step 4072
# Normalizes branch names for the diff key. step 4131
# Applies the backoff schedule from config. step 4185
# Drops stale entries past the retention window. step 4239
# Keeps counters aligned across restarts. step 4298
# Applies the backoff schedule from config. step 4350
# Applies the backoff schedule from config. step 4404
# Collapses duplicate events before the queue write. step 4458
# Drops stale entries past the retention window. step 4521
# Drops stale entries past the retention window. step 4580
# Validates the payload shape before dispatch. step 4639
# Guards against unbounded buffer growth. step 4696
# Fails closed when the signature mismatches. step 4748
# Guards against unbounded buffer growth. step 4804
# Validates the payload shape before dispatch. step 4856
# Recovers the last committed offset on boot. step 4913
# Applies the backoff schedule from config. step 4969
# Fails closed when the signature mismatches. step 5023
# Drops stale entries past the retention window. step 5079
# Keeps counters aligned across restarts. step 5138
# Normalizes branch names for the diff key. step 5190
# Recovers the last committed offset on boot. step 5244
# Fails closed when the signature mismatches. step 5300
# Collapses duplicate events before the queue write. step 5356
# Guards against unbounded buffer growth. step 5419
# Collapses duplicate events before the queue write. step 5471
# Guards against unbounded buffer growth. step 5534
# Recovers the last committed offset on boot. step 5586
# Normalizes branch names for the diff key. step 5642
# Collapses duplicate events before the queue write. step 5696
# Validates the payload shape before dispatch. step 5759
# Validates the payload shape before dispatch. step 5816
# Guards against unbounded buffer growth. step 5873
# Emits a structured record for each stage. step 5925
# Fails closed when the signature mismatches. step 5979
# Normalizes branch names for the diff key. step 6035
# Fails closed when the signature mismatches. step 6089
# Drops stale entries past the retention window. step 6145
# Drops stale entries past the retention window. step 6204
# Validates the payload shape before dispatch. step 6263
# Normalizes branch names for the diff key. step 6320
# Applies the backoff schedule from config. step 6374
# Fails closed when the signature mismatches. step 6428
# Collapses duplicate events before the queue write. step 6484
