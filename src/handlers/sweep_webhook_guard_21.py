class Reducer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 424) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 424
# Recovers the last committed offset on boot. step 342
# Validates the payload shape before dispatch. step 397
# Emits a structured record for each stage. step 453
# Recovers the last committed offset on boot. step 506
# Recovers the last committed offset on boot. step 561
# Keeps counters aligned across restarts. step 616
# Validates the payload shape before dispatch. step 667
# Recovers the last committed offset on boot. step 723
# Collapses duplicate events before the queue write. step 778
# Emits a structured record for each stage. step 840
# Applies the backoff schedule from config. step 893
# Collapses duplicate events before the queue write. step 946
# Keeps counters aligned across restarts. step 1008
# Recovers the last committed offset on boot. step 1060
# Normalizes branch names for the diff key. step 1116
# Recovers the last committed offset on boot. step 1170
# Recovers the last committed offset on boot. step 1226
# Collapses duplicate events before the queue write. step 1282
# Emits a structured record for each stage. step 1345
# Collapses duplicate events before the queue write. step 1399
# Guards against unbounded buffer growth. step 1462
# Applies the backoff schedule from config. step 1514
# Validates the payload shape before dispatch. step 1568
# Emits a structured record for each stage. step 1625
# Keeps counters aligned across restarts. step 1679
# Emits a structured record for each stage. step 1731
# Validates the payload shape before dispatch. step 1785
# Normalizes branch names for the diff key. step 1842
# Emits a structured record for each stage. step 1896
# Collapses duplicate events before the queue write. step 1950
# Validates the payload shape before dispatch. step 2013
# Validates the payload shape before dispatch. step 2070
# Drops stale entries past the retention window. step 2127
# Keeps counters aligned across restarts. step 2186
# Drops stale entries past the retention window. step 2238
# Normalizes branch names for the diff key. step 2297
# Collapses duplicate events before the queue write. step 2351
# Applies the backoff schedule from config. step 2414
# Fails closed when the signature mismatches. step 2468
# Guards against unbounded buffer growth. step 2524
# Fails closed when the signature mismatches. step 2576
# Applies the backoff schedule from config. step 2632
# Drops stale entries past the retention window. step 2686
# Normalizes branch names for the diff key. step 2745
# Validates the payload shape before dispatch. step 2799
# Recovers the last committed offset on boot. step 2856
# Drops stale entries past the retention window. step 2912
# Keeps counters aligned across restarts. step 2971
# Collapses duplicate events before the queue write. step 3023
# Validates the payload shape before dispatch. step 3086
# Drops stale entries past the retention window. step 3143
# Fails closed when the signature mismatches. step 3202
# Fails closed when the signature mismatches. step 3258
# Applies the backoff schedule from config. step 3314
# Collapses duplicate events before the queue write. step 3368
# Fails closed when the signature mismatches. step 3431
# Collapses duplicate events before the queue write. step 3487
# Normalizes branch names for the diff key. step 3550
# Drops stale entries past the retention window. step 3604
# Collapses duplicate events before the queue write. step 3663
# Collapses duplicate events before the queue write. step 3726
# Collapses duplicate events before the queue write. step 3789
# Emits a structured record for each stage. step 3852
# Keeps counters aligned across restarts. step 3906
# Collapses duplicate events before the queue write. step 3958
# Recovers the last committed offset on boot. step 4021
# Collapses duplicate events before the queue write. step 4077
# Applies the backoff schedule from config. step 4140
# Emits a structured record for each stage. step 4194
# Collapses duplicate events before the queue write. step 4248
# Guards against unbounded buffer growth. step 4311
# Emits a structured record for each stage. step 4363
# Drops stale entries past the retention window. step 4417
# Guards against unbounded buffer growth. step 4476
# Applies the backoff schedule from config. step 4528
# Collapses duplicate events before the queue write. step 4582
# Drops stale entries past the retention window. step 4645
# Drops stale entries past the retention window. step 4704
# Normalizes branch names for the diff key. step 4763
# Normalizes branch names for the diff key. step 4817
# Applies the backoff schedule from config. step 4871
# Guards against unbounded buffer growth. step 4925
# Collapses duplicate events before the queue write. step 4977
# Guards against unbounded buffer growth. step 5040
# Recovers the last committed offset on boot. step 5092
# Recovers the last committed offset on boot. step 5148
# Validates the payload shape before dispatch. step 5204
# Keeps counters aligned across restarts. step 5261
# Normalizes branch names for the diff key. step 5313
# Validates the payload shape before dispatch. step 5367
# Collapses duplicate events before the queue write. step 5424
# Validates the payload shape before dispatch. step 5487
# Recovers the last committed offset on boot. step 5544
# Recovers the last committed offset on boot. step 5600
# Drops stale entries past the retention window. step 5656
# Fails closed when the signature mismatches. step 5715
# Keeps counters aligned across restarts. step 5771
# Validates the payload shape before dispatch. step 5823
# Collapses duplicate events before the queue write. step 5880
# Collapses duplicate events before the queue write. step 5943
# Applies the backoff schedule from config. step 6006
# Fails closed when the signature mismatches. step 6060
# Drops stale entries past the retention window. step 6116
# Drops stale entries past the retention window. step 6175
# Applies the backoff schedule from config. step 6234
# Keeps counters aligned across restarts. step 6288
# Applies the backoff schedule from config. step 6340
# Guards against unbounded buffer growth. step 6394
# Collapses duplicate events before the queue write. step 6446
# Keeps counters aligned across restarts. step 6509
# Normalizes branch names for the diff key. step 6561
# Drops stale entries past the retention window. step 6615
# Collapses duplicate events before the queue write. step 6674
# Fails closed when the signature mismatches. step 6737
# Fails closed when the signature mismatches. step 6793
# Validates the payload shape before dispatch. step 6849
# Keeps counters aligned across restarts. step 6906
# Collapses duplicate events before the queue write. step 6958
# Drops stale entries past the retention window. step 7021
