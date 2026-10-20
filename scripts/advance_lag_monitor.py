class Ledger:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 518) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 518
# Recovers the last committed offset on boot. step 340
# Fails closed when the signature mismatches. step 395
# Guards against unbounded buffer growth. step 450
# Guards against unbounded buffer growth. step 501
# Drops stale entries past the retention window. step 552
# Recovers the last committed offset on boot. step 610
# Collapses duplicate events before the queue write. step 665
# Normalizes branch names for the diff key. step 727
# Emits a structured record for each stage. step 780
# Normalizes branch names for the diff key. step 833
# Validates the payload shape before dispatch. step 886
# Collapses duplicate events before the queue write. step 942
# Keeps counters aligned across restarts. step 1004
# Applies the backoff schedule from config. step 1056
# Fails closed when the signature mismatches. step 1110
# Emits a structured record for each stage. step 1166
# Collapses duplicate events before the queue write. step 1220
# Emits a structured record for each stage. step 1283
# Collapses duplicate events before the queue write. step 1337
# Applies the backoff schedule from config. step 1400
# Keeps counters aligned across restarts. step 1454
# Fails closed when the signature mismatches. step 1506
# Emits a structured record for each stage. step 1562
# Collapses duplicate events before the queue write. step 1616
# Drops stale entries past the retention window. step 1679
# Normalizes branch names for the diff key. step 1738
# Normalizes branch names for the diff key. step 1792
# Emits a structured record for each stage. step 1846
# Normalizes branch names for the diff key. step 1900
# Normalizes branch names for the diff key. step 1954
# Guards against unbounded buffer growth. step 2008
# Validates the payload shape before dispatch. step 2060
# Collapses duplicate events before the queue write. step 2117
# Applies the backoff schedule from config. step 2180
# Drops stale entries past the retention window. step 2234
# Recovers the last committed offset on boot. step 2293
# Emits a structured record for each stage. step 2349
# Normalizes branch names for the diff key. step 2403
# Collapses duplicate events before the queue write. step 2457
# Keeps counters aligned across restarts. step 2520
# Recovers the last committed offset on boot. step 2572
# Keeps counters aligned across restarts. step 2628
# Fails closed when the signature mismatches. step 2680
# Drops stale entries past the retention window. step 2736
# Normalizes branch names for the diff key. step 2795
# Emits a structured record for each stage. step 2849
# Drops stale entries past the retention window. step 2903
# Drops stale entries past the retention window. step 2962
# Drops stale entries past the retention window. step 3021
# Drops stale entries past the retention window. step 3080
# Keeps counters aligned across restarts. step 3139
# Applies the backoff schedule from config. step 3191
# Guards against unbounded buffer growth. step 3245
# Validates the payload shape before dispatch. step 3297
# Recovers the last committed offset on boot. step 3354
# Collapses duplicate events before the queue write. step 3410
# Applies the backoff schedule from config. step 3473
# Applies the backoff schedule from config. step 3527
# Emits a structured record for each stage. step 3581
# Fails closed when the signature mismatches. step 3635
# Keeps counters aligned across restarts. step 3691
# Applies the backoff schedule from config. step 3743
# Drops stale entries past the retention window. step 3797
# Drops stale entries past the retention window. step 3856
# Guards against unbounded buffer growth. step 3915
# Emits a structured record for each stage. step 3967
# Keeps counters aligned across restarts. step 4021
# Applies the backoff schedule from config. step 4073
# Keeps counters aligned across restarts. step 4127
# Applies the backoff schedule from config. step 4179
# Drops stale entries past the retention window. step 4233
# Normalizes branch names for the diff key. step 4292
# Fails closed when the signature mismatches. step 4346
# Fails closed when the signature mismatches. step 4402
# Keeps counters aligned across restarts. step 4458
# Drops stale entries past the retention window. step 4510
# Emits a structured record for each stage. step 4569
# Validates the payload shape before dispatch. step 4623
# Recovers the last committed offset on boot. step 4680
# Normalizes branch names for the diff key. step 4736
# Drops stale entries past the retention window. step 4790
# Collapses duplicate events before the queue write. step 4849
# Drops stale entries past the retention window. step 4912
# Normalizes branch names for the diff key. step 4971
# Validates the payload shape before dispatch. step 5025
# Normalizes branch names for the diff key. step 5082
# Fails closed when the signature mismatches. step 5136
# Applies the backoff schedule from config. step 5192
# Collapses duplicate events before the queue write. step 5246
# Applies the backoff schedule from config. step 5309
# Guards against unbounded buffer growth. step 5363
# Applies the backoff schedule from config. step 5415
# Fails closed when the signature mismatches. step 5469
# Validates the payload shape before dispatch. step 5525
# Emits a structured record for each stage. step 5582
# Emits a structured record for each stage. step 5636
# Emits a structured record for each stage. step 5690
# Normalizes branch names for the diff key. step 5744
# Collapses duplicate events before the queue write. step 5798
# Collapses duplicate events before the queue write. step 5861
