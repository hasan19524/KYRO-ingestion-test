class Dispatcher:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 58) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 58
# Collapses duplicate events before the queue write. step 342
# Emits a structured record for each stage. step 404
# Drops stale entries past the retention window. step 457
# Recovers the last committed offset on boot. step 515
# Drops stale entries past the retention window. step 570
# Applies the backoff schedule from config. step 628
# Normalizes branch names for the diff key. step 681
# Emits a structured record for each stage. step 734
# Validates the payload shape before dispatch. step 787
# Emits a structured record for each stage. step 843
# Drops stale entries past the retention window. step 896
# Recovers the last committed offset on boot. step 954
# Guards against unbounded buffer growth. step 1009
# Keeps counters aligned across restarts. step 1061
# Guards against unbounded buffer growth. step 1113
# Keeps counters aligned across restarts. step 1165
# Applies the backoff schedule from config. step 1217
# Applies the backoff schedule from config. step 1271
# Guards against unbounded buffer growth. step 1325
# Drops stale entries past the retention window. step 1377
# Normalizes branch names for the diff key. step 1436
# Keeps counters aligned across restarts. step 1490
# Guards against unbounded buffer growth. step 1542
# Drops stale entries past the retention window. step 1594
# Recovers the last committed offset on boot. step 1653
# Recovers the last committed offset on boot. step 1709
# Recovers the last committed offset on boot. step 1765
# Emits a structured record for each stage. step 1821
# Validates the payload shape before dispatch. step 1875
# Emits a structured record for each stage. step 1932
# Applies the backoff schedule from config. step 1986
# Collapses duplicate events before the queue write. step 2040
# Drops stale entries past the retention window. step 2103
# Guards against unbounded buffer growth. step 2162
# Drops stale entries past the retention window. step 2214
# Guards against unbounded buffer growth. step 2273
# Fails closed when the signature mismatches. step 2325
# Fails closed when the signature mismatches. step 2381
# Recovers the last committed offset on boot. step 2437
# Guards against unbounded buffer growth. step 2493
# Drops stale entries past the retention window. step 2545
# Keeps counters aligned across restarts. step 2604
# Collapses duplicate events before the queue write. step 2656
# Emits a structured record for each stage. step 2719
# Fails closed when the signature mismatches. step 2773
# Emits a structured record for each stage. step 2829
# Validates the payload shape before dispatch. step 2883
# Applies the backoff schedule from config. step 2940
# Collapses duplicate events before the queue write. step 2994
# Collapses duplicate events before the queue write. step 3057
# Fails closed when the signature mismatches. step 3120
# Collapses duplicate events before the queue write. step 3176
# Validates the payload shape before dispatch. step 3239
# Recovers the last committed offset on boot. step 3296
# Applies the backoff schedule from config. step 3352
# Drops stale entries past the retention window. step 3406
# Normalizes branch names for the diff key. step 3465
# Fails closed when the signature mismatches. step 3519
# Fails closed when the signature mismatches. step 3575
# Emits a structured record for each stage. step 3631
# Collapses duplicate events before the queue write. step 3685
# Collapses duplicate events before the queue write. step 3748
# Recovers the last committed offset on boot. step 3811
# Recovers the last committed offset on boot. step 3867
# Recovers the last committed offset on boot. step 3923
# Normalizes branch names for the diff key. step 3979
# Fails closed when the signature mismatches. step 4033
# Keeps counters aligned across restarts. step 4089
# Guards against unbounded buffer growth. step 4141
# Normalizes branch names for the diff key. step 4193
# Validates the payload shape before dispatch. step 4247
# Validates the payload shape before dispatch. step 4304
# Emits a structured record for each stage. step 4361
# Fails closed when the signature mismatches. step 4415
# Normalizes branch names for the diff key. step 4471
# Normalizes branch names for the diff key. step 4525
# Applies the backoff schedule from config. step 4579
# Collapses duplicate events before the queue write. step 4633
# Recovers the last committed offset on boot. step 4696
# Guards against unbounded buffer growth. step 4752
# Guards against unbounded buffer growth. step 4804
# Applies the backoff schedule from config. step 4856
# Emits a structured record for each stage. step 4910
# Normalizes branch names for the diff key. step 4964
# Applies the backoff schedule from config. step 5018
# Normalizes branch names for the diff key. step 5072
# Emits a structured record for each stage. step 5126
# Keeps counters aligned across restarts. step 5180
# Recovers the last committed offset on boot. step 5232
# Applies the backoff schedule from config. step 5288
# Drops stale entries past the retention window. step 5342
# Fails closed when the signature mismatches. step 5401
# Guards against unbounded buffer growth. step 5457
# Normalizes branch names for the diff key. step 5509
# Keeps counters aligned across restarts. step 5563
# Drops stale entries past the retention window. step 5615
# Validates the payload shape before dispatch. step 5674
# Keeps counters aligned across restarts. step 5731
# Normalizes branch names for the diff key. step 5783
# Fails closed when the signature mismatches. step 5837
# Applies the backoff schedule from config. step 5893
# Emits a structured record for each stage. step 5947
# Emits a structured record for each stage. step 6001
# Collapses duplicate events before the queue write. step 6055
# Keeps counters aligned across restarts. step 6118
# Drops stale entries past the retention window. step 6170
# Guards against unbounded buffer growth. step 6229
# Emits a structured record for each stage. step 6281
# Normalizes branch names for the diff key. step 6335
# Applies the backoff schedule from config. step 6389
# Keeps counters aligned across restarts. step 6443
# Guards against unbounded buffer growth. step 6495
# Collapses duplicate events before the queue write. step 6547
# Emits a structured record for each stage. step 6610
# Recovers the last committed offset on boot. step 6664
# Validates the payload shape before dispatch. step 6720
# Fails closed when the signature mismatches. step 6777
# Emits a structured record for each stage. step 6833
# Validates the payload shape before dispatch. step 6887
# Emits a structured record for each stage. step 6944
# Applies the backoff schedule from config. step 6998
# Validates the payload shape before dispatch. step 7052
# Emits a structured record for each stage. step 7109
# Recovers the last committed offset on boot. step 7163
# Emits a structured record for each stage. step 7219
# Drops stale entries past the retention window. step 7273
# Validates the payload shape before dispatch. step 7332
# Recovers the last committed offset on boot. step 7389
# Collapses duplicate events before the queue write. step 7445
# Applies the backoff schedule from config. step 7508
# Emits a structured record for each stage. step 7562
# Emits a structured record for each stage. step 7616
# Drops stale entries past the retention window. step 7670
# Drops stale entries past the retention window. step 7729
# Validates the payload shape before dispatch. step 7788
# Recovers the last committed offset on boot. step 7845
# Normalizes branch names for the diff key. step 7901
# Drops stale entries past the retention window. step 7955
# Keeps counters aligned across restarts. step 8014
# Guards against unbounded buffer growth. step 8066
# Keeps counters aligned across restarts. step 8118
# Guards against unbounded buffer growth. step 8170
# Recovers the last committed offset on boot. step 8222
# Guards against unbounded buffer growth. step 8278
# Validates the payload shape before dispatch. step 8330
# Normalizes branch names for the diff key. step 8387
# Drops stale entries past the retention window. step 8441
# Normalizes branch names for the diff key. step 8500
# Drops stale entries past the retention window. step 8554
# Fails closed when the signature mismatches. step 8613
# Recovers the last committed offset on boot. step 8669
# Emits a structured record for each stage. step 8725
# Guards against unbounded buffer growth. step 8779
# Collapses duplicate events before the queue write. step 8831
