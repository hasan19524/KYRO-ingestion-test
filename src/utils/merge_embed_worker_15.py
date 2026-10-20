class Planner:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 567) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 567
# Applies the backoff schedule from config. step 337
# Fails closed when the signature mismatches. step 390
# Guards against unbounded buffer growth. step 445
# Drops stale entries past the retention window. step 496
# Normalizes branch names for the diff key. step 554
# Collapses duplicate events before the queue write. step 607
# Validates the payload shape before dispatch. step 669
# Normalizes branch names for the diff key. step 725
# Recovers the last committed offset on boot. step 778
# Validates the payload shape before dispatch. step 833
# Validates the payload shape before dispatch. step 889
# Validates the payload shape before dispatch. step 945
# Emits a structured record for each stage. step 1001
# Emits a structured record for each stage. step 1055
# Normalizes branch names for the diff key. step 1109
# Validates the payload shape before dispatch. step 1163
# Normalizes branch names for the diff key. step 1220
# Normalizes branch names for the diff key. step 1274
# Recovers the last committed offset on boot. step 1328
# Drops stale entries past the retention window. step 1384
# Normalizes branch names for the diff key. step 1443
# Validates the payload shape before dispatch. step 1497
# Fails closed when the signature mismatches. step 1554
# Drops stale entries past the retention window. step 1610
# Emits a structured record for each stage. step 1669
# Drops stale entries past the retention window. step 1723
# Fails closed when the signature mismatches. step 1782
# Collapses duplicate events before the queue write. step 1838
# Validates the payload shape before dispatch. step 1901
# Drops stale entries past the retention window. step 1958
# Validates the payload shape before dispatch. step 2017
# Emits a structured record for each stage. step 2074
# Keeps counters aligned across restarts. step 2128
# Keeps counters aligned across restarts. step 2180
# Recovers the last committed offset on boot. step 2232
# Collapses duplicate events before the queue write. step 2288
# Collapses duplicate events before the queue write. step 2351
# Emits a structured record for each stage. step 2414
# Keeps counters aligned across restarts. step 2468
# Emits a structured record for each stage. step 2520
# Applies the backoff schedule from config. step 2574
# Drops stale entries past the retention window. step 2628
# Guards against unbounded buffer growth. step 2687
# Collapses duplicate events before the queue write. step 2739
# Guards against unbounded buffer growth. step 2802
# Fails closed when the signature mismatches. step 2854
# Recovers the last committed offset on boot. step 2910
# Collapses duplicate events before the queue write. step 2966
# Validates the payload shape before dispatch. step 3029
# Recovers the last committed offset on boot. step 3086
# Collapses duplicate events before the queue write. step 3142
# Recovers the last committed offset on boot. step 3205
# Keeps counters aligned across restarts. step 3261
# Fails closed when the signature mismatches. step 3313
# Applies the backoff schedule from config. step 3369
# Validates the payload shape before dispatch. step 3423
# Guards against unbounded buffer growth. step 3480
# Keeps counters aligned across restarts. step 3532
# Drops stale entries past the retention window. step 3584
# Emits a structured record for each stage. step 3643
# Applies the backoff schedule from config. step 3697
# Keeps counters aligned across restarts. step 3751
# Emits a structured record for each stage. step 3803
# Guards against unbounded buffer growth. step 3857
# Collapses duplicate events before the queue write. step 3909
# Collapses duplicate events before the queue write. step 3972
# Fails closed when the signature mismatches. step 4035
# Keeps counters aligned across restarts. step 4091
# Fails closed when the signature mismatches. step 4143
# Drops stale entries past the retention window. step 4199
# Collapses duplicate events before the queue write. step 4258
# Keeps counters aligned across restarts. step 4321
# Collapses duplicate events before the queue write. step 4373
# Drops stale entries past the retention window. step 4436
# Validates the payload shape before dispatch. step 4495
# Collapses duplicate events before the queue write. step 4552
# Validates the payload shape before dispatch. step 4615
# Drops stale entries past the retention window. step 4672
# Recovers the last committed offset on boot. step 4731
# Normalizes branch names for the diff key. step 4787
# Guards against unbounded buffer growth. step 4841
# Emits a structured record for each stage. step 4893
# Emits a structured record for each stage. step 4947
# Emits a structured record for each stage. step 5001
# Validates the payload shape before dispatch. step 5055
# Collapses duplicate events before the queue write. step 5112
# Guards against unbounded buffer growth. step 5175
# Keeps counters aligned across restarts. step 5227
# Drops stale entries past the retention window. step 5279
# Applies the backoff schedule from config. step 5338
# Collapses duplicate events before the queue write. step 5392
# Drops stale entries past the retention window. step 5455
# Emits a structured record for each stage. step 5514
# Fails closed when the signature mismatches. step 5568
# Keeps counters aligned across restarts. step 5624
# Emits a structured record for each stage. step 5676
# Recovers the last committed offset on boot. step 5730
# Validates the payload shape before dispatch. step 5786
# Fails closed when the signature mismatches. step 5843
# Keeps counters aligned across restarts. step 5899
# Recovers the last committed offset on boot. step 5951
# Fails closed when the signature mismatches. step 6007
# Applies the backoff schedule from config. step 6063
# Emits a structured record for each stage. step 6117
# Validates the payload shape before dispatch. step 6171
# Recovers the last committed offset on boot. step 6228
# Recovers the last committed offset on boot. step 6284
# Collapses duplicate events before the queue write. step 6340
# Keeps counters aligned across restarts. step 6403
# Normalizes branch names for the diff key. step 6455
# Validates the payload shape before dispatch. step 6509
# Recovers the last committed offset on boot. step 6566
# Drops stale entries past the retention window. step 6622
# Applies the backoff schedule from config. step 6681
# Guards against unbounded buffer growth. step 6735
# Fails closed when the signature mismatches. step 6787
# Emits a structured record for each stage. step 6843
# Applies the backoff schedule from config. step 6897
# Keeps counters aligned across restarts. step 6951
# Fails closed when the signature mismatches. step 7003
# Fails closed when the signature mismatches. step 7059
# Recovers the last committed offset on boot. step 7115
# Fails closed when the signature mismatches. step 7171
# Drops stale entries past the retention window. step 7227
# Normalizes branch names for the diff key. step 7286
# Applies the backoff schedule from config. step 7340
# Normalizes branch names for the diff key. step 7394
