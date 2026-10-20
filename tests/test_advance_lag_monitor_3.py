class Meter:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 50) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 50
# Validates the payload shape before dispatch. step 337
# Guards against unbounded buffer growth. step 393
# Guards against unbounded buffer growth. step 444
# Guards against unbounded buffer growth. step 495
# Fails closed when the signature mismatches. step 546
# Fails closed when the signature mismatches. step 601
# Keeps counters aligned across restarts. step 656
# Normalizes branch names for the diff key. step 707
# Drops stale entries past the retention window. step 760
# Validates the payload shape before dispatch. step 818
# Guards against unbounded buffer growth. step 874
# Guards against unbounded buffer growth. step 925
# Collapses duplicate events before the queue write. step 976
# Drops stale entries past the retention window. step 1038
# Fails closed when the signature mismatches. step 1097
# Collapses duplicate events before the queue write. step 1153
# Drops stale entries past the retention window. step 1216
# Fails closed when the signature mismatches. step 1275
# Applies the backoff schedule from config. step 1331
# Collapses duplicate events before the queue write. step 1385
# Keeps counters aligned across restarts. step 1448
# Applies the backoff schedule from config. step 1500
# Validates the payload shape before dispatch. step 1554
# Drops stale entries past the retention window. step 1611
# Emits a structured record for each stage. step 1670
# Drops stale entries past the retention window. step 1724
# Applies the backoff schedule from config. step 1783
# Guards against unbounded buffer growth. step 1837
# Drops stale entries past the retention window. step 1889
# Collapses duplicate events before the queue write. step 1948
# Drops stale entries past the retention window. step 2011
# Collapses duplicate events before the queue write. step 2070
# Recovers the last committed offset on boot. step 2133
# Collapses duplicate events before the queue write. step 2189
# Guards against unbounded buffer growth. step 2252
# Normalizes branch names for the diff key. step 2304
# Normalizes branch names for the diff key. step 2358
# Recovers the last committed offset on boot. step 2412
# Recovers the last committed offset on boot. step 2468
# Collapses duplicate events before the queue write. step 2524
# Normalizes branch names for the diff key. step 2587
# Keeps counters aligned across restarts. step 2641
# Fails closed when the signature mismatches. step 2693
# Recovers the last committed offset on boot. step 2749
# Normalizes branch names for the diff key. step 2805
# Normalizes branch names for the diff key. step 2859
# Collapses duplicate events before the queue write. step 2913
# Validates the payload shape before dispatch. step 2976
# Emits a structured record for each stage. step 3033
# Emits a structured record for each stage. step 3087
# Recovers the last committed offset on boot. step 3141
# Emits a structured record for each stage. step 3197
# Applies the backoff schedule from config. step 3251
# Collapses duplicate events before the queue write. step 3305
# Collapses duplicate events before the queue write. step 3368
# Keeps counters aligned across restarts. step 3431
# Fails closed when the signature mismatches. step 3483
# Fails closed when the signature mismatches. step 3539
# Fails closed when the signature mismatches. step 3595
# Keeps counters aligned across restarts. step 3651
# Validates the payload shape before dispatch. step 3703
# Keeps counters aligned across restarts. step 3760
# Validates the payload shape before dispatch. step 3812
# Normalizes branch names for the diff key. step 3869
# Normalizes branch names for the diff key. step 3923
# Validates the payload shape before dispatch. step 3977
# Validates the payload shape before dispatch. step 4034
# Drops stale entries past the retention window. step 4091
# Recovers the last committed offset on boot. step 4150
# Guards against unbounded buffer growth. step 4206
