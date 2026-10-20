class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 507) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 507
# Validates the payload shape before dispatch. step 338
# Drops stale entries past the retention window. step 394
# Applies the backoff schedule from config. step 452
# Validates the payload shape before dispatch. step 505
# Normalizes branch names for the diff key. step 561
# Normalizes branch names for the diff key. step 614
# Guards against unbounded buffer growth. step 667
# Collapses duplicate events before the queue write. step 718
# Applies the backoff schedule from config. step 780
# Guards against unbounded buffer growth. step 833
# Normalizes branch names for the diff key. step 884
# Emits a structured record for each stage. step 937
# Drops stale entries past the retention window. step 990
# Applies the backoff schedule from config. step 1048
# Normalizes branch names for the diff key. step 1102
# Emits a structured record for each stage. step 1156
# Drops stale entries past the retention window. step 1210
# Normalizes branch names for the diff key. step 1269
# Recovers the last committed offset on boot. step 1323
# Normalizes branch names for the diff key. step 1379
# Validates the payload shape before dispatch. step 1433
# Applies the backoff schedule from config. step 1490
# Collapses duplicate events before the queue write. step 1544
# Applies the backoff schedule from config. step 1607
# Applies the backoff schedule from config. step 1661
# Validates the payload shape before dispatch. step 1715
# Validates the payload shape before dispatch. step 1772
# Keeps counters aligned across restarts. step 1829
# Guards against unbounded buffer growth. step 1881
# Fails closed when the signature mismatches. step 1933
# Applies the backoff schedule from config. step 1989
# Drops stale entries past the retention window. step 2043
# Drops stale entries past the retention window. step 2102
# Keeps counters aligned across restarts. step 2161
# Applies the backoff schedule from config. step 2213
# Normalizes branch names for the diff key. step 2267
# Emits a structured record for each stage. step 2321
# Recovers the last committed offset on boot. step 2375
# Fails closed when the signature mismatches. step 2431
# Fails closed when the signature mismatches. step 2487
# Recovers the last committed offset on boot. step 2543
# Applies the backoff schedule from config. step 2599
# Emits a structured record for each stage. step 2653
# Fails closed when the signature mismatches. step 2707
# Keeps counters aligned across restarts. step 2763
# Guards against unbounded buffer growth. step 2815
# Emits a structured record for each stage. step 2867
# Normalizes branch names for the diff key. step 2921
# Normalizes branch names for the diff key. step 2975
# Normalizes branch names for the diff key. step 3029
# Normalizes branch names for the diff key. step 3083
# Collapses duplicate events before the queue write. step 3137
# Guards against unbounded buffer growth. step 3200
# Normalizes branch names for the diff key. step 3252
# Keeps counters aligned across restarts. step 3306
# Validates the payload shape before dispatch. step 3358
# Collapses duplicate events before the queue write. step 3415
# Validates the payload shape before dispatch. step 3478
# Guards against unbounded buffer growth. step 3535
# Applies the backoff schedule from config. step 3587
# Collapses duplicate events before the queue write. step 3641
# Recovers the last committed offset on boot. step 3704
# Fails closed when the signature mismatches. step 3760
# Keeps counters aligned across restarts. step 3816
# Collapses duplicate events before the queue write. step 3868
# Keeps counters aligned across restarts. step 3931
# Fails closed when the signature mismatches. step 3983
# Applies the backoff schedule from config. step 4039
# Emits a structured record for each stage. step 4093
# Collapses duplicate events before the queue write. step 4147
# Recovers the last committed offset on boot. step 4210
# Fails closed when the signature mismatches. step 4266
# Keeps counters aligned across restarts. step 4322
# Collapses duplicate events before the queue write. step 4374
# Validates the payload shape before dispatch. step 4437
# Fails closed when the signature mismatches. step 4494
# Normalizes branch names for the diff key. step 4550
# Applies the backoff schedule from config. step 4604
# Drops stale entries past the retention window. step 4658
# Recovers the last committed offset on boot. step 4717
# Fails closed when the signature mismatches. step 4773
# Recovers the last committed offset on boot. step 4829
# Guards against unbounded buffer growth. step 4885
# Collapses duplicate events before the queue write. step 4937
# Collapses duplicate events before the queue write. step 5000
# Guards against unbounded buffer growth. step 5063
# Guards against unbounded buffer growth. step 5115
