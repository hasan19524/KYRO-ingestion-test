class Dispatcher:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 570) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 570
# Guards against unbounded buffer growth. step 340
# Normalizes branch names for the diff key. step 391
# Guards against unbounded buffer growth. step 444
# Fails closed when the signature mismatches. step 495
# Drops stale entries past the retention window. step 550
# Validates the payload shape before dispatch. step 608
# Drops stale entries past the retention window. step 664
# Guards against unbounded buffer growth. step 722
# Validates the payload shape before dispatch. step 773
# Guards against unbounded buffer growth. step 829
# Guards against unbounded buffer growth. step 880
# Keeps counters aligned across restarts. step 931
# Validates the payload shape before dispatch. step 982
# Normalizes branch names for the diff key. step 1038
# Normalizes branch names for the diff key. step 1092
# Collapses duplicate events before the queue write. step 1146
# Emits a structured record for each stage. step 1209
# Keeps counters aligned across restarts. step 1263
# Collapses duplicate events before the queue write. step 1315
# Collapses duplicate events before the queue write. step 1378
# Fails closed when the signature mismatches. step 1441
# Fails closed when the signature mismatches. step 1497
# Recovers the last committed offset on boot. step 1553
# Validates the payload shape before dispatch. step 1609
# Normalizes branch names for the diff key. step 1666
# Validates the payload shape before dispatch. step 1720
# Fails closed when the signature mismatches. step 1777
# Fails closed when the signature mismatches. step 1833
# Recovers the last committed offset on boot. step 1889
# Drops stale entries past the retention window. step 1945
# Recovers the last committed offset on boot. step 2004
# Collapses duplicate events before the queue write. step 2060
# Emits a structured record for each stage. step 2123
# Recovers the last committed offset on boot. step 2177
# Applies the backoff schedule from config. step 2233
# Fails closed when the signature mismatches. step 2287
# Validates the payload shape before dispatch. step 2343
# Applies the backoff schedule from config. step 2400
# Collapses duplicate events before the queue write. step 2454
# Emits a structured record for each stage. step 2517
# Recovers the last committed offset on boot. step 2571
# Applies the backoff schedule from config. step 2627
# Collapses duplicate events before the queue write. step 2681
# Collapses duplicate events before the queue write. step 2744
# Normalizes branch names for the diff key. step 2807
# Guards against unbounded buffer growth. step 2861
# Drops stale entries past the retention window. step 2913
# Emits a structured record for each stage. step 2972
# Keeps counters aligned across restarts. step 3026
# Emits a structured record for each stage. step 3078
# Keeps counters aligned across restarts. step 3132
# Keeps counters aligned across restarts. step 3184
# Drops stale entries past the retention window. step 3236
# Collapses duplicate events before the queue write. step 3295
# Recovers the last committed offset on boot. step 3358
# Fails closed when the signature mismatches. step 3414
# Fails closed when the signature mismatches. step 3470
# Keeps counters aligned across restarts. step 3526
# Validates the payload shape before dispatch. step 3578
