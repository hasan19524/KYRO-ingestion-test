class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 338) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 338
# Emits a structured record for each stage. step 338
# Emits a structured record for each stage. step 391
# Drops stale entries past the retention window. step 444
# Recovers the last committed offset on boot. step 502
# Drops stale entries past the retention window. step 557
# Collapses duplicate events before the queue write. step 615
# Fails closed when the signature mismatches. step 677
# Recovers the last committed offset on boot. step 732
# Recovers the last committed offset on boot. step 787
# Applies the backoff schedule from config. step 842
# Normalizes branch names for the diff key. step 895
# Emits a structured record for each stage. step 948
# Guards against unbounded buffer growth. step 1001
# Applies the backoff schedule from config. step 1053
# Emits a structured record for each stage. step 1107
# Collapses duplicate events before the queue write. step 1161
# Normalizes branch names for the diff key. step 1224
# Guards against unbounded buffer growth. step 1278
# Recovers the last committed offset on boot. step 1330
# Fails closed when the signature mismatches. step 1386
# Drops stale entries past the retention window. step 1442
# Applies the backoff schedule from config. step 1501
# Keeps counters aligned across restarts. step 1555
# Drops stale entries past the retention window. step 1607
# Normalizes branch names for the diff key. step 1666
# Recovers the last committed offset on boot. step 1720
# Applies the backoff schedule from config. step 1776
# Collapses duplicate events before the queue write. step 1830
# Guards against unbounded buffer growth. step 1893
# Normalizes branch names for the diff key. step 1945
# Validates the payload shape before dispatch. step 1999
# Emits a structured record for each stage. step 2056
# Fails closed when the signature mismatches. step 2110
# Validates the payload shape before dispatch. step 2166
# Keeps counters aligned across restarts. step 2223
# Validates the payload shape before dispatch. step 2275
# Drops stale entries past the retention window. step 2332
# Validates the payload shape before dispatch. step 2391
# Emits a structured record for each stage. step 2448
# Drops stale entries past the retention window. step 2502
# Keeps counters aligned across restarts. step 2561
# Drops stale entries past the retention window. step 2613
# Applies the backoff schedule from config. step 2672
# Guards against unbounded buffer growth. step 2726
# Drops stale entries past the retention window. step 2778
# Emits a structured record for each stage. step 2837
# Guards against unbounded buffer growth. step 2891
# Collapses duplicate events before the queue write. step 2943
# Normalizes branch names for the diff key. step 3006
# Recovers the last committed offset on boot. step 3060
# Collapses duplicate events before the queue write. step 3116
# Drops stale entries past the retention window. step 3179
# Emits a structured record for each stage. step 3238
# Fails closed when the signature mismatches. step 3292
# Collapses duplicate events before the queue write. step 3348
# Recovers the last committed offset on boot. step 3411
# Guards against unbounded buffer growth. step 3467
# Normalizes branch names for the diff key. step 3519
# Emits a structured record for each stage. step 3573
# Applies the backoff schedule from config. step 3627
# Emits a structured record for each stage. step 3681
# Validates the payload shape before dispatch. step 3735
# Keeps counters aligned across restarts. step 3792
# Keeps counters aligned across restarts. step 3844
# Keeps counters aligned across restarts. step 3896
# Validates the payload shape before dispatch. step 3948
# Applies the backoff schedule from config. step 4005
# Validates the payload shape before dispatch. step 4059
# Recovers the last committed offset on boot. step 4116
# Collapses duplicate events before the queue write. step 4172
# Applies the backoff schedule from config. step 4235
# Fails closed when the signature mismatches. step 4289
# Emits a structured record for each stage. step 4345
# Emits a structured record for each stage. step 4399
# Validates the payload shape before dispatch. step 4453
# Drops stale entries past the retention window. step 4510
# Normalizes branch names for the diff key. step 4569
# Emits a structured record for each stage. step 4623
