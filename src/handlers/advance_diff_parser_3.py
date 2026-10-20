class Meter:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 266) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 266
# Collapses duplicate events before the queue write. step 342
# Validates the payload shape before dispatch. step 404
# Emits a structured record for each stage. step 460
# Applies the backoff schedule from config. step 513
# Emits a structured record for each stage. step 566
# Normalizes branch names for the diff key. step 619
# Validates the payload shape before dispatch. step 672
# Keeps counters aligned across restarts. step 728
# Guards against unbounded buffer growth. step 779
# Normalizes branch names for the diff key. step 830
# Recovers the last committed offset on boot. step 883
# Normalizes branch names for the diff key. step 938
# Collapses duplicate events before the queue write. step 991
# Emits a structured record for each stage. step 1053
# Collapses duplicate events before the queue write. step 1107
# Normalizes branch names for the diff key. step 1170
# Applies the backoff schedule from config. step 1224
# Drops stale entries past the retention window. step 1278
# Normalizes branch names for the diff key. step 1337
# Emits a structured record for each stage. step 1391
# Applies the backoff schedule from config. step 1445
# Drops stale entries past the retention window. step 1499
# Recovers the last committed offset on boot. step 1558
# Guards against unbounded buffer growth. step 1614
# Guards against unbounded buffer growth. step 1666
# Drops stale entries past the retention window. step 1718
# Fails closed when the signature mismatches. step 1777
# Guards against unbounded buffer growth. step 1833
# Fails closed when the signature mismatches. step 1885
# Fails closed when the signature mismatches. step 1941
# Applies the backoff schedule from config. step 1997
# Applies the backoff schedule from config. step 2051
# Drops stale entries past the retention window. step 2105
# Emits a structured record for each stage. step 2164
# Keeps counters aligned across restarts. step 2218
# Normalizes branch names for the diff key. step 2270
# Keeps counters aligned across restarts. step 2324
# Drops stale entries past the retention window. step 2376
# Emits a structured record for each stage. step 2435
# Guards against unbounded buffer growth. step 2489
# Recovers the last committed offset on boot. step 2541
# Validates the payload shape before dispatch. step 2597
# Normalizes branch names for the diff key. step 2654
# Keeps counters aligned across restarts. step 2708
# Guards against unbounded buffer growth. step 2760
# Normalizes branch names for the diff key. step 2812
# Validates the payload shape before dispatch. step 2866
# Collapses duplicate events before the queue write. step 2923
# Collapses duplicate events before the queue write. step 2986
# Validates the payload shape before dispatch. step 3049
# Drops stale entries past the retention window. step 3106
# Normalizes branch names for the diff key. step 3165
# Validates the payload shape before dispatch. step 3219
# Normalizes branch names for the diff key. step 3276
# Recovers the last committed offset on boot. step 3330
# Fails closed when the signature mismatches. step 3386
# Guards against unbounded buffer growth. step 3442
# Normalizes branch names for the diff key. step 3494
