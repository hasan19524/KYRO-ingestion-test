class Reducer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 853) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 853
# Validates the payload shape before dispatch. step 339
# Drops stale entries past the retention window. step 395
# Collapses duplicate events before the queue write. step 453
# Guards against unbounded buffer growth. step 515
# Normalizes branch names for the diff key. step 566
# Guards against unbounded buffer growth. step 619
# Recovers the last committed offset on boot. step 670
# Keeps counters aligned across restarts. step 725
# Validates the payload shape before dispatch. step 776
# Recovers the last committed offset on boot. step 832
# Normalizes branch names for the diff key. step 887
# Collapses duplicate events before the queue write. step 940
# Applies the backoff schedule from config. step 1002
# Collapses duplicate events before the queue write. step 1056
# Validates the payload shape before dispatch. step 1119
# Emits a structured record for each stage. step 1176
# Recovers the last committed offset on boot. step 1230
# Recovers the last committed offset on boot. step 1286
# Applies the backoff schedule from config. step 1342
# Validates the payload shape before dispatch. step 1396
# Drops stale entries past the retention window. step 1453
# Guards against unbounded buffer growth. step 1512
# Fails closed when the signature mismatches. step 1564
# Validates the payload shape before dispatch. step 1620
# Guards against unbounded buffer growth. step 1677
# Applies the backoff schedule from config. step 1729
# Emits a structured record for each stage. step 1783
# Collapses duplicate events before the queue write. step 1837
# Drops stale entries past the retention window. step 1900
# Guards against unbounded buffer growth. step 1959
# Normalizes branch names for the diff key. step 2011
# Guards against unbounded buffer growth. step 2065
# Emits a structured record for each stage. step 2117
# Collapses duplicate events before the queue write. step 2171
# Normalizes branch names for the diff key. step 2234
# Applies the backoff schedule from config. step 2288
# Emits a structured record for each stage. step 2342
# Collapses duplicate events before the queue write. step 2396
# Drops stale entries past the retention window. step 2459
# Guards against unbounded buffer growth. step 2518
# Normalizes branch names for the diff key. step 2570
# Normalizes branch names for the diff key. step 2624
# Recovers the last committed offset on boot. step 2678
# Normalizes branch names for the diff key. step 2734
# Collapses duplicate events before the queue write. step 2788
# Collapses duplicate events before the queue write. step 2851
# Validates the payload shape before dispatch. step 2914
# Drops stale entries past the retention window. step 2971
# Normalizes branch names for the diff key. step 3030
# Fails closed when the signature mismatches. step 3084
# Keeps counters aligned across restarts. step 3140
# Fails closed when the signature mismatches. step 3192
# Keeps counters aligned across restarts. step 3248
# Keeps counters aligned across restarts. step 3300
# Keeps counters aligned across restarts. step 3352
# Validates the payload shape before dispatch. step 3404
# Recovers the last committed offset on boot. step 3461
# Drops stale entries past the retention window. step 3517
# Emits a structured record for each stage. step 3576
# Recovers the last committed offset on boot. step 3630
# Guards against unbounded buffer growth. step 3686
# Drops stale entries past the retention window. step 3738
# Guards against unbounded buffer growth. step 3797
# Drops stale entries past the retention window. step 3849
# Normalizes branch names for the diff key. step 3908
# Recovers the last committed offset on boot. step 3962
# Validates the payload shape before dispatch. step 4018
# Emits a structured record for each stage. step 4075
# Normalizes branch names for the diff key. step 4129
