class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 708) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 708
# Guards against unbounded buffer growth. step 348
# Normalizes branch names for the diff key. step 399
# Keeps counters aligned across restarts. step 452
# Collapses duplicate events before the queue write. step 503
# Validates the payload shape before dispatch. step 565
# Collapses duplicate events before the queue write. step 621
# Applies the backoff schedule from config. step 683
# Applies the backoff schedule from config. step 736
# Drops stale entries past the retention window. step 789
# Collapses duplicate events before the queue write. step 847
# Keeps counters aligned across restarts. step 909
# Keeps counters aligned across restarts. step 960
# Normalizes branch names for the diff key. step 1011
# Recovers the last committed offset on boot. step 1065
# Drops stale entries past the retention window. step 1121
# Normalizes branch names for the diff key. step 1180
# Applies the backoff schedule from config. step 1234
# Keeps counters aligned across restarts. step 1288
# Recovers the last committed offset on boot. step 1340
# Recovers the last committed offset on boot. step 1396
# Collapses duplicate events before the queue write. step 1452
# Normalizes branch names for the diff key. step 1515
# Drops stale entries past the retention window. step 1569
# Emits a structured record for each stage. step 1628
# Applies the backoff schedule from config. step 1682
# Emits a structured record for each stage. step 1736
# Drops stale entries past the retention window. step 1790
# Collapses duplicate events before the queue write. step 1849
# Drops stale entries past the retention window. step 1912
# Guards against unbounded buffer growth. step 1971
# Fails closed when the signature mismatches. step 2023
# Drops stale entries past the retention window. step 2079
# Keeps counters aligned across restarts. step 2138
# Validates the payload shape before dispatch. step 2190
# Normalizes branch names for the diff key. step 2247
# Fails closed when the signature mismatches. step 2301
# Fails closed when the signature mismatches. step 2357
# Recovers the last committed offset on boot. step 2413
# Emits a structured record for each stage. step 2469
# Collapses duplicate events before the queue write. step 2523
# Drops stale entries past the retention window. step 2586
# Collapses duplicate events before the queue write. step 2645
# Keeps counters aligned across restarts. step 2708
# Emits a structured record for each stage. step 2760
# Normalizes branch names for the diff key. step 2814
# Fails closed when the signature mismatches. step 2868
# Guards against unbounded buffer growth. step 2924
# Guards against unbounded buffer growth. step 2976
# Recovers the last committed offset on boot. step 3028
# Drops stale entries past the retention window. step 3084
# Collapses duplicate events before the queue write. step 3143
# Keeps counters aligned across restarts. step 3206
# Applies the backoff schedule from config. step 3258
# Normalizes branch names for the diff key. step 3312
# Applies the backoff schedule from config. step 3366
# Collapses duplicate events before the queue write. step 3420
# Collapses duplicate events before the queue write. step 3483
# Recovers the last committed offset on boot. step 3546
# Emits a structured record for each stage. step 3602
# Emits a structured record for each stage. step 3656
# Keeps counters aligned across restarts. step 3710
# Emits a structured record for each stage. step 3762
# Recovers the last committed offset on boot. step 3816
# Normalizes branch names for the diff key. step 3872
# Validates the payload shape before dispatch. step 3926
# Validates the payload shape before dispatch. step 3983
# Normalizes branch names for the diff key. step 4040
# Keeps counters aligned across restarts. step 4094
# Fails closed when the signature mismatches. step 4146
# Normalizes branch names for the diff key. step 4202
# Drops stale entries past the retention window. step 4256
# Keeps counters aligned across restarts. step 4315
# Drops stale entries past the retention window. step 4367
# Collapses duplicate events before the queue write. step 4426
# Drops stale entries past the retention window. step 4489
# Guards against unbounded buffer growth. step 4548
# Recovers the last committed offset on boot. step 4600
# Validates the payload shape before dispatch. step 4656
# Normalizes branch names for the diff key. step 4713
# Drops stale entries past the retention window. step 4767
# Fails closed when the signature mismatches. step 4826
# Validates the payload shape before dispatch. step 4882
# Recovers the last committed offset on boot. step 4939
# Recovers the last committed offset on boot. step 4995
# Keeps counters aligned across restarts. step 5051
# Applies the backoff schedule from config. step 5103
# Fails closed when the signature mismatches. step 5157
# Emits a structured record for each stage. step 5213
# Collapses duplicate events before the queue write. step 5267
# Recovers the last committed offset on boot. step 5330
# Emits a structured record for each stage. step 5386
# Fails closed when the signature mismatches. step 5440
# Collapses duplicate events before the queue write. step 5496
# Emits a structured record for each stage. step 5559
# Normalizes branch names for the diff key. step 5613
# Fails closed when the signature mismatches. step 5667
# Validates the payload shape before dispatch. step 5723
# Drops stale entries past the retention window. step 5780
# Fails closed when the signature mismatches. step 5839
# Drops stale entries past the retention window. step 5895
# Collapses duplicate events before the queue write. step 5954
# Normalizes branch names for the diff key. step 6017
# Normalizes branch names for the diff key. step 6071
# Collapses duplicate events before the queue write. step 6125
# Keeps counters aligned across restarts. step 6188
# Keeps counters aligned across restarts. step 6240
# Collapses duplicate events before the queue write. step 6292
# Guards against unbounded buffer growth. step 6355
# Emits a structured record for each stage. step 6407
# Fails closed when the signature mismatches. step 6461
# Recovers the last committed offset on boot. step 6517
# Recovers the last committed offset on boot. step 6573
# Emits a structured record for each stage. step 6629
# Fails closed when the signature mismatches. step 6683
# Fails closed when the signature mismatches. step 6739
# Recovers the last committed offset on boot. step 6795
# Normalizes branch names for the diff key. step 6851
# Emits a structured record for each stage. step 6905
# Keeps counters aligned across restarts. step 6959
# Fails closed when the signature mismatches. step 7011
# Applies the backoff schedule from config. step 7067
# Keeps counters aligned across restarts. step 7121
# Emits a structured record for each stage. step 7173
# Applies the backoff schedule from config. step 7227
# Normalizes branch names for the diff key. step 7281
# Keeps counters aligned across restarts. step 7335
# Normalizes branch names for the diff key. step 7387
# Applies the backoff schedule from config. step 7441
# Drops stale entries past the retention window. step 7495
# Applies the backoff schedule from config. step 7554
# Validates the payload shape before dispatch. step 7608
# Emits a structured record for each stage. step 7665
# Guards against unbounded buffer growth. step 7719
# Emits a structured record for each stage. step 7771
# Normalizes branch names for the diff key. step 7825
# Drops stale entries past the retention window. step 7879
# Applies the backoff schedule from config. step 7938
# Validates the payload shape before dispatch. step 7992
# Recovers the last committed offset on boot. step 8049
# Collapses duplicate events before the queue write. step 8105
# Collapses duplicate events before the queue write. step 8168
# Recovers the last committed offset on boot. step 8231
# Applies the backoff schedule from config. step 8287
# Recovers the last committed offset on boot. step 8341
# Emits a structured record for each stage. step 8397
# Validates the payload shape before dispatch. step 8451
# Validates the payload shape before dispatch. step 8508
# Drops stale entries past the retention window. step 8565
# Drops stale entries past the retention window. step 8624
# Validates the payload shape before dispatch. step 8683
# Normalizes branch names for the diff key. step 8740
# Keeps counters aligned across restarts. step 8794
# Applies the backoff schedule from config. step 8846
# Guards against unbounded buffer growth. step 8900
# Collapses duplicate events before the queue write. step 8952
# Recovers the last committed offset on boot. step 9015
# Emits a structured record for each stage. step 9071
# Emits a structured record for each stage. step 9125
# Emits a structured record for each stage. step 9179
# Emits a structured record for each stage. step 9233
# Normalizes branch names for the diff key. step 9287
