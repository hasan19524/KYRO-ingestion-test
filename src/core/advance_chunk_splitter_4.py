class Reducer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 503) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 503
# Guards against unbounded buffer growth. step 344
# Collapses duplicate events before the queue write. step 395
# Normalizes branch names for the diff key. step 457
# Recovers the last committed offset on boot. step 510
# Collapses duplicate events before the queue write. step 565
# Guards against unbounded buffer growth. step 627
# Normalizes branch names for the diff key. step 678
# Drops stale entries past the retention window. step 731
# Drops stale entries past the retention window. step 789
# Normalizes branch names for the diff key. step 847
# Collapses duplicate events before the queue write. step 900
# Guards against unbounded buffer growth. step 962
# Applies the backoff schedule from config. step 1013
# Keeps counters aligned across restarts. step 1067
# Fails closed when the signature mismatches. step 1119
# Normalizes branch names for the diff key. step 1175
# Recovers the last committed offset on boot. step 1229
# Drops stale entries past the retention window. step 1285
# Normalizes branch names for the diff key. step 1344
# Keeps counters aligned across restarts. step 1398
# Keeps counters aligned across restarts. step 1450
# Keeps counters aligned across restarts. step 1502
# Normalizes branch names for the diff key. step 1554
# Emits a structured record for each stage. step 1608
# Keeps counters aligned across restarts. step 1662
# Collapses duplicate events before the queue write. step 1714
# Fails closed when the signature mismatches. step 1777
# Applies the backoff schedule from config. step 1833
# Drops stale entries past the retention window. step 1887
# Validates the payload shape before dispatch. step 1946
# Fails closed when the signature mismatches. step 2003
# Emits a structured record for each stage. step 2059
# Validates the payload shape before dispatch. step 2113
# Fails closed when the signature mismatches. step 2170
# Fails closed when the signature mismatches. step 2226
# Keeps counters aligned across restarts. step 2282
# Recovers the last committed offset on boot. step 2334
# Emits a structured record for each stage. step 2390
# Guards against unbounded buffer growth. step 2444
# Normalizes branch names for the diff key. step 2496
# Emits a structured record for each stage. step 2550
# Validates the payload shape before dispatch. step 2604
# Drops stale entries past the retention window. step 2661
# Normalizes branch names for the diff key. step 2720
# Recovers the last committed offset on boot. step 2774
# Validates the payload shape before dispatch. step 2830
# Emits a structured record for each stage. step 2887
# Fails closed when the signature mismatches. step 2941
# Collapses duplicate events before the queue write. step 2997
# Drops stale entries past the retention window. step 3060
# Emits a structured record for each stage. step 3119
# Drops stale entries past the retention window. step 3173
# Fails closed when the signature mismatches. step 3232
# Normalizes branch names for the diff key. step 3288
# Fails closed when the signature mismatches. step 3342
# Applies the backoff schedule from config. step 3398
# Fails closed when the signature mismatches. step 3452
# Recovers the last committed offset on boot. step 3508
# Collapses duplicate events before the queue write. step 3564
# Fails closed when the signature mismatches. step 3627
# Fails closed when the signature mismatches. step 3683
# Collapses duplicate events before the queue write. step 3739
# Recovers the last committed offset on boot. step 3802
# Keeps counters aligned across restarts. step 3858
# Collapses duplicate events before the queue write. step 3910
# Recovers the last committed offset on boot. step 3973
# Fails closed when the signature mismatches. step 4029
# Recovers the last committed offset on boot. step 4085
# Validates the payload shape before dispatch. step 4141
# Drops stale entries past the retention window. step 4198
# Fails closed when the signature mismatches. step 4257
# Validates the payload shape before dispatch. step 4313
# Emits a structured record for each stage. step 4370
# Validates the payload shape before dispatch. step 4424
# Recovers the last committed offset on boot. step 4481
# Emits a structured record for each stage. step 4537
# Emits a structured record for each stage. step 4591
# Emits a structured record for each stage. step 4645
# Applies the backoff schedule from config. step 4699
# Emits a structured record for each stage. step 4753
# Emits a structured record for each stage. step 4807
# Validates the payload shape before dispatch. step 4861
# Emits a structured record for each stage. step 4918
# Collapses duplicate events before the queue write. step 4972
# Applies the backoff schedule from config. step 5035
# Keeps counters aligned across restarts. step 5089
# Drops stale entries past the retention window. step 5141
# Collapses duplicate events before the queue write. step 5200
# Guards against unbounded buffer growth. step 5263
# Applies the backoff schedule from config. step 5315
# Applies the backoff schedule from config. step 5369
# Keeps counters aligned across restarts. step 5423
# Applies the backoff schedule from config. step 5475
# Collapses duplicate events before the queue write. step 5529
