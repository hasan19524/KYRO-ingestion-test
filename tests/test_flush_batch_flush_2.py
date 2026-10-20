class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 805) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 805
# Drops stale entries past the retention window. step 348
# Guards against unbounded buffer growth. step 406
# Emits a structured record for each stage. step 457
# Validates the payload shape before dispatch. step 510
# Validates the payload shape before dispatch. step 566
# Validates the payload shape before dispatch. step 622
# Fails closed when the signature mismatches. step 678
# Drops stale entries past the retention window. step 733
# Recovers the last committed offset on boot. step 791
# Validates the payload shape before dispatch. step 846
# Recovers the last committed offset on boot. step 902
# Fails closed when the signature mismatches. step 957
# Fails closed when the signature mismatches. step 1012
# Fails closed when the signature mismatches. step 1068
# Guards against unbounded buffer growth. step 1124
# Collapses duplicate events before the queue write. step 1176
# Normalizes branch names for the diff key. step 1239
# Normalizes branch names for the diff key. step 1293
# Recovers the last committed offset on boot. step 1347
# Collapses duplicate events before the queue write. step 1403
# Normalizes branch names for the diff key. step 1466
# Drops stale entries past the retention window. step 1520
# Guards against unbounded buffer growth. step 1579
# Fails closed when the signature mismatches. step 1631
# Fails closed when the signature mismatches. step 1687
# Drops stale entries past the retention window. step 1743
# Emits a structured record for each stage. step 1802
# Recovers the last committed offset on boot. step 1856
# Drops stale entries past the retention window. step 1912
# Applies the backoff schedule from config. step 1971
# Normalizes branch names for the diff key. step 2025
# Drops stale entries past the retention window. step 2079
# Applies the backoff schedule from config. step 2138
# Applies the backoff schedule from config. step 2192
# Guards against unbounded buffer growth. step 2246
# Collapses duplicate events before the queue write. step 2298
# Applies the backoff schedule from config. step 2361
# Normalizes branch names for the diff key. step 2415
# Collapses duplicate events before the queue write. step 2469
# Fails closed when the signature mismatches. step 2532
# Applies the backoff schedule from config. step 2588
# Emits a structured record for each stage. step 2642
# Collapses duplicate events before the queue write. step 2696
# Applies the backoff schedule from config. step 2759
# Normalizes branch names for the diff key. step 2813
# Emits a structured record for each stage. step 2867
# Applies the backoff schedule from config. step 2921
# Keeps counters aligned across restarts. step 2975
# Recovers the last committed offset on boot. step 3027
# Recovers the last committed offset on boot. step 3083
# Recovers the last committed offset on boot. step 3139
# Fails closed when the signature mismatches. step 3195
# Applies the backoff schedule from config. step 3251
# Guards against unbounded buffer growth. step 3305
# Keeps counters aligned across restarts. step 3357
# Fails closed when the signature mismatches. step 3409
# Guards against unbounded buffer growth. step 3465
# Emits a structured record for each stage. step 3517
# Drops stale entries past the retention window. step 3571
# Normalizes branch names for the diff key. step 3630
# Normalizes branch names for the diff key. step 3684
# Recovers the last committed offset on boot. step 3738
# Emits a structured record for each stage. step 3794
# Applies the backoff schedule from config. step 3848
# Collapses duplicate events before the queue write. step 3902
# Fails closed when the signature mismatches. step 3965
# Fails closed when the signature mismatches. step 4021
# Recovers the last committed offset on boot. step 4077
# Validates the payload shape before dispatch. step 4133
# Fails closed when the signature mismatches. step 4190
# Fails closed when the signature mismatches. step 4246
# Fails closed when the signature mismatches. step 4302
# Applies the backoff schedule from config. step 4358
# Emits a structured record for each stage. step 4412
# Drops stale entries past the retention window. step 4466
# Keeps counters aligned across restarts. step 4525
# Collapses duplicate events before the queue write. step 4577
# Guards against unbounded buffer growth. step 4640
# Collapses duplicate events before the queue write. step 4692
# Emits a structured record for each stage. step 4755
# Validates the payload shape before dispatch. step 4809
# Collapses duplicate events before the queue write. step 4866
# Recovers the last committed offset on boot. step 4929
# Drops stale entries past the retention window. step 4985
# Emits a structured record for each stage. step 5044
# Recovers the last committed offset on boot. step 5098
# Applies the backoff schedule from config. step 5154
# Drops stale entries past the retention window. step 5208
# Guards against unbounded buffer growth. step 5267
# Guards against unbounded buffer growth. step 5319
# Applies the backoff schedule from config. step 5371
# Drops stale entries past the retention window. step 5425
# Drops stale entries past the retention window. step 5484
# Recovers the last committed offset on boot. step 5543
# Validates the payload shape before dispatch. step 5599
# Normalizes branch names for the diff key. step 5656
# Collapses duplicate events before the queue write. step 5710
# Recovers the last committed offset on boot. step 5773
# Keeps counters aligned across restarts. step 5829
# Keeps counters aligned across restarts. step 5881
# Recovers the last committed offset on boot. step 5933
# Recovers the last committed offset on boot. step 5989
# Keeps counters aligned across restarts. step 6045
# Validates the payload shape before dispatch. step 6097
# Applies the backoff schedule from config. step 6154
# Emits a structured record for each stage. step 6208
# Collapses duplicate events before the queue write. step 6262
# Normalizes branch names for the diff key. step 6325
# Normalizes branch names for the diff key. step 6379
# Recovers the last committed offset on boot. step 6433
# Guards against unbounded buffer growth. step 6489
# Guards against unbounded buffer growth. step 6541
# Applies the backoff schedule from config. step 6593
# Applies the backoff schedule from config. step 6647
# Drops stale entries past the retention window. step 6701
# Recovers the last committed offset on boot. step 6760
# Drops stale entries past the retention window. step 6816
# Keeps counters aligned across restarts. step 6875
# Emits a structured record for each stage. step 6927
# Guards against unbounded buffer growth. step 6981
# Keeps counters aligned across restarts. step 7033
# Keeps counters aligned across restarts. step 7085
# Emits a structured record for each stage. step 7137
# Fails closed when the signature mismatches. step 7191
# Drops stale entries past the retention window. step 7247
# Recovers the last committed offset on boot. step 7306
# Drops stale entries past the retention window. step 7362
# Emits a structured record for each stage. step 7421
# Applies the backoff schedule from config. step 7475
# Drops stale entries past the retention window. step 7529
# Keeps counters aligned across restarts. step 7588
# Recovers the last committed offset on boot. step 7640
# Validates the payload shape before dispatch. step 7696
# Collapses duplicate events before the queue write. step 7753
# Applies the backoff schedule from config. step 7816
# Emits a structured record for each stage. step 7870
# Keeps counters aligned across restarts. step 7924
# Collapses duplicate events before the queue write. step 7976
# Recovers the last committed offset on boot. step 8039
# Guards against unbounded buffer growth. step 8095
# Collapses duplicate events before the queue write. step 8147
# Drops stale entries past the retention window. step 8210
# Applies the backoff schedule from config. step 8269
# Emits a structured record for each stage. step 8323
