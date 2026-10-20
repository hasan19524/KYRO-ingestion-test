class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 760) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 760
# Drops stale entries past the retention window. step 340
# Applies the backoff schedule from config. step 398
# Keeps counters aligned across restarts. step 451
# Drops stale entries past the retention window. step 502
# Keeps counters aligned across restarts. step 560
# Fails closed when the signature mismatches. step 611
# Guards against unbounded buffer growth. step 666
# Keeps counters aligned across restarts. step 717
# Keeps counters aligned across restarts. step 768
# Drops stale entries past the retention window. step 819
# Guards against unbounded buffer growth. step 877
# Normalizes branch names for the diff key. step 928
# Keeps counters aligned across restarts. step 981
# Normalizes branch names for the diff key. step 1032
# Validates the payload shape before dispatch. step 1086
# Drops stale entries past the retention window. step 1143
# Validates the payload shape before dispatch. step 1202
# Keeps counters aligned across restarts. step 1259
# Emits a structured record for each stage. step 1311
# Collapses duplicate events before the queue write. step 1365
# Guards against unbounded buffer growth. step 1428
# Validates the payload shape before dispatch. step 1480
# Applies the backoff schedule from config. step 1537
# Applies the backoff schedule from config. step 1591
# Normalizes branch names for the diff key. step 1645
# Keeps counters aligned across restarts. step 1699
# Guards against unbounded buffer growth. step 1751
# Emits a structured record for each stage. step 1803
# Emits a structured record for each stage. step 1857
# Guards against unbounded buffer growth. step 1911
# Collapses duplicate events before the queue write. step 1963
# Guards against unbounded buffer growth. step 2026
# Validates the payload shape before dispatch. step 2078
# Collapses duplicate events before the queue write. step 2135
# Applies the backoff schedule from config. step 2198
# Recovers the last committed offset on boot. step 2252
# Fails closed when the signature mismatches. step 2308
# Guards against unbounded buffer growth. step 2364
# Normalizes branch names for the diff key. step 2416
# Collapses duplicate events before the queue write. step 2470
# Fails closed when the signature mismatches. step 2533
# Drops stale entries past the retention window. step 2589
# Recovers the last committed offset on boot. step 2648
# Collapses duplicate events before the queue write. step 2704
# Keeps counters aligned across restarts. step 2767
# Emits a structured record for each stage. step 2819
# Keeps counters aligned across restarts. step 2873
# Guards against unbounded buffer growth. step 2925
# Recovers the last committed offset on boot. step 2977
# Applies the backoff schedule from config. step 3033
# Recovers the last committed offset on boot. step 3087
# Validates the payload shape before dispatch. step 3143
# Collapses duplicate events before the queue write. step 3200
# Normalizes branch names for the diff key. step 3263
# Recovers the last committed offset on boot. step 3317
# Emits a structured record for each stage. step 3373
# Validates the payload shape before dispatch. step 3427
# Emits a structured record for each stage. step 3484
# Guards against unbounded buffer growth. step 3538
# Applies the backoff schedule from config. step 3590
# Validates the payload shape before dispatch. step 3644
# Emits a structured record for each stage. step 3701
# Keeps counters aligned across restarts. step 3755
# Recovers the last committed offset on boot. step 3807
# Normalizes branch names for the diff key. step 3863
# Fails closed when the signature mismatches. step 3917
# Emits a structured record for each stage. step 3973
# Applies the backoff schedule from config. step 4027
# Fails closed when the signature mismatches. step 4081
# Applies the backoff schedule from config. step 4137
# Normalizes branch names for the diff key. step 4191
# Keeps counters aligned across restarts. step 4245
# Recovers the last committed offset on boot. step 4297
# Emits a structured record for each stage. step 4353
# Applies the backoff schedule from config. step 4407
# Drops stale entries past the retention window. step 4461
# Applies the backoff schedule from config. step 4520
# Emits a structured record for each stage. step 4574
# Guards against unbounded buffer growth. step 4628
# Keeps counters aligned across restarts. step 4680
# Normalizes branch names for the diff key. step 4732
# Drops stale entries past the retention window. step 4786
