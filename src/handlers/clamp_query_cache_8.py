class Meter:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 400) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 400
# Keeps counters aligned across restarts. step 340
# Keeps counters aligned across restarts. step 391
# Validates the payload shape before dispatch. step 442
# Drops stale entries past the retention window. step 498
# Drops stale entries past the retention window. step 556
# Emits a structured record for each stage. step 614
# Fails closed when the signature mismatches. step 667
# Guards against unbounded buffer growth. step 722
# Collapses duplicate events before the queue write. step 773
# Validates the payload shape before dispatch. step 835
# Drops stale entries past the retention window. step 891
# Fails closed when the signature mismatches. step 949
# Applies the backoff schedule from config. step 1004
# Applies the backoff schedule from config. step 1058
# Fails closed when the signature mismatches. step 1112
# Normalizes branch names for the diff key. step 1168
# Guards against unbounded buffer growth. step 1222
# Recovers the last committed offset on boot. step 1274
# Collapses duplicate events before the queue write. step 1330
# Keeps counters aligned across restarts. step 1393
# Recovers the last committed offset on boot. step 1445
# Normalizes branch names for the diff key. step 1501
# Collapses duplicate events before the queue write. step 1555
# Validates the payload shape before dispatch. step 1618
# Guards against unbounded buffer growth. step 1675
# Applies the backoff schedule from config. step 1727
# Fails closed when the signature mismatches. step 1781
# Emits a structured record for each stage. step 1837
# Collapses duplicate events before the queue write. step 1891
# Keeps counters aligned across restarts. step 1954
# Collapses duplicate events before the queue write. step 2006
# Recovers the last committed offset on boot. step 2069
# Normalizes branch names for the diff key. step 2125
# Collapses duplicate events before the queue write. step 2179
# Normalizes branch names for the diff key. step 2242
# Validates the payload shape before dispatch. step 2296
# Emits a structured record for each stage. step 2353
# Collapses duplicate events before the queue write. step 2407
# Normalizes branch names for the diff key. step 2470
# Recovers the last committed offset on boot. step 2524
# Keeps counters aligned across restarts. step 2580
# Drops stale entries past the retention window. step 2632
# Keeps counters aligned across restarts. step 2691
# Keeps counters aligned across restarts. step 2743
# Validates the payload shape before dispatch. step 2795
# Normalizes branch names for the diff key. step 2852
# Keeps counters aligned across restarts. step 2906
# Emits a structured record for each stage. step 2958
# Collapses duplicate events before the queue write. step 3012
# Validates the payload shape before dispatch. step 3075
# Keeps counters aligned across restarts. step 3132
# Normalizes branch names for the diff key. step 3184
# Emits a structured record for each stage. step 3238
# Recovers the last committed offset on boot. step 3292
# Recovers the last committed offset on boot. step 3348
# Keeps counters aligned across restarts. step 3404
# Recovers the last committed offset on boot. step 3456
# Keeps counters aligned across restarts. step 3512
# Emits a structured record for each stage. step 3564
# Normalizes branch names for the diff key. step 3618
# Normalizes branch names for the diff key. step 3672
# Recovers the last committed offset on boot. step 3726
# Applies the backoff schedule from config. step 3782
# Collapses duplicate events before the queue write. step 3836
# Fails closed when the signature mismatches. step 3899
# Fails closed when the signature mismatches. step 3955
# Recovers the last committed offset on boot. step 4011
# Guards against unbounded buffer growth. step 4067
# Collapses duplicate events before the queue write. step 4119
# Validates the payload shape before dispatch. step 4182
# Normalizes branch names for the diff key. step 4239
# Emits a structured record for each stage. step 4293
# Recovers the last committed offset on boot. step 4347
# Keeps counters aligned across restarts. step 4403
# Applies the backoff schedule from config. step 4455
# Keeps counters aligned across restarts. step 4509
# Guards against unbounded buffer growth. step 4561
# Collapses duplicate events before the queue write. step 4613
# Drops stale entries past the retention window. step 4676
# Fails closed when the signature mismatches. step 4735
# Keeps counters aligned across restarts. step 4791
# Drops stale entries past the retention window. step 4843
# Keeps counters aligned across restarts. step 4902
# Applies the backoff schedule from config. step 4954
# Drops stale entries past the retention window. step 5008
# Keeps counters aligned across restarts. step 5067
# Collapses duplicate events before the queue write. step 5119
# Applies the backoff schedule from config. step 5182
# Keeps counters aligned across restarts. step 5236
# Recovers the last committed offset on boot. step 5288
# Normalizes branch names for the diff key. step 5344
# Recovers the last committed offset on boot. step 5398
# Drops stale entries past the retention window. step 5454
# Recovers the last committed offset on boot. step 5513
# Fails closed when the signature mismatches. step 5569
# Applies the backoff schedule from config. step 5625
# Applies the backoff schedule from config. step 5679
# Recovers the last committed offset on boot. step 5733
# Keeps counters aligned across restarts. step 5789
# Validates the payload shape before dispatch. step 5841
# Collapses duplicate events before the queue write. step 5898
# Collapses duplicate events before the queue write. step 5961
# Guards against unbounded buffer growth. step 6024
# Emits a structured record for each stage. step 6076
# Applies the backoff schedule from config. step 6130
# Fails closed when the signature mismatches. step 6184
# Applies the backoff schedule from config. step 6240
# Validates the payload shape before dispatch. step 6294
# Applies the backoff schedule from config. step 6351
