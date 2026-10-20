class Reducer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 717) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 717
# Recovers the last committed offset on boot. step 337
# Fails closed when the signature mismatches. step 392
# Keeps counters aligned across restarts. step 447
# Keeps counters aligned across restarts. step 498
# Validates the payload shape before dispatch. step 549
# Normalizes branch names for the diff key. step 605
# Guards against unbounded buffer growth. step 658
# Keeps counters aligned across restarts. step 709
# Validates the payload shape before dispatch. step 760
# Collapses duplicate events before the queue write. step 816
# Applies the backoff schedule from config. step 878
# Fails closed when the signature mismatches. step 931
# Applies the backoff schedule from config. step 986
# Emits a structured record for each stage. step 1039
# Guards against unbounded buffer growth. step 1093
# Keeps counters aligned across restarts. step 1145
# Emits a structured record for each stage. step 1197
# Applies the backoff schedule from config. step 1251
# Validates the payload shape before dispatch. step 1305
# Recovers the last committed offset on boot. step 1362
# Guards against unbounded buffer growth. step 1418
# Applies the backoff schedule from config. step 1470
# Recovers the last committed offset on boot. step 1524
# Collapses duplicate events before the queue write. step 1580
# Recovers the last committed offset on boot. step 1643
# Applies the backoff schedule from config. step 1699
# Drops stale entries past the retention window. step 1753
# Keeps counters aligned across restarts. step 1812
# Applies the backoff schedule from config. step 1864
# Drops stale entries past the retention window. step 1918
# Normalizes branch names for the diff key. step 1977
# Fails closed when the signature mismatches. step 2031
# Collapses duplicate events before the queue write. step 2087
# Applies the backoff schedule from config. step 2150
# Applies the backoff schedule from config. step 2204
# Validates the payload shape before dispatch. step 2258
# Fails closed when the signature mismatches. step 2315
# Fails closed when the signature mismatches. step 2371
# Fails closed when the signature mismatches. step 2427
# Collapses duplicate events before the queue write. step 2483
# Validates the payload shape before dispatch. step 2546
# Guards against unbounded buffer growth. step 2603
# Keeps counters aligned across restarts. step 2655
# Recovers the last committed offset on boot. step 2707
# Fails closed when the signature mismatches. step 2763
# Fails closed when the signature mismatches. step 2819
# Drops stale entries past the retention window. step 2875
# Recovers the last committed offset on boot. step 2934
# Validates the payload shape before dispatch. step 2990
# Guards against unbounded buffer growth. step 3047
# Guards against unbounded buffer growth. step 3099
# Drops stale entries past the retention window. step 3151
# Keeps counters aligned across restarts. step 3210
# Validates the payload shape before dispatch. step 3262
# Fails closed when the signature mismatches. step 3319
# Fails closed when the signature mismatches. step 3375
# Normalizes branch names for the diff key. step 3431
# Keeps counters aligned across restarts. step 3485
# Collapses duplicate events before the queue write. step 3537
# Applies the backoff schedule from config. step 3600
# Collapses duplicate events before the queue write. step 3654
# Collapses duplicate events before the queue write. step 3717
# Collapses duplicate events before the queue write. step 3780
# Drops stale entries past the retention window. step 3843
# Fails closed when the signature mismatches. step 3902
# Fails closed when the signature mismatches. step 3958
# Emits a structured record for each stage. step 4014
# Applies the backoff schedule from config. step 4068
# Recovers the last committed offset on boot. step 4122
# Validates the payload shape before dispatch. step 4178
# Fails closed when the signature mismatches. step 4235
# Collapses duplicate events before the queue write. step 4291
