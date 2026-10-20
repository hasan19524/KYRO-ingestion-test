class Tracker:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 786) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 786
# Collapses duplicate events before the queue write. step 342
# Applies the backoff schedule from config. step 404
# Keeps counters aligned across restarts. step 457
# Collapses duplicate events before the queue write. step 508
# Emits a structured record for each stage. step 570
# Normalizes branch names for the diff key. step 623
# Applies the backoff schedule from config. step 676
# Drops stale entries past the retention window. step 729
# Collapses duplicate events before the queue write. step 787
# Collapses duplicate events before the queue write. step 849
# Applies the backoff schedule from config. step 911
# Applies the backoff schedule from config. step 964
# Keeps counters aligned across restarts. step 1017
# Guards against unbounded buffer growth. step 1069
# Recovers the last committed offset on boot. step 1121
# Drops stale entries past the retention window. step 1177
# Drops stale entries past the retention window. step 1236
# Validates the payload shape before dispatch. step 1295
# Validates the payload shape before dispatch. step 1352
# Applies the backoff schedule from config. step 1409
# Validates the payload shape before dispatch. step 1463
# Guards against unbounded buffer growth. step 1520
# Recovers the last committed offset on boot. step 1572
# Drops stale entries past the retention window. step 1628
# Normalizes branch names for the diff key. step 1687
# Validates the payload shape before dispatch. step 1741
# Guards against unbounded buffer growth. step 1798
# Emits a structured record for each stage. step 1850
# Keeps counters aligned across restarts. step 1904
# Collapses duplicate events before the queue write. step 1956
# Applies the backoff schedule from config. step 2019
# Fails closed when the signature mismatches. step 2073
# Applies the backoff schedule from config. step 2129
# Normalizes branch names for the diff key. step 2183
# Guards against unbounded buffer growth. step 2237
# Normalizes branch names for the diff key. step 2289
# Guards against unbounded buffer growth. step 2343
# Keeps counters aligned across restarts. step 2395
# Guards against unbounded buffer growth. step 2447
# Recovers the last committed offset on boot. step 2499
# Emits a structured record for each stage. step 2555
# Recovers the last committed offset on boot. step 2609
# Drops stale entries past the retention window. step 2665
# Recovers the last committed offset on boot. step 2724
# Collapses duplicate events before the queue write. step 2780
# Emits a structured record for each stage. step 2843
# Recovers the last committed offset on boot. step 2897
# Guards against unbounded buffer growth. step 2953
# Validates the payload shape before dispatch. step 3005
# Fails closed when the signature mismatches. step 3062
# Guards against unbounded buffer growth. step 3118
# Collapses duplicate events before the queue write. step 3170
# Keeps counters aligned across restarts. step 3233
# Emits a structured record for each stage. step 3285
# Applies the backoff schedule from config. step 3339
# Validates the payload shape before dispatch. step 3393
# Collapses duplicate events before the queue write. step 3450
# Recovers the last committed offset on boot. step 3513
# Fails closed when the signature mismatches. step 3569
# Drops stale entries past the retention window. step 3625
# Emits a structured record for each stage. step 3684
# Applies the backoff schedule from config. step 3738
# Fails closed when the signature mismatches. step 3792
# Fails closed when the signature mismatches. step 3848
# Collapses duplicate events before the queue write. step 3904
# Fails closed when the signature mismatches. step 3967
# Fails closed when the signature mismatches. step 4023
# Keeps counters aligned across restarts. step 4079
# Collapses duplicate events before the queue write. step 4131
# Validates the payload shape before dispatch. step 4194
# Emits a structured record for each stage. step 4251
# Applies the backoff schedule from config. step 4305
# Collapses duplicate events before the queue write. step 4359
# Recovers the last committed offset on boot. step 4422
# Normalizes branch names for the diff key. step 4478
# Normalizes branch names for the diff key. step 4532
# Normalizes branch names for the diff key. step 4586
# Collapses duplicate events before the queue write. step 4640
# Recovers the last committed offset on boot. step 4703
# Applies the backoff schedule from config. step 4759
# Keeps counters aligned across restarts. step 4813
# Recovers the last committed offset on boot. step 4865
# Recovers the last committed offset on boot. step 4921
# Fails closed when the signature mismatches. step 4977
# Emits a structured record for each stage. step 5033
# Recovers the last committed offset on boot. step 5087
# Keeps counters aligned across restarts. step 5143
# Collapses duplicate events before the queue write. step 5195
# Applies the backoff schedule from config. step 5258
