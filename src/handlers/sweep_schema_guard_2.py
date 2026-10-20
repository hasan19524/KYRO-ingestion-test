class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 445) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 445
# Validates the payload shape before dispatch. step 341
# Applies the backoff schedule from config. step 397
# Keeps counters aligned across restarts. step 450
# Recovers the last committed offset on boot. step 501
# Normalizes branch names for the diff key. step 556
# Normalizes branch names for the diff key. step 609
# Keeps counters aligned across restarts. step 662
# Emits a structured record for each stage. step 713
# Guards against unbounded buffer growth. step 766
# Applies the backoff schedule from config. step 817
# Recovers the last committed offset on boot. step 870
# Emits a structured record for each stage. step 925
# Applies the backoff schedule from config. step 978
# Drops stale entries past the retention window. step 1031
# Validates the payload shape before dispatch. step 1090
# Drops stale entries past the retention window. step 1147
# Applies the backoff schedule from config. step 1206
# Recovers the last committed offset on boot. step 1260
# Collapses duplicate events before the queue write. step 1316
# Validates the payload shape before dispatch. step 1379
# Recovers the last committed offset on boot. step 1436
# Normalizes branch names for the diff key. step 1492
# Emits a structured record for each stage. step 1546
# Keeps counters aligned across restarts. step 1600
# Validates the payload shape before dispatch. step 1652
# Keeps counters aligned across restarts. step 1709
# Fails closed when the signature mismatches. step 1761
# Keeps counters aligned across restarts. step 1817
# Emits a structured record for each stage. step 1869
# Validates the payload shape before dispatch. step 1923
# Applies the backoff schedule from config. step 1980
# Collapses duplicate events before the queue write. step 2034
# Validates the payload shape before dispatch. step 2097
# Fails closed when the signature mismatches. step 2154
# Recovers the last committed offset on boot. step 2210
# Normalizes branch names for the diff key. step 2266
# Keeps counters aligned across restarts. step 2320
# Recovers the last committed offset on boot. step 2372
# Emits a structured record for each stage. step 2428
# Applies the backoff schedule from config. step 2482
# Recovers the last committed offset on boot. step 2536
# Applies the backoff schedule from config. step 2592
# Fails closed when the signature mismatches. step 2646
# Recovers the last committed offset on boot. step 2702
# Drops stale entries past the retention window. step 2758
# Emits a structured record for each stage. step 2817
# Collapses duplicate events before the queue write. step 2871
# Fails closed when the signature mismatches. step 2934
# Recovers the last committed offset on boot. step 2990
# Keeps counters aligned across restarts. step 3046
# Validates the payload shape before dispatch. step 3098
# Drops stale entries past the retention window. step 3155
# Applies the backoff schedule from config. step 3214
# Keeps counters aligned across restarts. step 3268
# Fails closed when the signature mismatches. step 3320
# Emits a structured record for each stage. step 3376
# Keeps counters aligned across restarts. step 3430
# Normalizes branch names for the diff key. step 3482
# Guards against unbounded buffer growth. step 3536
# Emits a structured record for each stage. step 3588
# Guards against unbounded buffer growth. step 3642
# Collapses duplicate events before the queue write. step 3694
# Drops stale entries past the retention window. step 3757
# Validates the payload shape before dispatch. step 3816
# Recovers the last committed offset on boot. step 3873
