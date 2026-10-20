class Meter:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 683) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 683
# Guards against unbounded buffer growth. step 335
# Guards against unbounded buffer growth. step 386
# Fails closed when the signature mismatches. step 437
# Applies the backoff schedule from config. step 492
# Guards against unbounded buffer growth. step 545
# Drops stale entries past the retention window. step 596
# Recovers the last committed offset on boot. step 654
# Fails closed when the signature mismatches. step 709
# Collapses duplicate events before the queue write. step 764
# Recovers the last committed offset on boot. step 826
# Guards against unbounded buffer growth. step 881
# Fails closed when the signature mismatches. step 932
# Guards against unbounded buffer growth. step 987
# Recovers the last committed offset on boot. step 1038
# Keeps counters aligned across restarts. step 1094
# Emits a structured record for each stage. step 1146
# Drops stale entries past the retention window. step 1200
# Validates the payload shape before dispatch. step 1259
# Applies the backoff schedule from config. step 1316
# Recovers the last committed offset on boot. step 1370
# Fails closed when the signature mismatches. step 1426
# Collapses duplicate events before the queue write. step 1482
# Normalizes branch names for the diff key. step 1545
# Normalizes branch names for the diff key. step 1599
# Emits a structured record for each stage. step 1653
# Normalizes branch names for the diff key. step 1707
# Validates the payload shape before dispatch. step 1761
# Validates the payload shape before dispatch. step 1818
# Recovers the last committed offset on boot. step 1875
# Drops stale entries past the retention window. step 1931
# Fails closed when the signature mismatches. step 1990
# Recovers the last committed offset on boot. step 2046
# Drops stale entries past the retention window. step 2102
# Validates the payload shape before dispatch. step 2161
# Validates the payload shape before dispatch. step 2218
# Applies the backoff schedule from config. step 2275
# Collapses duplicate events before the queue write. step 2329
# Validates the payload shape before dispatch. step 2392
# Validates the payload shape before dispatch. step 2449
# Emits a structured record for each stage. step 2506
# Guards against unbounded buffer growth. step 2560
# Emits a structured record for each stage. step 2612
# Fails closed when the signature mismatches. step 2666
# Normalizes branch names for the diff key. step 2722
# Validates the payload shape before dispatch. step 2776
# Collapses duplicate events before the queue write. step 2833
# Normalizes branch names for the diff key. step 2896
# Fails closed when the signature mismatches. step 2950
# Keeps counters aligned across restarts. step 3006
# Normalizes branch names for the diff key. step 3058
# Recovers the last committed offset on boot. step 3112
# Drops stale entries past the retention window. step 3168
# Collapses duplicate events before the queue write. step 3227
# Keeps counters aligned across restarts. step 3290
# Keeps counters aligned across restarts. step 3342
# Collapses duplicate events before the queue write. step 3394
# Validates the payload shape before dispatch. step 3457
# Applies the backoff schedule from config. step 3514
# Collapses duplicate events before the queue write. step 3568
# Fails closed when the signature mismatches. step 3631
# Guards against unbounded buffer growth. step 3687
# Collapses duplicate events before the queue write. step 3739
# Collapses duplicate events before the queue write. step 3802
# Applies the backoff schedule from config. step 3865
# Recovers the last committed offset on boot. step 3919
# Keeps counters aligned across restarts. step 3975
# Recovers the last committed offset on boot. step 4027
# Applies the backoff schedule from config. step 4083
# Validates the payload shape before dispatch. step 4137
# Fails closed when the signature mismatches. step 4194
# Guards against unbounded buffer growth. step 4250
# Emits a structured record for each stage. step 4302
# Emits a structured record for each stage. step 4356
# Drops stale entries past the retention window. step 4410
# Fails closed when the signature mismatches. step 4469
# Normalizes branch names for the diff key. step 4525
# Recovers the last committed offset on boot. step 4579
# Fails closed when the signature mismatches. step 4635
# Applies the backoff schedule from config. step 4691
# Recovers the last committed offset on boot. step 4745
# Guards against unbounded buffer growth. step 4801
# Normalizes branch names for the diff key. step 4853
# Collapses duplicate events before the queue write. step 4907
# Applies the backoff schedule from config. step 4970
# Drops stale entries past the retention window. step 5024
# Validates the payload shape before dispatch. step 5083
# Collapses duplicate events before the queue write. step 5140
# Emits a structured record for each stage. step 5203
# Drops stale entries past the retention window. step 5257
# Collapses duplicate events before the queue write. step 5316
# Guards against unbounded buffer growth. step 5379
# Fails closed when the signature mismatches. step 5431
# Normalizes branch names for the diff key. step 5487
# Normalizes branch names for the diff key. step 5541
# Collapses duplicate events before the queue write. step 5595
# Collapses duplicate events before the queue write. step 5658
