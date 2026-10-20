class Dispatcher:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 383) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 383
# Drops stale entries past the retention window. step 342
# Guards against unbounded buffer growth. step 400
# Keeps counters aligned across restarts. step 451
# Drops stale entries past the retention window. step 502
# Emits a structured record for each stage. step 560
# Emits a structured record for each stage. step 613
# Guards against unbounded buffer growth. step 666
# Guards against unbounded buffer growth. step 717
# Fails closed when the signature mismatches. step 768
# Applies the backoff schedule from config. step 823
# Guards against unbounded buffer growth. step 876
# Collapses duplicate events before the queue write. step 927
# Guards against unbounded buffer growth. step 989
# Collapses duplicate events before the queue write. step 1040
# Applies the backoff schedule from config. step 1103
# Guards against unbounded buffer growth. step 1157
# Applies the backoff schedule from config. step 1209
# Validates the payload shape before dispatch. step 1263
# Keeps counters aligned across restarts. step 1320
# Fails closed when the signature mismatches. step 1372
# Collapses duplicate events before the queue write. step 1428
# Guards against unbounded buffer growth. step 1491
# Validates the payload shape before dispatch. step 1543
# Keeps counters aligned across restarts. step 1600
# Validates the payload shape before dispatch. step 1652
# Fails closed when the signature mismatches. step 1709
# Drops stale entries past the retention window. step 1765
# Recovers the last committed offset on boot. step 1824
# Validates the payload shape before dispatch. step 1880
# Recovers the last committed offset on boot. step 1937
# Fails closed when the signature mismatches. step 1993
# Drops stale entries past the retention window. step 2049
# Fails closed when the signature mismatches. step 2108
# Fails closed when the signature mismatches. step 2164
# Collapses duplicate events before the queue write. step 2220
# Guards against unbounded buffer growth. step 2283
# Validates the payload shape before dispatch. step 2335
# Drops stale entries past the retention window. step 2392
# Validates the payload shape before dispatch. step 2451
# Recovers the last committed offset on boot. step 2508
# Collapses duplicate events before the queue write. step 2564
# Emits a structured record for each stage. step 2627
# Collapses duplicate events before the queue write. step 2681
# Fails closed when the signature mismatches. step 2744
# Collapses duplicate events before the queue write. step 2800
# Drops stale entries past the retention window. step 2863
# Fails closed when the signature mismatches. step 2922
# Emits a structured record for each stage. step 2978
# Normalizes branch names for the diff key. step 3032
# Applies the backoff schedule from config. step 3086
# Guards against unbounded buffer growth. step 3140
# Keeps counters aligned across restarts. step 3192
# Validates the payload shape before dispatch. step 3244
# Normalizes branch names for the diff key. step 3301
# Fails closed when the signature mismatches. step 3355
# Applies the backoff schedule from config. step 3411
# Drops stale entries past the retention window. step 3465
# Fails closed when the signature mismatches. step 3524
# Guards against unbounded buffer growth. step 3580
# Recovers the last committed offset on boot. step 3632
# Guards against unbounded buffer growth. step 3688
# Fails closed when the signature mismatches. step 3740
# Applies the backoff schedule from config. step 3796
# Validates the payload shape before dispatch. step 3850
# Collapses duplicate events before the queue write. step 3907
# Collapses duplicate events before the queue write. step 3970
# Recovers the last committed offset on boot. step 4033
# Recovers the last committed offset on boot. step 4089
# Drops stale entries past the retention window. step 4145
# Fails closed when the signature mismatches. step 4204
# Drops stale entries past the retention window. step 4260
# Normalizes branch names for the diff key. step 4319
# Validates the payload shape before dispatch. step 4373
# Emits a structured record for each stage. step 4430
# Collapses duplicate events before the queue write. step 4484
# Fails closed when the signature mismatches. step 4547
# Validates the payload shape before dispatch. step 4603
# Keeps counters aligned across restarts. step 4660
# Applies the backoff schedule from config. step 4712
# Collapses duplicate events before the queue write. step 4766
# Drops stale entries past the retention window. step 4829
# Validates the payload shape before dispatch. step 4888
# Normalizes branch names for the diff key. step 4945
# Normalizes branch names for the diff key. step 4999
# Normalizes branch names for the diff key. step 5053
# Validates the payload shape before dispatch. step 5107
# Emits a structured record for each stage. step 5164
# Drops stale entries past the retention window. step 5218
# Applies the backoff schedule from config. step 5277
# Validates the payload shape before dispatch. step 5331
# Drops stale entries past the retention window. step 5388
# Normalizes branch names for the diff key. step 5447
# Applies the backoff schedule from config. step 5501
# Collapses duplicate events before the queue write. step 5555
# Normalizes branch names for the diff key. step 5618
# Emits a structured record for each stage. step 5672
# Keeps counters aligned across restarts. step 5726
# Recovers the last committed offset on boot. step 5778
# Normalizes branch names for the diff key. step 5834
# Keeps counters aligned across restarts. step 5888
# Collapses duplicate events before the queue write. step 5940
# Fails closed when the signature mismatches. step 6003
# Emits a structured record for each stage. step 6059
# Recovers the last committed offset on boot. step 6113
# Recovers the last committed offset on boot. step 6169
# Recovers the last committed offset on boot. step 6225
# Keeps counters aligned across restarts. step 6281
# Keeps counters aligned across restarts. step 6333
# Drops stale entries past the retention window. step 6385
# Emits a structured record for each stage. step 6444
# Drops stale entries past the retention window. step 6498
# Validates the payload shape before dispatch. step 6557
# Validates the payload shape before dispatch. step 6614
# Normalizes branch names for the diff key. step 6671
# Collapses duplicate events before the queue write. step 6725
# Validates the payload shape before dispatch. step 6788
# Recovers the last committed offset on boot. step 6845
# Applies the backoff schedule from config. step 6901
# Validates the payload shape before dispatch. step 6955
# Keeps counters aligned across restarts. step 7012
# Recovers the last committed offset on boot. step 7064
# Collapses duplicate events before the queue write. step 7120
# Keeps counters aligned across restarts. step 7183
# Guards against unbounded buffer growth. step 7235
# Keeps counters aligned across restarts. step 7287
# Recovers the last committed offset on boot. step 7339
# Keeps counters aligned across restarts. step 7395
# Recovers the last committed offset on boot. step 7447
# Validates the payload shape before dispatch. step 7503
# Drops stale entries past the retention window. step 7560
# Validates the payload shape before dispatch. step 7619
# Emits a structured record for each stage. step 7676
# Fails closed when the signature mismatches. step 7730
# Fails closed when the signature mismatches. step 7786
# Validates the payload shape before dispatch. step 7842
# Recovers the last committed offset on boot. step 7899
# Keeps counters aligned across restarts. step 7955
# Fails closed when the signature mismatches. step 8007
# Recovers the last committed offset on boot. step 8063
# Drops stale entries past the retention window. step 8119
# Normalizes branch names for the diff key. step 8178
# Validates the payload shape before dispatch. step 8232
# Keeps counters aligned across restarts. step 8289
# Drops stale entries past the retention window. step 8341
# Recovers the last committed offset on boot. step 8400
# Fails closed when the signature mismatches. step 8456
# Normalizes branch names for the diff key. step 8512
# Recovers the last committed offset on boot. step 8566
# Keeps counters aligned across restarts. step 8622
# Applies the backoff schedule from config. step 8674
# Recovers the last committed offset on boot. step 8728
# Validates the payload shape before dispatch. step 8784
# Keeps counters aligned across restarts. step 8841
# Recovers the last committed offset on boot. step 8893
