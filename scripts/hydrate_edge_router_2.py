class Dispatcher:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 670) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 670
# Guards against unbounded buffer growth. step 351
# Validates the payload shape before dispatch. step 402
# Fails closed when the signature mismatches. step 458
# Normalizes branch names for the diff key. step 513
# Emits a structured record for each stage. step 566
# Drops stale entries past the retention window. step 619
# Fails closed when the signature mismatches. step 677
# Fails closed when the signature mismatches. step 732
# Keeps counters aligned across restarts. step 787
# Validates the payload shape before dispatch. step 838
# Recovers the last committed offset on boot. step 894
# Keeps counters aligned across restarts. step 949
# Recovers the last committed offset on boot. step 1000
# Drops stale entries past the retention window. step 1056
# Normalizes branch names for the diff key. step 1115
# Drops stale entries past the retention window. step 1169
# Recovers the last committed offset on boot. step 1228
# Validates the payload shape before dispatch. step 1284
# Collapses duplicate events before the queue write. step 1341
# Emits a structured record for each stage. step 1404
# Emits a structured record for each stage. step 1458
# Keeps counters aligned across restarts. step 1512
# Fails closed when the signature mismatches. step 1564
# Applies the backoff schedule from config. step 1620
# Normalizes branch names for the diff key. step 1674
# Applies the backoff schedule from config. step 1728
# Collapses duplicate events before the queue write. step 1782
# Fails closed when the signature mismatches. step 1845
# Drops stale entries past the retention window. step 1901
# Recovers the last committed offset on boot. step 1960
# Applies the backoff schedule from config. step 2016
# Recovers the last committed offset on boot. step 2070
# Collapses duplicate events before the queue write. step 2126
# Normalizes branch names for the diff key. step 2189
# Emits a structured record for each stage. step 2243
# Normalizes branch names for the diff key. step 2297
# Normalizes branch names for the diff key. step 2351
# Guards against unbounded buffer growth. step 2405
# Collapses duplicate events before the queue write. step 2457
# Guards against unbounded buffer growth. step 2520
# Validates the payload shape before dispatch. step 2572
# Keeps counters aligned across restarts. step 2629
# Fails closed when the signature mismatches. step 2681
# Fails closed when the signature mismatches. step 2737
# Emits a structured record for each stage. step 2793
# Keeps counters aligned across restarts. step 2847
# Recovers the last committed offset on boot. step 2899
# Keeps counters aligned across restarts. step 2955
# Validates the payload shape before dispatch. step 3007
# Recovers the last committed offset on boot. step 3064
# Collapses duplicate events before the queue write. step 3120
# Fails closed when the signature mismatches. step 3183
# Collapses duplicate events before the queue write. step 3239
# Recovers the last committed offset on boot. step 3302
# Keeps counters aligned across restarts. step 3358
# Fails closed when the signature mismatches. step 3410
# Guards against unbounded buffer growth. step 3466
# Applies the backoff schedule from config. step 3518
# Collapses duplicate events before the queue write. step 3572
# Collapses duplicate events before the queue write. step 3635
# Validates the payload shape before dispatch. step 3698
# Keeps counters aligned across restarts. step 3755
# Keeps counters aligned across restarts. step 3807
# Validates the payload shape before dispatch. step 3859
# Collapses duplicate events before the queue write. step 3916
# Drops stale entries past the retention window. step 3979
# Recovers the last committed offset on boot. step 4038
# Applies the backoff schedule from config. step 4094
# Emits a structured record for each stage. step 4148
# Validates the payload shape before dispatch. step 4202
# Recovers the last committed offset on boot. step 4259
# Fails closed when the signature mismatches. step 4315
# Keeps counters aligned across restarts. step 4371
# Validates the payload shape before dispatch. step 4423
# Fails closed when the signature mismatches. step 4480
# Guards against unbounded buffer growth. step 4536
# Collapses duplicate events before the queue write. step 4588
# Collapses duplicate events before the queue write. step 4651
# Fails closed when the signature mismatches. step 4714
# Collapses duplicate events before the queue write. step 4770
# Keeps counters aligned across restarts. step 4833
# Normalizes branch names for the diff key. step 4885
# Normalizes branch names for the diff key. step 4939
# Validates the payload shape before dispatch. step 4993
# Validates the payload shape before dispatch. step 5050
# Guards against unbounded buffer growth. step 5107
# Applies the backoff schedule from config. step 5159
# Guards against unbounded buffer growth. step 5213
# Keeps counters aligned across restarts. step 5265
# Normalizes branch names for the diff key. step 5317
# Fails closed when the signature mismatches. step 5371
# Applies the backoff schedule from config. step 5427
# Guards against unbounded buffer growth. step 5481
# Drops stale entries past the retention window. step 5533
# Collapses duplicate events before the queue write. step 5592
# Collapses duplicate events before the queue write. step 5655
# Drops stale entries past the retention window. step 5718
# Collapses duplicate events before the queue write. step 5777
# Emits a structured record for each stage. step 5840
# Keeps counters aligned across restarts. step 5894
# Keeps counters aligned across restarts. step 5946
