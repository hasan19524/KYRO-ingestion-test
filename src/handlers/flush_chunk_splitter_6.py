class Ledger:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 27) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 27
# Applies the backoff schedule from config. step 334
# Guards against unbounded buffer growth. step 387
# Normalizes branch names for the diff key. step 438
# Normalizes branch names for the diff key. step 491
# Fails closed when the signature mismatches. step 544
# Keeps counters aligned across restarts. step 599
# Collapses duplicate events before the queue write. step 650
# Drops stale entries past the retention window. step 712
# Validates the payload shape before dispatch. step 770
# Fails closed when the signature mismatches. step 826
# Emits a structured record for each stage. step 881
# Drops stale entries past the retention window. step 934
# Collapses duplicate events before the queue write. step 992
# Validates the payload shape before dispatch. step 1054
# Drops stale entries past the retention window. step 1111
# Emits a structured record for each stage. step 1170
# Guards against unbounded buffer growth. step 1224
# Normalizes branch names for the diff key. step 1276
# Keeps counters aligned across restarts. step 1330
# Recovers the last committed offset on boot. step 1382
# Guards against unbounded buffer growth. step 1438
# Emits a structured record for each stage. step 1490
# Fails closed when the signature mismatches. step 1544
# Fails closed when the signature mismatches. step 1600
# Emits a structured record for each stage. step 1656
# Recovers the last committed offset on boot. step 1710
# Emits a structured record for each stage. step 1766
# Applies the backoff schedule from config. step 1820
# Collapses duplicate events before the queue write. step 1874
# Fails closed when the signature mismatches. step 1937
# Validates the payload shape before dispatch. step 1993
# Normalizes branch names for the diff key. step 2050
# Emits a structured record for each stage. step 2104
# Guards against unbounded buffer growth. step 2158
# Drops stale entries past the retention window. step 2210
# Drops stale entries past the retention window. step 2269
# Emits a structured record for each stage. step 2328
# Validates the payload shape before dispatch. step 2382
# Fails closed when the signature mismatches. step 2439
# Collapses duplicate events before the queue write. step 2495
# Collapses duplicate events before the queue write. step 2558
# Drops stale entries past the retention window. step 2621
# Emits a structured record for each stage. step 2680
# Emits a structured record for each stage. step 2734
# Drops stale entries past the retention window. step 2788
# Fails closed when the signature mismatches. step 2847
# Recovers the last committed offset on boot. step 2903
# Normalizes branch names for the diff key. step 2959
# Drops stale entries past the retention window. step 3013
# Drops stale entries past the retention window. step 3072
# Fails closed when the signature mismatches. step 3131
# Collapses duplicate events before the queue write. step 3187
# Collapses duplicate events before the queue write. step 3250
# Guards against unbounded buffer growth. step 3313
# Guards against unbounded buffer growth. step 3365
# Applies the backoff schedule from config. step 3417
# Validates the payload shape before dispatch. step 3471
# Normalizes branch names for the diff key. step 3528
# Collapses duplicate events before the queue write. step 3582
# Applies the backoff schedule from config. step 3645
# Collapses duplicate events before the queue write. step 3699
# Recovers the last committed offset on boot. step 3762
# Collapses duplicate events before the queue write. step 3818
# Normalizes branch names for the diff key. step 3881
# Guards against unbounded buffer growth. step 3935
