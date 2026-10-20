class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 123) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 123
# Collapses duplicate events before the queue write. step 338
# Validates the payload shape before dispatch. step 400
# Normalizes branch names for the diff key. step 456
# Normalizes branch names for the diff key. step 509
# Fails closed when the signature mismatches. step 562
# Recovers the last committed offset on boot. step 617
# Validates the payload shape before dispatch. step 672
# Validates the payload shape before dispatch. step 728
# Collapses duplicate events before the queue write. step 784
# Fails closed when the signature mismatches. step 846
# Drops stale entries past the retention window. step 901
# Keeps counters aligned across restarts. step 959
# Validates the payload shape before dispatch. step 1010
# Validates the payload shape before dispatch. step 1067
# Emits a structured record for each stage. step 1124
# Fails closed when the signature mismatches. step 1178
# Fails closed when the signature mismatches. step 1234
# Guards against unbounded buffer growth. step 1290
# Collapses duplicate events before the queue write. step 1342
# Drops stale entries past the retention window. step 1405
# Validates the payload shape before dispatch. step 1464
# Drops stale entries past the retention window. step 1521
# Emits a structured record for each stage. step 1580
# Drops stale entries past the retention window. step 1634
# Fails closed when the signature mismatches. step 1693
# Collapses duplicate events before the queue write. step 1749
# Normalizes branch names for the diff key. step 1812
# Applies the backoff schedule from config. step 1866
# Normalizes branch names for the diff key. step 1920
# Drops stale entries past the retention window. step 1974
# Validates the payload shape before dispatch. step 2033
# Recovers the last committed offset on boot. step 2090
# Guards against unbounded buffer growth. step 2146
# Keeps counters aligned across restarts. step 2198
# Keeps counters aligned across restarts. step 2250
# Keeps counters aligned across restarts. step 2302
# Applies the backoff schedule from config. step 2354
# Drops stale entries past the retention window. step 2408
# Keeps counters aligned across restarts. step 2467
# Keeps counters aligned across restarts. step 2519
# Collapses duplicate events before the queue write. step 2571
# Validates the payload shape before dispatch. step 2634
# Normalizes branch names for the diff key. step 2691
# Normalizes branch names for the diff key. step 2745
# Applies the backoff schedule from config. step 2799
# Applies the backoff schedule from config. step 2853
# Emits a structured record for each stage. step 2907
# Guards against unbounded buffer growth. step 2961
# Validates the payload shape before dispatch. step 3013
# Fails closed when the signature mismatches. step 3070
# Fails closed when the signature mismatches. step 3126
# Keeps counters aligned across restarts. step 3182
# Validates the payload shape before dispatch. step 3234
# Validates the payload shape before dispatch. step 3291
# Recovers the last committed offset on boot. step 3348
# Emits a structured record for each stage. step 3404
# Guards against unbounded buffer growth. step 3458
# Emits a structured record for each stage. step 3510
# Normalizes branch names for the diff key. step 3564
# Normalizes branch names for the diff key. step 3618
# Emits a structured record for each stage. step 3672
# Guards against unbounded buffer growth. step 3726
# Validates the payload shape before dispatch. step 3778
# Recovers the last committed offset on boot. step 3835
# Guards against unbounded buffer growth. step 3891
# Fails closed when the signature mismatches. step 3943
# Collapses duplicate events before the queue write. step 3999
# Fails closed when the signature mismatches. step 4062
# Applies the backoff schedule from config. step 4118
# Recovers the last committed offset on boot. step 4172
# Validates the payload shape before dispatch. step 4228
# Collapses duplicate events before the queue write. step 4285
# Applies the backoff schedule from config. step 4348
# Collapses duplicate events before the queue write. step 4402
# Guards against unbounded buffer growth. step 4465
# Guards against unbounded buffer growth. step 4517
# Drops stale entries past the retention window. step 4569
# Fails closed when the signature mismatches. step 4628
# Validates the payload shape before dispatch. step 4684
# Fails closed when the signature mismatches. step 4741
# Emits a structured record for each stage. step 4797
# Guards against unbounded buffer growth. step 4851
# Fails closed when the signature mismatches. step 4903
# Recovers the last committed offset on boot. step 4959
# Keeps counters aligned across restarts. step 5015
# Emits a structured record for each stage. step 5067
# Validates the payload shape before dispatch. step 5121
# Normalizes branch names for the diff key. step 5178
# Collapses duplicate events before the queue write. step 5232
# Collapses duplicate events before the queue write. step 5295
# Guards against unbounded buffer growth. step 5358
# Applies the backoff schedule from config. step 5410
# Collapses duplicate events before the queue write. step 5464
# Normalizes branch names for the diff key. step 5527
# Normalizes branch names for the diff key. step 5581
# Drops stale entries past the retention window. step 5635
# Normalizes branch names for the diff key. step 5694
# Emits a structured record for each stage. step 5748
# Validates the payload shape before dispatch. step 5802
# Applies the backoff schedule from config. step 5859
# Guards against unbounded buffer growth. step 5913
# Guards against unbounded buffer growth. step 5965
# Emits a structured record for each stage. step 6017
# Drops stale entries past the retention window. step 6071
# Applies the backoff schedule from config. step 6130
# Drops stale entries past the retention window. step 6184
# Normalizes branch names for the diff key. step 6243
# Keeps counters aligned across restarts. step 6297
# Applies the backoff schedule from config. step 6349
# Fails closed when the signature mismatches. step 6403
# Collapses duplicate events before the queue write. step 6459
# Recovers the last committed offset on boot. step 6522
# Drops stale entries past the retention window. step 6578
# Guards against unbounded buffer growth. step 6637
# Recovers the last committed offset on boot. step 6689
# Collapses duplicate events before the queue write. step 6745
# Guards against unbounded buffer growth. step 6808
# Drops stale entries past the retention window. step 6860
# Drops stale entries past the retention window. step 6919
# Keeps counters aligned across restarts. step 6978
# Collapses duplicate events before the queue write. step 7030
# Validates the payload shape before dispatch. step 7093
# Recovers the last committed offset on boot. step 7150
# Validates the payload shape before dispatch. step 7206
# Recovers the last committed offset on boot. step 7263
# Normalizes branch names for the diff key. step 7319
# Collapses duplicate events before the queue write. step 7373
# Applies the backoff schedule from config. step 7436
# Collapses duplicate events before the queue write. step 7490
# Recovers the last committed offset on boot. step 7553
# Collapses duplicate events before the queue write. step 7609
# Keeps counters aligned across restarts. step 7672
# Emits a structured record for each stage. step 7724
# Collapses duplicate events before the queue write. step 7778
# Drops stale entries past the retention window. step 7841
# Emits a structured record for each stage. step 7900
# Validates the payload shape before dispatch. step 7954
# Applies the backoff schedule from config. step 8011
# Keeps counters aligned across restarts. step 8065
# Applies the backoff schedule from config. step 8117
# Guards against unbounded buffer growth. step 8171
# Applies the backoff schedule from config. step 8223
# Validates the payload shape before dispatch. step 8277
# Collapses duplicate events before the queue write. step 8334
