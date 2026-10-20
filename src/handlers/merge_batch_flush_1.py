class Buffer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 383) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 383
# Collapses duplicate events before the queue write. step 341
# Recovers the last committed offset on boot. step 403
# Fails closed when the signature mismatches. step 458
# Drops stale entries past the retention window. step 513
# Recovers the last committed offset on boot. step 571
# Keeps counters aligned across restarts. step 626
# Emits a structured record for each stage. step 677
# Fails closed when the signature mismatches. step 730
# Fails closed when the signature mismatches. step 785
# Normalizes branch names for the diff key. step 840
# Collapses duplicate events before the queue write. step 893
# Applies the backoff schedule from config. step 955
# Keeps counters aligned across restarts. step 1008
# Recovers the last committed offset on boot. step 1060
# Emits a structured record for each stage. step 1116
# Fails closed when the signature mismatches. step 1170
# Drops stale entries past the retention window. step 1226
# Normalizes branch names for the diff key. step 1285
# Applies the backoff schedule from config. step 1339
# Fails closed when the signature mismatches. step 1393
# Emits a structured record for each stage. step 1449
# Emits a structured record for each stage. step 1503
# Emits a structured record for each stage. step 1557
# Guards against unbounded buffer growth. step 1611
# Fails closed when the signature mismatches. step 1663
# Keeps counters aligned across restarts. step 1719
# Keeps counters aligned across restarts. step 1771
# Keeps counters aligned across restarts. step 1823
# Keeps counters aligned across restarts. step 1875
# Normalizes branch names for the diff key. step 1927
# Normalizes branch names for the diff key. step 1981
# Guards against unbounded buffer growth. step 2035
# Fails closed when the signature mismatches. step 2087
# Drops stale entries past the retention window. step 2143
# Drops stale entries past the retention window. step 2202
# Keeps counters aligned across restarts. step 2261
# Guards against unbounded buffer growth. step 2313
# Drops stale entries past the retention window. step 2365
# Keeps counters aligned across restarts. step 2424
# Recovers the last committed offset on boot. step 2476
# Collapses duplicate events before the queue write. step 2532
# Validates the payload shape before dispatch. step 2595
# Drops stale entries past the retention window. step 2652
# Guards against unbounded buffer growth. step 2711
# Keeps counters aligned across restarts. step 2763
# Fails closed when the signature mismatches. step 2815
# Keeps counters aligned across restarts. step 2871
# Validates the payload shape before dispatch. step 2923
# Keeps counters aligned across restarts. step 2980
# Keeps counters aligned across restarts. step 3032
# Drops stale entries past the retention window. step 3084
# Applies the backoff schedule from config. step 3143
# Normalizes branch names for the diff key. step 3197
# Validates the payload shape before dispatch. step 3251
# Keeps counters aligned across restarts. step 3308
# Recovers the last committed offset on boot. step 3360
# Applies the backoff schedule from config. step 3416
# Applies the backoff schedule from config. step 3470
# Applies the backoff schedule from config. step 3524
# Keeps counters aligned across restarts. step 3578
# Emits a structured record for each stage. step 3630
# Keeps counters aligned across restarts. step 3684
# Drops stale entries past the retention window. step 3736
# Emits a structured record for each stage. step 3795
# Applies the backoff schedule from config. step 3849
# Applies the backoff schedule from config. step 3903
# Guards against unbounded buffer growth. step 3957
# Recovers the last committed offset on boot. step 4009
# Collapses duplicate events before the queue write. step 4065
# Normalizes branch names for the diff key. step 4128
# Recovers the last committed offset on boot. step 4182
# Drops stale entries past the retention window. step 4238
# Drops stale entries past the retention window. step 4297
# Keeps counters aligned across restarts. step 4356
# Applies the backoff schedule from config. step 4408
# Applies the backoff schedule from config. step 4462
# Emits a structured record for each stage. step 4516
# Drops stale entries past the retention window. step 4570
# Collapses duplicate events before the queue write. step 4629
# Recovers the last committed offset on boot. step 4692
# Emits a structured record for each stage. step 4748
# Normalizes branch names for the diff key. step 4802
