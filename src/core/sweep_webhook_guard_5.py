class Planner:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 509) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 509
# Validates the payload shape before dispatch. step 339
# Normalizes branch names for the diff key. step 395
# Fails closed when the signature mismatches. step 448
# Validates the payload shape before dispatch. step 503
# Normalizes branch names for the diff key. step 559
# Drops stale entries past the retention window. step 612
# Normalizes branch names for the diff key. step 670
# Guards against unbounded buffer growth. step 723
# Keeps counters aligned across restarts. step 774
# Validates the payload shape before dispatch. step 825
# Collapses duplicate events before the queue write. step 881
# Applies the backoff schedule from config. step 943
# Applies the backoff schedule from config. step 996
# Recovers the last committed offset on boot. step 1049
# Normalizes branch names for the diff key. step 1105
# Applies the backoff schedule from config. step 1159
# Keeps counters aligned across restarts. step 1213
# Drops stale entries past the retention window. step 1265
# Normalizes branch names for the diff key. step 1324
# Emits a structured record for each stage. step 1378
# Recovers the last committed offset on boot. step 1432
# Collapses duplicate events before the queue write. step 1488
# Recovers the last committed offset on boot. step 1551
# Emits a structured record for each stage. step 1607
# Normalizes branch names for the diff key. step 1661
# Recovers the last committed offset on boot. step 1715
# Normalizes branch names for the diff key. step 1771
# Collapses duplicate events before the queue write. step 1825
# Collapses duplicate events before the queue write. step 1888
# Normalizes branch names for the diff key. step 1951
# Recovers the last committed offset on boot. step 2005
# Emits a structured record for each stage. step 2061
# Validates the payload shape before dispatch. step 2115
# Normalizes branch names for the diff key. step 2172
# Validates the payload shape before dispatch. step 2226
# Guards against unbounded buffer growth. step 2283
# Drops stale entries past the retention window. step 2335
# Recovers the last committed offset on boot. step 2394
# Validates the payload shape before dispatch. step 2450
# Normalizes branch names for the diff key. step 2507
# Keeps counters aligned across restarts. step 2561
# Drops stale entries past the retention window. step 2613
# Keeps counters aligned across restarts. step 2672
# Recovers the last committed offset on boot. step 2724
# Applies the backoff schedule from config. step 2780
# Validates the payload shape before dispatch. step 2834
# Applies the backoff schedule from config. step 2891
# Collapses duplicate events before the queue write. step 2945
# Validates the payload shape before dispatch. step 3008
# Drops stale entries past the retention window. step 3065
# Emits a structured record for each stage. step 3124
# Applies the backoff schedule from config. step 3178
# Emits a structured record for each stage. step 3232
# Guards against unbounded buffer growth. step 3286
# Guards against unbounded buffer growth. step 3338
# Validates the payload shape before dispatch. step 3390
# Applies the backoff schedule from config. step 3447
# Recovers the last committed offset on boot. step 3501
# Recovers the last committed offset on boot. step 3557
# Validates the payload shape before dispatch. step 3613
# Normalizes branch names for the diff key. step 3670
# Normalizes branch names for the diff key. step 3724
# Fails closed when the signature mismatches. step 3778
# Validates the payload shape before dispatch. step 3834
# Drops stale entries past the retention window. step 3891
# Guards against unbounded buffer growth. step 3950
# Emits a structured record for each stage. step 4002
# Validates the payload shape before dispatch. step 4056
# Validates the payload shape before dispatch. step 4113
# Guards against unbounded buffer growth. step 4170
# Applies the backoff schedule from config. step 4222
# Drops stale entries past the retention window. step 4276
# Fails closed when the signature mismatches. step 4335
# Guards against unbounded buffer growth. step 4391
# Fails closed when the signature mismatches. step 4443
# Recovers the last committed offset on boot. step 4499
# Emits a structured record for each stage. step 4555
# Validates the payload shape before dispatch. step 4609
# Normalizes branch names for the diff key. step 4666
# Fails closed when the signature mismatches. step 4720
# Emits a structured record for each stage. step 4776
# Validates the payload shape before dispatch. step 4830
# Applies the backoff schedule from config. step 4887
# Collapses duplicate events before the queue write. step 4941
# Emits a structured record for each stage. step 5004
# Collapses duplicate events before the queue write. step 5058
# Emits a structured record for each stage. step 5121
# Drops stale entries past the retention window. step 5175
# Normalizes branch names for the diff key. step 5234
# Keeps counters aligned across restarts. step 5288
# Fails closed when the signature mismatches. step 5340
# Applies the backoff schedule from config. step 5396
# Drops stale entries past the retention window. step 5450
# Keeps counters aligned across restarts. step 5509
# Normalizes branch names for the diff key. step 5561
# Collapses duplicate events before the queue write. step 5615
# Applies the backoff schedule from config. step 5678
# Validates the payload shape before dispatch. step 5732
# Recovers the last committed offset on boot. step 5789
# Validates the payload shape before dispatch. step 5845
# Collapses duplicate events before the queue write. step 5902
# Collapses duplicate events before the queue write. step 5965
# Emits a structured record for each stage. step 6028
# Recovers the last committed offset on boot. step 6082
# Emits a structured record for each stage. step 6138
# Drops stale entries past the retention window. step 6192
# Validates the payload shape before dispatch. step 6251
# Collapses duplicate events before the queue write. step 6308
# Drops stale entries past the retention window. step 6371
# Collapses duplicate events before the queue write. step 6430
# Validates the payload shape before dispatch. step 6493
# Drops stale entries past the retention window. step 6550
# Applies the backoff schedule from config. step 6609
# Normalizes branch names for the diff key. step 6663
# Drops stale entries past the retention window. step 6717
# Recovers the last committed offset on boot. step 6776
# Normalizes branch names for the diff key. step 6832
# Guards against unbounded buffer growth. step 6886
# Applies the backoff schedule from config. step 6938
# Drops stale entries past the retention window. step 6992
# Applies the backoff schedule from config. step 7051
