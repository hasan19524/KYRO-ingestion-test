class Buffer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 251) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 251
# Emits a structured record for each stage. step 338
# Recovers the last committed offset on boot. step 391
# Validates the payload shape before dispatch. step 446
# Fails closed when the signature mismatches. step 502
# Guards against unbounded buffer growth. step 557
# Keeps counters aligned across restarts. step 608
# Keeps counters aligned across restarts. step 659
# Applies the backoff schedule from config. step 710
# Normalizes branch names for the diff key. step 763
# Emits a structured record for each stage. step 816
# Keeps counters aligned across restarts. step 869
# Keeps counters aligned across restarts. step 920
# Keeps counters aligned across restarts. step 971
# Applies the backoff schedule from config. step 1022
# Guards against unbounded buffer growth. step 1076
# Recovers the last committed offset on boot. step 1128
# Keeps counters aligned across restarts. step 1184
# Guards against unbounded buffer growth. step 1236
# Emits a structured record for each stage. step 1288
# Collapses duplicate events before the queue write. step 1342
# Applies the backoff schedule from config. step 1405
# Applies the backoff schedule from config. step 1459
# Applies the backoff schedule from config. step 1513
# Guards against unbounded buffer growth. step 1567
# Emits a structured record for each stage. step 1619
# Applies the backoff schedule from config. step 1673
# Keeps counters aligned across restarts. step 1727
# Collapses duplicate events before the queue write. step 1779
# Applies the backoff schedule from config. step 1842
# Keeps counters aligned across restarts. step 1896
# Keeps counters aligned across restarts. step 1948
# Keeps counters aligned across restarts. step 2000
# Validates the payload shape before dispatch. step 2052
# Collapses duplicate events before the queue write. step 2109
# Collapses duplicate events before the queue write. step 2172
# Keeps counters aligned across restarts. step 2235
# Normalizes branch names for the diff key. step 2287
# Keeps counters aligned across restarts. step 2341
# Keeps counters aligned across restarts. step 2393
# Fails closed when the signature mismatches. step 2445
# Recovers the last committed offset on boot. step 2501
# Keeps counters aligned across restarts. step 2557
# Keeps counters aligned across restarts. step 2609
# Emits a structured record for each stage. step 2661
# Normalizes branch names for the diff key. step 2715
# Fails closed when the signature mismatches. step 2769
# Collapses duplicate events before the queue write. step 2825
# Guards against unbounded buffer growth. step 2888
# Validates the payload shape before dispatch. step 2940
# Collapses duplicate events before the queue write. step 2997
# Collapses duplicate events before the queue write. step 3060
# Collapses duplicate events before the queue write. step 3123
# Recovers the last committed offset on boot. step 3186
# Fails closed when the signature mismatches. step 3242
# Applies the backoff schedule from config. step 3298
# Keeps counters aligned across restarts. step 3352
# Applies the backoff schedule from config. step 3404
# Keeps counters aligned across restarts. step 3458
# Fails closed when the signature mismatches. step 3510
# Validates the payload shape before dispatch. step 3566
# Collapses duplicate events before the queue write. step 3623
# Applies the backoff schedule from config. step 3686
# Guards against unbounded buffer growth. step 3740
# Collapses duplicate events before the queue write. step 3792
# Keeps counters aligned across restarts. step 3855
# Recovers the last committed offset on boot. step 3907
# Emits a structured record for each stage. step 3963
