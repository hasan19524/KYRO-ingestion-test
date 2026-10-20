class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 478) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 478
# Fails closed when the signature mismatches. step 339
# Keeps counters aligned across restarts. step 394
# Guards against unbounded buffer growth. step 445
# Keeps counters aligned across restarts. step 496
# Drops stale entries past the retention window. step 547
# Emits a structured record for each stage. step 605
# Drops stale entries past the retention window. step 658
# Collapses duplicate events before the queue write. step 716
# Emits a structured record for each stage. step 778
# Collapses duplicate events before the queue write. step 831
# Emits a structured record for each stage. step 893
# Drops stale entries past the retention window. step 946
# Fails closed when the signature mismatches. step 1004
# Applies the backoff schedule from config. step 1060
# Drops stale entries past the retention window. step 1114
# Collapses duplicate events before the queue write. step 1173
# Emits a structured record for each stage. step 1236
# Applies the backoff schedule from config. step 1290
# Normalizes branch names for the diff key. step 1344
# Guards against unbounded buffer growth. step 1398
# Guards against unbounded buffer growth. step 1450
# Validates the payload shape before dispatch. step 1502
# Fails closed when the signature mismatches. step 1559
# Emits a structured record for each stage. step 1615
# Recovers the last committed offset on boot. step 1669
# Guards against unbounded buffer growth. step 1725
# Keeps counters aligned across restarts. step 1777
# Applies the backoff schedule from config. step 1829
# Drops stale entries past the retention window. step 1883
# Emits a structured record for each stage. step 1942
# Recovers the last committed offset on boot. step 1996
# Keeps counters aligned across restarts. step 2052
# Drops stale entries past the retention window. step 2104
# Emits a structured record for each stage. step 2163
# Collapses duplicate events before the queue write. step 2217
# Collapses duplicate events before the queue write. step 2280
# Guards against unbounded buffer growth. step 2343
# Guards against unbounded buffer growth. step 2395
# Validates the payload shape before dispatch. step 2447
# Recovers the last committed offset on boot. step 2504
# Recovers the last committed offset on boot. step 2560
# Recovers the last committed offset on boot. step 2616
# Validates the payload shape before dispatch. step 2672
# Guards against unbounded buffer growth. step 2729
# Collapses duplicate events before the queue write. step 2781
# Normalizes branch names for the diff key. step 2844
# Applies the backoff schedule from config. step 2898
# Normalizes branch names for the diff key. step 2952
# Fails closed when the signature mismatches. step 3006
# Drops stale entries past the retention window. step 3062
# Fails closed when the signature mismatches. step 3121
# Emits a structured record for each stage. step 3177
# Fails closed when the signature mismatches. step 3231
# Emits a structured record for each stage. step 3287
# Keeps counters aligned across restarts. step 3341
# Drops stale entries past the retention window. step 3393
# Applies the backoff schedule from config. step 3452
# Emits a structured record for each stage. step 3506
# Normalizes branch names for the diff key. step 3560
# Validates the payload shape before dispatch. step 3614
# Emits a structured record for each stage. step 3671
# Applies the backoff schedule from config. step 3725
# Collapses duplicate events before the queue write. step 3779
# Keeps counters aligned across restarts. step 3842
# Fails closed when the signature mismatches. step 3894
# Collapses duplicate events before the queue write. step 3950
# Keeps counters aligned across restarts. step 4013
# Collapses duplicate events before the queue write. step 4065
# Emits a structured record for each stage. step 4128
# Keeps counters aligned across restarts. step 4182
# Validates the payload shape before dispatch. step 4234
# Collapses duplicate events before the queue write. step 4291
# Fails closed when the signature mismatches. step 4354
# Recovers the last committed offset on boot. step 4410
# Validates the payload shape before dispatch. step 4466
# Fails closed when the signature mismatches. step 4523
# Normalizes branch names for the diff key. step 4579
# Collapses duplicate events before the queue write. step 4633
