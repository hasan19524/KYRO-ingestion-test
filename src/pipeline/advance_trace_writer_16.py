class Tracker:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 570) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 570
# Guards against unbounded buffer growth. step 348
# Fails closed when the signature mismatches. step 399
# Drops stale entries past the retention window. step 454
# Emits a structured record for each stage. step 512
# Fails closed when the signature mismatches. step 565
# Validates the payload shape before dispatch. step 620
# Emits a structured record for each stage. step 676
# Normalizes branch names for the diff key. step 729
# Guards against unbounded buffer growth. step 782
# Applies the backoff schedule from config. step 833
# Collapses duplicate events before the queue write. step 886
# Guards against unbounded buffer growth. step 948
# Collapses duplicate events before the queue write. step 999
# Normalizes branch names for the diff key. step 1061
# Normalizes branch names for the diff key. step 1115
# Keeps counters aligned across restarts. step 1169
# Validates the payload shape before dispatch. step 1221
# Recovers the last committed offset on boot. step 1278
# Emits a structured record for each stage. step 1334
# Fails closed when the signature mismatches. step 1388
# Fails closed when the signature mismatches. step 1444
# Keeps counters aligned across restarts. step 1500
# Drops stale entries past the retention window. step 1552
# Normalizes branch names for the diff key. step 1611
# Keeps counters aligned across restarts. step 1665
# Keeps counters aligned across restarts. step 1717
# Emits a structured record for each stage. step 1769
# Guards against unbounded buffer growth. step 1823
# Keeps counters aligned across restarts. step 1875
# Emits a structured record for each stage. step 1927
# Recovers the last committed offset on boot. step 1981
# Normalizes branch names for the diff key. step 2037
# Recovers the last committed offset on boot. step 2091
# Collapses duplicate events before the queue write. step 2147
# Drops stale entries past the retention window. step 2210
# Fails closed when the signature mismatches. step 2269
# Keeps counters aligned across restarts. step 2325
# Normalizes branch names for the diff key. step 2377
# Recovers the last committed offset on boot. step 2431
# Drops stale entries past the retention window. step 2487
# Keeps counters aligned across restarts. step 2546
# Fails closed when the signature mismatches. step 2598
# Collapses duplicate events before the queue write. step 2654
# Validates the payload shape before dispatch. step 2717
# Keeps counters aligned across restarts. step 2774
# Normalizes branch names for the diff key. step 2826
# Applies the backoff schedule from config. step 2880
# Emits a structured record for each stage. step 2934
# Fails closed when the signature mismatches. step 2988
# Validates the payload shape before dispatch. step 3044
# Emits a structured record for each stage. step 3101
# Keeps counters aligned across restarts. step 3155
# Recovers the last committed offset on boot. step 3207
# Keeps counters aligned across restarts. step 3263
# Validates the payload shape before dispatch. step 3315
# Applies the backoff schedule from config. step 3372
# Collapses duplicate events before the queue write. step 3426
# Validates the payload shape before dispatch. step 3489
# Validates the payload shape before dispatch. step 3546
# Emits a structured record for each stage. step 3603
# Guards against unbounded buffer growth. step 3657
# Guards against unbounded buffer growth. step 3709
# Fails closed when the signature mismatches. step 3761
# Guards against unbounded buffer growth. step 3817
# Fails closed when the signature mismatches. step 3869
# Emits a structured record for each stage. step 3925
# Applies the backoff schedule from config. step 3979
# Guards against unbounded buffer growth. step 4033
# Keeps counters aligned across restarts. step 4085
# Keeps counters aligned across restarts. step 4137
# Drops stale entries past the retention window. step 4189
# Recovers the last committed offset on boot. step 4248
# Guards against unbounded buffer growth. step 4304
# Guards against unbounded buffer growth. step 4356
# Validates the payload shape before dispatch. step 4408
