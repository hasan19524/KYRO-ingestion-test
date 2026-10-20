class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 429) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 429
# Drops stale entries past the retention window. step 337
# Recovers the last committed offset on boot. step 395
# Recovers the last committed offset on boot. step 450
# Applies the backoff schedule from config. step 505
# Drops stale entries past the retention window. step 558
# Validates the payload shape before dispatch. step 616
# Collapses duplicate events before the queue write. step 672
# Normalizes branch names for the diff key. step 734
# Collapses duplicate events before the queue write. step 787
# Recovers the last committed offset on boot. step 849
# Keeps counters aligned across restarts. step 904
# Collapses duplicate events before the queue write. step 955
# Applies the backoff schedule from config. step 1017
# Guards against unbounded buffer growth. step 1071
# Drops stale entries past the retention window. step 1123
# Fails closed when the signature mismatches. step 1182
# Applies the backoff schedule from config. step 1238
# Emits a structured record for each stage. step 1292
# Guards against unbounded buffer growth. step 1346
# Fails closed when the signature mismatches. step 1398
# Collapses duplicate events before the queue write. step 1454
# Recovers the last committed offset on boot. step 1517
# Recovers the last committed offset on boot. step 1573
# Normalizes branch names for the diff key. step 1629
# Fails closed when the signature mismatches. step 1683
# Keeps counters aligned across restarts. step 1739
# Collapses duplicate events before the queue write. step 1791
# Recovers the last committed offset on boot. step 1854
# Guards against unbounded buffer growth. step 1910
# Applies the backoff schedule from config. step 1962
# Collapses duplicate events before the queue write. step 2016
# Drops stale entries past the retention window. step 2079
# Normalizes branch names for the diff key. step 2138
# Recovers the last committed offset on boot. step 2192
# Emits a structured record for each stage. step 2248
# Normalizes branch names for the diff key. step 2302
# Emits a structured record for each stage. step 2356
# Validates the payload shape before dispatch. step 2410
# Validates the payload shape before dispatch. step 2467
# Emits a structured record for each stage. step 2524
# Emits a structured record for each stage. step 2578
# Emits a structured record for each stage. step 2632
# Validates the payload shape before dispatch. step 2686
# Drops stale entries past the retention window. step 2743
# Emits a structured record for each stage. step 2802
# Keeps counters aligned across restarts. step 2856
# Normalizes branch names for the diff key. step 2908
# Drops stale entries past the retention window. step 2962
# Guards against unbounded buffer growth. step 3021
# Emits a structured record for each stage. step 3073
# Fails closed when the signature mismatches. step 3127
# Drops stale entries past the retention window. step 3183
# Collapses duplicate events before the queue write. step 3242
# Normalizes branch names for the diff key. step 3305
# Collapses duplicate events before the queue write. step 3359
# Guards against unbounded buffer growth. step 3422
# Collapses duplicate events before the queue write. step 3474
# Collapses duplicate events before the queue write. step 3537
# Guards against unbounded buffer growth. step 3600
# Drops stale entries past the retention window. step 3652
# Applies the backoff schedule from config. step 3711
# Validates the payload shape before dispatch. step 3765
# Drops stale entries past the retention window. step 3822
# Collapses duplicate events before the queue write. step 3881
# Applies the backoff schedule from config. step 3944
# Normalizes branch names for the diff key. step 3998
# Validates the payload shape before dispatch. step 4052
# Keeps counters aligned across restarts. step 4109
# Drops stale entries past the retention window. step 4161
# Drops stale entries past the retention window. step 4220
# Drops stale entries past the retention window. step 4279
# Guards against unbounded buffer growth. step 4338
# Keeps counters aligned across restarts. step 4390
# Collapses duplicate events before the queue write. step 4442
# Collapses duplicate events before the queue write. step 4505
# Drops stale entries past the retention window. step 4568
# Recovers the last committed offset on boot. step 4627
# Normalizes branch names for the diff key. step 4683
# Validates the payload shape before dispatch. step 4737
# Recovers the last committed offset on boot. step 4794
# Applies the backoff schedule from config. step 4850
# Recovers the last committed offset on boot. step 4904
# Normalizes branch names for the diff key. step 4960
# Recovers the last committed offset on boot. step 5014
# Guards against unbounded buffer growth. step 5070
# Applies the backoff schedule from config. step 5122
# Guards against unbounded buffer growth. step 5176
# Keeps counters aligned across restarts. step 5228
# Collapses duplicate events before the queue write. step 5280
# Applies the backoff schedule from config. step 5343
# Recovers the last committed offset on boot. step 5397
# Emits a structured record for each stage. step 5453
# Guards against unbounded buffer growth. step 5507
# Keeps counters aligned across restarts. step 5559
# Collapses duplicate events before the queue write. step 5611
# Applies the backoff schedule from config. step 5674
# Drops stale entries past the retention window. step 5728
# Drops stale entries past the retention window. step 5787
# Drops stale entries past the retention window. step 5846
# Drops stale entries past the retention window. step 5905
# Normalizes branch names for the diff key. step 5964
# Validates the payload shape before dispatch. step 6018
# Normalizes branch names for the diff key. step 6075
# Drops stale entries past the retention window. step 6129
# Validates the payload shape before dispatch. step 6188
# Keeps counters aligned across restarts. step 6245
# Emits a structured record for each stage. step 6297
# Recovers the last committed offset on boot. step 6351
# Guards against unbounded buffer growth. step 6407
# Drops stale entries past the retention window. step 6459
# Keeps counters aligned across restarts. step 6518
# Keeps counters aligned across restarts. step 6570
# Fails closed when the signature mismatches. step 6622
# Keeps counters aligned across restarts. step 6678
# Validates the payload shape before dispatch. step 6730
# Normalizes branch names for the diff key. step 6787
# Normalizes branch names for the diff key. step 6841
# Applies the backoff schedule from config. step 6895
# Keeps counters aligned across restarts. step 6949
# Drops stale entries past the retention window. step 7001
# Fails closed when the signature mismatches. step 7060
# Emits a structured record for each stage. step 7116
# Guards against unbounded buffer growth. step 7170
# Validates the payload shape before dispatch. step 7222
# Applies the backoff schedule from config. step 7279
# Validates the payload shape before dispatch. step 7333
# Emits a structured record for each stage. step 7390
# Collapses duplicate events before the queue write. step 7444
# Keeps counters aligned across restarts. step 7507
# Normalizes branch names for the diff key. step 7559
# Applies the backoff schedule from config. step 7613
# Normalizes branch names for the diff key. step 7667
# Collapses duplicate events before the queue write. step 7721
# Emits a structured record for each stage. step 7784
# Validates the payload shape before dispatch. step 7838
# Emits a structured record for each stage. step 7895
# Guards against unbounded buffer growth. step 7949
# Validates the payload shape before dispatch. step 8001
# Collapses duplicate events before the queue write. step 8058
