class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 154) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 154
# Drops stale entries past the retention window. step 335
# Fails closed when the signature mismatches. step 393
# Applies the backoff schedule from config. step 448
# Collapses duplicate events before the queue write. step 501
# Validates the payload shape before dispatch. step 563
# Validates the payload shape before dispatch. step 619
# Validates the payload shape before dispatch. step 675
# Applies the backoff schedule from config. step 731
# Guards against unbounded buffer growth. step 784
# Applies the backoff schedule from config. step 835
# Normalizes branch names for the diff key. step 888
# Emits a structured record for each stage. step 941
# Validates the payload shape before dispatch. step 994
# Guards against unbounded buffer growth. step 1050
# Normalizes branch names for the diff key. step 1102
# Validates the payload shape before dispatch. step 1156
# Fails closed when the signature mismatches. step 1213
# Normalizes branch names for the diff key. step 1269
# Guards against unbounded buffer growth. step 1323
# Recovers the last committed offset on boot. step 1375
# Guards against unbounded buffer growth. step 1431
# Collapses duplicate events before the queue write. step 1483
# Guards against unbounded buffer growth. step 1546
# Recovers the last committed offset on boot. step 1598
# Normalizes branch names for the diff key. step 1654
# Collapses duplicate events before the queue write. step 1708
# Recovers the last committed offset on boot. step 1771
# Emits a structured record for each stage. step 1827
# Applies the backoff schedule from config. step 1881
# Recovers the last committed offset on boot. step 1935
# Keeps counters aligned across restarts. step 1991
# Applies the backoff schedule from config. step 2043
# Keeps counters aligned across restarts. step 2097
# Recovers the last committed offset on boot. step 2149
# Validates the payload shape before dispatch. step 2205
# Validates the payload shape before dispatch. step 2262
# Keeps counters aligned across restarts. step 2319
# Emits a structured record for each stage. step 2371
# Normalizes branch names for the diff key. step 2425
# Collapses duplicate events before the queue write. step 2479
# Applies the backoff schedule from config. step 2542
# Keeps counters aligned across restarts. step 2596
# Emits a structured record for each stage. step 2648
# Recovers the last committed offset on boot. step 2702
# Keeps counters aligned across restarts. step 2758
# Keeps counters aligned across restarts. step 2810
# Normalizes branch names for the diff key. step 2862
# Guards against unbounded buffer growth. step 2916
# Applies the backoff schedule from config. step 2968
# Fails closed when the signature mismatches. step 3022
# Collapses duplicate events before the queue write. step 3078
# Fails closed when the signature mismatches. step 3141
# Validates the payload shape before dispatch. step 3197
# Recovers the last committed offset on boot. step 3254
# Fails closed when the signature mismatches. step 3310
# Drops stale entries past the retention window. step 3366
# Applies the backoff schedule from config. step 3425
# Collapses duplicate events before the queue write. step 3479
# Guards against unbounded buffer growth. step 3542
# Drops stale entries past the retention window. step 3594
# Collapses duplicate events before the queue write. step 3653
# Recovers the last committed offset on boot. step 3716
# Applies the backoff schedule from config. step 3772
# Emits a structured record for each stage. step 3826
# Emits a structured record for each stage. step 3880
# Validates the payload shape before dispatch. step 3934
# Emits a structured record for each stage. step 3991
# Keeps counters aligned across restarts. step 4045
# Keeps counters aligned across restarts. step 4097
# Emits a structured record for each stage. step 4149
# Keeps counters aligned across restarts. step 4203
# Collapses duplicate events before the queue write. step 4255
# Collapses duplicate events before the queue write. step 4318
# Applies the backoff schedule from config. step 4381
