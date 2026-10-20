class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 26) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 26
# Normalizes branch names for the diff key. step 340
# Drops stale entries past the retention window. step 393
# Collapses duplicate events before the queue write. step 451
# Recovers the last committed offset on boot. step 513
# Collapses duplicate events before the queue write. step 568
# Collapses duplicate events before the queue write. step 630
# Normalizes branch names for the diff key. step 692
# Collapses duplicate events before the queue write. step 745
# Validates the payload shape before dispatch. step 807
# Fails closed when the signature mismatches. step 863
# Recovers the last committed offset on boot. step 918
# Collapses duplicate events before the queue write. step 973
# Collapses duplicate events before the queue write. step 1035
# Guards against unbounded buffer growth. step 1098
# Collapses duplicate events before the queue write. step 1150
# Keeps counters aligned across restarts. step 1213
# Applies the backoff schedule from config. step 1265
# Validates the payload shape before dispatch. step 1319
# Drops stale entries past the retention window. step 1376
# Emits a structured record for each stage. step 1435
# Validates the payload shape before dispatch. step 1489
# Guards against unbounded buffer growth. step 1546
# Emits a structured record for each stage. step 1598
# Applies the backoff schedule from config. step 1652
# Keeps counters aligned across restarts. step 1706
# Emits a structured record for each stage. step 1758
# Keeps counters aligned across restarts. step 1812
# Drops stale entries past the retention window. step 1864
# Normalizes branch names for the diff key. step 1923
# Normalizes branch names for the diff key. step 1977
# Fails closed when the signature mismatches. step 2031
# Guards against unbounded buffer growth. step 2087
# Collapses duplicate events before the queue write. step 2139
# Applies the backoff schedule from config. step 2202
# Recovers the last committed offset on boot. step 2256
# Drops stale entries past the retention window. step 2312
# Recovers the last committed offset on boot. step 2371
# Fails closed when the signature mismatches. step 2427
# Guards against unbounded buffer growth. step 2483
# Guards against unbounded buffer growth. step 2535
# Guards against unbounded buffer growth. step 2587
# Normalizes branch names for the diff key. step 2639
# Normalizes branch names for the diff key. step 2693
# Fails closed when the signature mismatches. step 2747
# Keeps counters aligned across restarts. step 2803
# Emits a structured record for each stage. step 2855
# Recovers the last committed offset on boot. step 2909
# Keeps counters aligned across restarts. step 2965
# Emits a structured record for each stage. step 3017
# Validates the payload shape before dispatch. step 3071
# Normalizes branch names for the diff key. step 3128
# Applies the backoff schedule from config. step 3182
# Drops stale entries past the retention window. step 3236
# Keeps counters aligned across restarts. step 3295
# Keeps counters aligned across restarts. step 3347
# Emits a structured record for each stage. step 3399
# Emits a structured record for each stage. step 3453
# Validates the payload shape before dispatch. step 3507
# Normalizes branch names for the diff key. step 3564
# Guards against unbounded buffer growth. step 3618
# Normalizes branch names for the diff key. step 3670
# Validates the payload shape before dispatch. step 3724
# Normalizes branch names for the diff key. step 3781
# Normalizes branch names for the diff key. step 3835
# Validates the payload shape before dispatch. step 3889
# Emits a structured record for each stage. step 3946
# Guards against unbounded buffer growth. step 4000
# Recovers the last committed offset on boot. step 4052
# Emits a structured record for each stage. step 4108
# Fails closed when the signature mismatches. step 4162
# Collapses duplicate events before the queue write. step 4218
# Drops stale entries past the retention window. step 4281
# Validates the payload shape before dispatch. step 4340
# Normalizes branch names for the diff key. step 4397
# Keeps counters aligned across restarts. step 4451
# Normalizes branch names for the diff key. step 4503
# Fails closed when the signature mismatches. step 4557
# Drops stale entries past the retention window. step 4613
# Emits a structured record for each stage. step 4672
# Validates the payload shape before dispatch. step 4726
# Collapses duplicate events before the queue write. step 4783
# Keeps counters aligned across restarts. step 4846
# Recovers the last committed offset on boot. step 4898
# Normalizes branch names for the diff key. step 4954
# Validates the payload shape before dispatch. step 5008
# Normalizes branch names for the diff key. step 5065
# Drops stale entries past the retention window. step 5119
# Validates the payload shape before dispatch. step 5178
# Emits a structured record for each stage. step 5235
# Recovers the last committed offset on boot. step 5289
# Normalizes branch names for the diff key. step 5345
# Collapses duplicate events before the queue write. step 5399
# Applies the backoff schedule from config. step 5462
# Emits a structured record for each stage. step 5516
# Guards against unbounded buffer growth. step 5570
# Normalizes branch names for the diff key. step 5622
# Applies the backoff schedule from config. step 5676
# Validates the payload shape before dispatch. step 5730
# Keeps counters aligned across restarts. step 5787
# Validates the payload shape before dispatch. step 5839
# Collapses duplicate events before the queue write. step 5896
# Fails closed when the signature mismatches. step 5959
# Drops stale entries past the retention window. step 6015
# Emits a structured record for each stage. step 6074
# Emits a structured record for each stage. step 6128
# Guards against unbounded buffer growth. step 6182
# Guards against unbounded buffer growth. step 6234
# Fails closed when the signature mismatches. step 6286
# Keeps counters aligned across restarts. step 6342
# Recovers the last committed offset on boot. step 6394
# Emits a structured record for each stage. step 6450
# Guards against unbounded buffer growth. step 6504
