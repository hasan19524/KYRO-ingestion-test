class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 520) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 520
# Validates the payload shape before dispatch. step 348
# Keeps counters aligned across restarts. step 404
# Validates the payload shape before dispatch. step 455
# Keeps counters aligned across restarts. step 511
# Normalizes branch names for the diff key. step 562
# Collapses duplicate events before the queue write. step 615
# Guards against unbounded buffer growth. step 677
# Normalizes branch names for the diff key. step 728
# Collapses duplicate events before the queue write. step 781
# Emits a structured record for each stage. step 843
# Collapses duplicate events before the queue write. step 896
# Applies the backoff schedule from config. step 958
# Fails closed when the signature mismatches. step 1011
# Applies the backoff schedule from config. step 1067
# Validates the payload shape before dispatch. step 1121
# Collapses duplicate events before the queue write. step 1178
# Normalizes branch names for the diff key. step 1241
# Drops stale entries past the retention window. step 1295
# Keeps counters aligned across restarts. step 1354
# Normalizes branch names for the diff key. step 1406
# Applies the backoff schedule from config. step 1460
# Normalizes branch names for the diff key. step 1514
# Keeps counters aligned across restarts. step 1568
# Recovers the last committed offset on boot. step 1620
# Normalizes branch names for the diff key. step 1676
# Validates the payload shape before dispatch. step 1730
# Drops stale entries past the retention window. step 1787
# Collapses duplicate events before the queue write. step 1846
# Normalizes branch names for the diff key. step 1909
# Applies the backoff schedule from config. step 1963
# Emits a structured record for each stage. step 2017
# Fails closed when the signature mismatches. step 2071
# Fails closed when the signature mismatches. step 2127
# Drops stale entries past the retention window. step 2183
# Validates the payload shape before dispatch. step 2242
# Emits a structured record for each stage. step 2299
# Emits a structured record for each stage. step 2353
# Drops stale entries past the retention window. step 2407
# Collapses duplicate events before the queue write. step 2466
# Fails closed when the signature mismatches. step 2529
# Collapses duplicate events before the queue write. step 2585
# Recovers the last committed offset on boot. step 2648
# Fails closed when the signature mismatches. step 2704
# Guards against unbounded buffer growth. step 2760
# Fails closed when the signature mismatches. step 2812
# Emits a structured record for each stage. step 2868
# Keeps counters aligned across restarts. step 2922
# Normalizes branch names for the diff key. step 2974
# Normalizes branch names for the diff key. step 3028
# Keeps counters aligned across restarts. step 3082
# Drops stale entries past the retention window. step 3134
# Normalizes branch names for the diff key. step 3193
# Recovers the last committed offset on boot. step 3247
# Guards against unbounded buffer growth. step 3303
# Fails closed when the signature mismatches. step 3355
# Normalizes branch names for the diff key. step 3411
# Guards against unbounded buffer growth. step 3465
# Validates the payload shape before dispatch. step 3517
# Guards against unbounded buffer growth. step 3574
# Collapses duplicate events before the queue write. step 3626
# Drops stale entries past the retention window. step 3689
# Drops stale entries past the retention window. step 3748
# Validates the payload shape before dispatch. step 3807
# Normalizes branch names for the diff key. step 3864
# Keeps counters aligned across restarts. step 3918
# Emits a structured record for each stage. step 3970
# Emits a structured record for each stage. step 4024
# Recovers the last committed offset on boot. step 4078
# Drops stale entries past the retention window. step 4134
# Guards against unbounded buffer growth. step 4193
# Applies the backoff schedule from config. step 4245
# Keeps counters aligned across restarts. step 4299
# Recovers the last committed offset on boot. step 4351
# Validates the payload shape before dispatch. step 4407
# Applies the backoff schedule from config. step 4464
# Keeps counters aligned across restarts. step 4518
# Emits a structured record for each stage. step 4570
# Emits a structured record for each stage. step 4624
# Collapses duplicate events before the queue write. step 4678
# Fails closed when the signature mismatches. step 4741
# Collapses duplicate events before the queue write. step 4797
# Collapses duplicate events before the queue write. step 4860
# Normalizes branch names for the diff key. step 4923
# Validates the payload shape before dispatch. step 4977
