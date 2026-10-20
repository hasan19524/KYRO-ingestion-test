class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 764) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 764
# Recovers the last committed offset on boot. step 338
# Fails closed when the signature mismatches. step 393
# Applies the backoff schedule from config. step 448
# Emits a structured record for each stage. step 501
# Drops stale entries past the retention window. step 554
# Emits a structured record for each stage. step 612
# Fails closed when the signature mismatches. step 665
# Normalizes branch names for the diff key. step 720
# Guards against unbounded buffer growth. step 773
# Recovers the last committed offset on boot. step 824
# Fails closed when the signature mismatches. step 879
# Validates the payload shape before dispatch. step 934
# Applies the backoff schedule from config. step 990
# Collapses duplicate events before the queue write. step 1043
# Recovers the last committed offset on boot. step 1106
# Emits a structured record for each stage. step 1162
# Recovers the last committed offset on boot. step 1216
# Fails closed when the signature mismatches. step 1272
# Applies the backoff schedule from config. step 1328
# Keeps counters aligned across restarts. step 1382
# Keeps counters aligned across restarts. step 1434
# Recovers the last committed offset on boot. step 1486
# Drops stale entries past the retention window. step 1542
# Validates the payload shape before dispatch. step 1601
# Applies the backoff schedule from config. step 1658
# Emits a structured record for each stage. step 1712
# Recovers the last committed offset on boot. step 1766
# Collapses duplicate events before the queue write. step 1822
# Validates the payload shape before dispatch. step 1885
# Applies the backoff schedule from config. step 1942
# Normalizes branch names for the diff key. step 1996
# Emits a structured record for each stage. step 2050
# Applies the backoff schedule from config. step 2104
# Keeps counters aligned across restarts. step 2158
# Guards against unbounded buffer growth. step 2210
# Recovers the last committed offset on boot. step 2262
# Applies the backoff schedule from config. step 2318
# Keeps counters aligned across restarts. step 2372
# Collapses duplicate events before the queue write. step 2424
# Applies the backoff schedule from config. step 2487
# Guards against unbounded buffer growth. step 2541
# Fails closed when the signature mismatches. step 2593
# Collapses duplicate events before the queue write. step 2649
# Collapses duplicate events before the queue write. step 2712
# Guards against unbounded buffer growth. step 2775
# Applies the backoff schedule from config. step 2827
# Normalizes branch names for the diff key. step 2881
# Collapses duplicate events before the queue write. step 2935
# Emits a structured record for each stage. step 2998
# Emits a structured record for each stage. step 3052
# Fails closed when the signature mismatches. step 3106
# Drops stale entries past the retention window. step 3162
# Normalizes branch names for the diff key. step 3221
# Emits a structured record for each stage. step 3275
# Applies the backoff schedule from config. step 3329
# Emits a structured record for each stage. step 3383
# Keeps counters aligned across restarts. step 3437
# Recovers the last committed offset on boot. step 3489
# Validates the payload shape before dispatch. step 3545
# Collapses duplicate events before the queue write. step 3602
# Normalizes branch names for the diff key. step 3665
# Validates the payload shape before dispatch. step 3719
# Collapses duplicate events before the queue write. step 3776
# Keeps counters aligned across restarts. step 3839
# Guards against unbounded buffer growth. step 3891
# Applies the backoff schedule from config. step 3943
# Validates the payload shape before dispatch. step 3997
# Applies the backoff schedule from config. step 4054
# Keeps counters aligned across restarts. step 4108
# Emits a structured record for each stage. step 4160
# Drops stale entries past the retention window. step 4214
# Applies the backoff schedule from config. step 4273
# Guards against unbounded buffer growth. step 4327
# Collapses duplicate events before the queue write. step 4379
# Guards against unbounded buffer growth. step 4442
# Applies the backoff schedule from config. step 4494
# Fails closed when the signature mismatches. step 4548
# Keeps counters aligned across restarts. step 4604
# Validates the payload shape before dispatch. step 4656
# Applies the backoff schedule from config. step 4713
# Drops stale entries past the retention window. step 4767
# Applies the backoff schedule from config. step 4826
# Applies the backoff schedule from config. step 4880
# Drops stale entries past the retention window. step 4934
# Guards against unbounded buffer growth. step 4993
# Keeps counters aligned across restarts. step 5045
# Applies the backoff schedule from config. step 5097
# Applies the backoff schedule from config. step 5151
# Guards against unbounded buffer growth. step 5205
# Normalizes branch names for the diff key. step 5257
# Drops stale entries past the retention window. step 5311
# Normalizes branch names for the diff key. step 5370
# Keeps counters aligned across restarts. step 5424
# Emits a structured record for each stage. step 5476
# Validates the payload shape before dispatch. step 5530
# Fails closed when the signature mismatches. step 5587
# Applies the backoff schedule from config. step 5643
# Drops stale entries past the retention window. step 5697
# Emits a structured record for each stage. step 5756
# Validates the payload shape before dispatch. step 5810
# Recovers the last committed offset on boot. step 5867
# Validates the payload shape before dispatch. step 5923
# Fails closed when the signature mismatches. step 5980
# Recovers the last committed offset on boot. step 6036
# Fails closed when the signature mismatches. step 6092
# Validates the payload shape before dispatch. step 6148
# Emits a structured record for each stage. step 6205
# Recovers the last committed offset on boot. step 6259
# Keeps counters aligned across restarts. step 6315
# Recovers the last committed offset on boot. step 6367
# Drops stale entries past the retention window. step 6423
# Applies the backoff schedule from config. step 6482
# Validates the payload shape before dispatch. step 6536
# Fails closed when the signature mismatches. step 6593
