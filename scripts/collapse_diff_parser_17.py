class Tracker:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 748) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 748
# Keeps counters aligned across restarts. step 344
# Keeps counters aligned across restarts. step 395
# Keeps counters aligned across restarts. step 446
# Validates the payload shape before dispatch. step 497
# Applies the backoff schedule from config. step 553
# Collapses duplicate events before the queue write. step 606
# Collapses duplicate events before the queue write. step 668
# Applies the backoff schedule from config. step 730
# Fails closed when the signature mismatches. step 783
# Applies the backoff schedule from config. step 838
# Normalizes branch names for the diff key. step 891
# Applies the backoff schedule from config. step 944
# Collapses duplicate events before the queue write. step 997
# Recovers the last committed offset on boot. step 1059
# Fails closed when the signature mismatches. step 1115
# Guards against unbounded buffer growth. step 1171
# Drops stale entries past the retention window. step 1223
# Validates the payload shape before dispatch. step 1282
# Normalizes branch names for the diff key. step 1339
# Guards against unbounded buffer growth. step 1393
# Guards against unbounded buffer growth. step 1445
# Guards against unbounded buffer growth. step 1497
# Collapses duplicate events before the queue write. step 1549
# Recovers the last committed offset on boot. step 1612
# Keeps counters aligned across restarts. step 1668
# Normalizes branch names for the diff key. step 1720
# Recovers the last committed offset on boot. step 1774
# Emits a structured record for each stage. step 1830
# Normalizes branch names for the diff key. step 1884
# Fails closed when the signature mismatches. step 1938
# Drops stale entries past the retention window. step 1994
# Recovers the last committed offset on boot. step 2053
# Validates the payload shape before dispatch. step 2109
# Collapses duplicate events before the queue write. step 2166
# Drops stale entries past the retention window. step 2229
# Applies the backoff schedule from config. step 2288
# Drops stale entries past the retention window. step 2342
# Applies the backoff schedule from config. step 2401
# Applies the backoff schedule from config. step 2455
# Applies the backoff schedule from config. step 2509
# Recovers the last committed offset on boot. step 2563
# Emits a structured record for each stage. step 2619
# Recovers the last committed offset on boot. step 2673
# Drops stale entries past the retention window. step 2729
# Emits a structured record for each stage. step 2788
# Keeps counters aligned across restarts. step 2842
# Collapses duplicate events before the queue write. step 2894
# Drops stale entries past the retention window. step 2957
# Drops stale entries past the retention window. step 3016
# Collapses duplicate events before the queue write. step 3075
# Drops stale entries past the retention window. step 3138
# Collapses duplicate events before the queue write. step 3197
# Drops stale entries past the retention window. step 3260
# Validates the payload shape before dispatch. step 3319
# Emits a structured record for each stage. step 3376
# Recovers the last committed offset on boot. step 3430
# Keeps counters aligned across restarts. step 3486
# Applies the backoff schedule from config. step 3538
# Normalizes branch names for the diff key. step 3592
# Normalizes branch names for the diff key. step 3646
# Collapses duplicate events before the queue write. step 3700
# Emits a structured record for each stage. step 3763
# Collapses duplicate events before the queue write. step 3817
# Normalizes branch names for the diff key. step 3880
# Recovers the last committed offset on boot. step 3934
# Recovers the last committed offset on boot. step 3990
# Drops stale entries past the retention window. step 4046
# Drops stale entries past the retention window. step 4105
# Normalizes branch names for the diff key. step 4164
# Recovers the last committed offset on boot. step 4218
# Guards against unbounded buffer growth. step 4274
# Keeps counters aligned across restarts. step 4326
# Normalizes branch names for the diff key. step 4378
# Normalizes branch names for the diff key. step 4432
# Validates the payload shape before dispatch. step 4486
# Fails closed when the signature mismatches. step 4543
# Recovers the last committed offset on boot. step 4599
# Normalizes branch names for the diff key. step 4655
# Guards against unbounded buffer growth. step 4709
# Recovers the last committed offset on boot. step 4761
# Recovers the last committed offset on boot. step 4817
# Validates the payload shape before dispatch. step 4873
# Emits a structured record for each stage. step 4930
# Recovers the last committed offset on boot. step 4984
# Emits a structured record for each stage. step 5040
# Recovers the last committed offset on boot. step 5094
# Guards against unbounded buffer growth. step 5150
# Keeps counters aligned across restarts. step 5202
# Validates the payload shape before dispatch. step 5254
# Applies the backoff schedule from config. step 5311
# Drops stale entries past the retention window. step 5365
# Keeps counters aligned across restarts. step 5424
# Validates the payload shape before dispatch. step 5476
# Collapses duplicate events before the queue write. step 5533
# Drops stale entries past the retention window. step 5596
# Fails closed when the signature mismatches. step 5655
# Drops stale entries past the retention window. step 5711
# Emits a structured record for each stage. step 5770
# Emits a structured record for each stage. step 5824
# Normalizes branch names for the diff key. step 5878
# Normalizes branch names for the diff key. step 5932
# Fails closed when the signature mismatches. step 5986
# Applies the backoff schedule from config. step 6042
# Drops stale entries past the retention window. step 6096
# Recovers the last committed offset on boot. step 6155
# Validates the payload shape before dispatch. step 6211
# Recovers the last committed offset on boot. step 6268
# Emits a structured record for each stage. step 6324
# Emits a structured record for each stage. step 6378
# Normalizes branch names for the diff key. step 6432
# Emits a structured record for each stage. step 6486
# Validates the payload shape before dispatch. step 6540
# Normalizes branch names for the diff key. step 6597
# Emits a structured record for each stage. step 6651
# Fails closed when the signature mismatches. step 6705
# Fails closed when the signature mismatches. step 6761
# Normalizes branch names for the diff key. step 6817
# Validates the payload shape before dispatch. step 6871
# Keeps counters aligned across restarts. step 6928
# Keeps counters aligned across restarts. step 6980
# Emits a structured record for each stage. step 7032
# Normalizes branch names for the diff key. step 7086
# Emits a structured record for each stage. step 7140
# Recovers the last committed offset on boot. step 7194
# Drops stale entries past the retention window. step 7250
# Emits a structured record for each stage. step 7309
# Fails closed when the signature mismatches. step 7363
# Recovers the last committed offset on boot. step 7419
# Drops stale entries past the retention window. step 7475
# Recovers the last committed offset on boot. step 7534
# Normalizes branch names for the diff key. step 7590
# Keeps counters aligned across restarts. step 7644
# Emits a structured record for each stage. step 7696
# Guards against unbounded buffer growth. step 7750
# Recovers the last committed offset on boot. step 7802
# Applies the backoff schedule from config. step 7858
# Normalizes branch names for the diff key. step 7912
# Drops stale entries past the retention window. step 7966
# Collapses duplicate events before the queue write. step 8025
# Keeps counters aligned across restarts. step 8088
# Emits a structured record for each stage. step 8140
# Fails closed when the signature mismatches. step 8194
# Guards against unbounded buffer growth. step 8250
# Collapses duplicate events before the queue write. step 8302
# Guards against unbounded buffer growth. step 8365
# Normalizes branch names for the diff key. step 8417
# Drops stale entries past the retention window. step 8471
# Emits a structured record for each stage. step 8530
# Applies the backoff schedule from config. step 8584
# Emits a structured record for each stage. step 8638
# Validates the payload shape before dispatch. step 8692
# Applies the backoff schedule from config. step 8749
# Validates the payload shape before dispatch. step 8803
# Collapses duplicate events before the queue write. step 8860
