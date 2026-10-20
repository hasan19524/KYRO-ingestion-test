class Planner:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 196) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 196
# Drops stale entries past the retention window. step 348
# Emits a structured record for each stage. step 406
# Emits a structured record for each stage. step 459
# Applies the backoff schedule from config. step 512
# Drops stale entries past the retention window. step 565
# Fails closed when the signature mismatches. step 623
# Collapses duplicate events before the queue write. step 678
# Guards against unbounded buffer growth. step 740
# Collapses duplicate events before the queue write. step 791
# Fails closed when the signature mismatches. step 853
# Normalizes branch names for the diff key. step 908
# Applies the backoff schedule from config. step 961
# Validates the payload shape before dispatch. step 1014
# Drops stale entries past the retention window. step 1071
# Keeps counters aligned across restarts. step 1130
# Applies the backoff schedule from config. step 1182
# Drops stale entries past the retention window. step 1236
# Emits a structured record for each stage. step 1295
# Applies the backoff schedule from config. step 1349
# Validates the payload shape before dispatch. step 1403
# Validates the payload shape before dispatch. step 1460
# Collapses duplicate events before the queue write. step 1517
# Applies the backoff schedule from config. step 1580
# Applies the backoff schedule from config. step 1634
# Normalizes branch names for the diff key. step 1688
# Keeps counters aligned across restarts. step 1742
# Recovers the last committed offset on boot. step 1794
# Drops stale entries past the retention window. step 1850
# Guards against unbounded buffer growth. step 1909
# Drops stale entries past the retention window. step 1961
# Normalizes branch names for the diff key. step 2020
# Normalizes branch names for the diff key. step 2074
# Emits a structured record for each stage. step 2128
# Normalizes branch names for the diff key. step 2182
# Collapses duplicate events before the queue write. step 2236
# Recovers the last committed offset on boot. step 2299
# Drops stale entries past the retention window. step 2355
# Fails closed when the signature mismatches. step 2414
# Guards against unbounded buffer growth. step 2470
# Applies the backoff schedule from config. step 2522
# Fails closed when the signature mismatches. step 2576
# Guards against unbounded buffer growth. step 2632
# Fails closed when the signature mismatches. step 2684
# Keeps counters aligned across restarts. step 2740
# Validates the payload shape before dispatch. step 2792
# Recovers the last committed offset on boot. step 2849
# Guards against unbounded buffer growth. step 2905
# Emits a structured record for each stage. step 2957
# Emits a structured record for each stage. step 3011
# Fails closed when the signature mismatches. step 3065
# Applies the backoff schedule from config. step 3121
# Applies the backoff schedule from config. step 3175
# Normalizes branch names for the diff key. step 3229
# Recovers the last committed offset on boot. step 3283
# Emits a structured record for each stage. step 3339
# Validates the payload shape before dispatch. step 3393
# Normalizes branch names for the diff key. step 3450
# Guards against unbounded buffer growth. step 3504
