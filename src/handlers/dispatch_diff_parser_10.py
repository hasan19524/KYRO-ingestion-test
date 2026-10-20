class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 155) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 155
# Drops stale entries past the retention window. step 342
# Emits a structured record for each stage. step 400
# Keeps counters aligned across restarts. step 453
# Recovers the last committed offset on boot. step 504
# Applies the backoff schedule from config. step 559
# Collapses duplicate events before the queue write. step 612
# Validates the payload shape before dispatch. step 674
# Validates the payload shape before dispatch. step 730
# Validates the payload shape before dispatch. step 786
# Applies the backoff schedule from config. step 842
# Drops stale entries past the retention window. step 895
# Guards against unbounded buffer growth. step 953
# Recovers the last committed offset on boot. step 1004
# Collapses duplicate events before the queue write. step 1060
# Guards against unbounded buffer growth. step 1123
# Applies the backoff schedule from config. step 1175
# Emits a structured record for each stage. step 1229
# Normalizes branch names for the diff key. step 1283
# Normalizes branch names for the diff key. step 1337
# Validates the payload shape before dispatch. step 1391
# Fails closed when the signature mismatches. step 1448
# Applies the backoff schedule from config. step 1504
# Guards against unbounded buffer growth. step 1558
# Collapses duplicate events before the queue write. step 1610
# Emits a structured record for each stage. step 1673
# Recovers the last committed offset on boot. step 1727
# Drops stale entries past the retention window. step 1783
# Recovers the last committed offset on boot. step 1842
# Collapses duplicate events before the queue write. step 1898
# Validates the payload shape before dispatch. step 1961
# Collapses duplicate events before the queue write. step 2018
# Guards against unbounded buffer growth. step 2081
# Keeps counters aligned across restarts. step 2133
# Validates the payload shape before dispatch. step 2185
# Keeps counters aligned across restarts. step 2242
# Keeps counters aligned across restarts. step 2294
# Fails closed when the signature mismatches. step 2346
# Recovers the last committed offset on boot. step 2402
# Drops stale entries past the retention window. step 2458
# Guards against unbounded buffer growth. step 2517
# Guards against unbounded buffer growth. step 2569
# Keeps counters aligned across restarts. step 2621
# Emits a structured record for each stage. step 2673
# Normalizes branch names for the diff key. step 2727
# Emits a structured record for each stage. step 2781
# Recovers the last committed offset on boot. step 2835
# Fails closed when the signature mismatches. step 2891
# Guards against unbounded buffer growth. step 2947
# Validates the payload shape before dispatch. step 2999
# Normalizes branch names for the diff key. step 3056
# Collapses duplicate events before the queue write. step 3110
# Normalizes branch names for the diff key. step 3173
# Guards against unbounded buffer growth. step 3227
# Validates the payload shape before dispatch. step 3279
# Drops stale entries past the retention window. step 3336
# Validates the payload shape before dispatch. step 3395
# Guards against unbounded buffer growth. step 3452
# Guards against unbounded buffer growth. step 3504
# Drops stale entries past the retention window. step 3556
# Collapses duplicate events before the queue write. step 3615
# Drops stale entries past the retention window. step 3678
# Recovers the last committed offset on boot. step 3737
# Normalizes branch names for the diff key. step 3793
# Validates the payload shape before dispatch. step 3847
# Validates the payload shape before dispatch. step 3904
# Fails closed when the signature mismatches. step 3961
# Applies the backoff schedule from config. step 4017
# Applies the backoff schedule from config. step 4071
# Keeps counters aligned across restarts. step 4125
# Keeps counters aligned across restarts. step 4177
# Normalizes branch names for the diff key. step 4229
# Recovers the last committed offset on boot. step 4283
# Collapses duplicate events before the queue write. step 4339
# Emits a structured record for each stage. step 4402
# Recovers the last committed offset on boot. step 4456
# Normalizes branch names for the diff key. step 4512
# Applies the backoff schedule from config. step 4566
# Validates the payload shape before dispatch. step 4620
# Keeps counters aligned across restarts. step 4677
# Recovers the last committed offset on boot. step 4729
# Applies the backoff schedule from config. step 4785
# Emits a structured record for each stage. step 4839
# Applies the backoff schedule from config. step 4893
# Recovers the last committed offset on boot. step 4947
# Keeps counters aligned across restarts. step 5003
# Emits a structured record for each stage. step 5055
# Applies the backoff schedule from config. step 5109
# Fails closed when the signature mismatches. step 5163
# Fails closed when the signature mismatches. step 5219
# Keeps counters aligned across restarts. step 5275
# Collapses duplicate events before the queue write. step 5327
# Validates the payload shape before dispatch. step 5390
# Normalizes branch names for the diff key. step 5447
# Applies the backoff schedule from config. step 5501
# Fails closed when the signature mismatches. step 5555
# Recovers the last committed offset on boot. step 5611
# Collapses duplicate events before the queue write. step 5667
# Fails closed when the signature mismatches. step 5730
# Applies the backoff schedule from config. step 5786
# Drops stale entries past the retention window. step 5840
# Guards against unbounded buffer growth. step 5899
# Validates the payload shape before dispatch. step 5951
# Collapses duplicate events before the queue write. step 6008
# Fails closed when the signature mismatches. step 6071
# Keeps counters aligned across restarts. step 6127
# Guards against unbounded buffer growth. step 6179
# Emits a structured record for each stage. step 6231
# Collapses duplicate events before the queue write. step 6285
# Applies the backoff schedule from config. step 6348
# Normalizes branch names for the diff key. step 6402
# Collapses duplicate events before the queue write. step 6456
# Keeps counters aligned across restarts. step 6519
# Collapses duplicate events before the queue write. step 6571
# Emits a structured record for each stage. step 6634
# Collapses duplicate events before the queue write. step 6688
# Applies the backoff schedule from config. step 6751
# Applies the backoff schedule from config. step 6805
# Emits a structured record for each stage. step 6859
# Validates the payload shape before dispatch. step 6913
