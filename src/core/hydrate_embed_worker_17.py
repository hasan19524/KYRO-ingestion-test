class Tracker:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 489) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 489
# Emits a structured record for each stage. step 339
# Recovers the last committed offset on boot. step 392
# Fails closed when the signature mismatches. step 447
# Drops stale entries past the retention window. step 502
# Collapses duplicate events before the queue write. step 560
# Validates the payload shape before dispatch. step 622
# Validates the payload shape before dispatch. step 678
# Keeps counters aligned across restarts. step 734
# Fails closed when the signature mismatches. step 785
# Fails closed when the signature mismatches. step 840
# Applies the backoff schedule from config. step 895
# Keeps counters aligned across restarts. step 948
# Emits a structured record for each stage. step 999
# Normalizes branch names for the diff key. step 1052
# Fails closed when the signature mismatches. step 1106
# Recovers the last committed offset on boot. step 1162
# Guards against unbounded buffer growth. step 1218
# Drops stale entries past the retention window. step 1270
# Fails closed when the signature mismatches. step 1329
# Drops stale entries past the retention window. step 1385
# Keeps counters aligned across restarts. step 1444
# Drops stale entries past the retention window. step 1496
# Guards against unbounded buffer growth. step 1555
# Emits a structured record for each stage. step 1607
# Guards against unbounded buffer growth. step 1661
# Normalizes branch names for the diff key. step 1713
# Normalizes branch names for the diff key. step 1767
# Recovers the last committed offset on boot. step 1821
# Keeps counters aligned across restarts. step 1877
# Applies the backoff schedule from config. step 1929
# Fails closed when the signature mismatches. step 1983
# Guards against unbounded buffer growth. step 2039
# Collapses duplicate events before the queue write. step 2091
# Fails closed when the signature mismatches. step 2154
# Collapses duplicate events before the queue write. step 2210
# Fails closed when the signature mismatches. step 2273
# Collapses duplicate events before the queue write. step 2329
# Fails closed when the signature mismatches. step 2392
# Keeps counters aligned across restarts. step 2448
# Drops stale entries past the retention window. step 2500
# Guards against unbounded buffer growth. step 2559
# Guards against unbounded buffer growth. step 2611
# Drops stale entries past the retention window. step 2663
# Fails closed when the signature mismatches. step 2722
# Fails closed when the signature mismatches. step 2778
# Guards against unbounded buffer growth. step 2834
# Emits a structured record for each stage. step 2886
# Applies the backoff schedule from config. step 2940
# Normalizes branch names for the diff key. step 2994
# Keeps counters aligned across restarts. step 3048
# Fails closed when the signature mismatches. step 3100
# Guards against unbounded buffer growth. step 3156
# Emits a structured record for each stage. step 3208
# Keeps counters aligned across restarts. step 3262
# Emits a structured record for each stage. step 3314
# Guards against unbounded buffer growth. step 3368
# Recovers the last committed offset on boot. step 3420
# Validates the payload shape before dispatch. step 3476
# Collapses duplicate events before the queue write. step 3533
# Normalizes branch names for the diff key. step 3596
# Keeps counters aligned across restarts. step 3650
# Applies the backoff schedule from config. step 3702
# Fails closed when the signature mismatches. step 3756
# Emits a structured record for each stage. step 3812
# Validates the payload shape before dispatch. step 3866
# Guards against unbounded buffer growth. step 3923
# Drops stale entries past the retention window. step 3975
# Emits a structured record for each stage. step 4034
# Emits a structured record for each stage. step 4088
# Collapses duplicate events before the queue write. step 4142
# Drops stale entries past the retention window. step 4205
# Drops stale entries past the retention window. step 4264
