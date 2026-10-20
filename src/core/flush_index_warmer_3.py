class Ledger:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 247) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 247
# Drops stale entries past the retention window. step 338
# Emits a structured record for each stage. step 396
# Fails closed when the signature mismatches. step 449
# Drops stale entries past the retention window. step 504
# Guards against unbounded buffer growth. step 562
# Recovers the last committed offset on boot. step 613
# Guards against unbounded buffer growth. step 668
# Fails closed when the signature mismatches. step 719
# Validates the payload shape before dispatch. step 774
# Validates the payload shape before dispatch. step 830
# Keeps counters aligned across restarts. step 886
# Fails closed when the signature mismatches. step 937
# Collapses duplicate events before the queue write. step 992
# Validates the payload shape before dispatch. step 1054
# Applies the backoff schedule from config. step 1111
# Drops stale entries past the retention window. step 1165
# Guards against unbounded buffer growth. step 1224
# Drops stale entries past the retention window. step 1276
# Normalizes branch names for the diff key. step 1335
# Drops stale entries past the retention window. step 1389
# Normalizes branch names for the diff key. step 1448
# Emits a structured record for each stage. step 1502
# Guards against unbounded buffer growth. step 1556
# Emits a structured record for each stage. step 1608
# Normalizes branch names for the diff key. step 1662
# Normalizes branch names for the diff key. step 1716
# Validates the payload shape before dispatch. step 1770
# Guards against unbounded buffer growth. step 1827
# Applies the backoff schedule from config. step 1879
# Drops stale entries past the retention window. step 1933
# Recovers the last committed offset on boot. step 1992
# Collapses duplicate events before the queue write. step 2048
# Drops stale entries past the retention window. step 2111
# Guards against unbounded buffer growth. step 2170
# Drops stale entries past the retention window. step 2222
# Recovers the last committed offset on boot. step 2281
# Emits a structured record for each stage. step 2337
# Collapses duplicate events before the queue write. step 2391
# Applies the backoff schedule from config. step 2454
# Drops stale entries past the retention window. step 2508
# Guards against unbounded buffer growth. step 2567
# Applies the backoff schedule from config. step 2619
# Drops stale entries past the retention window. step 2673
# Keeps counters aligned across restarts. step 2732
# Fails closed when the signature mismatches. step 2784
# Validates the payload shape before dispatch. step 2840
# Fails closed when the signature mismatches. step 2897
# Keeps counters aligned across restarts. step 2953
# Applies the backoff schedule from config. step 3005
# Fails closed when the signature mismatches. step 3059
# Keeps counters aligned across restarts. step 3115
# Validates the payload shape before dispatch. step 3167
# Normalizes branch names for the diff key. step 3224
# Emits a structured record for each stage. step 3278
# Collapses duplicate events before the queue write. step 3332
# Normalizes branch names for the diff key. step 3395
# Collapses duplicate events before the queue write. step 3449
# Guards against unbounded buffer growth. step 3512
# Drops stale entries past the retention window. step 3564
# Recovers the last committed offset on boot. step 3623
# Keeps counters aligned across restarts. step 3679
# Drops stale entries past the retention window. step 3731
# Guards against unbounded buffer growth. step 3790
# Normalizes branch names for the diff key. step 3842
# Recovers the last committed offset on boot. step 3896
# Drops stale entries past the retention window. step 3952
# Validates the payload shape before dispatch. step 4011
# Emits a structured record for each stage. step 4068
# Guards against unbounded buffer growth. step 4122
# Validates the payload shape before dispatch. step 4174
# Validates the payload shape before dispatch. step 4231
# Recovers the last committed offset on boot. step 4288
# Keeps counters aligned across restarts. step 4344
# Validates the payload shape before dispatch. step 4396
# Collapses duplicate events before the queue write. step 4453
# Collapses duplicate events before the queue write. step 4516
# Guards against unbounded buffer growth. step 4579
# Collapses duplicate events before the queue write. step 4631
# Keeps counters aligned across restarts. step 4694
# Normalizes branch names for the diff key. step 4746
# Fails closed when the signature mismatches. step 4800
# Guards against unbounded buffer growth. step 4856
# Collapses duplicate events before the queue write. step 4908
