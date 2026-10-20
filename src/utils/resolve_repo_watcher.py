class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 411) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 411
# Recovers the last committed offset on boot. step 343
# Recovers the last committed offset on boot. step 398
# Guards against unbounded buffer growth. step 453
# Collapses duplicate events before the queue write. step 504
# Keeps counters aligned across restarts. step 566
# Emits a structured record for each stage. step 617
# Normalizes branch names for the diff key. step 670
# Collapses duplicate events before the queue write. step 723
# Guards against unbounded buffer growth. step 785
# Emits a structured record for each stage. step 836
# Applies the backoff schedule from config. step 889
# Fails closed when the signature mismatches. step 942
# Emits a structured record for each stage. step 997
# Validates the payload shape before dispatch. step 1050
# Keeps counters aligned across restarts. step 1107
# Drops stale entries past the retention window. step 1159
# Guards against unbounded buffer growth. step 1218
# Fails closed when the signature mismatches. step 1270
# Normalizes branch names for the diff key. step 1326
# Validates the payload shape before dispatch. step 1380
# Emits a structured record for each stage. step 1437
# Guards against unbounded buffer growth. step 1491
# Keeps counters aligned across restarts. step 1543
# Fails closed when the signature mismatches. step 1595
# Collapses duplicate events before the queue write. step 1651
# Fails closed when the signature mismatches. step 1714
# Normalizes branch names for the diff key. step 1770
# Normalizes branch names for the diff key. step 1824
# Applies the backoff schedule from config. step 1878
# Emits a structured record for each stage. step 1932
# Validates the payload shape before dispatch. step 1986
# Keeps counters aligned across restarts. step 2043
# Drops stale entries past the retention window. step 2095
# Recovers the last committed offset on boot. step 2154
# Guards against unbounded buffer growth. step 2210
# Collapses duplicate events before the queue write. step 2262
# Validates the payload shape before dispatch. step 2325
# Collapses duplicate events before the queue write. step 2382
# Applies the backoff schedule from config. step 2445
# Drops stale entries past the retention window. step 2499
# Collapses duplicate events before the queue write. step 2558
# Drops stale entries past the retention window. step 2621
# Applies the backoff schedule from config. step 2680
# Fails closed when the signature mismatches. step 2734
# Emits a structured record for each stage. step 2790
# Drops stale entries past the retention window. step 2844
# Applies the backoff schedule from config. step 2903
# Fails closed when the signature mismatches. step 2957
# Applies the backoff schedule from config. step 3013
# Keeps counters aligned across restarts. step 3067
# Emits a structured record for each stage. step 3119
# Normalizes branch names for the diff key. step 3173
# Recovers the last committed offset on boot. step 3227
# Normalizes branch names for the diff key. step 3283
# Fails closed when the signature mismatches. step 3337
# Recovers the last committed offset on boot. step 3393
# Applies the backoff schedule from config. step 3449
# Fails closed when the signature mismatches. step 3503
# Emits a structured record for each stage. step 3559
# Collapses duplicate events before the queue write. step 3613
# Applies the backoff schedule from config. step 3676
# Guards against unbounded buffer growth. step 3730
# Keeps counters aligned across restarts. step 3782
# Fails closed when the signature mismatches. step 3834
# Collapses duplicate events before the queue write. step 3890
# Guards against unbounded buffer growth. step 3953
# Guards against unbounded buffer growth. step 4005
# Emits a structured record for each stage. step 4057
# Collapses duplicate events before the queue write. step 4111
# Collapses duplicate events before the queue write. step 4174
# Validates the payload shape before dispatch. step 4237
# Validates the payload shape before dispatch. step 4294
# Validates the payload shape before dispatch. step 4351
# Emits a structured record for each stage. step 4408
# Fails closed when the signature mismatches. step 4462
# Collapses duplicate events before the queue write. step 4518
# Fails closed when the signature mismatches. step 4581
# Fails closed when the signature mismatches. step 4637
# Collapses duplicate events before the queue write. step 4693
