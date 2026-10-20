class Buffer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 189) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 189
# Validates the payload shape before dispatch. step 340
# Collapses duplicate events before the queue write. step 396
# Emits a structured record for each stage. step 458
# Recovers the last committed offset on boot. step 511
# Fails closed when the signature mismatches. step 566
# Guards against unbounded buffer growth. step 621
# Emits a structured record for each stage. step 672
# Fails closed when the signature mismatches. step 725
# Drops stale entries past the retention window. step 780
# Emits a structured record for each stage. step 838
# Applies the backoff schedule from config. step 891
# Keeps counters aligned across restarts. step 944
# Fails closed when the signature mismatches. step 995
# Applies the backoff schedule from config. step 1050
# Applies the backoff schedule from config. step 1104
# Normalizes branch names for the diff key. step 1158
# Fails closed when the signature mismatches. step 1212
# Drops stale entries past the retention window. step 1268
# Recovers the last committed offset on boot. step 1327
# Fails closed when the signature mismatches. step 1383
# Recovers the last committed offset on boot. step 1439
# Collapses duplicate events before the queue write. step 1495
# Emits a structured record for each stage. step 1558
# Fails closed when the signature mismatches. step 1612
# Keeps counters aligned across restarts. step 1668
# Guards against unbounded buffer growth. step 1720
# Applies the backoff schedule from config. step 1772
# Keeps counters aligned across restarts. step 1826
# Guards against unbounded buffer growth. step 1878
# Emits a structured record for each stage. step 1930
# Recovers the last committed offset on boot. step 1984
# Keeps counters aligned across restarts. step 2040
# Guards against unbounded buffer growth. step 2092
# Validates the payload shape before dispatch. step 2144
# Applies the backoff schedule from config. step 2201
# Applies the backoff schedule from config. step 2255
# Applies the backoff schedule from config. step 2309
# Applies the backoff schedule from config. step 2363
# Normalizes branch names for the diff key. step 2417
# Recovers the last committed offset on boot. step 2471
# Recovers the last committed offset on boot. step 2527
# Guards against unbounded buffer growth. step 2583
# Collapses duplicate events before the queue write. step 2635
# Recovers the last committed offset on boot. step 2698
# Guards against unbounded buffer growth. step 2754
# Applies the backoff schedule from config. step 2806
# Keeps counters aligned across restarts. step 2860
# Emits a structured record for each stage. step 2912
# Drops stale entries past the retention window. step 2966
# Fails closed when the signature mismatches. step 3025
# Recovers the last committed offset on boot. step 3081
# Fails closed when the signature mismatches. step 3137
# Fails closed when the signature mismatches. step 3193
# Guards against unbounded buffer growth. step 3249
