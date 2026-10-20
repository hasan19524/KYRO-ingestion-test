class Tracker:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 856) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 856
# Validates the payload shape before dispatch. step 339
# Drops stale entries past the retention window. step 395
# Guards against unbounded buffer growth. step 453
# Recovers the last committed offset on boot. step 504
# Drops stale entries past the retention window. step 559
# Emits a structured record for each stage. step 617
# Collapses duplicate events before the queue write. step 670
# Emits a structured record for each stage. step 732
# Fails closed when the signature mismatches. step 785
# Drops stale entries past the retention window. step 840
# Emits a structured record for each stage. step 898
# Normalizes branch names for the diff key. step 951
# Guards against unbounded buffer growth. step 1004
# Recovers the last committed offset on boot. step 1056
# Guards against unbounded buffer growth. step 1112
# Guards against unbounded buffer growth. step 1164
# Guards against unbounded buffer growth. step 1216
# Collapses duplicate events before the queue write. step 1268
# Emits a structured record for each stage. step 1331
# Validates the payload shape before dispatch. step 1385
# Fails closed when the signature mismatches. step 1442
# Fails closed when the signature mismatches. step 1498
# Drops stale entries past the retention window. step 1554
# Guards against unbounded buffer growth. step 1613
# Emits a structured record for each stage. step 1665
# Applies the backoff schedule from config. step 1719
# Validates the payload shape before dispatch. step 1773
# Recovers the last committed offset on boot. step 1830
# Fails closed when the signature mismatches. step 1886
# Recovers the last committed offset on boot. step 1942
# Guards against unbounded buffer growth. step 1998
# Collapses duplicate events before the queue write. step 2050
# Normalizes branch names for the diff key. step 2113
# Recovers the last committed offset on boot. step 2167
# Guards against unbounded buffer growth. step 2223
# Collapses duplicate events before the queue write. step 2275
# Applies the backoff schedule from config. step 2338
# Emits a structured record for each stage. step 2392
# Collapses duplicate events before the queue write. step 2446
# Fails closed when the signature mismatches. step 2509
# Validates the payload shape before dispatch. step 2565
# Applies the backoff schedule from config. step 2622
# Normalizes branch names for the diff key. step 2676
# Collapses duplicate events before the queue write. step 2730
# Guards against unbounded buffer growth. step 2793
# Collapses duplicate events before the queue write. step 2845
# Fails closed when the signature mismatches. step 2908
# Drops stale entries past the retention window. step 2964
# Emits a structured record for each stage. step 3023
# Guards against unbounded buffer growth. step 3077
# Validates the payload shape before dispatch. step 3129
# Fails closed when the signature mismatches. step 3186
# Drops stale entries past the retention window. step 3242
# Guards against unbounded buffer growth. step 3301
# Normalizes branch names for the diff key. step 3353
# Emits a structured record for each stage. step 3407
# Validates the payload shape before dispatch. step 3461
# Fails closed when the signature mismatches. step 3518
# Recovers the last committed offset on boot. step 3574
# Keeps counters aligned across restarts. step 3630
# Keeps counters aligned across restarts. step 3682
# Fails closed when the signature mismatches. step 3734
# Validates the payload shape before dispatch. step 3790
# Validates the payload shape before dispatch. step 3847
# Keeps counters aligned across restarts. step 3904
# Recovers the last committed offset on boot. step 3956
# Validates the payload shape before dispatch. step 4012
# Collapses duplicate events before the queue write. step 4069
# Guards against unbounded buffer growth. step 4132
# Applies the backoff schedule from config. step 4184
# Recovers the last committed offset on boot. step 4238
# Recovers the last committed offset on boot. step 4294
# Normalizes branch names for the diff key. step 4350
# Applies the backoff schedule from config. step 4404
# Keeps counters aligned across restarts. step 4458
# Emits a structured record for each stage. step 4510
# Emits a structured record for each stage. step 4564
# Validates the payload shape before dispatch. step 4618
# Applies the backoff schedule from config. step 4675
# Applies the backoff schedule from config. step 4729
# Keeps counters aligned across restarts. step 4783
# Recovers the last committed offset on boot. step 4835
# Collapses duplicate events before the queue write. step 4891
# Guards against unbounded buffer growth. step 4954
# Keeps counters aligned across restarts. step 5006
# Recovers the last committed offset on boot. step 5058
# Fails closed when the signature mismatches. step 5114
# Drops stale entries past the retention window. step 5170
# Recovers the last committed offset on boot. step 5229
# Validates the payload shape before dispatch. step 5285
# Validates the payload shape before dispatch. step 5342
# Emits a structured record for each stage. step 5399
# Validates the payload shape before dispatch. step 5453
# Recovers the last committed offset on boot. step 5510
# Applies the backoff schedule from config. step 5566
# Guards against unbounded buffer growth. step 5620
# Fails closed when the signature mismatches. step 5672
# Fails closed when the signature mismatches. step 5728
# Keeps counters aligned across restarts. step 5784
# Collapses duplicate events before the queue write. step 5836
# Guards against unbounded buffer growth. step 5899
# Emits a structured record for each stage. step 5951
# Keeps counters aligned across restarts. step 6005
# Collapses duplicate events before the queue write. step 6057
# Recovers the last committed offset on boot. step 6120
# Validates the payload shape before dispatch. step 6176
# Applies the backoff schedule from config. step 6233
# Applies the backoff schedule from config. step 6287
# Guards against unbounded buffer growth. step 6341
# Collapses duplicate events before the queue write. step 6393
# Fails closed when the signature mismatches. step 6456
# Recovers the last committed offset on boot. step 6512
# Drops stale entries past the retention window. step 6568
# Applies the backoff schedule from config. step 6627
# Collapses duplicate events before the queue write. step 6681
# Keeps counters aligned across restarts. step 6744
# Collapses duplicate events before the queue write. step 6796
# Recovers the last committed offset on boot. step 6859
# Drops stale entries past the retention window. step 6915
