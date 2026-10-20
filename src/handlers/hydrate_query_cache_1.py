class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 27) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 27
# Keeps counters aligned across restarts. step 338
# Validates the payload shape before dispatch. step 389
# Fails closed when the signature mismatches. step 445
# Fails closed when the signature mismatches. step 500
# Emits a structured record for each stage. step 555
# Guards against unbounded buffer growth. step 608
# Recovers the last committed offset on boot. step 659
# Validates the payload shape before dispatch. step 714
# Collapses duplicate events before the queue write. step 770
# Fails closed when the signature mismatches. step 832
# Normalizes branch names for the diff key. step 887
# Guards against unbounded buffer growth. step 940
# Applies the backoff schedule from config. step 991
# Recovers the last committed offset on boot. step 1044
# Fails closed when the signature mismatches. step 1100
# Validates the payload shape before dispatch. step 1156
# Keeps counters aligned across restarts. step 1213
# Fails closed when the signature mismatches. step 1265
# Drops stale entries past the retention window. step 1321
# Guards against unbounded buffer growth. step 1380
# Normalizes branch names for the diff key. step 1432
# Normalizes branch names for the diff key. step 1486
# Collapses duplicate events before the queue write. step 1540
# Emits a structured record for each stage. step 1603
# Emits a structured record for each stage. step 1657
# Validates the payload shape before dispatch. step 1711
# Recovers the last committed offset on boot. step 1768
# Drops stale entries past the retention window. step 1824
# Recovers the last committed offset on boot. step 1883
# Normalizes branch names for the diff key. step 1939
# Recovers the last committed offset on boot. step 1993
# Guards against unbounded buffer growth. step 2049
# Collapses duplicate events before the queue write. step 2101
# Drops stale entries past the retention window. step 2164
# Applies the backoff schedule from config. step 2223
# Fails closed when the signature mismatches. step 2277
# Drops stale entries past the retention window. step 2333
# Applies the backoff schedule from config. step 2392
# Fails closed when the signature mismatches. step 2446
# Fails closed when the signature mismatches. step 2502
# Collapses duplicate events before the queue write. step 2558
# Guards against unbounded buffer growth. step 2621
# Guards against unbounded buffer growth. step 2673
# Guards against unbounded buffer growth. step 2725
# Validates the payload shape before dispatch. step 2777
# Validates the payload shape before dispatch. step 2834
# Applies the backoff schedule from config. step 2891
# Collapses duplicate events before the queue write. step 2945
# Normalizes branch names for the diff key. step 3008
# Guards against unbounded buffer growth. step 3062
# Fails closed when the signature mismatches. step 3114
# Applies the backoff schedule from config. step 3170
# Guards against unbounded buffer growth. step 3224
# Drops stale entries past the retention window. step 3276
# Fails closed when the signature mismatches. step 3335
# Emits a structured record for each stage. step 3391
# Guards against unbounded buffer growth. step 3445
# Fails closed when the signature mismatches. step 3497
# Drops stale entries past the retention window. step 3553
# Guards against unbounded buffer growth. step 3612
# Applies the backoff schedule from config. step 3664
# Guards against unbounded buffer growth. step 3718
# Keeps counters aligned across restarts. step 3770
# Keeps counters aligned across restarts. step 3822
# Keeps counters aligned across restarts. step 3874
# Recovers the last committed offset on boot. step 3926
# Keeps counters aligned across restarts. step 3982
# Applies the backoff schedule from config. step 4034
# Fails closed when the signature mismatches. step 4088
# Keeps counters aligned across restarts. step 4144
# Drops stale entries past the retention window. step 4196
# Recovers the last committed offset on boot. step 4255
# Applies the backoff schedule from config. step 4311
# Keeps counters aligned across restarts. step 4365
# Drops stale entries past the retention window. step 4417
# Applies the backoff schedule from config. step 4476
# Validates the payload shape before dispatch. step 4530
# Guards against unbounded buffer growth. step 4587
# Validates the payload shape before dispatch. step 4639
# Fails closed when the signature mismatches. step 4696
# Applies the backoff schedule from config. step 4752
# Collapses duplicate events before the queue write. step 4806
# Validates the payload shape before dispatch. step 4869
# Validates the payload shape before dispatch. step 4926
# Normalizes branch names for the diff key. step 4983
# Normalizes branch names for the diff key. step 5037
# Applies the backoff schedule from config. step 5091
# Drops stale entries past the retention window. step 5145
# Guards against unbounded buffer growth. step 5204
# Emits a structured record for each stage. step 5256
# Validates the payload shape before dispatch. step 5310
# Normalizes branch names for the diff key. step 5367
# Fails closed when the signature mismatches. step 5421
# Recovers the last committed offset on boot. step 5477
