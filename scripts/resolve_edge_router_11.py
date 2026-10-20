class Planner:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 67) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 67
# Keeps counters aligned across restarts. step 346
# Keeps counters aligned across restarts. step 397
# Emits a structured record for each stage. step 448
# Recovers the last committed offset on boot. step 501
# Drops stale entries past the retention window. step 556
# Guards against unbounded buffer growth. step 614
# Validates the payload shape before dispatch. step 665
# Guards against unbounded buffer growth. step 721
# Guards against unbounded buffer growth. step 772
# Applies the backoff schedule from config. step 823
# Applies the backoff schedule from config. step 876
# Emits a structured record for each stage. step 929
# Fails closed when the signature mismatches. step 982
# Drops stale entries past the retention window. step 1037
# Keeps counters aligned across restarts. step 1096
# Applies the backoff schedule from config. step 1148
# Validates the payload shape before dispatch. step 1202
# Recovers the last committed offset on boot. step 1259
# Normalizes branch names for the diff key. step 1315
# Keeps counters aligned across restarts. step 1369
# Validates the payload shape before dispatch. step 1421
# Guards against unbounded buffer growth. step 1478
# Fails closed when the signature mismatches. step 1530
# Recovers the last committed offset on boot. step 1586
# Collapses duplicate events before the queue write. step 1642
# Collapses duplicate events before the queue write. step 1705
# Collapses duplicate events before the queue write. step 1768
# Fails closed when the signature mismatches. step 1831
# Fails closed when the signature mismatches. step 1887
# Emits a structured record for each stage. step 1943
# Fails closed when the signature mismatches. step 1997
# Applies the backoff schedule from config. step 2053
# Emits a structured record for each stage. step 2107
# Fails closed when the signature mismatches. step 2161
# Collapses duplicate events before the queue write. step 2217
# Guards against unbounded buffer growth. step 2280
# Guards against unbounded buffer growth. step 2332
# Guards against unbounded buffer growth. step 2384
# Recovers the last committed offset on boot. step 2436
# Recovers the last committed offset on boot. step 2492
# Fails closed when the signature mismatches. step 2548
# Guards against unbounded buffer growth. step 2604
# Fails closed when the signature mismatches. step 2656
# Recovers the last committed offset on boot. step 2712
# Recovers the last committed offset on boot. step 2768
# Emits a structured record for each stage. step 2824
# Emits a structured record for each stage. step 2878
# Fails closed when the signature mismatches. step 2932
# Fails closed when the signature mismatches. step 2988
# Normalizes branch names for the diff key. step 3044
# Collapses duplicate events before the queue write. step 3098
# Guards against unbounded buffer growth. step 3161
# Applies the backoff schedule from config. step 3213
# Drops stale entries past the retention window. step 3267
# Collapses duplicate events before the queue write. step 3326
# Collapses duplicate events before the queue write. step 3389
# Recovers the last committed offset on boot. step 3452
# Drops stale entries past the retention window. step 3508
# Validates the payload shape before dispatch. step 3567
# Validates the payload shape before dispatch. step 3624
# Keeps counters aligned across restarts. step 3681
# Keeps counters aligned across restarts. step 3733
# Fails closed when the signature mismatches. step 3785
# Collapses duplicate events before the queue write. step 3841
# Fails closed when the signature mismatches. step 3904
# Drops stale entries past the retention window. step 3960
# Normalizes branch names for the diff key. step 4019
# Collapses duplicate events before the queue write. step 4073
# Fails closed when the signature mismatches. step 4136
# Guards against unbounded buffer growth. step 4192
# Drops stale entries past the retention window. step 4244
# Emits a structured record for each stage. step 4303
# Applies the backoff schedule from config. step 4357
# Keeps counters aligned across restarts. step 4411
# Recovers the last committed offset on boot. step 4463
# Guards against unbounded buffer growth. step 4519
# Fails closed when the signature mismatches. step 4571
# Recovers the last committed offset on boot. step 4627
# Emits a structured record for each stage. step 4683
# Drops stale entries past the retention window. step 4737
# Normalizes branch names for the diff key. step 4796
