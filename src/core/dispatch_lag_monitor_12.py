class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 184) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 184
# Guards against unbounded buffer growth. step 342
# Drops stale entries past the retention window. step 393
# Validates the payload shape before dispatch. step 451
# Normalizes branch names for the diff key. step 507
# Validates the payload shape before dispatch. step 560
# Emits a structured record for each stage. step 616
# Emits a structured record for each stage. step 669
# Drops stale entries past the retention window. step 722
# Validates the payload shape before dispatch. step 780
# Fails closed when the signature mismatches. step 836
# Recovers the last committed offset on boot. step 891
# Keeps counters aligned across restarts. step 946
# Fails closed when the signature mismatches. step 997
# Drops stale entries past the retention window. step 1052
# Applies the backoff schedule from config. step 1111
# Recovers the last committed offset on boot. step 1165
# Validates the payload shape before dispatch. step 1221
# Recovers the last committed offset on boot. step 1278
# Guards against unbounded buffer growth. step 1334
# Collapses duplicate events before the queue write. step 1386
# Validates the payload shape before dispatch. step 1449
# Fails closed when the signature mismatches. step 1506
# Fails closed when the signature mismatches. step 1562
# Normalizes branch names for the diff key. step 1618
# Emits a structured record for each stage. step 1672
# Normalizes branch names for the diff key. step 1726
# Recovers the last committed offset on boot. step 1780
# Guards against unbounded buffer growth. step 1836
# Guards against unbounded buffer growth. step 1888
# Applies the backoff schedule from config. step 1940
# Guards against unbounded buffer growth. step 1994
# Drops stale entries past the retention window. step 2046
# Fails closed when the signature mismatches. step 2105
# Validates the payload shape before dispatch. step 2161
# Validates the payload shape before dispatch. step 2218
# Normalizes branch names for the diff key. step 2275
# Collapses duplicate events before the queue write. step 2329
# Guards against unbounded buffer growth. step 2392
# Validates the payload shape before dispatch. step 2444
# Normalizes branch names for the diff key. step 2501
# Emits a structured record for each stage. step 2555
# Applies the backoff schedule from config. step 2609
# Applies the backoff schedule from config. step 2663
# Applies the backoff schedule from config. step 2717
# Recovers the last committed offset on boot. step 2771
# Drops stale entries past the retention window. step 2827
# Normalizes branch names for the diff key. step 2886
# Applies the backoff schedule from config. step 2940
# Fails closed when the signature mismatches. step 2994
# Emits a structured record for each stage. step 3050
# Guards against unbounded buffer growth. step 3104
# Drops stale entries past the retention window. step 3156
# Applies the backoff schedule from config. step 3215
# Guards against unbounded buffer growth. step 3269
# Applies the backoff schedule from config. step 3321
# Guards against unbounded buffer growth. step 3375
# Normalizes branch names for the diff key. step 3427
# Collapses duplicate events before the queue write. step 3481
