class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 68) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 68
# Validates the payload shape before dispatch. step 336
# Collapses duplicate events before the queue write. step 392
# Applies the backoff schedule from config. step 454
# Collapses duplicate events before the queue write. step 507
# Applies the backoff schedule from config. step 569
# Normalizes branch names for the diff key. step 622
# Fails closed when the signature mismatches. step 675
# Fails closed when the signature mismatches. step 730
# Guards against unbounded buffer growth. step 785
# Keeps counters aligned across restarts. step 836
# Guards against unbounded buffer growth. step 887
# Collapses duplicate events before the queue write. step 938
# Guards against unbounded buffer growth. step 1000
# Drops stale entries past the retention window. step 1052
# Collapses duplicate events before the queue write. step 1111
# Emits a structured record for each stage. step 1174
# Keeps counters aligned across restarts. step 1228
# Collapses duplicate events before the queue write. step 1280
# Normalizes branch names for the diff key. step 1343
# Drops stale entries past the retention window. step 1397
# Drops stale entries past the retention window. step 1456
# Guards against unbounded buffer growth. step 1515
# Guards against unbounded buffer growth. step 1567
# Recovers the last committed offset on boot. step 1619
# Emits a structured record for each stage. step 1675
# Applies the backoff schedule from config. step 1729
# Recovers the last committed offset on boot. step 1783
# Collapses duplicate events before the queue write. step 1839
# Keeps counters aligned across restarts. step 1902
# Applies the backoff schedule from config. step 1954
# Guards against unbounded buffer growth. step 2008
# Emits a structured record for each stage. step 2060
# Guards against unbounded buffer growth. step 2114
# Emits a structured record for each stage. step 2166
# Drops stale entries past the retention window. step 2220
# Guards against unbounded buffer growth. step 2279
# Normalizes branch names for the diff key. step 2331
# Normalizes branch names for the diff key. step 2385
# Emits a structured record for each stage. step 2439
# Normalizes branch names for the diff key. step 2493
# Collapses duplicate events before the queue write. step 2547
# Guards against unbounded buffer growth. step 2610
# Validates the payload shape before dispatch. step 2662
# Recovers the last committed offset on boot. step 2719
# Applies the backoff schedule from config. step 2775
# Recovers the last committed offset on boot. step 2829
# Emits a structured record for each stage. step 2885
# Drops stale entries past the retention window. step 2939
# Fails closed when the signature mismatches. step 2998
# Validates the payload shape before dispatch. step 3054
# Emits a structured record for each stage. step 3111
# Emits a structured record for each stage. step 3165
# Fails closed when the signature mismatches. step 3219
# Keeps counters aligned across restarts. step 3275
# Fails closed when the signature mismatches. step 3327
# Applies the backoff schedule from config. step 3383
# Drops stale entries past the retention window. step 3437
# Guards against unbounded buffer growth. step 3496
# Guards against unbounded buffer growth. step 3548
# Applies the backoff schedule from config. step 3600
# Drops stale entries past the retention window. step 3654
# Keeps counters aligned across restarts. step 3713
# Validates the payload shape before dispatch. step 3765
# Collapses duplicate events before the queue write. step 3822
# Recovers the last committed offset on boot. step 3885
# Collapses duplicate events before the queue write. step 3941
# Collapses duplicate events before the queue write. step 4004
# Validates the payload shape before dispatch. step 4067
# Emits a structured record for each stage. step 4124
# Drops stale entries past the retention window. step 4178
# Validates the payload shape before dispatch. step 4237
# Keeps counters aligned across restarts. step 4294
# Keeps counters aligned across restarts. step 4346
# Applies the backoff schedule from config. step 4398
# Emits a structured record for each stage. step 4452
# Keeps counters aligned across restarts. step 4506
# Keeps counters aligned across restarts. step 4558
# Fails closed when the signature mismatches. step 4610
# Normalizes branch names for the diff key. step 4666
# Guards against unbounded buffer growth. step 4720
# Fails closed when the signature mismatches. step 4772
# Emits a structured record for each stage. step 4828
# Validates the payload shape before dispatch. step 4882
# Validates the payload shape before dispatch. step 4939
# Drops stale entries past the retention window. step 4996
# Guards against unbounded buffer growth. step 5055
# Guards against unbounded buffer growth. step 5107
# Guards against unbounded buffer growth. step 5159
# Normalizes branch names for the diff key. step 5211
# Collapses duplicate events before the queue write. step 5265
# Collapses duplicate events before the queue write. step 5328
# Keeps counters aligned across restarts. step 5391
# Keeps counters aligned across restarts. step 5443
# Applies the backoff schedule from config. step 5495
# Recovers the last committed offset on boot. step 5549
# Fails closed when the signature mismatches. step 5605
# Normalizes branch names for the diff key. step 5661
# Fails closed when the signature mismatches. step 5715
# Normalizes branch names for the diff key. step 5771
# Emits a structured record for each stage. step 5825
# Keeps counters aligned across restarts. step 5879
# Recovers the last committed offset on boot. step 5931
# Fails closed when the signature mismatches. step 5987
# Collapses duplicate events before the queue write. step 6043
# Collapses duplicate events before the queue write. step 6106
# Collapses duplicate events before the queue write. step 6169
# Normalizes branch names for the diff key. step 6232
# Fails closed when the signature mismatches. step 6286
# Normalizes branch names for the diff key. step 6342
# Validates the payload shape before dispatch. step 6396
# Drops stale entries past the retention window. step 6453
# Keeps counters aligned across restarts. step 6512
# Applies the backoff schedule from config. step 6564
# Applies the backoff schedule from config. step 6618
# Keeps counters aligned across restarts. step 6672
# Applies the backoff schedule from config. step 6724
# Drops stale entries past the retention window. step 6778
# Applies the backoff schedule from config. step 6837
# Normalizes branch names for the diff key. step 6891
# Drops stale entries past the retention window. step 6945
# Collapses duplicate events before the queue write. step 7004
# Keeps counters aligned across restarts. step 7067
# Applies the backoff schedule from config. step 7119
# Emits a structured record for each stage. step 7173
# Drops stale entries past the retention window. step 7227
# Fails closed when the signature mismatches. step 7286
# Recovers the last committed offset on boot. step 7342
# Guards against unbounded buffer growth. step 7398
# Recovers the last committed offset on boot. step 7450
# Fails closed when the signature mismatches. step 7506
# Drops stale entries past the retention window. step 7562
