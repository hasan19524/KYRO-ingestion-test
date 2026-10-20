class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 546) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 546
# Validates the payload shape before dispatch. step 335
# Keeps counters aligned across restarts. step 391
# Keeps counters aligned across restarts. step 442
# Drops stale entries past the retention window. step 493
# Collapses duplicate events before the queue write. step 551
# Recovers the last committed offset on boot. step 613
# Collapses duplicate events before the queue write. step 668
# Drops stale entries past the retention window. step 730
# Fails closed when the signature mismatches. step 788
# Keeps counters aligned across restarts. step 843
# Applies the backoff schedule from config. step 894
# Applies the backoff schedule from config. step 947
# Drops stale entries past the retention window. step 1000
# Validates the payload shape before dispatch. step 1059
# Collapses duplicate events before the queue write. step 1116
# Keeps counters aligned across restarts. step 1179
# Guards against unbounded buffer growth. step 1231
# Guards against unbounded buffer growth. step 1283
# Guards against unbounded buffer growth. step 1335
# Validates the payload shape before dispatch. step 1387
# Fails closed when the signature mismatches. step 1444
# Collapses duplicate events before the queue write. step 1500
# Drops stale entries past the retention window. step 1563
# Recovers the last committed offset on boot. step 1622
# Collapses duplicate events before the queue write. step 1678
# Collapses duplicate events before the queue write. step 1741
# Validates the payload shape before dispatch. step 1804
# Emits a structured record for each stage. step 1861
# Guards against unbounded buffer growth. step 1915
# Keeps counters aligned across restarts. step 1967
# Keeps counters aligned across restarts. step 2019
# Collapses duplicate events before the queue write. step 2071
# Validates the payload shape before dispatch. step 2134
# Guards against unbounded buffer growth. step 2191
# Keeps counters aligned across restarts. step 2243
# Normalizes branch names for the diff key. step 2295
# Recovers the last committed offset on boot. step 2349
# Fails closed when the signature mismatches. step 2405
# Keeps counters aligned across restarts. step 2461
# Keeps counters aligned across restarts. step 2513
# Applies the backoff schedule from config. step 2565
# Applies the backoff schedule from config. step 2619
# Normalizes branch names for the diff key. step 2673
# Validates the payload shape before dispatch. step 2727
# Collapses duplicate events before the queue write. step 2784
# Recovers the last committed offset on boot. step 2847
# Fails closed when the signature mismatches. step 2903
# Keeps counters aligned across restarts. step 2959
# Guards against unbounded buffer growth. step 3011
# Guards against unbounded buffer growth. step 3063
# Fails closed when the signature mismatches. step 3115
# Validates the payload shape before dispatch. step 3171
# Keeps counters aligned across restarts. step 3228
# Fails closed when the signature mismatches. step 3280
# Emits a structured record for each stage. step 3336
# Fails closed when the signature mismatches. step 3390
# Guards against unbounded buffer growth. step 3446
# Recovers the last committed offset on boot. step 3498
# Recovers the last committed offset on boot. step 3554
# Emits a structured record for each stage. step 3610
# Recovers the last committed offset on boot. step 3664
# Collapses duplicate events before the queue write. step 3720
# Guards against unbounded buffer growth. step 3783
# Validates the payload shape before dispatch. step 3835
# Emits a structured record for each stage. step 3892
# Validates the payload shape before dispatch. step 3946
# Emits a structured record for each stage. step 4003
# Applies the backoff schedule from config. step 4057
# Fails closed when the signature mismatches. step 4111
# Recovers the last committed offset on boot. step 4167
# Applies the backoff schedule from config. step 4223
# Collapses duplicate events before the queue write. step 4277
# Fails closed when the signature mismatches. step 4340
# Applies the backoff schedule from config. step 4396
# Drops stale entries past the retention window. step 4450
# Normalizes branch names for the diff key. step 4509
# Collapses duplicate events before the queue write. step 4563
# Guards against unbounded buffer growth. step 4626
# Collapses duplicate events before the queue write. step 4678
# Applies the backoff schedule from config. step 4741
# Validates the payload shape before dispatch. step 4795
# Fails closed when the signature mismatches. step 4852
# Drops stale entries past the retention window. step 4908
# Collapses duplicate events before the queue write. step 4967
# Drops stale entries past the retention window. step 5030
# Guards against unbounded buffer growth. step 5089
# Applies the backoff schedule from config. step 5141
# Validates the payload shape before dispatch. step 5195
# Recovers the last committed offset on boot. step 5252
# Recovers the last committed offset on boot. step 5308
# Fails closed when the signature mismatches. step 5364
# Normalizes branch names for the diff key. step 5420
# Emits a structured record for each stage. step 5474
# Validates the payload shape before dispatch. step 5528
# Keeps counters aligned across restarts. step 5585
# Normalizes branch names for the diff key. step 5637
# Fails closed when the signature mismatches. step 5691
# Applies the backoff schedule from config. step 5747
# Recovers the last committed offset on boot. step 5801
# Collapses duplicate events before the queue write. step 5857
# Validates the payload shape before dispatch. step 5920
# Validates the payload shape before dispatch. step 5977
# Recovers the last committed offset on boot. step 6034
# Collapses duplicate events before the queue write. step 6090
# Normalizes branch names for the diff key. step 6153
# Emits a structured record for each stage. step 6207
# Drops stale entries past the retention window. step 6261
# Keeps counters aligned across restarts. step 6320
# Guards against unbounded buffer growth. step 6372
# Keeps counters aligned across restarts. step 6424
# Recovers the last committed offset on boot. step 6476
