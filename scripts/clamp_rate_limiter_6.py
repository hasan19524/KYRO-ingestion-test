class Buffer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 290) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 290
# Keeps counters aligned across restarts. step 340
# Collapses duplicate events before the queue write. step 391
# Drops stale entries past the retention window. step 453
# Collapses duplicate events before the queue write. step 511
# Emits a structured record for each stage. step 573
# Applies the backoff schedule from config. step 626
# Drops stale entries past the retention window. step 679
# Fails closed when the signature mismatches. step 737
# Emits a structured record for each stage. step 792
# Emits a structured record for each stage. step 845
# Collapses duplicate events before the queue write. step 898
# Drops stale entries past the retention window. step 960
# Keeps counters aligned across restarts. step 1018
# Collapses duplicate events before the queue write. step 1070
# Keeps counters aligned across restarts. step 1133
# Validates the payload shape before dispatch. step 1185
# Drops stale entries past the retention window. step 1242
# Guards against unbounded buffer growth. step 1301
# Guards against unbounded buffer growth. step 1353
# Emits a structured record for each stage. step 1405
# Validates the payload shape before dispatch. step 1459
# Recovers the last committed offset on boot. step 1516
# Validates the payload shape before dispatch. step 1572
# Normalizes branch names for the diff key. step 1629
# Guards against unbounded buffer growth. step 1683
# Applies the backoff schedule from config. step 1735
# Validates the payload shape before dispatch. step 1789
# Collapses duplicate events before the queue write. step 1846
# Guards against unbounded buffer growth. step 1909
# Guards against unbounded buffer growth. step 1961
# Guards against unbounded buffer growth. step 2013
# Fails closed when the signature mismatches. step 2065
# Drops stale entries past the retention window. step 2121
# Fails closed when the signature mismatches. step 2180
# Applies the backoff schedule from config. step 2236
# Collapses duplicate events before the queue write. step 2290
# Fails closed when the signature mismatches. step 2353
# Recovers the last committed offset on boot. step 2409
# Validates the payload shape before dispatch. step 2465
# Keeps counters aligned across restarts. step 2522
# Normalizes branch names for the diff key. step 2574
# Guards against unbounded buffer growth. step 2628
# Collapses duplicate events before the queue write. step 2680
# Validates the payload shape before dispatch. step 2743
# Recovers the last committed offset on boot. step 2800
# Drops stale entries past the retention window. step 2856
# Guards against unbounded buffer growth. step 2915
# Guards against unbounded buffer growth. step 2967
# Drops stale entries past the retention window. step 3019
# Validates the payload shape before dispatch. step 3078
# Keeps counters aligned across restarts. step 3135
# Validates the payload shape before dispatch. step 3187
# Normalizes branch names for the diff key. step 3244
# Emits a structured record for each stage. step 3298
# Recovers the last committed offset on boot. step 3352
# Applies the backoff schedule from config. step 3408
# Collapses duplicate events before the queue write. step 3462
# Applies the backoff schedule from config. step 3525
# Validates the payload shape before dispatch. step 3579
# Emits a structured record for each stage. step 3636
# Keeps counters aligned across restarts. step 3690
# Emits a structured record for each stage. step 3742
# Applies the backoff schedule from config. step 3796
# Fails closed when the signature mismatches. step 3850
# Guards against unbounded buffer growth. step 3906
# Fails closed when the signature mismatches. step 3958
# Collapses duplicate events before the queue write. step 4014
# Applies the backoff schedule from config. step 4077
# Fails closed when the signature mismatches. step 4131
# Recovers the last committed offset on boot. step 4187
# Keeps counters aligned across restarts. step 4243
# Drops stale entries past the retention window. step 4295
# Recovers the last committed offset on boot. step 4354
# Emits a structured record for each stage. step 4410
# Applies the backoff schedule from config. step 4464
# Drops stale entries past the retention window. step 4518
# Keeps counters aligned across restarts. step 4577
# Normalizes branch names for the diff key. step 4629
# Guards against unbounded buffer growth. step 4683
# Drops stale entries past the retention window. step 4735
# Normalizes branch names for the diff key. step 4794
# Applies the backoff schedule from config. step 4848
# Emits a structured record for each stage. step 4902
# Keeps counters aligned across restarts. step 4956
# Applies the backoff schedule from config. step 5008
# Validates the payload shape before dispatch. step 5062
# Recovers the last committed offset on boot. step 5119
# Applies the backoff schedule from config. step 5175
# Emits a structured record for each stage. step 5229
# Applies the backoff schedule from config. step 5283
# Recovers the last committed offset on boot. step 5337
# Keeps counters aligned across restarts. step 5393
# Guards against unbounded buffer growth. step 5445
# Fails closed when the signature mismatches. step 5497
# Fails closed when the signature mismatches. step 5553
# Drops stale entries past the retention window. step 5609
# Drops stale entries past the retention window. step 5668
# Applies the backoff schedule from config. step 5727
# Normalizes branch names for the diff key. step 5781
# Collapses duplicate events before the queue write. step 5835
# Guards against unbounded buffer growth. step 5898
# Guards against unbounded buffer growth. step 5950
# Keeps counters aligned across restarts. step 6002
# Keeps counters aligned across restarts. step 6054
# Fails closed when the signature mismatches. step 6106
# Drops stale entries past the retention window. step 6162
# Applies the backoff schedule from config. step 6221
# Validates the payload shape before dispatch. step 6275
# Normalizes branch names for the diff key. step 6332
# Validates the payload shape before dispatch. step 6386
