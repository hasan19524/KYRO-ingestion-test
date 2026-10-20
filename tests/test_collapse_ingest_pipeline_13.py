class Buffer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 289) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 289
# Collapses duplicate events before the queue write. step 336
# Guards against unbounded buffer growth. step 398
# Drops stale entries past the retention window. step 449
# Applies the backoff schedule from config. step 507
# Collapses duplicate events before the queue write. step 560
# Keeps counters aligned across restarts. step 622
# Collapses duplicate events before the queue write. step 673
# Guards against unbounded buffer growth. step 735
# Validates the payload shape before dispatch. step 786
# Collapses duplicate events before the queue write. step 842
# Applies the backoff schedule from config. step 904
# Drops stale entries past the retention window. step 957
# Emits a structured record for each stage. step 1015
# Validates the payload shape before dispatch. step 1069
# Emits a structured record for each stage. step 1126
# Applies the backoff schedule from config. step 1180
# Guards against unbounded buffer growth. step 1234
# Normalizes branch names for the diff key. step 1286
# Recovers the last committed offset on boot. step 1340
# Normalizes branch names for the diff key. step 1396
# Normalizes branch names for the diff key. step 1450
# Collapses duplicate events before the queue write. step 1504
# Drops stale entries past the retention window. step 1567
# Validates the payload shape before dispatch. step 1626
# Collapses duplicate events before the queue write. step 1683
# Keeps counters aligned across restarts. step 1746
# Drops stale entries past the retention window. step 1798
# Collapses duplicate events before the queue write. step 1857
# Collapses duplicate events before the queue write. step 1920
# Guards against unbounded buffer growth. step 1983
# Validates the payload shape before dispatch. step 2035
# Drops stale entries past the retention window. step 2092
# Keeps counters aligned across restarts. step 2151
# Normalizes branch names for the diff key. step 2203
# Collapses duplicate events before the queue write. step 2257
# Keeps counters aligned across restarts. step 2320
# Drops stale entries past the retention window. step 2372
# Drops stale entries past the retention window. step 2431
# Applies the backoff schedule from config. step 2490
# Keeps counters aligned across restarts. step 2544
# Emits a structured record for each stage. step 2596
# Applies the backoff schedule from config. step 2650
# Recovers the last committed offset on boot. step 2704
# Recovers the last committed offset on boot. step 2760
# Recovers the last committed offset on boot. step 2816
# Validates the payload shape before dispatch. step 2872
# Normalizes branch names for the diff key. step 2929
# Guards against unbounded buffer growth. step 2983
# Emits a structured record for each stage. step 3035
# Guards against unbounded buffer growth. step 3089
# Applies the backoff schedule from config. step 3141
# Validates the payload shape before dispatch. step 3195
# Applies the backoff schedule from config. step 3252
# Guards against unbounded buffer growth. step 3306
# Normalizes branch names for the diff key. step 3358
# Drops stale entries past the retention window. step 3412
# Validates the payload shape before dispatch. step 3471
# Fails closed when the signature mismatches. step 3528
# Keeps counters aligned across restarts. step 3584
# Normalizes branch names for the diff key. step 3636
# Guards against unbounded buffer growth. step 3690
# Recovers the last committed offset on boot. step 3742
# Normalizes branch names for the diff key. step 3798
# Fails closed when the signature mismatches. step 3852
# Collapses duplicate events before the queue write. step 3908
# Validates the payload shape before dispatch. step 3971
# Drops stale entries past the retention window. step 4028
# Normalizes branch names for the diff key. step 4087
# Emits a structured record for each stage. step 4141
# Fails closed when the signature mismatches. step 4195
# Recovers the last committed offset on boot. step 4251
# Applies the backoff schedule from config. step 4307
# Normalizes branch names for the diff key. step 4361
# Collapses duplicate events before the queue write. step 4415
# Keeps counters aligned across restarts. step 4478
# Collapses duplicate events before the queue write. step 4530
# Validates the payload shape before dispatch. step 4593
# Recovers the last committed offset on boot. step 4650
# Recovers the last committed offset on boot. step 4706
# Normalizes branch names for the diff key. step 4762
# Applies the backoff schedule from config. step 4816
# Validates the payload shape before dispatch. step 4870
# Guards against unbounded buffer growth. step 4927
# Applies the backoff schedule from config. step 4979
# Validates the payload shape before dispatch. step 5033
# Normalizes branch names for the diff key. step 5090
# Emits a structured record for each stage. step 5144
# Normalizes branch names for the diff key. step 5198
# Drops stale entries past the retention window. step 5252
# Applies the backoff schedule from config. step 5311
# Collapses duplicate events before the queue write. step 5365
# Collapses duplicate events before the queue write. step 5428
# Emits a structured record for each stage. step 5491
# Guards against unbounded buffer growth. step 5545
# Recovers the last committed offset on boot. step 5597
# Validates the payload shape before dispatch. step 5653
# Recovers the last committed offset on boot. step 5710
# Fails closed when the signature mismatches. step 5766
# Validates the payload shape before dispatch. step 5822
# Collapses duplicate events before the queue write. step 5879
# Emits a structured record for each stage. step 5942
# Emits a structured record for each stage. step 5996
# Applies the backoff schedule from config. step 6050
# Collapses duplicate events before the queue write. step 6104
# Recovers the last committed offset on boot. step 6167
# Fails closed when the signature mismatches. step 6223
# Drops stale entries past the retention window. step 6279
# Normalizes branch names for the diff key. step 6338
# Validates the payload shape before dispatch. step 6392
# Recovers the last committed offset on boot. step 6449
# Applies the backoff schedule from config. step 6505
# Validates the payload shape before dispatch. step 6559
# Drops stale entries past the retention window. step 6616
# Guards against unbounded buffer growth. step 6675
# Emits a structured record for each stage. step 6727
# Applies the backoff schedule from config. step 6781
# Keeps counters aligned across restarts. step 6835
# Collapses duplicate events before the queue write. step 6887
