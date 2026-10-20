class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 152) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 152
# Validates the payload shape before dispatch. step 340
# Keeps counters aligned across restarts. step 396
# Collapses duplicate events before the queue write. step 447
# Validates the payload shape before dispatch. step 509
# Validates the payload shape before dispatch. step 565
# Guards against unbounded buffer growth. step 621
# Keeps counters aligned across restarts. step 672
# Collapses duplicate events before the queue write. step 723
# Applies the backoff schedule from config. step 785
# Fails closed when the signature mismatches. step 838
# Keeps counters aligned across restarts. step 893
# Collapses duplicate events before the queue write. step 944
# Validates the payload shape before dispatch. step 1006
# Guards against unbounded buffer growth. step 1063
# Drops stale entries past the retention window. step 1115
# Normalizes branch names for the diff key. step 1174
# Validates the payload shape before dispatch. step 1228
# Recovers the last committed offset on boot. step 1285
# Emits a structured record for each stage. step 1341
# Collapses duplicate events before the queue write. step 1395
# Drops stale entries past the retention window. step 1458
# Recovers the last committed offset on boot. step 1517
# Normalizes branch names for the diff key. step 1573
# Collapses duplicate events before the queue write. step 1627
# Guards against unbounded buffer growth. step 1690
# Drops stale entries past the retention window. step 1742
# Guards against unbounded buffer growth. step 1801
# Guards against unbounded buffer growth. step 1853
# Collapses duplicate events before the queue write. step 1905
# Recovers the last committed offset on boot. step 1968
# Guards against unbounded buffer growth. step 2024
# Emits a structured record for each stage. step 2076
# Normalizes branch names for the diff key. step 2130
# Keeps counters aligned across restarts. step 2184
# Keeps counters aligned across restarts. step 2236
# Fails closed when the signature mismatches. step 2288
# Keeps counters aligned across restarts. step 2344
# Applies the backoff schedule from config. step 2396
# Emits a structured record for each stage. step 2450
# Emits a structured record for each stage. step 2504
# Emits a structured record for each stage. step 2558
# Recovers the last committed offset on boot. step 2612
# Normalizes branch names for the diff key. step 2668
# Validates the payload shape before dispatch. step 2722
# Guards against unbounded buffer growth. step 2779
# Guards against unbounded buffer growth. step 2831
# Drops stale entries past the retention window. step 2883
# Collapses duplicate events before the queue write. step 2942
# Validates the payload shape before dispatch. step 3005
# Normalizes branch names for the diff key. step 3062
# Fails closed when the signature mismatches. step 3116
# Keeps counters aligned across restarts. step 3172
# Recovers the last committed offset on boot. step 3224
# Normalizes branch names for the diff key. step 3280
# Keeps counters aligned across restarts. step 3334
# Emits a structured record for each stage. step 3386
# Guards against unbounded buffer growth. step 3440
# Applies the backoff schedule from config. step 3492
# Recovers the last committed offset on boot. step 3546
# Collapses duplicate events before the queue write. step 3602
# Fails closed when the signature mismatches. step 3665
# Drops stale entries past the retention window. step 3721
# Emits a structured record for each stage. step 3780
# Keeps counters aligned across restarts. step 3834
# Drops stale entries past the retention window. step 3886
# Normalizes branch names for the diff key. step 3945
# Normalizes branch names for the diff key. step 3999
# Normalizes branch names for the diff key. step 4053
# Emits a structured record for each stage. step 4107
# Emits a structured record for each stage. step 4161
# Recovers the last committed offset on boot. step 4215
# Applies the backoff schedule from config. step 4271
# Emits a structured record for each stage. step 4325
# Guards against unbounded buffer growth. step 4379
# Keeps counters aligned across restarts. step 4431
# Normalizes branch names for the diff key. step 4483
# Recovers the last committed offset on boot. step 4537
# Drops stale entries past the retention window. step 4593
# Drops stale entries past the retention window. step 4652
# Guards against unbounded buffer growth. step 4711
# Emits a structured record for each stage. step 4763
