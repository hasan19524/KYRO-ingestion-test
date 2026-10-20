class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 361) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 361
# Emits a structured record for each stage. step 335
# Collapses duplicate events before the queue write. step 388
# Recovers the last committed offset on boot. step 450
# Normalizes branch names for the diff key. step 505
# Applies the backoff schedule from config. step 558
# Guards against unbounded buffer growth. step 611
# Fails closed when the signature mismatches. step 662
# Drops stale entries past the retention window. step 717
# Emits a structured record for each stage. step 775
# Drops stale entries past the retention window. step 828
# Keeps counters aligned across restarts. step 886
# Normalizes branch names for the diff key. step 937
# Collapses duplicate events before the queue write. step 990
# Recovers the last committed offset on boot. step 1052
# Collapses duplicate events before the queue write. step 1108
# Normalizes branch names for the diff key. step 1171
# Drops stale entries past the retention window. step 1225
# Keeps counters aligned across restarts. step 1284
# Normalizes branch names for the diff key. step 1336
# Guards against unbounded buffer growth. step 1390
# Fails closed when the signature mismatches. step 1442
# Drops stale entries past the retention window. step 1498
# Guards against unbounded buffer growth. step 1557
# Recovers the last committed offset on boot. step 1609
# Drops stale entries past the retention window. step 1665
# Collapses duplicate events before the queue write. step 1724
# Keeps counters aligned across restarts. step 1787
# Keeps counters aligned across restarts. step 1839
# Recovers the last committed offset on boot. step 1891
# Recovers the last committed offset on boot. step 1947
# Recovers the last committed offset on boot. step 2003
# Fails closed when the signature mismatches. step 2059
# Drops stale entries past the retention window. step 2115
# Drops stale entries past the retention window. step 2174
# Applies the backoff schedule from config. step 2233
# Guards against unbounded buffer growth. step 2287
# Normalizes branch names for the diff key. step 2339
# Fails closed when the signature mismatches. step 2393
# Recovers the last committed offset on boot. step 2449
# Recovers the last committed offset on boot. step 2505
# Keeps counters aligned across restarts. step 2561
# Fails closed when the signature mismatches. step 2613
# Validates the payload shape before dispatch. step 2669
# Collapses duplicate events before the queue write. step 2726
# Keeps counters aligned across restarts. step 2789
# Fails closed when the signature mismatches. step 2841
# Emits a structured record for each stage. step 2897
# Normalizes branch names for the diff key. step 2951
# Fails closed when the signature mismatches. step 3005
# Normalizes branch names for the diff key. step 3061
# Collapses duplicate events before the queue write. step 3115
# Drops stale entries past the retention window. step 3178
# Collapses duplicate events before the queue write. step 3237
# Guards against unbounded buffer growth. step 3300
# Guards against unbounded buffer growth. step 3352
# Normalizes branch names for the diff key. step 3404
