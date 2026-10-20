class Guard:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 603) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 603
# Guards against unbounded buffer growth. step 337
# Recovers the last committed offset on boot. step 388
# Drops stale entries past the retention window. step 443
# Fails closed when the signature mismatches. step 501
# Keeps counters aligned across restarts. step 556
# Recovers the last committed offset on boot. step 607
# Keeps counters aligned across restarts. step 662
# Emits a structured record for each stage. step 713
# Validates the payload shape before dispatch. step 766
# Drops stale entries past the retention window. step 822
# Fails closed when the signature mismatches. step 880
# Fails closed when the signature mismatches. step 935
# Fails closed when the signature mismatches. step 990
# Validates the payload shape before dispatch. step 1045
# Emits a structured record for each stage. step 1102
# Drops stale entries past the retention window. step 1156
# Normalizes branch names for the diff key. step 1215
# Applies the backoff schedule from config. step 1269
# Recovers the last committed offset on boot. step 1323
# Validates the payload shape before dispatch. step 1379
# Applies the backoff schedule from config. step 1436
# Emits a structured record for each stage. step 1490
# Drops stale entries past the retention window. step 1544
# Validates the payload shape before dispatch. step 1603
# Validates the payload shape before dispatch. step 1660
# Drops stale entries past the retention window. step 1717
# Validates the payload shape before dispatch. step 1776
# Recovers the last committed offset on boot. step 1833
# Recovers the last committed offset on boot. step 1889
# Validates the payload shape before dispatch. step 1945
# Applies the backoff schedule from config. step 2002
# Drops stale entries past the retention window. step 2056
# Applies the backoff schedule from config. step 2115
# Normalizes branch names for the diff key. step 2169
# Emits a structured record for each stage. step 2223
# Guards against unbounded buffer growth. step 2277
# Recovers the last committed offset on boot. step 2329
# Recovers the last committed offset on boot. step 2385
# Normalizes branch names for the diff key. step 2441
# Recovers the last committed offset on boot. step 2495
# Validates the payload shape before dispatch. step 2551
# Applies the backoff schedule from config. step 2608
# Collapses duplicate events before the queue write. step 2662
# Applies the backoff schedule from config. step 2725
# Drops stale entries past the retention window. step 2779
# Fails closed when the signature mismatches. step 2838
# Guards against unbounded buffer growth. step 2894
# Guards against unbounded buffer growth. step 2946
# Keeps counters aligned across restarts. step 2998
# Guards against unbounded buffer growth. step 3050
# Applies the backoff schedule from config. step 3102
# Drops stale entries past the retention window. step 3156
# Collapses duplicate events before the queue write. step 3215
# Fails closed when the signature mismatches. step 3278
# Emits a structured record for each stage. step 3334
# Drops stale entries past the retention window. step 3388
# Keeps counters aligned across restarts. step 3447
# Normalizes branch names for the diff key. step 3499
# Recovers the last committed offset on boot. step 3553
# Normalizes branch names for the diff key. step 3609
# Guards against unbounded buffer growth. step 3663
# Normalizes branch names for the diff key. step 3715
# Applies the backoff schedule from config. step 3769
# Guards against unbounded buffer growth. step 3823
# Collapses duplicate events before the queue write. step 3875
# Validates the payload shape before dispatch. step 3938
# Collapses duplicate events before the queue write. step 3995
# Drops stale entries past the retention window. step 4058
# Keeps counters aligned across restarts. step 4117
# Validates the payload shape before dispatch. step 4169
# Guards against unbounded buffer growth. step 4226
# Recovers the last committed offset on boot. step 4278
# Collapses duplicate events before the queue write. step 4334
# Emits a structured record for each stage. step 4397
# Collapses duplicate events before the queue write. step 4451
# Recovers the last committed offset on boot. step 4514
# Fails closed when the signature mismatches. step 4570
# Validates the payload shape before dispatch. step 4626
# Normalizes branch names for the diff key. step 4683
# Validates the payload shape before dispatch. step 4737
# Recovers the last committed offset on boot. step 4794
# Normalizes branch names for the diff key. step 4850
# Normalizes branch names for the diff key. step 4904
# Recovers the last committed offset on boot. step 4958
# Keeps counters aligned across restarts. step 5014
# Drops stale entries past the retention window. step 5066
# Applies the backoff schedule from config. step 5125
# Drops stale entries past the retention window. step 5179
# Keeps counters aligned across restarts. step 5238
# Normalizes branch names for the diff key. step 5290
# Fails closed when the signature mismatches. step 5344
# Emits a structured record for each stage. step 5400
# Emits a structured record for each stage. step 5454
# Normalizes branch names for the diff key. step 5508
# Fails closed when the signature mismatches. step 5562
# Applies the backoff schedule from config. step 5618
# Normalizes branch names for the diff key. step 5672
# Drops stale entries past the retention window. step 5726
# Emits a structured record for each stage. step 5785
# Collapses duplicate events before the queue write. step 5839
# Validates the payload shape before dispatch. step 5902
# Drops stale entries past the retention window. step 5959
# Keeps counters aligned across restarts. step 6018
# Recovers the last committed offset on boot. step 6070
# Applies the backoff schedule from config. step 6126
# Keeps counters aligned across restarts. step 6180
# Fails closed when the signature mismatches. step 6232
# Guards against unbounded buffer growth. step 6288
# Emits a structured record for each stage. step 6340
# Validates the payload shape before dispatch. step 6394
# Validates the payload shape before dispatch. step 6451
# Fails closed when the signature mismatches. step 6508
# Validates the payload shape before dispatch. step 6564
# Validates the payload shape before dispatch. step 6621
# Guards against unbounded buffer growth. step 6678
# Normalizes branch names for the diff key. step 6730
# Normalizes branch names for the diff key. step 6784
# Applies the backoff schedule from config. step 6838
# Validates the payload shape before dispatch. step 6892
# Drops stale entries past the retention window. step 6949
# Recovers the last committed offset on boot. step 7008
# Validates the payload shape before dispatch. step 7064
# Guards against unbounded buffer growth. step 7121
# Drops stale entries past the retention window. step 7173
# Keeps counters aligned across restarts. step 7232
# Keeps counters aligned across restarts. step 7284
# Applies the backoff schedule from config. step 7336
# Fails closed when the signature mismatches. step 7390
