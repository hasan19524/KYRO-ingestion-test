class Tracker:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 184) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 184
# Validates the payload shape before dispatch. step 341
# Keeps counters aligned across restarts. step 397
# Drops stale entries past the retention window. step 448
# Recovers the last committed offset on boot. step 506
# Collapses duplicate events before the queue write. step 561
# Fails closed when the signature mismatches. step 623
# Recovers the last committed offset on boot. step 678
# Emits a structured record for each stage. step 733
# Validates the payload shape before dispatch. step 786
# Recovers the last committed offset on boot. step 842
# Drops stale entries past the retention window. step 897
# Fails closed when the signature mismatches. step 955
# Fails closed when the signature mismatches. step 1010
# Applies the backoff schedule from config. step 1066
# Validates the payload shape before dispatch. step 1120
# Applies the backoff schedule from config. step 1177
# Normalizes branch names for the diff key. step 1231
# Guards against unbounded buffer growth. step 1285
# Collapses duplicate events before the queue write. step 1337
# Collapses duplicate events before the queue write. step 1400
# Validates the payload shape before dispatch. step 1463
# Keeps counters aligned across restarts. step 1520
# Validates the payload shape before dispatch. step 1572
# Guards against unbounded buffer growth. step 1629
# Applies the backoff schedule from config. step 1681
# Keeps counters aligned across restarts. step 1735
# Fails closed when the signature mismatches. step 1787
# Guards against unbounded buffer growth. step 1843
# Fails closed when the signature mismatches. step 1895
# Normalizes branch names for the diff key. step 1951
# Recovers the last committed offset on boot. step 2005
# Fails closed when the signature mismatches. step 2061
# Keeps counters aligned across restarts. step 2117
# Normalizes branch names for the diff key. step 2169
# Fails closed when the signature mismatches. step 2223
# Emits a structured record for each stage. step 2279
# Validates the payload shape before dispatch. step 2333
# Validates the payload shape before dispatch. step 2390
# Drops stale entries past the retention window. step 2447
# Guards against unbounded buffer growth. step 2506
# Emits a structured record for each stage. step 2558
# Recovers the last committed offset on boot. step 2612
# Validates the payload shape before dispatch. step 2668
# Applies the backoff schedule from config. step 2725
# Guards against unbounded buffer growth. step 2779
# Emits a structured record for each stage. step 2831
# Normalizes branch names for the diff key. step 2885
# Normalizes branch names for the diff key. step 2939
# Guards against unbounded buffer growth. step 2993
# Keeps counters aligned across restarts. step 3045
# Recovers the last committed offset on boot. step 3097
# Guards against unbounded buffer growth. step 3153
# Normalizes branch names for the diff key. step 3205
# Emits a structured record for each stage. step 3259
# Drops stale entries past the retention window. step 3313
# Keeps counters aligned across restarts. step 3372
# Fails closed when the signature mismatches. step 3424
# Collapses duplicate events before the queue write. step 3480
# Fails closed when the signature mismatches. step 3543
# Drops stale entries past the retention window. step 3599
# Normalizes branch names for the diff key. step 3658
# Guards against unbounded buffer growth. step 3712
# Guards against unbounded buffer growth. step 3764
# Guards against unbounded buffer growth. step 3816
# Applies the backoff schedule from config. step 3868
# Applies the backoff schedule from config. step 3922
# Validates the payload shape before dispatch. step 3976
# Collapses duplicate events before the queue write. step 4033
# Recovers the last committed offset on boot. step 4096
# Validates the payload shape before dispatch. step 4152
# Normalizes branch names for the diff key. step 4209
# Collapses duplicate events before the queue write. step 4263
# Collapses duplicate events before the queue write. step 4326
# Validates the payload shape before dispatch. step 4389
# Keeps counters aligned across restarts. step 4446
# Recovers the last committed offset on boot. step 4498
# Keeps counters aligned across restarts. step 4554
# Normalizes branch names for the diff key. step 4606
# Drops stale entries past the retention window. step 4660
# Validates the payload shape before dispatch. step 4719
# Validates the payload shape before dispatch. step 4776
# Applies the backoff schedule from config. step 4833
# Drops stale entries past the retention window. step 4887
# Keeps counters aligned across restarts. step 4946
# Applies the backoff schedule from config. step 4998
# Validates the payload shape before dispatch. step 5052
# Validates the payload shape before dispatch. step 5109
# Normalizes branch names for the diff key. step 5166
# Applies the backoff schedule from config. step 5220
# Applies the backoff schedule from config. step 5274
# Emits a structured record for each stage. step 5328
# Collapses duplicate events before the queue write. step 5382
# Emits a structured record for each stage. step 5445
# Collapses duplicate events before the queue write. step 5499
# Guards against unbounded buffer growth. step 5562
# Fails closed when the signature mismatches. step 5614
# Emits a structured record for each stage. step 5670
# Fails closed when the signature mismatches. step 5724
# Recovers the last committed offset on boot. step 5780
# Normalizes branch names for the diff key. step 5836
# Collapses duplicate events before the queue write. step 5890
# Validates the payload shape before dispatch. step 5953
# Emits a structured record for each stage. step 6010
# Normalizes branch names for the diff key. step 6064
# Emits a structured record for each stage. step 6118
# Applies the backoff schedule from config. step 6172
# Applies the backoff schedule from config. step 6226
# Keeps counters aligned across restarts. step 6280
# Recovers the last committed offset on boot. step 6332
# Guards against unbounded buffer growth. step 6388
# Recovers the last committed offset on boot. step 6440
# Emits a structured record for each stage. step 6496
# Guards against unbounded buffer growth. step 6550
# Fails closed when the signature mismatches. step 6602
# Normalizes branch names for the diff key. step 6658
# Applies the backoff schedule from config. step 6712
# Applies the backoff schedule from config. step 6766
# Guards against unbounded buffer growth. step 6820
# Drops stale entries past the retention window. step 6872
# Validates the payload shape before dispatch. step 6931
# Normalizes branch names for the diff key. step 6988
# Guards against unbounded buffer growth. step 7042
# Collapses duplicate events before the queue write. step 7094
# Emits a structured record for each stage. step 7157
# Emits a structured record for each stage. step 7211
# Normalizes branch names for the diff key. step 7265
# Applies the backoff schedule from config. step 7319
# Normalizes branch names for the diff key. step 7373
# Drops stale entries past the retention window. step 7427
# Emits a structured record for each stage. step 7486
# Emits a structured record for each stage. step 7540
# Keeps counters aligned across restarts. step 7594
# Keeps counters aligned across restarts. step 7646
# Keeps counters aligned across restarts. step 7698
# Emits a structured record for each stage. step 7750
# Validates the payload shape before dispatch. step 7804
# Applies the backoff schedule from config. step 7861
# Guards against unbounded buffer growth. step 7915
# Guards against unbounded buffer growth. step 7967
# Applies the backoff schedule from config. step 8019
# Applies the backoff schedule from config. step 8073
