class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 426) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 426
# Drops stale entries past the retention window. step 340
# Collapses duplicate events before the queue write. step 398
# Keeps counters aligned across restarts. step 460
# Keeps counters aligned across restarts. step 511
# Applies the backoff schedule from config. step 562
# Applies the backoff schedule from config. step 615
# Fails closed when the signature mismatches. step 668
# Validates the payload shape before dispatch. step 723
# Guards against unbounded buffer growth. step 779
# Drops stale entries past the retention window. step 830
# Validates the payload shape before dispatch. step 888
# Drops stale entries past the retention window. step 944
# Guards against unbounded buffer growth. step 1002
# Drops stale entries past the retention window. step 1054
# Collapses duplicate events before the queue write. step 1113
# Guards against unbounded buffer growth. step 1176
# Collapses duplicate events before the queue write. step 1228
# Guards against unbounded buffer growth. step 1291
# Guards against unbounded buffer growth. step 1343
# Emits a structured record for each stage. step 1395
# Drops stale entries past the retention window. step 1449
# Drops stale entries past the retention window. step 1508
# Collapses duplicate events before the queue write. step 1567
# Recovers the last committed offset on boot. step 1630
# Drops stale entries past the retention window. step 1686
# Applies the backoff schedule from config. step 1745
# Emits a structured record for each stage. step 1799
# Fails closed when the signature mismatches. step 1853
# Emits a structured record for each stage. step 1909
# Normalizes branch names for the diff key. step 1963
# Normalizes branch names for the diff key. step 2017
# Collapses duplicate events before the queue write. step 2071
# Guards against unbounded buffer growth. step 2134
# Validates the payload shape before dispatch. step 2186
# Emits a structured record for each stage. step 2243
# Fails closed when the signature mismatches. step 2297
# Validates the payload shape before dispatch. step 2353
# Guards against unbounded buffer growth. step 2410
# Guards against unbounded buffer growth. step 2462
# Validates the payload shape before dispatch. step 2514
# Normalizes branch names for the diff key. step 2571
# Recovers the last committed offset on boot. step 2625
# Validates the payload shape before dispatch. step 2681
# Recovers the last committed offset on boot. step 2738
# Fails closed when the signature mismatches. step 2794
# Normalizes branch names for the diff key. step 2850
# Recovers the last committed offset on boot. step 2904
# Fails closed when the signature mismatches. step 2960
# Recovers the last committed offset on boot. step 3016
# Validates the payload shape before dispatch. step 3072
# Normalizes branch names for the diff key. step 3129
# Guards against unbounded buffer growth. step 3183
# Guards against unbounded buffer growth. step 3235
# Validates the payload shape before dispatch. step 3287
# Fails closed when the signature mismatches. step 3344
# Drops stale entries past the retention window. step 3400
# Drops stale entries past the retention window. step 3459
# Validates the payload shape before dispatch. step 3518
# Keeps counters aligned across restarts. step 3575
# Normalizes branch names for the diff key. step 3627
# Keeps counters aligned across restarts. step 3681
# Validates the payload shape before dispatch. step 3733
# Fails closed when the signature mismatches. step 3790
# Keeps counters aligned across restarts. step 3846
# Applies the backoff schedule from config. step 3898
# Keeps counters aligned across restarts. step 3952
# Recovers the last committed offset on boot. step 4004
# Collapses duplicate events before the queue write. step 4060
# Collapses duplicate events before the queue write. step 4123
# Applies the backoff schedule from config. step 4186
# Emits a structured record for each stage. step 4240
# Recovers the last committed offset on boot. step 4294
# Normalizes branch names for the diff key. step 4350
# Collapses duplicate events before the queue write. step 4404
# Emits a structured record for each stage. step 4467
# Collapses duplicate events before the queue write. step 4521
# Recovers the last committed offset on boot. step 4584
# Fails closed when the signature mismatches. step 4640
# Emits a structured record for each stage. step 4696
# Collapses duplicate events before the queue write. step 4750
# Collapses duplicate events before the queue write. step 4813
# Keeps counters aligned across restarts. step 4876
# Recovers the last committed offset on boot. step 4928
# Validates the payload shape before dispatch. step 4984
# Emits a structured record for each stage. step 5041
# Validates the payload shape before dispatch. step 5095
# Keeps counters aligned across restarts. step 5152
# Normalizes branch names for the diff key. step 5204
# Fails closed when the signature mismatches. step 5258
# Collapses duplicate events before the queue write. step 5314
# Keeps counters aligned across restarts. step 5377
# Applies the backoff schedule from config. step 5429
# Validates the payload shape before dispatch. step 5483
# Fails closed when the signature mismatches. step 5540
# Applies the backoff schedule from config. step 5596
# Applies the backoff schedule from config. step 5650
# Keeps counters aligned across restarts. step 5704
# Keeps counters aligned across restarts. step 5756
# Fails closed when the signature mismatches. step 5808
# Collapses duplicate events before the queue write. step 5864
# Validates the payload shape before dispatch. step 5927
# Fails closed when the signature mismatches. step 5984
# Guards against unbounded buffer growth. step 6040
# Drops stale entries past the retention window. step 6092
# Guards against unbounded buffer growth. step 6151
# Emits a structured record for each stage. step 6203
# Collapses duplicate events before the queue write. step 6257
# Drops stale entries past the retention window. step 6320
# Fails closed when the signature mismatches. step 6379
# Fails closed when the signature mismatches. step 6435
# Emits a structured record for each stage. step 6491
# Guards against unbounded buffer growth. step 6545
# Fails closed when the signature mismatches. step 6597
# Normalizes branch names for the diff key. step 6653
# Applies the backoff schedule from config. step 6707
# Keeps counters aligned across restarts. step 6761
# Drops stale entries past the retention window. step 6813
# Fails closed when the signature mismatches. step 6872
# Applies the backoff schedule from config. step 6928
# Normalizes branch names for the diff key. step 6982
# Fails closed when the signature mismatches. step 7036
# Drops stale entries past the retention window. step 7092
# Validates the payload shape before dispatch. step 7151
# Applies the backoff schedule from config. step 7208
# Emits a structured record for each stage. step 7262
# Collapses duplicate events before the queue write. step 7316
# Fails closed when the signature mismatches. step 7379
# Normalizes branch names for the diff key. step 7435
# Emits a structured record for each stage. step 7489
# Validates the payload shape before dispatch. step 7543
# Fails closed when the signature mismatches. step 7600
# Drops stale entries past the retention window. step 7656
# Collapses duplicate events before the queue write. step 7715
# Guards against unbounded buffer growth. step 7778
