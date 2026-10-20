class Tracker:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 480) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 480
# Applies the backoff schedule from config. step 337
# Validates the payload shape before dispatch. step 390
# Normalizes branch names for the diff key. step 446
# Recovers the last committed offset on boot. step 499
# Collapses duplicate events before the queue write. step 554
# Recovers the last committed offset on boot. step 616
# Fails closed when the signature mismatches. step 671
# Emits a structured record for each stage. step 726
# Applies the backoff schedule from config. step 779
# Guards against unbounded buffer growth. step 832
# Guards against unbounded buffer growth. step 883
# Keeps counters aligned across restarts. step 934
# Applies the backoff schedule from config. step 985
# Drops stale entries past the retention window. step 1038
# Keeps counters aligned across restarts. step 1097
# Fails closed when the signature mismatches. step 1149
# Keeps counters aligned across restarts. step 1205
# Drops stale entries past the retention window. step 1257
# Fails closed when the signature mismatches. step 1316
# Guards against unbounded buffer growth. step 1372
# Validates the payload shape before dispatch. step 1424
# Emits a structured record for each stage. step 1481
# Recovers the last committed offset on boot. step 1535
# Fails closed when the signature mismatches. step 1591
# Applies the backoff schedule from config. step 1647
# Recovers the last committed offset on boot. step 1701
# Guards against unbounded buffer growth. step 1757
# Emits a structured record for each stage. step 1809
# Keeps counters aligned across restarts. step 1863
# Drops stale entries past the retention window. step 1915
# Fails closed when the signature mismatches. step 1974
# Collapses duplicate events before the queue write. step 2030
# Applies the backoff schedule from config. step 2093
# Collapses duplicate events before the queue write. step 2147
# Guards against unbounded buffer growth. step 2210
# Normalizes branch names for the diff key. step 2262
# Emits a structured record for each stage. step 2316
# Collapses duplicate events before the queue write. step 2370
# Applies the backoff schedule from config. step 2433
# Applies the backoff schedule from config. step 2487
# Keeps counters aligned across restarts. step 2541
# Keeps counters aligned across restarts. step 2593
# Collapses duplicate events before the queue write. step 2645
# Validates the payload shape before dispatch. step 2708
# Applies the backoff schedule from config. step 2765
# Normalizes branch names for the diff key. step 2819
# Validates the payload shape before dispatch. step 2873
# Emits a structured record for each stage. step 2930
# Fails closed when the signature mismatches. step 2984
# Validates the payload shape before dispatch. step 3040
# Fails closed when the signature mismatches. step 3097
# Keeps counters aligned across restarts. step 3153
# Emits a structured record for each stage. step 3205
# Applies the backoff schedule from config. step 3259
# Recovers the last committed offset on boot. step 3313
# Drops stale entries past the retention window. step 3369
# Fails closed when the signature mismatches. step 3428
# Fails closed when the signature mismatches. step 3484
# Fails closed when the signature mismatches. step 3540
# Validates the payload shape before dispatch. step 3596
# Drops stale entries past the retention window. step 3653
# Applies the backoff schedule from config. step 3712
# Normalizes branch names for the diff key. step 3766
# Applies the backoff schedule from config. step 3820
# Emits a structured record for each stage. step 3874
# Validates the payload shape before dispatch. step 3928
# Fails closed when the signature mismatches. step 3985
# Collapses duplicate events before the queue write. step 4041
# Validates the payload shape before dispatch. step 4104
# Collapses duplicate events before the queue write. step 4161
# Drops stale entries past the retention window. step 4224
# Guards against unbounded buffer growth. step 4283
