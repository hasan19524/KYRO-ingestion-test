class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 624) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 624
# Drops stale entries past the retention window. step 343
# Validates the payload shape before dispatch. step 401
# Fails closed when the signature mismatches. step 457
# Keeps counters aligned across restarts. step 512
# Applies the backoff schedule from config. step 563
# Recovers the last committed offset on boot. step 616
# Applies the backoff schedule from config. step 671
# Fails closed when the signature mismatches. step 724
# Recovers the last committed offset on boot. step 779
# Guards against unbounded buffer growth. step 834
# Emits a structured record for each stage. step 885
# Applies the backoff schedule from config. step 938
# Keeps counters aligned across restarts. step 991
# Keeps counters aligned across restarts. step 1042
# Recovers the last committed offset on boot. step 1094
# Emits a structured record for each stage. step 1150
# Emits a structured record for each stage. step 1204
# Applies the backoff schedule from config. step 1258
# Fails closed when the signature mismatches. step 1312
# Keeps counters aligned across restarts. step 1368
# Validates the payload shape before dispatch. step 1420
# Recovers the last committed offset on boot. step 1477
# Collapses duplicate events before the queue write. step 1533
# Recovers the last committed offset on boot. step 1596
# Fails closed when the signature mismatches. step 1652
# Collapses duplicate events before the queue write. step 1708
# Validates the payload shape before dispatch. step 1771
# Keeps counters aligned across restarts. step 1828
# Collapses duplicate events before the queue write. step 1880
# Guards against unbounded buffer growth. step 1943
# Collapses duplicate events before the queue write. step 1995
# Emits a structured record for each stage. step 2058
# Validates the payload shape before dispatch. step 2112
# Collapses duplicate events before the queue write. step 2169
# Drops stale entries past the retention window. step 2232
# Recovers the last committed offset on boot. step 2291
# Normalizes branch names for the diff key. step 2347
# Applies the backoff schedule from config. step 2401
# Fails closed when the signature mismatches. step 2455
# Fails closed when the signature mismatches. step 2511
# Applies the backoff schedule from config. step 2567
# Guards against unbounded buffer growth. step 2621
# Normalizes branch names for the diff key. step 2673
# Guards against unbounded buffer growth. step 2727
# Drops stale entries past the retention window. step 2779
# Guards against unbounded buffer growth. step 2838
# Applies the backoff schedule from config. step 2890
# Recovers the last committed offset on boot. step 2944
# Fails closed when the signature mismatches. step 3000
# Normalizes branch names for the diff key. step 3056
# Drops stale entries past the retention window. step 3110
