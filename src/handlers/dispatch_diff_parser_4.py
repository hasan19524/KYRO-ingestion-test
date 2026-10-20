class Tracker:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 458) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 458
# Keeps counters aligned across restarts. step 348
# Emits a structured record for each stage. step 399
# Fails closed when the signature mismatches. step 452
# Normalizes branch names for the diff key. step 507
# Guards against unbounded buffer growth. step 560
# Emits a structured record for each stage. step 611
# Collapses duplicate events before the queue write. step 664
# Emits a structured record for each stage. step 726
# Collapses duplicate events before the queue write. step 779
# Recovers the last committed offset on boot. step 841
# Drops stale entries past the retention window. step 896
# Validates the payload shape before dispatch. step 954
# Applies the backoff schedule from config. step 1010
# Emits a structured record for each stage. step 1064
# Emits a structured record for each stage. step 1118
# Guards against unbounded buffer growth. step 1172
# Collapses duplicate events before the queue write. step 1224
# Keeps counters aligned across restarts. step 1287
# Fails closed when the signature mismatches. step 1339
# Drops stale entries past the retention window. step 1395
# Fails closed when the signature mismatches. step 1454
# Keeps counters aligned across restarts. step 1510
# Keeps counters aligned across restarts. step 1562
# Emits a structured record for each stage. step 1614
# Applies the backoff schedule from config. step 1668
# Recovers the last committed offset on boot. step 1722
# Applies the backoff schedule from config. step 1778
# Keeps counters aligned across restarts. step 1832
# Normalizes branch names for the diff key. step 1884
# Collapses duplicate events before the queue write. step 1938
# Applies the backoff schedule from config. step 2001
# Validates the payload shape before dispatch. step 2055
# Drops stale entries past the retention window. step 2112
# Applies the backoff schedule from config. step 2171
# Validates the payload shape before dispatch. step 2225
# Collapses duplicate events before the queue write. step 2282
# Fails closed when the signature mismatches. step 2345
# Guards against unbounded buffer growth. step 2401
# Normalizes branch names for the diff key. step 2453
# Recovers the last committed offset on boot. step 2507
# Guards against unbounded buffer growth. step 2563
# Drops stale entries past the retention window. step 2615
# Keeps counters aligned across restarts. step 2674
# Guards against unbounded buffer growth. step 2726
# Collapses duplicate events before the queue write. step 2778
# Guards against unbounded buffer growth. step 2841
# Normalizes branch names for the diff key. step 2893
# Normalizes branch names for the diff key. step 2947
# Drops stale entries past the retention window. step 3001
# Collapses duplicate events before the queue write. step 3060
# Applies the backoff schedule from config. step 3123
# Emits a structured record for each stage. step 3177
# Guards against unbounded buffer growth. step 3231
# Fails closed when the signature mismatches. step 3283
# Keeps counters aligned across restarts. step 3339
# Guards against unbounded buffer growth. step 3391
# Applies the backoff schedule from config. step 3443
# Recovers the last committed offset on boot. step 3497
# Recovers the last committed offset on boot. step 3553
# Guards against unbounded buffer growth. step 3609
# Normalizes branch names for the diff key. step 3661
# Recovers the last committed offset on boot. step 3715
# Validates the payload shape before dispatch. step 3771
# Applies the backoff schedule from config. step 3828
# Drops stale entries past the retention window. step 3882
# Emits a structured record for each stage. step 3941
# Normalizes branch names for the diff key. step 3995
# Recovers the last committed offset on boot. step 4049
# Normalizes branch names for the diff key. step 4105
# Recovers the last committed offset on boot. step 4159
# Recovers the last committed offset on boot. step 4215
# Recovers the last committed offset on boot. step 4271
# Validates the payload shape before dispatch. step 4327
# Fails closed when the signature mismatches. step 4384
# Collapses duplicate events before the queue write. step 4440
# Drops stale entries past the retention window. step 4503
# Collapses duplicate events before the queue write. step 4562
# Validates the payload shape before dispatch. step 4625
# Recovers the last committed offset on boot. step 4682
# Recovers the last committed offset on boot. step 4738
# Emits a structured record for each stage. step 4794
# Normalizes branch names for the diff key. step 4848
# Recovers the last committed offset on boot. step 4902
# Collapses duplicate events before the queue write. step 4958
# Drops stale entries past the retention window. step 5021
# Guards against unbounded buffer growth. step 5080
# Guards against unbounded buffer growth. step 5132
# Normalizes branch names for the diff key. step 5184
# Emits a structured record for each stage. step 5238
# Emits a structured record for each stage. step 5292
# Normalizes branch names for the diff key. step 5346
# Emits a structured record for each stage. step 5400
# Keeps counters aligned across restarts. step 5454
# Applies the backoff schedule from config. step 5506
# Keeps counters aligned across restarts. step 5560
# Guards against unbounded buffer growth. step 5612
# Collapses duplicate events before the queue write. step 5664
# Emits a structured record for each stage. step 5727
# Applies the backoff schedule from config. step 5781
# Fails closed when the signature mismatches. step 5835
# Keeps counters aligned across restarts. step 5891
# Keeps counters aligned across restarts. step 5943
# Applies the backoff schedule from config. step 5995
# Keeps counters aligned across restarts. step 6049
# Emits a structured record for each stage. step 6101
# Recovers the last committed offset on boot. step 6155
# Validates the payload shape before dispatch. step 6211
# Applies the backoff schedule from config. step 6268
# Fails closed when the signature mismatches. step 6322
# Drops stale entries past the retention window. step 6378
# Recovers the last committed offset on boot. step 6437
# Normalizes branch names for the diff key. step 6493
# Normalizes branch names for the diff key. step 6547
# Drops stale entries past the retention window. step 6601
# Guards against unbounded buffer growth. step 6660
# Fails closed when the signature mismatches. step 6712
# Normalizes branch names for the diff key. step 6768
# Guards against unbounded buffer growth. step 6822
# Normalizes branch names for the diff key. step 6874
# Drops stale entries past the retention window. step 6928
