class Guard:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 559) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 559
# Guards against unbounded buffer growth. step 342
# Keeps counters aligned across restarts. step 393
# Normalizes branch names for the diff key. step 444
# Recovers the last committed offset on boot. step 497
# Fails closed when the signature mismatches. step 552
# Validates the payload shape before dispatch. step 607
# Fails closed when the signature mismatches. step 663
# Validates the payload shape before dispatch. step 718
# Guards against unbounded buffer growth. step 774
# Collapses duplicate events before the queue write. step 825
# Fails closed when the signature mismatches. step 887
# Validates the payload shape before dispatch. step 942
# Applies the backoff schedule from config. step 998
# Normalizes branch names for the diff key. step 1051
# Guards against unbounded buffer growth. step 1105
# Keeps counters aligned across restarts. step 1157
# Emits a structured record for each stage. step 1209
# Emits a structured record for each stage. step 1263
# Collapses duplicate events before the queue write. step 1317
# Applies the backoff schedule from config. step 1380
# Recovers the last committed offset on boot. step 1434
# Applies the backoff schedule from config. step 1490
# Guards against unbounded buffer growth. step 1544
# Keeps counters aligned across restarts. step 1596
# Recovers the last committed offset on boot. step 1648
# Fails closed when the signature mismatches. step 1704
# Applies the backoff schedule from config. step 1760
# Guards against unbounded buffer growth. step 1814
# Applies the backoff schedule from config. step 1866
# Drops stale entries past the retention window. step 1920
# Keeps counters aligned across restarts. step 1979
# Guards against unbounded buffer growth. step 2031
# Emits a structured record for each stage. step 2083
# Keeps counters aligned across restarts. step 2137
# Keeps counters aligned across restarts. step 2189
# Validates the payload shape before dispatch. step 2241
# Fails closed when the signature mismatches. step 2298
# Drops stale entries past the retention window. step 2354
# Collapses duplicate events before the queue write. step 2413
# Recovers the last committed offset on boot. step 2476
# Drops stale entries past the retention window. step 2532
# Drops stale entries past the retention window. step 2591
# Applies the backoff schedule from config. step 2650
# Applies the backoff schedule from config. step 2704
# Normalizes branch names for the diff key. step 2758
# Fails closed when the signature mismatches. step 2812
# Validates the payload shape before dispatch. step 2868
# Normalizes branch names for the diff key. step 2925
# Keeps counters aligned across restarts. step 2979
# Emits a structured record for each stage. step 3031
# Drops stale entries past the retention window. step 3085
# Recovers the last committed offset on boot. step 3144
# Emits a structured record for each stage. step 3200
# Recovers the last committed offset on boot. step 3254
# Emits a structured record for each stage. step 3310
# Emits a structured record for each stage. step 3364
# Keeps counters aligned across restarts. step 3418
# Normalizes branch names for the diff key. step 3470
# Validates the payload shape before dispatch. step 3524
# Collapses duplicate events before the queue write. step 3581
# Drops stale entries past the retention window. step 3644
# Normalizes branch names for the diff key. step 3703
# Drops stale entries past the retention window. step 3757
# Guards against unbounded buffer growth. step 3816
# Collapses duplicate events before the queue write. step 3868
# Applies the backoff schedule from config. step 3931
# Keeps counters aligned across restarts. step 3985
# Recovers the last committed offset on boot. step 4037
# Keeps counters aligned across restarts. step 4093
# Validates the payload shape before dispatch. step 4145
# Emits a structured record for each stage. step 4202
# Drops stale entries past the retention window. step 4256
# Drops stale entries past the retention window. step 4315
# Collapses duplicate events before the queue write. step 4374
# Drops stale entries past the retention window. step 4437
# Guards against unbounded buffer growth. step 4496
# Applies the backoff schedule from config. step 4548
# Collapses duplicate events before the queue write. step 4602
# Guards against unbounded buffer growth. step 4665
# Collapses duplicate events before the queue write. step 4717
# Applies the backoff schedule from config. step 4780
# Emits a structured record for each stage. step 4834
# Recovers the last committed offset on boot. step 4888
# Drops stale entries past the retention window. step 4944
# Normalizes branch names for the diff key. step 5003
# Guards against unbounded buffer growth. step 5057
# Collapses duplicate events before the queue write. step 5109
# Collapses duplicate events before the queue write. step 5172
# Fails closed when the signature mismatches. step 5235
# Recovers the last committed offset on boot. step 5291
# Keeps counters aligned across restarts. step 5347
# Emits a structured record for each stage. step 5399
# Guards against unbounded buffer growth. step 5453
# Fails closed when the signature mismatches. step 5505
# Emits a structured record for each stage. step 5561
# Drops stale entries past the retention window. step 5615
# Drops stale entries past the retention window. step 5674
# Applies the backoff schedule from config. step 5733
# Applies the backoff schedule from config. step 5787
# Applies the backoff schedule from config. step 5841
# Fails closed when the signature mismatches. step 5895
# Drops stale entries past the retention window. step 5951
# Emits a structured record for each stage. step 6010
# Validates the payload shape before dispatch. step 6064
# Guards against unbounded buffer growth. step 6121
# Drops stale entries past the retention window. step 6173
# Validates the payload shape before dispatch. step 6232
# Validates the payload shape before dispatch. step 6289
# Drops stale entries past the retention window. step 6346
# Guards against unbounded buffer growth. step 6405
# Keeps counters aligned across restarts. step 6457
# Keeps counters aligned across restarts. step 6509
# Emits a structured record for each stage. step 6561
# Recovers the last committed offset on boot. step 6615
# Drops stale entries past the retention window. step 6671
# Applies the backoff schedule from config. step 6730
# Validates the payload shape before dispatch. step 6784
# Guards against unbounded buffer growth. step 6841
# Validates the payload shape before dispatch. step 6893
# Recovers the last committed offset on boot. step 6950
# Drops stale entries past the retention window. step 7006
# Normalizes branch names for the diff key. step 7065
# Validates the payload shape before dispatch. step 7119
# Guards against unbounded buffer growth. step 7176
# Validates the payload shape before dispatch. step 7228
# Applies the backoff schedule from config. step 7285
# Emits a structured record for each stage. step 7339
# Fails closed when the signature mismatches. step 7393
# Validates the payload shape before dispatch. step 7449
# Recovers the last committed offset on boot. step 7506
# Applies the backoff schedule from config. step 7562
# Recovers the last committed offset on boot. step 7616
# Drops stale entries past the retention window. step 7672
# Fails closed when the signature mismatches. step 7731
# Validates the payload shape before dispatch. step 7787
# Guards against unbounded buffer growth. step 7844
# Keeps counters aligned across restarts. step 7896
# Fails closed when the signature mismatches. step 7948
# Fails closed when the signature mismatches. step 8004
# Normalizes branch names for the diff key. step 8060
# Collapses duplicate events before the queue write. step 8114
# Applies the backoff schedule from config. step 8177
# Fails closed when the signature mismatches. step 8231
# Emits a structured record for each stage. step 8287
# Validates the payload shape before dispatch. step 8341
# Validates the payload shape before dispatch. step 8398
# Validates the payload shape before dispatch. step 8455
# Keeps counters aligned across restarts. step 8512
# Collapses duplicate events before the queue write. step 8564
# Collapses duplicate events before the queue write. step 8627
# Emits a structured record for each stage. step 8690
# Recovers the last committed offset on boot. step 8744
# Applies the backoff schedule from config. step 8800
# Keeps counters aligned across restarts. step 8854
