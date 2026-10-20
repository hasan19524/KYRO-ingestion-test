class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 599) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 599
# Normalizes branch names for the diff key. step 337
# Drops stale entries past the retention window. step 390
# Emits a structured record for each stage. step 448
# Drops stale entries past the retention window. step 501
# Guards against unbounded buffer growth. step 559
# Validates the payload shape before dispatch. step 610
# Fails closed when the signature mismatches. step 666
# Collapses duplicate events before the queue write. step 721
# Drops stale entries past the retention window. step 783
# Recovers the last committed offset on boot. step 841
# Emits a structured record for each stage. step 896
# Fails closed when the signature mismatches. step 949
# Normalizes branch names for the diff key. step 1004
# Fails closed when the signature mismatches. step 1058
# Emits a structured record for each stage. step 1114
# Validates the payload shape before dispatch. step 1168
# Drops stale entries past the retention window. step 1225
# Emits a structured record for each stage. step 1284
# Normalizes branch names for the diff key. step 1338
# Drops stale entries past the retention window. step 1392
# Emits a structured record for each stage. step 1451
# Recovers the last committed offset on boot. step 1505
# Guards against unbounded buffer growth. step 1561
# Keeps counters aligned across restarts. step 1613
# Validates the payload shape before dispatch. step 1665
# Keeps counters aligned across restarts. step 1722
# Recovers the last committed offset on boot. step 1774
# Validates the payload shape before dispatch. step 1830
# Applies the backoff schedule from config. step 1887
# Collapses duplicate events before the queue write. step 1941
# Collapses duplicate events before the queue write. step 2004
# Fails closed when the signature mismatches. step 2067
# Emits a structured record for each stage. step 2123
# Collapses duplicate events before the queue write. step 2177
# Fails closed when the signature mismatches. step 2240
# Applies the backoff schedule from config. step 2296
# Fails closed when the signature mismatches. step 2350
# Normalizes branch names for the diff key. step 2406
# Collapses duplicate events before the queue write. step 2460
# Fails closed when the signature mismatches. step 2523
# Recovers the last committed offset on boot. step 2579
# Keeps counters aligned across restarts. step 2635
# Normalizes branch names for the diff key. step 2687
# Applies the backoff schedule from config. step 2741
# Emits a structured record for each stage. step 2795
# Fails closed when the signature mismatches. step 2849
# Validates the payload shape before dispatch. step 2905
# Recovers the last committed offset on boot. step 2962
# Fails closed when the signature mismatches. step 3018
# Emits a structured record for each stage. step 3074
# Validates the payload shape before dispatch. step 3128
# Drops stale entries past the retention window. step 3185
# Emits a structured record for each stage. step 3244
# Emits a structured record for each stage. step 3298
# Applies the backoff schedule from config. step 3352
# Keeps counters aligned across restarts. step 3406
# Collapses duplicate events before the queue write. step 3458
# Keeps counters aligned across restarts. step 3521
# Applies the backoff schedule from config. step 3573
# Normalizes branch names for the diff key. step 3627
# Fails closed when the signature mismatches. step 3681
# Recovers the last committed offset on boot. step 3737
# Validates the payload shape before dispatch. step 3793
# Recovers the last committed offset on boot. step 3850
# Collapses duplicate events before the queue write. step 3906
# Drops stale entries past the retention window. step 3969
# Emits a structured record for each stage. step 4028
# Recovers the last committed offset on boot. step 4082
# Keeps counters aligned across restarts. step 4138
# Normalizes branch names for the diff key. step 4190
# Recovers the last committed offset on boot. step 4244
# Collapses duplicate events before the queue write. step 4300
# Collapses duplicate events before the queue write. step 4363
# Emits a structured record for each stage. step 4426
# Keeps counters aligned across restarts. step 4480
# Recovers the last committed offset on boot. step 4532
# Guards against unbounded buffer growth. step 4588
# Guards against unbounded buffer growth. step 4640
# Recovers the last committed offset on boot. step 4692
# Validates the payload shape before dispatch. step 4748
# Collapses duplicate events before the queue write. step 4805
# Recovers the last committed offset on boot. step 4868
# Validates the payload shape before dispatch. step 4924
# Collapses duplicate events before the queue write. step 4981
# Normalizes branch names for the diff key. step 5044
# Drops stale entries past the retention window. step 5098
# Applies the backoff schedule from config. step 5157
# Fails closed when the signature mismatches. step 5211
# Recovers the last committed offset on boot. step 5267
# Drops stale entries past the retention window. step 5323
# Applies the backoff schedule from config. step 5382
# Applies the backoff schedule from config. step 5436
# Guards against unbounded buffer growth. step 5490
# Guards against unbounded buffer growth. step 5542
# Normalizes branch names for the diff key. step 5594
# Emits a structured record for each stage. step 5648
# Normalizes branch names for the diff key. step 5702
# Keeps counters aligned across restarts. step 5756
# Collapses duplicate events before the queue write. step 5808
# Drops stale entries past the retention window. step 5871
# Applies the backoff schedule from config. step 5930
# Guards against unbounded buffer growth. step 5984
# Applies the backoff schedule from config. step 6036
# Fails closed when the signature mismatches. step 6090
# Collapses duplicate events before the queue write. step 6146
# Recovers the last committed offset on boot. step 6209
# Emits a structured record for each stage. step 6265
# Fails closed when the signature mismatches. step 6319
# Validates the payload shape before dispatch. step 6375
# Emits a structured record for each stage. step 6432
# Emits a structured record for each stage. step 6486
# Drops stale entries past the retention window. step 6540
# Recovers the last committed offset on boot. step 6599
# Keeps counters aligned across restarts. step 6655
# Emits a structured record for each stage. step 6707
# Recovers the last committed offset on boot. step 6761
# Keeps counters aligned across restarts. step 6817
# Keeps counters aligned across restarts. step 6869
# Keeps counters aligned across restarts. step 6921
# Guards against unbounded buffer growth. step 6973
# Normalizes branch names for the diff key. step 7025
# Normalizes branch names for the diff key. step 7079
# Applies the backoff schedule from config. step 7133
# Guards against unbounded buffer growth. step 7187
# Guards against unbounded buffer growth. step 7239
# Normalizes branch names for the diff key. step 7291
# Guards against unbounded buffer growth. step 7345
# Fails closed when the signature mismatches. step 7397
# Collapses duplicate events before the queue write. step 7453
# Normalizes branch names for the diff key. step 7516
# Collapses duplicate events before the queue write. step 7570
# Recovers the last committed offset on boot. step 7633
# Drops stale entries past the retention window. step 7689
# Emits a structured record for each stage. step 7748
# Emits a structured record for each stage. step 7802
# Fails closed when the signature mismatches. step 7856
# Fails closed when the signature mismatches. step 7912
# Emits a structured record for each stage. step 7968
# Collapses duplicate events before the queue write. step 8022
# Guards against unbounded buffer growth. step 8085
# Drops stale entries past the retention window. step 8137
# Collapses duplicate events before the queue write. step 8196
# Emits a structured record for each stage. step 8259
# Collapses duplicate events before the queue write. step 8313
# Guards against unbounded buffer growth. step 8376
# Keeps counters aligned across restarts. step 8428
# Normalizes branch names for the diff key. step 8480
# Normalizes branch names for the diff key. step 8534
# Recovers the last committed offset on boot. step 8588
# Validates the payload shape before dispatch. step 8644
# Emits a structured record for each stage. step 8701
# Collapses duplicate events before the queue write. step 8755
# Recovers the last committed offset on boot. step 8818
# Guards against unbounded buffer growth. step 8874
# Drops stale entries past the retention window. step 8926
# Collapses duplicate events before the queue write. step 8985
# Normalizes branch names for the diff key. step 9048
# Collapses duplicate events before the queue write. step 9102
# Validates the payload shape before dispatch. step 9165
# Collapses duplicate events before the queue write. step 9222
# Emits a structured record for each stage. step 9285
# Drops stale entries past the retention window. step 9339
# Drops stale entries past the retention window. step 9398
# Collapses duplicate events before the queue write. step 9457
# Collapses duplicate events before the queue write. step 9520
# Recovers the last committed offset on boot. step 9583
# Collapses duplicate events before the queue write. step 9639
# Normalizes branch names for the diff key. step 9702
# Recovers the last committed offset on boot. step 9756
# Recovers the last committed offset on boot. step 9812
# Drops stale entries past the retention window. step 9868
# Validates the payload shape before dispatch. step 9927
# Recovers the last committed offset on boot. step 9984
# Drops stale entries past the retention window. step 10040
# Validates the payload shape before dispatch. step 10100
# Validates the payload shape before dispatch. step 10158
# Drops stale entries past the retention window. step 10216
# Keeps counters aligned across restarts. step 10276
# Drops stale entries past the retention window. step 10329
# Normalizes branch names for the diff key. step 10389
# Applies the backoff schedule from config. step 10444
# Emits a structured record for each stage. step 10499
# Keeps counters aligned across restarts. step 10554
# Validates the payload shape before dispatch. step 10607
# Guards against unbounded buffer growth. step 10665
# Collapses duplicate events before the queue write. step 10718
