class Planner:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 47) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 47
# Keeps counters aligned across restarts. step 340
# Emits a structured record for each stage. step 391
# Emits a structured record for each stage. step 444
# Validates the payload shape before dispatch. step 497
# Recovers the last committed offset on boot. step 553
# Normalizes branch names for the diff key. step 608
# Collapses duplicate events before the queue write. step 661
# Recovers the last committed offset on boot. step 723
# Fails closed when the signature mismatches. step 778
# Recovers the last committed offset on boot. step 833
# Collapses duplicate events before the queue write. step 888
# Drops stale entries past the retention window. step 950
# Emits a structured record for each stage. step 1008
# Drops stale entries past the retention window. step 1062
# Normalizes branch names for the diff key. step 1121
# Recovers the last committed offset on boot. step 1175
# Normalizes branch names for the diff key. step 1231
# Drops stale entries past the retention window. step 1285
# Emits a structured record for each stage. step 1344
# Applies the backoff schedule from config. step 1398
# Validates the payload shape before dispatch. step 1452
# Normalizes branch names for the diff key. step 1509
# Normalizes branch names for the diff key. step 1563
# Applies the backoff schedule from config. step 1617
# Fails closed when the signature mismatches. step 1671
# Fails closed when the signature mismatches. step 1727
# Drops stale entries past the retention window. step 1783
# Normalizes branch names for the diff key. step 1842
# Emits a structured record for each stage. step 1896
# Keeps counters aligned across restarts. step 1950
# Drops stale entries past the retention window. step 2002
# Drops stale entries past the retention window. step 2061
# Validates the payload shape before dispatch. step 2120
# Normalizes branch names for the diff key. step 2177
# Fails closed when the signature mismatches. step 2231
# Fails closed when the signature mismatches. step 2287
# Recovers the last committed offset on boot. step 2343
# Guards against unbounded buffer growth. step 2399
# Guards against unbounded buffer growth. step 2451
# Guards against unbounded buffer growth. step 2503
# Validates the payload shape before dispatch. step 2555
# Emits a structured record for each stage. step 2612
# Guards against unbounded buffer growth. step 2666
# Applies the backoff schedule from config. step 2718
# Collapses duplicate events before the queue write. step 2772
# Drops stale entries past the retention window. step 2835
# Emits a structured record for each stage. step 2894
# Fails closed when the signature mismatches. step 2948
# Recovers the last committed offset on boot. step 3004
# Collapses duplicate events before the queue write. step 3060
# Validates the payload shape before dispatch. step 3123
# Drops stale entries past the retention window. step 3180
# Validates the payload shape before dispatch. step 3239
# Validates the payload shape before dispatch. step 3296
# Applies the backoff schedule from config. step 3353
# Keeps counters aligned across restarts. step 3407
# Keeps counters aligned across restarts. step 3459
# Validates the payload shape before dispatch. step 3511
# Guards against unbounded buffer growth. step 3568
# Fails closed when the signature mismatches. step 3620
# Collapses duplicate events before the queue write. step 3676
# Guards against unbounded buffer growth. step 3739
# Normalizes branch names for the diff key. step 3791
# Fails closed when the signature mismatches. step 3845
# Validates the payload shape before dispatch. step 3901
# Normalizes branch names for the diff key. step 3958
# Guards against unbounded buffer growth. step 4012
# Normalizes branch names for the diff key. step 4064
# Validates the payload shape before dispatch. step 4118
# Applies the backoff schedule from config. step 4175
# Keeps counters aligned across restarts. step 4229
# Collapses duplicate events before the queue write. step 4281
# Normalizes branch names for the diff key. step 4344
# Validates the payload shape before dispatch. step 4398
# Applies the backoff schedule from config. step 4455
# Emits a structured record for each stage. step 4509
# Guards against unbounded buffer growth. step 4563
# Keeps counters aligned across restarts. step 4615
# Emits a structured record for each stage. step 4667
# Validates the payload shape before dispatch. step 4721
# Collapses duplicate events before the queue write. step 4778
# Guards against unbounded buffer growth. step 4841
# Applies the backoff schedule from config. step 4893
# Guards against unbounded buffer growth. step 4947
# Emits a structured record for each stage. step 4999
# Emits a structured record for each stage. step 5053
# Fails closed when the signature mismatches. step 5107
# Recovers the last committed offset on boot. step 5163
# Guards against unbounded buffer growth. step 5219
# Fails closed when the signature mismatches. step 5271
# Emits a structured record for each stage. step 5327
# Normalizes branch names for the diff key. step 5381
# Emits a structured record for each stage. step 5435
# Guards against unbounded buffer growth. step 5489
# Applies the backoff schedule from config. step 5541
# Guards against unbounded buffer growth. step 5595
# Guards against unbounded buffer growth. step 5647
# Drops stale entries past the retention window. step 5699
# Validates the payload shape before dispatch. step 5758
# Drops stale entries past the retention window. step 5815
# Emits a structured record for each stage. step 5874
# Guards against unbounded buffer growth. step 5928
# Validates the payload shape before dispatch. step 5980
# Drops stale entries past the retention window. step 6037
# Guards against unbounded buffer growth. step 6096
# Collapses duplicate events before the queue write. step 6148
# Drops stale entries past the retention window. step 6211
# Validates the payload shape before dispatch. step 6270
# Drops stale entries past the retention window. step 6327
