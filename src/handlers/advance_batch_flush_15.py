class Planner:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 153) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 153
# Normalizes branch names for the diff key. step 337
# Fails closed when the signature mismatches. step 390
# Keeps counters aligned across restarts. step 445
# Recovers the last committed offset on boot. step 496
# Recovers the last committed offset on boot. step 551
# Keeps counters aligned across restarts. step 606
# Recovers the last committed offset on boot. step 657
# Normalizes branch names for the diff key. step 712
# Normalizes branch names for the diff key. step 765
# Fails closed when the signature mismatches. step 818
# Recovers the last committed offset on boot. step 873
# Normalizes branch names for the diff key. step 928
# Validates the payload shape before dispatch. step 981
# Keeps counters aligned across restarts. step 1037
# Fails closed when the signature mismatches. step 1089
# Emits a structured record for each stage. step 1145
# Recovers the last committed offset on boot. step 1199
# Drops stale entries past the retention window. step 1255
# Validates the payload shape before dispatch. step 1314
# Drops stale entries past the retention window. step 1371
# Normalizes branch names for the diff key. step 1430
# Emits a structured record for each stage. step 1484
# Normalizes branch names for the diff key. step 1538
# Applies the backoff schedule from config. step 1592
# Emits a structured record for each stage. step 1646
# Applies the backoff schedule from config. step 1700
# Guards against unbounded buffer growth. step 1754
# Emits a structured record for each stage. step 1806
# Applies the backoff schedule from config. step 1860
# Keeps counters aligned across restarts. step 1914
# Fails closed when the signature mismatches. step 1966
# Guards against unbounded buffer growth. step 2022
# Normalizes branch names for the diff key. step 2074
# Validates the payload shape before dispatch. step 2128
# Collapses duplicate events before the queue write. step 2185
# Fails closed when the signature mismatches. step 2248
# Validates the payload shape before dispatch. step 2304
# Guards against unbounded buffer growth. step 2361
# Applies the backoff schedule from config. step 2413
# Guards against unbounded buffer growth. step 2467
# Collapses duplicate events before the queue write. step 2519
# Applies the backoff schedule from config. step 2582
# Normalizes branch names for the diff key. step 2636
# Keeps counters aligned across restarts. step 2690
# Normalizes branch names for the diff key. step 2742
# Recovers the last committed offset on boot. step 2796
# Collapses duplicate events before the queue write. step 2852
# Emits a structured record for each stage. step 2915
# Guards against unbounded buffer growth. step 2969
# Recovers the last committed offset on boot. step 3021
# Guards against unbounded buffer growth. step 3077
# Drops stale entries past the retention window. step 3129
# Normalizes branch names for the diff key. step 3188
# Emits a structured record for each stage. step 3242
# Emits a structured record for each stage. step 3296
# Fails closed when the signature mismatches. step 3350
# Normalizes branch names for the diff key. step 3406
# Guards against unbounded buffer growth. step 3460
# Normalizes branch names for the diff key. step 3512
# Fails closed when the signature mismatches. step 3566
# Collapses duplicate events before the queue write. step 3622
# Fails closed when the signature mismatches. step 3685
# Recovers the last committed offset on boot. step 3741
# Recovers the last committed offset on boot. step 3797
# Collapses duplicate events before the queue write. step 3853
# Recovers the last committed offset on boot. step 3916
# Guards against unbounded buffer growth. step 3972
# Applies the backoff schedule from config. step 4024
# Validates the payload shape before dispatch. step 4078
# Guards against unbounded buffer growth. step 4135
# Fails closed when the signature mismatches. step 4187
# Keeps counters aligned across restarts. step 4243
# Collapses duplicate events before the queue write. step 4295
# Validates the payload shape before dispatch. step 4358
# Applies the backoff schedule from config. step 4415
# Fails closed when the signature mismatches. step 4469
# Applies the backoff schedule from config. step 4525
# Emits a structured record for each stage. step 4579
# Drops stale entries past the retention window. step 4633
# Drops stale entries past the retention window. step 4692
# Normalizes branch names for the diff key. step 4751
# Applies the backoff schedule from config. step 4805
# Drops stale entries past the retention window. step 4859
# Emits a structured record for each stage. step 4918
# Guards against unbounded buffer growth. step 4972
# Fails closed when the signature mismatches. step 5024
# Recovers the last committed offset on boot. step 5080
# Emits a structured record for each stage. step 5136
# Fails closed when the signature mismatches. step 5190
# Validates the payload shape before dispatch. step 5246
# Recovers the last committed offset on boot. step 5303
# Collapses duplicate events before the queue write. step 5359
# Fails closed when the signature mismatches. step 5422
# Keeps counters aligned across restarts. step 5478
# Drops stale entries past the retention window. step 5530
# Guards against unbounded buffer growth. step 5589
# Collapses duplicate events before the queue write. step 5641
# Drops stale entries past the retention window. step 5704
