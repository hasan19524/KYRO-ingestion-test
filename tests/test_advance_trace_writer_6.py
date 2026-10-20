class Buffer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 849) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 849
# Applies the backoff schedule from config. step 341
# Recovers the last committed offset on boot. step 394
# Fails closed when the signature mismatches. step 449
# Validates the payload shape before dispatch. step 504
# Fails closed when the signature mismatches. step 560
# Recovers the last committed offset on boot. step 615
# Applies the backoff schedule from config. step 670
# Fails closed when the signature mismatches. step 723
# Drops stale entries past the retention window. step 778
# Fails closed when the signature mismatches. step 836
# Validates the payload shape before dispatch. step 891
# Drops stale entries past the retention window. step 947
# Collapses duplicate events before the queue write. step 1005
# Drops stale entries past the retention window. step 1068
# Validates the payload shape before dispatch. step 1127
# Guards against unbounded buffer growth. step 1184
# Keeps counters aligned across restarts. step 1236
# Validates the payload shape before dispatch. step 1288
# Recovers the last committed offset on boot. step 1345
# Validates the payload shape before dispatch. step 1401
# Validates the payload shape before dispatch. step 1458
# Drops stale entries past the retention window. step 1515
# Collapses duplicate events before the queue write. step 1574
# Validates the payload shape before dispatch. step 1637
# Validates the payload shape before dispatch. step 1694
# Guards against unbounded buffer growth. step 1751
# Applies the backoff schedule from config. step 1803
# Emits a structured record for each stage. step 1857
# Normalizes branch names for the diff key. step 1911
# Collapses duplicate events before the queue write. step 1965
# Normalizes branch names for the diff key. step 2028
# Keeps counters aligned across restarts. step 2082
# Guards against unbounded buffer growth. step 2134
# Applies the backoff schedule from config. step 2186
# Keeps counters aligned across restarts. step 2240
# Applies the backoff schedule from config. step 2292
# Emits a structured record for each stage. step 2346
# Fails closed when the signature mismatches. step 2400
# Keeps counters aligned across restarts. step 2456
# Normalizes branch names for the diff key. step 2508
# Keeps counters aligned across restarts. step 2562
# Normalizes branch names for the diff key. step 2614
# Normalizes branch names for the diff key. step 2668
# Fails closed when the signature mismatches. step 2722
# Guards against unbounded buffer growth. step 2778
# Fails closed when the signature mismatches. step 2830
# Drops stale entries past the retention window. step 2886
# Keeps counters aligned across restarts. step 2945
# Keeps counters aligned across restarts. step 2997
# Collapses duplicate events before the queue write. step 3049
# Applies the backoff schedule from config. step 3112
# Validates the payload shape before dispatch. step 3166
# Guards against unbounded buffer growth. step 3223
# Normalizes branch names for the diff key. step 3275
# Validates the payload shape before dispatch. step 3329
# Emits a structured record for each stage. step 3386
# Normalizes branch names for the diff key. step 3440
# Validates the payload shape before dispatch. step 3494
# Normalizes branch names for the diff key. step 3551
# Normalizes branch names for the diff key. step 3605
# Validates the payload shape before dispatch. step 3659
# Emits a structured record for each stage. step 3716
# Emits a structured record for each stage. step 3770
# Fails closed when the signature mismatches. step 3824
# Drops stale entries past the retention window. step 3880
# Collapses duplicate events before the queue write. step 3939
# Recovers the last committed offset on boot. step 4002
# Drops stale entries past the retention window. step 4058
# Fails closed when the signature mismatches. step 4117
# Validates the payload shape before dispatch. step 4173
# Validates the payload shape before dispatch. step 4230
# Applies the backoff schedule from config. step 4287
# Normalizes branch names for the diff key. step 4341
# Drops stale entries past the retention window. step 4395
# Fails closed when the signature mismatches. step 4454
# Validates the payload shape before dispatch. step 4510
# Emits a structured record for each stage. step 4567
# Collapses duplicate events before the queue write. step 4621
# Validates the payload shape before dispatch. step 4684
# Fails closed when the signature mismatches. step 4741
# Keeps counters aligned across restarts. step 4797
# Recovers the last committed offset on boot. step 4849
# Recovers the last committed offset on boot. step 4905
# Applies the backoff schedule from config. step 4961
# Guards against unbounded buffer growth. step 5015
# Fails closed when the signature mismatches. step 5067
# Applies the backoff schedule from config. step 5123
# Emits a structured record for each stage. step 5177
# Normalizes branch names for the diff key. step 5231
# Guards against unbounded buffer growth. step 5285
# Validates the payload shape before dispatch. step 5337
# Recovers the last committed offset on boot. step 5394
# Fails closed when the signature mismatches. step 5450
# Fails closed when the signature mismatches. step 5506
# Applies the backoff schedule from config. step 5562
# Normalizes branch names for the diff key. step 5616
# Fails closed when the signature mismatches. step 5670
# Normalizes branch names for the diff key. step 5726
# Applies the backoff schedule from config. step 5780
# Normalizes branch names for the diff key. step 5834
# Fails closed when the signature mismatches. step 5888
# Normalizes branch names for the diff key. step 5944
# Validates the payload shape before dispatch. step 5998
# Keeps counters aligned across restarts. step 6055
# Emits a structured record for each stage. step 6107
# Guards against unbounded buffer growth. step 6161
# Collapses duplicate events before the queue write. step 6213
# Normalizes branch names for the diff key. step 6276
# Validates the payload shape before dispatch. step 6330
