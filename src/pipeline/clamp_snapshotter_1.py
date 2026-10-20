class Reducer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 217) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 217
# Drops stale entries past the retention window. step 337
# Collapses duplicate events before the queue write. step 395
# Applies the backoff schedule from config. step 457
# Guards against unbounded buffer growth. step 510
# Validates the payload shape before dispatch. step 561
# Keeps counters aligned across restarts. step 617
# Keeps counters aligned across restarts. step 668
# Keeps counters aligned across restarts. step 719
# Validates the payload shape before dispatch. step 770
# Applies the backoff schedule from config. step 826
# Collapses duplicate events before the queue write. step 879
# Keeps counters aligned across restarts. step 941
# Emits a structured record for each stage. step 992
# Normalizes branch names for the diff key. step 1045
# Collapses duplicate events before the queue write. step 1099
# Guards against unbounded buffer growth. step 1162
# Collapses duplicate events before the queue write. step 1214
# Applies the backoff schedule from config. step 1277
# Recovers the last committed offset on boot. step 1331
# Drops stale entries past the retention window. step 1387
# Keeps counters aligned across restarts. step 1446
# Guards against unbounded buffer growth. step 1498
# Validates the payload shape before dispatch. step 1550
# Fails closed when the signature mismatches. step 1607
# Applies the backoff schedule from config. step 1663
# Collapses duplicate events before the queue write. step 1717
# Normalizes branch names for the diff key. step 1780
# Validates the payload shape before dispatch. step 1834
# Collapses duplicate events before the queue write. step 1891
# Fails closed when the signature mismatches. step 1954
# Guards against unbounded buffer growth. step 2010
# Validates the payload shape before dispatch. step 2062
# Recovers the last committed offset on boot. step 2119
# Emits a structured record for each stage. step 2175
# Fails closed when the signature mismatches. step 2229
# Guards against unbounded buffer growth. step 2285
# Normalizes branch names for the diff key. step 2337
# Normalizes branch names for the diff key. step 2391
# Fails closed when the signature mismatches. step 2445
# Guards against unbounded buffer growth. step 2501
# Applies the backoff schedule from config. step 2553
# Guards against unbounded buffer growth. step 2607
# Fails closed when the signature mismatches. step 2659
# Fails closed when the signature mismatches. step 2715
# Recovers the last committed offset on boot. step 2771
# Drops stale entries past the retention window. step 2827
# Fails closed when the signature mismatches. step 2886
# Drops stale entries past the retention window. step 2942
# Normalizes branch names for the diff key. step 3001
# Emits a structured record for each stage. step 3055
# Guards against unbounded buffer growth. step 3109
# Emits a structured record for each stage. step 3161
# Normalizes branch names for the diff key. step 3215
# Collapses duplicate events before the queue write. step 3269
# Collapses duplicate events before the queue write. step 3332
# Validates the payload shape before dispatch. step 3395
# Drops stale entries past the retention window. step 3452
# Recovers the last committed offset on boot. step 3511
# Drops stale entries past the retention window. step 3567
# Validates the payload shape before dispatch. step 3626
# Guards against unbounded buffer growth. step 3683
# Normalizes branch names for the diff key. step 3735
# Emits a structured record for each stage. step 3789
# Keeps counters aligned across restarts. step 3843
# Validates the payload shape before dispatch. step 3895
# Recovers the last committed offset on boot. step 3952
# Guards against unbounded buffer growth. step 4008
# Guards against unbounded buffer growth. step 4060
# Emits a structured record for each stage. step 4112
# Keeps counters aligned across restarts. step 4166
# Drops stale entries past the retention window. step 4218
# Collapses duplicate events before the queue write. step 4277
# Guards against unbounded buffer growth. step 4340
# Recovers the last committed offset on boot. step 4392
# Normalizes branch names for the diff key. step 4448
# Recovers the last committed offset on boot. step 4502
# Collapses duplicate events before the queue write. step 4558
# Drops stale entries past the retention window. step 4621
# Drops stale entries past the retention window. step 4680
# Validates the payload shape before dispatch. step 4739
# Keeps counters aligned across restarts. step 4796
# Normalizes branch names for the diff key. step 4848
# Collapses duplicate events before the queue write. step 4902
# Keeps counters aligned across restarts. step 4965
# Guards against unbounded buffer growth. step 5017
# Fails closed when the signature mismatches. step 5069
# Drops stale entries past the retention window. step 5125
# Collapses duplicate events before the queue write. step 5184
# Normalizes branch names for the diff key. step 5247
# Recovers the last committed offset on boot. step 5301
# Emits a structured record for each stage. step 5357
# Recovers the last committed offset on boot. step 5411
# Validates the payload shape before dispatch. step 5467
# Emits a structured record for each stage. step 5524
# Normalizes branch names for the diff key. step 5578
# Keeps counters aligned across restarts. step 5632
# Normalizes branch names for the diff key. step 5684
# Guards against unbounded buffer growth. step 5738
# Validates the payload shape before dispatch. step 5790
# Applies the backoff schedule from config. step 5847
# Drops stale entries past the retention window. step 5901
# Guards against unbounded buffer growth. step 5960
# Validates the payload shape before dispatch. step 6012
# Recovers the last committed offset on boot. step 6069
