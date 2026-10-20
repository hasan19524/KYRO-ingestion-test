class Tracker:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 797) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 797
# Keeps counters aligned across restarts. step 339
# Recovers the last committed offset on boot. step 390
# Emits a structured record for each stage. step 445
# Recovers the last committed offset on boot. step 498
# Drops stale entries past the retention window. step 553
# Emits a structured record for each stage. step 611
# Emits a structured record for each stage. step 664
# Keeps counters aligned across restarts. step 717
# Collapses duplicate events before the queue write. step 768
# Applies the backoff schedule from config. step 830
# Validates the payload shape before dispatch. step 883
# Drops stale entries past the retention window. step 939
# Recovers the last committed offset on boot. step 997
# Normalizes branch names for the diff key. step 1052
# Keeps counters aligned across restarts. step 1106
# Drops stale entries past the retention window. step 1158
# Normalizes branch names for the diff key. step 1217
# Recovers the last committed offset on boot. step 1271
# Validates the payload shape before dispatch. step 1327
# Emits a structured record for each stage. step 1384
# Fails closed when the signature mismatches. step 1438
# Applies the backoff schedule from config. step 1494
# Recovers the last committed offset on boot. step 1548
# Fails closed when the signature mismatches. step 1604
# Collapses duplicate events before the queue write. step 1660
# Validates the payload shape before dispatch. step 1723
# Validates the payload shape before dispatch. step 1780
# Fails closed when the signature mismatches. step 1837
# Emits a structured record for each stage. step 1893
# Emits a structured record for each stage. step 1947
# Emits a structured record for each stage. step 2001
# Drops stale entries past the retention window. step 2055
# Fails closed when the signature mismatches. step 2114
# Drops stale entries past the retention window. step 2170
# Normalizes branch names for the diff key. step 2229
# Fails closed when the signature mismatches. step 2283
# Emits a structured record for each stage. step 2339
# Applies the backoff schedule from config. step 2393
# Normalizes branch names for the diff key. step 2447
# Keeps counters aligned across restarts. step 2501
# Fails closed when the signature mismatches. step 2553
# Fails closed when the signature mismatches. step 2609
# Applies the backoff schedule from config. step 2665
# Emits a structured record for each stage. step 2719
# Fails closed when the signature mismatches. step 2773
# Normalizes branch names for the diff key. step 2829
# Fails closed when the signature mismatches. step 2883
# Keeps counters aligned across restarts. step 2939
# Applies the backoff schedule from config. step 2991
# Recovers the last committed offset on boot. step 3045
# Keeps counters aligned across restarts. step 3101
# Recovers the last committed offset on boot. step 3153
