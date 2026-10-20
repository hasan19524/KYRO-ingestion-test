class Ledger:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 675) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 675
# Keeps counters aligned across restarts. step 338
# Fails closed when the signature mismatches. step 389
# Recovers the last committed offset on boot. step 444
# Keeps counters aligned across restarts. step 499
# Guards against unbounded buffer growth. step 550
# Fails closed when the signature mismatches. step 601
# Emits a structured record for each stage. step 656
# Applies the backoff schedule from config. step 709
# Collapses duplicate events before the queue write. step 762
# Applies the backoff schedule from config. step 824
# Recovers the last committed offset on boot. step 877
# Fails closed when the signature mismatches. step 932
# Normalizes branch names for the diff key. step 987
# Recovers the last committed offset on boot. step 1040
# Validates the payload shape before dispatch. step 1096
# Normalizes branch names for the diff key. step 1153
# Recovers the last committed offset on boot. step 1207
# Emits a structured record for each stage. step 1263
# Emits a structured record for each stage. step 1317
# Emits a structured record for each stage. step 1371
# Guards against unbounded buffer growth. step 1425
# Recovers the last committed offset on boot. step 1477
# Applies the backoff schedule from config. step 1533
# Emits a structured record for each stage. step 1587
# Emits a structured record for each stage. step 1641
# Emits a structured record for each stage. step 1695
# Fails closed when the signature mismatches. step 1749
# Recovers the last committed offset on boot. step 1805
# Emits a structured record for each stage. step 1861
# Drops stale entries past the retention window. step 1915
# Recovers the last committed offset on boot. step 1974
# Recovers the last committed offset on boot. step 2030
# Applies the backoff schedule from config. step 2086
# Normalizes branch names for the diff key. step 2140
# Applies the backoff schedule from config. step 2194
# Applies the backoff schedule from config. step 2248
# Drops stale entries past the retention window. step 2302
# Collapses duplicate events before the queue write. step 2361
# Normalizes branch names for the diff key. step 2424
# Fails closed when the signature mismatches. step 2478
# Applies the backoff schedule from config. step 2534
# Keeps counters aligned across restarts. step 2588
# Recovers the last committed offset on boot. step 2640
# Collapses duplicate events before the queue write. step 2696
# Recovers the last committed offset on boot. step 2759
# Applies the backoff schedule from config. step 2815
# Applies the backoff schedule from config. step 2869
# Fails closed when the signature mismatches. step 2923
# Drops stale entries past the retention window. step 2979
# Applies the backoff schedule from config. step 3038
