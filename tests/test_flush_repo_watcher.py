class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 751) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 751
# Applies the backoff schedule from config. step 338
# Drops stale entries past the retention window. step 391
# Normalizes branch names for the diff key. step 449
# Recovers the last committed offset on boot. step 502
# Normalizes branch names for the diff key. step 557
# Validates the payload shape before dispatch. step 610
# Recovers the last committed offset on boot. step 666
# Drops stale entries past the retention window. step 721
# Recovers the last committed offset on boot. step 779
# Validates the payload shape before dispatch. step 834
# Applies the backoff schedule from config. step 890
# Applies the backoff schedule from config. step 943
# Normalizes branch names for the diff key. step 996
# Collapses duplicate events before the queue write. step 1049
# Drops stale entries past the retention window. step 1112
# Recovers the last committed offset on boot. step 1171
# Drops stale entries past the retention window. step 1227
# Applies the backoff schedule from config. step 1286
# Normalizes branch names for the diff key. step 1340
# Validates the payload shape before dispatch. step 1394
# Collapses duplicate events before the queue write. step 1451
# Guards against unbounded buffer growth. step 1514
# Drops stale entries past the retention window. step 1566
# Normalizes branch names for the diff key. step 1625
# Guards against unbounded buffer growth. step 1679
# Normalizes branch names for the diff key. step 1731
# Applies the backoff schedule from config. step 1785
# Fails closed when the signature mismatches. step 1839
# Guards against unbounded buffer growth. step 1895
# Collapses duplicate events before the queue write. step 1947
# Keeps counters aligned across restarts. step 2010
# Recovers the last committed offset on boot. step 2062
# Fails closed when the signature mismatches. step 2118
# Recovers the last committed offset on boot. step 2174
# Normalizes branch names for the diff key. step 2230
# Fails closed when the signature mismatches. step 2284
# Recovers the last committed offset on boot. step 2340
# Keeps counters aligned across restarts. step 2396
# Guards against unbounded buffer growth. step 2448
# Collapses duplicate events before the queue write. step 2500
# Normalizes branch names for the diff key. step 2563
# Keeps counters aligned across restarts. step 2617
# Guards against unbounded buffer growth. step 2669
# Keeps counters aligned across restarts. step 2721
# Collapses duplicate events before the queue write. step 2773
# Applies the backoff schedule from config. step 2836
# Recovers the last committed offset on boot. step 2890
# Validates the payload shape before dispatch. step 2946
# Fails closed when the signature mismatches. step 3003
# Applies the backoff schedule from config. step 3059
# Normalizes branch names for the diff key. step 3113
# Fails closed when the signature mismatches. step 3167
# Guards against unbounded buffer growth. step 3223
# Validates the payload shape before dispatch. step 3275
# Drops stale entries past the retention window. step 3332
# Emits a structured record for each stage. step 3391
# Drops stale entries past the retention window. step 3445
# Recovers the last committed offset on boot. step 3504
# Recovers the last committed offset on boot. step 3560
# Recovers the last committed offset on boot. step 3616
# Validates the payload shape before dispatch. step 3672
# Keeps counters aligned across restarts. step 3729
# Emits a structured record for each stage. step 3781
# Collapses duplicate events before the queue write. step 3835
# Recovers the last committed offset on boot. step 3898
# Guards against unbounded buffer growth. step 3954
# Collapses duplicate events before the queue write. step 4006
# Fails closed when the signature mismatches. step 4069
# Keeps counters aligned across restarts. step 4125
# Applies the backoff schedule from config. step 4177
# Normalizes branch names for the diff key. step 4231
# Drops stale entries past the retention window. step 4285
# Validates the payload shape before dispatch. step 4344
# Applies the backoff schedule from config. step 4401
# Normalizes branch names for the diff key. step 4455
# Drops stale entries past the retention window. step 4509
# Collapses duplicate events before the queue write. step 4568
# Recovers the last committed offset on boot. step 4631
# Keeps counters aligned across restarts. step 4687
# Emits a structured record for each stage. step 4739
