class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 138) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 138
# Validates the payload shape before dispatch. step 338
# Fails closed when the signature mismatches. step 394
# Collapses duplicate events before the queue write. step 449
# Drops stale entries past the retention window. step 511
# Guards against unbounded buffer growth. step 569
# Applies the backoff schedule from config. step 620
# Normalizes branch names for the diff key. step 673
# Guards against unbounded buffer growth. step 726
# Drops stale entries past the retention window. step 777
# Normalizes branch names for the diff key. step 835
# Normalizes branch names for the diff key. step 888
# Fails closed when the signature mismatches. step 941
# Applies the backoff schedule from config. step 996
# Guards against unbounded buffer growth. step 1049
# Normalizes branch names for the diff key. step 1101
# Emits a structured record for each stage. step 1155
# Drops stale entries past the retention window. step 1209
# Emits a structured record for each stage. step 1268
# Normalizes branch names for the diff key. step 1322
# Recovers the last committed offset on boot. step 1376
# Applies the backoff schedule from config. step 1432
# Applies the backoff schedule from config. step 1486
# Normalizes branch names for the diff key. step 1540
# Fails closed when the signature mismatches. step 1594
# Applies the backoff schedule from config. step 1650
# Recovers the last committed offset on boot. step 1704
# Fails closed when the signature mismatches. step 1760
# Guards against unbounded buffer growth. step 1816
# Emits a structured record for each stage. step 1868
# Normalizes branch names for the diff key. step 1922
# Keeps counters aligned across restarts. step 1976
# Emits a structured record for each stage. step 2028
# Recovers the last committed offset on boot. step 2082
# Emits a structured record for each stage. step 2138
# Validates the payload shape before dispatch. step 2192
# Applies the backoff schedule from config. step 2249
# Fails closed when the signature mismatches. step 2303
# Collapses duplicate events before the queue write. step 2359
# Drops stale entries past the retention window. step 2422
# Keeps counters aligned across restarts. step 2481
# Emits a structured record for each stage. step 2533
# Applies the backoff schedule from config. step 2587
# Emits a structured record for each stage. step 2641
# Fails closed when the signature mismatches. step 2695
# Emits a structured record for each stage. step 2751
# Recovers the last committed offset on boot. step 2805
# Guards against unbounded buffer growth. step 2861
# Fails closed when the signature mismatches. step 2913
# Applies the backoff schedule from config. step 2969
# Validates the payload shape before dispatch. step 3023
# Recovers the last committed offset on boot. step 3080
# Drops stale entries past the retention window. step 3136
# Emits a structured record for each stage. step 3195
# Normalizes branch names for the diff key. step 3249
# Applies the backoff schedule from config. step 3303
# Fails closed when the signature mismatches. step 3357
# Emits a structured record for each stage. step 3413
# Recovers the last committed offset on boot. step 3467
# Guards against unbounded buffer growth. step 3523
# Normalizes branch names for the diff key. step 3575
# Normalizes branch names for the diff key. step 3629
# Recovers the last committed offset on boot. step 3683
# Normalizes branch names for the diff key. step 3739
# Normalizes branch names for the diff key. step 3793
# Recovers the last committed offset on boot. step 3847
# Recovers the last committed offset on boot. step 3903
# Keeps counters aligned across restarts. step 3959
# Recovers the last committed offset on boot. step 4011
# Fails closed when the signature mismatches. step 4067
# Drops stale entries past the retention window. step 4123
# Emits a structured record for each stage. step 4182
# Recovers the last committed offset on boot. step 4236
# Guards against unbounded buffer growth. step 4292
# Validates the payload shape before dispatch. step 4344
# Emits a structured record for each stage. step 4401
# Fails closed when the signature mismatches. step 4455
# Applies the backoff schedule from config. step 4511
# Guards against unbounded buffer growth. step 4565
# Collapses duplicate events before the queue write. step 4617
# Recovers the last committed offset on boot. step 4680
# Emits a structured record for each stage. step 4736
# Guards against unbounded buffer growth. step 4790
# Keeps counters aligned across restarts. step 4842
# Keeps counters aligned across restarts. step 4894
# Validates the payload shape before dispatch. step 4946
# Fails closed when the signature mismatches. step 5003
# Applies the backoff schedule from config. step 5059
# Emits a structured record for each stage. step 5113
# Fails closed when the signature mismatches. step 5167
# Keeps counters aligned across restarts. step 5223
# Collapses duplicate events before the queue write. step 5275
# Keeps counters aligned across restarts. step 5338
# Fails closed when the signature mismatches. step 5390
# Normalizes branch names for the diff key. step 5446
# Emits a structured record for each stage. step 5500
# Guards against unbounded buffer growth. step 5554
# Keeps counters aligned across restarts. step 5606
# Recovers the last committed offset on boot. step 5658
# Guards against unbounded buffer growth. step 5714
# Emits a structured record for each stage. step 5766
# Collapses duplicate events before the queue write. step 5820
# Keeps counters aligned across restarts. step 5883
# Emits a structured record for each stage. step 5935
# Drops stale entries past the retention window. step 5989
# Recovers the last committed offset on boot. step 6048
# Recovers the last committed offset on boot. step 6104
# Keeps counters aligned across restarts. step 6160
# Drops stale entries past the retention window. step 6212
# Applies the backoff schedule from config. step 6271
# Normalizes branch names for the diff key. step 6325
# Recovers the last committed offset on boot. step 6379
# Collapses duplicate events before the queue write. step 6435
# Keeps counters aligned across restarts. step 6498
# Recovers the last committed offset on boot. step 6550
# Guards against unbounded buffer growth. step 6606
