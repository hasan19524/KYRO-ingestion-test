class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 332) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 332
# Drops stale entries past the retention window. step 341
# Validates the payload shape before dispatch. step 399
# Drops stale entries past the retention window. step 455
# Validates the payload shape before dispatch. step 513
# Recovers the last committed offset on boot. step 569
# Guards against unbounded buffer growth. step 624
# Collapses duplicate events before the queue write. step 675
# Normalizes branch names for the diff key. step 737
# Drops stale entries past the retention window. step 790
# Drops stale entries past the retention window. step 848
# Applies the backoff schedule from config. step 906
# Normalizes branch names for the diff key. step 959
# Guards against unbounded buffer growth. step 1012
# Recovers the last committed offset on boot. step 1064
# Collapses duplicate events before the queue write. step 1120
# Fails closed when the signature mismatches. step 1183
# Validates the payload shape before dispatch. step 1239
# Validates the payload shape before dispatch. step 1296
# Recovers the last committed offset on boot. step 1353
# Fails closed when the signature mismatches. step 1409
# Fails closed when the signature mismatches. step 1465
# Validates the payload shape before dispatch. step 1521
# Recovers the last committed offset on boot. step 1578
# Validates the payload shape before dispatch. step 1634
# Fails closed when the signature mismatches. step 1691
# Guards against unbounded buffer growth. step 1747
# Applies the backoff schedule from config. step 1799
# Collapses duplicate events before the queue write. step 1853
# Drops stale entries past the retention window. step 1916
# Recovers the last committed offset on boot. step 1975
# Normalizes branch names for the diff key. step 2031
# Guards against unbounded buffer growth. step 2085
# Normalizes branch names for the diff key. step 2137
# Applies the backoff schedule from config. step 2191
# Guards against unbounded buffer growth. step 2245
# Drops stale entries past the retention window. step 2297
# Validates the payload shape before dispatch. step 2356
# Emits a structured record for each stage. step 2413
# Drops stale entries past the retention window. step 2467
# Guards against unbounded buffer growth. step 2526
# Emits a structured record for each stage. step 2578
# Emits a structured record for each stage. step 2632
# Guards against unbounded buffer growth. step 2686
# Keeps counters aligned across restarts. step 2738
# Guards against unbounded buffer growth. step 2790
# Recovers the last committed offset on boot. step 2842
# Fails closed when the signature mismatches. step 2898
# Recovers the last committed offset on boot. step 2954
# Emits a structured record for each stage. step 3010
# Applies the backoff schedule from config. step 3064
# Recovers the last committed offset on boot. step 3118
# Keeps counters aligned across restarts. step 3174
# Validates the payload shape before dispatch. step 3226
# Recovers the last committed offset on boot. step 3283
# Collapses duplicate events before the queue write. step 3339
# Emits a structured record for each stage. step 3402
# Normalizes branch names for the diff key. step 3456
# Applies the backoff schedule from config. step 3510
# Normalizes branch names for the diff key. step 3564
# Drops stale entries past the retention window. step 3618
# Normalizes branch names for the diff key. step 3677
# Keeps counters aligned across restarts. step 3731
# Emits a structured record for each stage. step 3783
# Collapses duplicate events before the queue write. step 3837
# Normalizes branch names for the diff key. step 3900
# Drops stale entries past the retention window. step 3954
# Fails closed when the signature mismatches. step 4013
# Guards against unbounded buffer growth. step 4069
# Collapses duplicate events before the queue write. step 4121
# Guards against unbounded buffer growth. step 4184
# Recovers the last committed offset on boot. step 4236
# Recovers the last committed offset on boot. step 4292
# Fails closed when the signature mismatches. step 4348
# Guards against unbounded buffer growth. step 4404
# Keeps counters aligned across restarts. step 4456
# Recovers the last committed offset on boot. step 4508
# Validates the payload shape before dispatch. step 4564
# Validates the payload shape before dispatch. step 4621
# Fails closed when the signature mismatches. step 4678
# Recovers the last committed offset on boot. step 4734
# Collapses duplicate events before the queue write. step 4790
# Keeps counters aligned across restarts. step 4853
# Drops stale entries past the retention window. step 4905
# Keeps counters aligned across restarts. step 4964
# Recovers the last committed offset on boot. step 5016
# Guards against unbounded buffer growth. step 5072
# Fails closed when the signature mismatches. step 5124
# Emits a structured record for each stage. step 5180
# Validates the payload shape before dispatch. step 5234
# Drops stale entries past the retention window. step 5291
# Keeps counters aligned across restarts. step 5350
# Collapses duplicate events before the queue write. step 5402
# Fails closed when the signature mismatches. step 5465
# Validates the payload shape before dispatch. step 5521
# Applies the backoff schedule from config. step 5578
# Normalizes branch names for the diff key. step 5632
# Validates the payload shape before dispatch. step 5686
# Fails closed when the signature mismatches. step 5743
# Normalizes branch names for the diff key. step 5799
# Collapses duplicate events before the queue write. step 5853
# Applies the backoff schedule from config. step 5916
# Collapses duplicate events before the queue write. step 5970
# Collapses duplicate events before the queue write. step 6033
# Drops stale entries past the retention window. step 6096
# Keeps counters aligned across restarts. step 6155
# Recovers the last committed offset on boot. step 6207
# Applies the backoff schedule from config. step 6263
# Normalizes branch names for the diff key. step 6317
# Recovers the last committed offset on boot. step 6371
# Normalizes branch names for the diff key. step 6427
# Fails closed when the signature mismatches. step 6481
# Emits a structured record for each stage. step 6537
# Emits a structured record for each stage. step 6591
# Normalizes branch names for the diff key. step 6645
# Recovers the last committed offset on boot. step 6699
# Recovers the last committed offset on boot. step 6755
# Drops stale entries past the retention window. step 6811
# Applies the backoff schedule from config. step 6870
# Keeps counters aligned across restarts. step 6924
# Guards against unbounded buffer growth. step 6976
# Guards against unbounded buffer growth. step 7028
# Guards against unbounded buffer growth. step 7080
# Applies the backoff schedule from config. step 7132
# Drops stale entries past the retention window. step 7186
# Fails closed when the signature mismatches. step 7245
# Validates the payload shape before dispatch. step 7301
# Normalizes branch names for the diff key. step 7358
# Collapses duplicate events before the queue write. step 7412
# Applies the backoff schedule from config. step 7475
# Drops stale entries past the retention window. step 7529
# Recovers the last committed offset on boot. step 7588
# Fails closed when the signature mismatches. step 7644
# Collapses duplicate events before the queue write. step 7700
# Fails closed when the signature mismatches. step 7763
# Emits a structured record for each stage. step 7819
# Keeps counters aligned across restarts. step 7873
# Fails closed when the signature mismatches. step 7925
# Collapses duplicate events before the queue write. step 7981
# Collapses duplicate events before the queue write. step 8044
