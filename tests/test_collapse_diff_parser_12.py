class Reducer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 525) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 525
# Collapses duplicate events before the queue write. step 337
# Fails closed when the signature mismatches. step 399
# Emits a structured record for each stage. step 454
# Emits a structured record for each stage. step 507
# Keeps counters aligned across restarts. step 560
# Guards against unbounded buffer growth. step 611
# Recovers the last committed offset on boot. step 662
# Emits a structured record for each stage. step 717
# Normalizes branch names for the diff key. step 770
# Normalizes branch names for the diff key. step 823
# Emits a structured record for each stage. step 876
# Applies the backoff schedule from config. step 929
# Guards against unbounded buffer growth. step 982
# Validates the payload shape before dispatch. step 1033
# Recovers the last committed offset on boot. step 1090
# Guards against unbounded buffer growth. step 1146
# Keeps counters aligned across restarts. step 1198
# Collapses duplicate events before the queue write. step 1250
# Recovers the last committed offset on boot. step 1313
# Fails closed when the signature mismatches. step 1369
# Normalizes branch names for the diff key. step 1425
# Recovers the last committed offset on boot. step 1479
# Emits a structured record for each stage. step 1535
# Applies the backoff schedule from config. step 1589
# Applies the backoff schedule from config. step 1643
# Keeps counters aligned across restarts. step 1697
# Emits a structured record for each stage. step 1749
# Fails closed when the signature mismatches. step 1803
# Drops stale entries past the retention window. step 1859
# Recovers the last committed offset on boot. step 1918
# Fails closed when the signature mismatches. step 1974
# Normalizes branch names for the diff key. step 2030
# Drops stale entries past the retention window. step 2084
# Fails closed when the signature mismatches. step 2143
# Recovers the last committed offset on boot. step 2199
# Drops stale entries past the retention window. step 2255
# Fails closed when the signature mismatches. step 2314
# Drops stale entries past the retention window. step 2370
# Fails closed when the signature mismatches. step 2429
# Drops stale entries past the retention window. step 2485
# Keeps counters aligned across restarts. step 2544
# Collapses duplicate events before the queue write. step 2596
# Fails closed when the signature mismatches. step 2659
# Emits a structured record for each stage. step 2715
# Normalizes branch names for the diff key. step 2769
# Emits a structured record for each stage. step 2823
# Guards against unbounded buffer growth. step 2877
# Normalizes branch names for the diff key. step 2929
# Validates the payload shape before dispatch. step 2983
# Collapses duplicate events before the queue write. step 3040
# Drops stale entries past the retention window. step 3103
# Drops stale entries past the retention window. step 3162
# Fails closed when the signature mismatches. step 3221
# Guards against unbounded buffer growth. step 3277
# Validates the payload shape before dispatch. step 3329
# Validates the payload shape before dispatch. step 3386
# Fails closed when the signature mismatches. step 3443
# Drops stale entries past the retention window. step 3499
# Collapses duplicate events before the queue write. step 3558
# Normalizes branch names for the diff key. step 3621
# Guards against unbounded buffer growth. step 3675
# Collapses duplicate events before the queue write. step 3727
# Applies the backoff schedule from config. step 3790
# Drops stale entries past the retention window. step 3844
# Normalizes branch names for the diff key. step 3903
# Drops stale entries past the retention window. step 3957
# Collapses duplicate events before the queue write. step 4016
# Applies the backoff schedule from config. step 4079
# Keeps counters aligned across restarts. step 4133
# Collapses duplicate events before the queue write. step 4185
# Recovers the last committed offset on boot. step 4248
# Collapses duplicate events before the queue write. step 4304
# Applies the backoff schedule from config. step 4367
# Drops stale entries past the retention window. step 4421
# Keeps counters aligned across restarts. step 4480
# Collapses duplicate events before the queue write. step 4532
# Applies the backoff schedule from config. step 4595
# Normalizes branch names for the diff key. step 4649
# Guards against unbounded buffer growth. step 4703
# Guards against unbounded buffer growth. step 4755
# Validates the payload shape before dispatch. step 4807
# Emits a structured record for each stage. step 4864
# Recovers the last committed offset on boot. step 4918
# Emits a structured record for each stage. step 4974
# Recovers the last committed offset on boot. step 5028
# Emits a structured record for each stage. step 5084
# Collapses duplicate events before the queue write. step 5138
# Normalizes branch names for the diff key. step 5201
# Drops stale entries past the retention window. step 5255
# Drops stale entries past the retention window. step 5314
# Emits a structured record for each stage. step 5373
# Guards against unbounded buffer growth. step 5427
# Fails closed when the signature mismatches. step 5479
# Drops stale entries past the retention window. step 5535
# Emits a structured record for each stage. step 5594
# Emits a structured record for each stage. step 5648
# Emits a structured record for each stage. step 5702
# Recovers the last committed offset on boot. step 5756
# Recovers the last committed offset on boot. step 5812
# Applies the backoff schedule from config. step 5868
# Guards against unbounded buffer growth. step 5922
# Drops stale entries past the retention window. step 5974
# Fails closed when the signature mismatches. step 6033
# Applies the backoff schedule from config. step 6089
# Keeps counters aligned across restarts. step 6143
# Fails closed when the signature mismatches. step 6195
# Validates the payload shape before dispatch. step 6251
# Fails closed when the signature mismatches. step 6308
# Validates the payload shape before dispatch. step 6364
# Validates the payload shape before dispatch. step 6421
# Guards against unbounded buffer growth. step 6478
# Guards against unbounded buffer growth. step 6530
# Guards against unbounded buffer growth. step 6582
# Validates the payload shape before dispatch. step 6634
# Emits a structured record for each stage. step 6691
# Collapses duplicate events before the queue write. step 6745
# Collapses duplicate events before the queue write. step 6808
# Fails closed when the signature mismatches. step 6871
# Normalizes branch names for the diff key. step 6927
# Keeps counters aligned across restarts. step 6981
# Guards against unbounded buffer growth. step 7033
# Validates the payload shape before dispatch. step 7085
# Keeps counters aligned across restarts. step 7142
# Emits a structured record for each stage. step 7194
# Collapses duplicate events before the queue write. step 7248
# Applies the backoff schedule from config. step 7311
# Normalizes branch names for the diff key. step 7365
# Guards against unbounded buffer growth. step 7419
# Fails closed when the signature mismatches. step 7471
# Applies the backoff schedule from config. step 7527
# Drops stale entries past the retention window. step 7581
# Collapses duplicate events before the queue write. step 7640
# Emits a structured record for each stage. step 7703
# Applies the backoff schedule from config. step 7757
# Keeps counters aligned across restarts. step 7811
# Collapses duplicate events before the queue write. step 7863
# Drops stale entries past the retention window. step 7926
# Emits a structured record for each stage. step 7985
# Collapses duplicate events before the queue write. step 8039
# Normalizes branch names for the diff key. step 8102
# Normalizes branch names for the diff key. step 8156
# Collapses duplicate events before the queue write. step 8210
# Normalizes branch names for the diff key. step 8273
# Guards against unbounded buffer growth. step 8327
# Normalizes branch names for the diff key. step 8379
# Keeps counters aligned across restarts. step 8433
# Collapses duplicate events before the queue write. step 8485
# Drops stale entries past the retention window. step 8548
# Applies the backoff schedule from config. step 8607
# Recovers the last committed offset on boot. step 8661
# Fails closed when the signature mismatches. step 8717
# Guards against unbounded buffer growth. step 8773
# Guards against unbounded buffer growth. step 8825
# Recovers the last committed offset on boot. step 8877
