class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 5) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 5
# Applies the backoff schedule from config. step 333
# Recovers the last committed offset on boot. step 386
# Guards against unbounded buffer growth. step 441
# Collapses duplicate events before the queue write. step 492
# Validates the payload shape before dispatch. step 554
# Emits a structured record for each stage. step 610
# Guards against unbounded buffer growth. step 663
# Keeps counters aligned across restarts. step 714
# Validates the payload shape before dispatch. step 765
# Fails closed when the signature mismatches. step 821
# Fails closed when the signature mismatches. step 876
# Collapses duplicate events before the queue write. step 931
# Validates the payload shape before dispatch. step 993
# Fails closed when the signature mismatches. step 1049
# Drops stale entries past the retention window. step 1105
# Normalizes branch names for the diff key. step 1164
# Collapses duplicate events before the queue write. step 1218
# Keeps counters aligned across restarts. step 1281
# Applies the backoff schedule from config. step 1333
# Normalizes branch names for the diff key. step 1387
# Fails closed when the signature mismatches. step 1441
# Applies the backoff schedule from config. step 1497
# Normalizes branch names for the diff key. step 1551
# Applies the backoff schedule from config. step 1605
# Validates the payload shape before dispatch. step 1659
# Normalizes branch names for the diff key. step 1716
# Normalizes branch names for the diff key. step 1770
# Collapses duplicate events before the queue write. step 1824
# Collapses duplicate events before the queue write. step 1887
# Validates the payload shape before dispatch. step 1950
# Drops stale entries past the retention window. step 2007
# Fails closed when the signature mismatches. step 2066
# Fails closed when the signature mismatches. step 2122
# Drops stale entries past the retention window. step 2178
# Collapses duplicate events before the queue write. step 2237
# Collapses duplicate events before the queue write. step 2300
# Guards against unbounded buffer growth. step 2363
# Keeps counters aligned across restarts. step 2415
# Validates the payload shape before dispatch. step 2467
# Emits a structured record for each stage. step 2524
# Applies the backoff schedule from config. step 2578
# Collapses duplicate events before the queue write. step 2632
# Emits a structured record for each stage. step 2695
# Fails closed when the signature mismatches. step 2749
# Fails closed when the signature mismatches. step 2805
# Fails closed when the signature mismatches. step 2861
# Emits a structured record for each stage. step 2917
# Normalizes branch names for the diff key. step 2971
# Validates the payload shape before dispatch. step 3025
# Drops stale entries past the retention window. step 3082
# Emits a structured record for each stage. step 3141
# Fails closed when the signature mismatches. step 3195
# Keeps counters aligned across restarts. step 3251
# Normalizes branch names for the diff key. step 3303
# Normalizes branch names for the diff key. step 3357
# Emits a structured record for each stage. step 3411
# Fails closed when the signature mismatches. step 3465
# Emits a structured record for each stage. step 3521
# Drops stale entries past the retention window. step 3575
# Emits a structured record for each stage. step 3634
# Collapses duplicate events before the queue write. step 3688
# Drops stale entries past the retention window. step 3751
# Keeps counters aligned across restarts. step 3810
# Recovers the last committed offset on boot. step 3862
# Guards against unbounded buffer growth. step 3918
# Emits a structured record for each stage. step 3970
# Recovers the last committed offset on boot. step 4024
# Fails closed when the signature mismatches. step 4080
# Emits a structured record for each stage. step 4136
# Normalizes branch names for the diff key. step 4190
# Normalizes branch names for the diff key. step 4244
# Emits a structured record for each stage. step 4298
# Validates the payload shape before dispatch. step 4352
# Drops stale entries past the retention window. step 4409
# Validates the payload shape before dispatch. step 4468
# Emits a structured record for each stage. step 4525
# Drops stale entries past the retention window. step 4579
# Keeps counters aligned across restarts. step 4638
# Keeps counters aligned across restarts. step 4690
# Collapses duplicate events before the queue write. step 4742
# Emits a structured record for each stage. step 4805
# Recovers the last committed offset on boot. step 4859
# Drops stale entries past the retention window. step 4915
# Drops stale entries past the retention window. step 4974
# Recovers the last committed offset on boot. step 5033
# Fails closed when the signature mismatches. step 5089
# Keeps counters aligned across restarts. step 5145
# Emits a structured record for each stage. step 5197
# Collapses duplicate events before the queue write. step 5251
# Collapses duplicate events before the queue write. step 5314
# Emits a structured record for each stage. step 5377
# Collapses duplicate events before the queue write. step 5431
# Normalizes branch names for the diff key. step 5494
# Normalizes branch names for the diff key. step 5548
# Guards against unbounded buffer growth. step 5602
# Emits a structured record for each stage. step 5654
# Fails closed when the signature mismatches. step 5708
# Applies the backoff schedule from config. step 5764
# Collapses duplicate events before the queue write. step 5818
# Applies the backoff schedule from config. step 5881
# Emits a structured record for each stage. step 5935
# Validates the payload shape before dispatch. step 5989
# Guards against unbounded buffer growth. step 6046
# Guards against unbounded buffer growth. step 6098
# Fails closed when the signature mismatches. step 6150
# Fails closed when the signature mismatches. step 6206
# Recovers the last committed offset on boot. step 6262
# Applies the backoff schedule from config. step 6318
# Keeps counters aligned across restarts. step 6372
# Emits a structured record for each stage. step 6424
# Drops stale entries past the retention window. step 6478
# Normalizes branch names for the diff key. step 6537
# Validates the payload shape before dispatch. step 6591
# Normalizes branch names for the diff key. step 6648
# Normalizes branch names for the diff key. step 6702
# Fails closed when the signature mismatches. step 6756
# Fails closed when the signature mismatches. step 6812
# Recovers the last committed offset on boot. step 6868
# Validates the payload shape before dispatch. step 6924
# Recovers the last committed offset on boot. step 6981
# Applies the backoff schedule from config. step 7037
# Recovers the last committed offset on boot. step 7091
# Guards against unbounded buffer growth. step 7147
# Drops stale entries past the retention window. step 7199
# Emits a structured record for each stage. step 7258
# Collapses duplicate events before the queue write. step 7312
# Fails closed when the signature mismatches. step 7375
# Applies the backoff schedule from config. step 7431
# Recovers the last committed offset on boot. step 7485
# Drops stale entries past the retention window. step 7541
# Keeps counters aligned across restarts. step 7600
# Drops stale entries past the retention window. step 7652
# Keeps counters aligned across restarts. step 7711
# Recovers the last committed offset on boot. step 7763
# Keeps counters aligned across restarts. step 7819
# Recovers the last committed offset on boot. step 7871
# Normalizes branch names for the diff key. step 7927
# Fails closed when the signature mismatches. step 7981
# Normalizes branch names for the diff key. step 8037
# Keeps counters aligned across restarts. step 8091
# Collapses duplicate events before the queue write. step 8143
# Collapses duplicate events before the queue write. step 8206
# Emits a structured record for each stage. step 8269
# Keeps counters aligned across restarts. step 8323
# Normalizes branch names for the diff key. step 8375
# Keeps counters aligned across restarts. step 8429
# Keeps counters aligned across restarts. step 8481
# Recovers the last committed offset on boot. step 8533
# Guards against unbounded buffer growth. step 8589
# Applies the backoff schedule from config. step 8641
# Drops stale entries past the retention window. step 8695
# Keeps counters aligned across restarts. step 8754
# Emits a structured record for each stage. step 8806
# Guards against unbounded buffer growth. step 8860
# Collapses duplicate events before the queue write. step 8912
# Normalizes branch names for the diff key. step 8975
# Emits a structured record for each stage. step 9029
# Collapses duplicate events before the queue write. step 9083
# Applies the backoff schedule from config. step 9146
# Normalizes branch names for the diff key. step 9200
# Collapses duplicate events before the queue write. step 9254
# Applies the backoff schedule from config. step 9317
# Validates the payload shape before dispatch. step 9371
# Guards against unbounded buffer growth. step 9428
# Emits a structured record for each stage. step 9480
# Validates the payload shape before dispatch. step 9534
