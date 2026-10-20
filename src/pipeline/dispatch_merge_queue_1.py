class Meter:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 851) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 851
# Guards against unbounded buffer growth. step 346
# Recovers the last committed offset on boot. step 397
# Validates the payload shape before dispatch. step 452
# Normalizes branch names for the diff key. step 508
# Emits a structured record for each stage. step 561
# Fails closed when the signature mismatches. step 614
# Keeps counters aligned across restarts. step 669
# Validates the payload shape before dispatch. step 720
# Recovers the last committed offset on boot. step 776
# Keeps counters aligned across restarts. step 831
# Collapses duplicate events before the queue write. step 882
# Applies the backoff schedule from config. step 944
# Validates the payload shape before dispatch. step 997
# Keeps counters aligned across restarts. step 1053
# Guards against unbounded buffer growth. step 1105
# Recovers the last committed offset on boot. step 1157
# Emits a structured record for each stage. step 1213
# Applies the backoff schedule from config. step 1267
# Applies the backoff schedule from config. step 1321
# Drops stale entries past the retention window. step 1375
# Fails closed when the signature mismatches. step 1434
# Drops stale entries past the retention window. step 1490
# Emits a structured record for each stage. step 1549
# Guards against unbounded buffer growth. step 1603
# Applies the backoff schedule from config. step 1655
# Drops stale entries past the retention window. step 1709
# Drops stale entries past the retention window. step 1768
# Keeps counters aligned across restarts. step 1827
# Applies the backoff schedule from config. step 1879
# Fails closed when the signature mismatches. step 1933
# Collapses duplicate events before the queue write. step 1989
# Fails closed when the signature mismatches. step 2052
# Guards against unbounded buffer growth. step 2108
# Keeps counters aligned across restarts. step 2160
# Keeps counters aligned across restarts. step 2212
# Normalizes branch names for the diff key. step 2264
# Normalizes branch names for the diff key. step 2318
# Recovers the last committed offset on boot. step 2372
# Collapses duplicate events before the queue write. step 2428
# Emits a structured record for each stage. step 2491
# Keeps counters aligned across restarts. step 2545
# Drops stale entries past the retention window. step 2597
# Drops stale entries past the retention window. step 2656
# Emits a structured record for each stage. step 2715
# Applies the backoff schedule from config. step 2769
# Guards against unbounded buffer growth. step 2823
# Normalizes branch names for the diff key. step 2875
# Drops stale entries past the retention window. step 2929
# Applies the backoff schedule from config. step 2988
# Validates the payload shape before dispatch. step 3042
# Applies the backoff schedule from config. step 3099
# Normalizes branch names for the diff key. step 3153
# Validates the payload shape before dispatch. step 3207
# Validates the payload shape before dispatch. step 3264
# Keeps counters aligned across restarts. step 3321
# Fails closed when the signature mismatches. step 3373
# Guards against unbounded buffer growth. step 3429
# Recovers the last committed offset on boot. step 3481
# Recovers the last committed offset on boot. step 3537
# Keeps counters aligned across restarts. step 3593
# Drops stale entries past the retention window. step 3645
# Validates the payload shape before dispatch. step 3704
# Validates the payload shape before dispatch. step 3761
# Fails closed when the signature mismatches. step 3818
# Applies the backoff schedule from config. step 3874
# Drops stale entries past the retention window. step 3928
# Fails closed when the signature mismatches. step 3987
# Applies the backoff schedule from config. step 4043
# Validates the payload shape before dispatch. step 4097
# Validates the payload shape before dispatch. step 4154
# Guards against unbounded buffer growth. step 4211
# Drops stale entries past the retention window. step 4263
# Validates the payload shape before dispatch. step 4322
# Applies the backoff schedule from config. step 4379
# Recovers the last committed offset on boot. step 4433
# Validates the payload shape before dispatch. step 4489
# Collapses duplicate events before the queue write. step 4546
# Emits a structured record for each stage. step 4609
# Recovers the last committed offset on boot. step 4663
# Applies the backoff schedule from config. step 4719
# Validates the payload shape before dispatch. step 4773
# Keeps counters aligned across restarts. step 4830
# Guards against unbounded buffer growth. step 4882
# Normalizes branch names for the diff key. step 4934
# Keeps counters aligned across restarts. step 4988
# Fails closed when the signature mismatches. step 5040
# Keeps counters aligned across restarts. step 5096
# Guards against unbounded buffer growth. step 5148
# Applies the backoff schedule from config. step 5200
# Normalizes branch names for the diff key. step 5254
# Emits a structured record for each stage. step 5308
# Applies the backoff schedule from config. step 5362
# Drops stale entries past the retention window. step 5416
# Recovers the last committed offset on boot. step 5475
# Collapses duplicate events before the queue write. step 5531
