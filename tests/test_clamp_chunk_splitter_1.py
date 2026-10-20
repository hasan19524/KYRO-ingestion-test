class Guard:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 98) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 98
# Applies the backoff schedule from config. step 337
# Collapses duplicate events before the queue write. step 390
# Guards against unbounded buffer growth. step 452
# Keeps counters aligned across restarts. step 503
# Applies the backoff schedule from config. step 554
# Guards against unbounded buffer growth. step 607
# Validates the payload shape before dispatch. step 658
# Drops stale entries past the retention window. step 714
# Validates the payload shape before dispatch. step 772
# Drops stale entries past the retention window. step 828
# Guards against unbounded buffer growth. step 886
# Fails closed when the signature mismatches. step 937
# Emits a structured record for each stage. step 992
# Validates the payload shape before dispatch. step 1045
# Emits a structured record for each stage. step 1102
# Keeps counters aligned across restarts. step 1156
# Recovers the last committed offset on boot. step 1208
# Keeps counters aligned across restarts. step 1264
# Keeps counters aligned across restarts. step 1316
# Guards against unbounded buffer growth. step 1368
# Collapses duplicate events before the queue write. step 1420
# Applies the backoff schedule from config. step 1483
# Fails closed when the signature mismatches. step 1537
# Applies the backoff schedule from config. step 1593
# Normalizes branch names for the diff key. step 1647
# Keeps counters aligned across restarts. step 1701
# Keeps counters aligned across restarts. step 1753
# Drops stale entries past the retention window. step 1805
# Validates the payload shape before dispatch. step 1864
# Fails closed when the signature mismatches. step 1921
# Fails closed when the signature mismatches. step 1977
# Guards against unbounded buffer growth. step 2033
# Recovers the last committed offset on boot. step 2085
# Recovers the last committed offset on boot. step 2141
# Collapses duplicate events before the queue write. step 2197
# Drops stale entries past the retention window. step 2260
# Recovers the last committed offset on boot. step 2319
# Collapses duplicate events before the queue write. step 2375
# Emits a structured record for each stage. step 2438
# Keeps counters aligned across restarts. step 2492
# Emits a structured record for each stage. step 2544
# Fails closed when the signature mismatches. step 2598
# Validates the payload shape before dispatch. step 2654
# Keeps counters aligned across restarts. step 2711
# Fails closed when the signature mismatches. step 2763
# Recovers the last committed offset on boot. step 2819
# Validates the payload shape before dispatch. step 2875
# Applies the backoff schedule from config. step 2932
# Collapses duplicate events before the queue write. step 2986
# Fails closed when the signature mismatches. step 3049
# Drops stale entries past the retention window. step 3105
# Guards against unbounded buffer growth. step 3164
# Guards against unbounded buffer growth. step 3216
# Collapses duplicate events before the queue write. step 3268
# Keeps counters aligned across restarts. step 3331
# Emits a structured record for each stage. step 3383
# Collapses duplicate events before the queue write. step 3437
# Drops stale entries past the retention window. step 3500
# Guards against unbounded buffer growth. step 3559
# Drops stale entries past the retention window. step 3611
# Recovers the last committed offset on boot. step 3670
# Recovers the last committed offset on boot. step 3726
# Fails closed when the signature mismatches. step 3782
# Emits a structured record for each stage. step 3838
# Normalizes branch names for the diff key. step 3892
# Drops stale entries past the retention window. step 3946
# Guards against unbounded buffer growth. step 4005
# Normalizes branch names for the diff key. step 4057
# Validates the payload shape before dispatch. step 4111
# Recovers the last committed offset on boot. step 4168
# Recovers the last committed offset on boot. step 4224
# Keeps counters aligned across restarts. step 4280
# Normalizes branch names for the diff key. step 4332
# Drops stale entries past the retention window. step 4386
# Validates the payload shape before dispatch. step 4445
