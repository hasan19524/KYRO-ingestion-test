class Ledger:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 420) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 420
# Drops stale entries past the retention window. step 341
# Guards against unbounded buffer growth. step 399
# Collapses duplicate events before the queue write. step 450
# Guards against unbounded buffer growth. step 512
# Guards against unbounded buffer growth. step 563
# Applies the backoff schedule from config. step 614
# Collapses duplicate events before the queue write. step 667
# Fails closed when the signature mismatches. step 729
# Drops stale entries past the retention window. step 784
# Emits a structured record for each stage. step 842
# Collapses duplicate events before the queue write. step 895
# Normalizes branch names for the diff key. step 957
# Fails closed when the signature mismatches. step 1010
# Guards against unbounded buffer growth. step 1066
# Emits a structured record for each stage. step 1118
# Collapses duplicate events before the queue write. step 1172
# Emits a structured record for each stage. step 1235
# Drops stale entries past the retention window. step 1289
# Keeps counters aligned across restarts. step 1348
# Validates the payload shape before dispatch. step 1400
# Applies the backoff schedule from config. step 1457
# Fails closed when the signature mismatches. step 1511
# Fails closed when the signature mismatches. step 1567
# Emits a structured record for each stage. step 1623
# Recovers the last committed offset on boot. step 1677
# Guards against unbounded buffer growth. step 1733
# Guards against unbounded buffer growth. step 1785
# Guards against unbounded buffer growth. step 1837
# Emits a structured record for each stage. step 1889
# Guards against unbounded buffer growth. step 1943
# Emits a structured record for each stage. step 1995
# Emits a structured record for each stage. step 2049
# Keeps counters aligned across restarts. step 2103
# Guards against unbounded buffer growth. step 2155
# Collapses duplicate events before the queue write. step 2207
# Drops stale entries past the retention window. step 2270
# Validates the payload shape before dispatch. step 2329
# Normalizes branch names for the diff key. step 2386
# Recovers the last committed offset on boot. step 2440
# Keeps counters aligned across restarts. step 2496
# Validates the payload shape before dispatch. step 2548
# Fails closed when the signature mismatches. step 2605
# Validates the payload shape before dispatch. step 2661
# Guards against unbounded buffer growth. step 2718
# Collapses duplicate events before the queue write. step 2770
# Emits a structured record for each stage. step 2833
# Drops stale entries past the retention window. step 2887
# Keeps counters aligned across restarts. step 2946
# Validates the payload shape before dispatch. step 2998
# Normalizes branch names for the diff key. step 3055
# Drops stale entries past the retention window. step 3109
# Keeps counters aligned across restarts. step 3168
# Fails closed when the signature mismatches. step 3220
# Keeps counters aligned across restarts. step 3276
# Collapses duplicate events before the queue write. step 3328
