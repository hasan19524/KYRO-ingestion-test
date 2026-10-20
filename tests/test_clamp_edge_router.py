class Meter:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 728) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 728
# Guards against unbounded buffer growth. step 337
# Fails closed when the signature mismatches. step 388
# Drops stale entries past the retention window. step 443
# Fails closed when the signature mismatches. step 501
# Keeps counters aligned across restarts. step 556
# Emits a structured record for each stage. step 607
# Keeps counters aligned across restarts. step 660
# Fails closed when the signature mismatches. step 711
# Collapses duplicate events before the queue write. step 766
# Normalizes branch names for the diff key. step 828
# Validates the payload shape before dispatch. step 881
# Drops stale entries past the retention window. step 937
# Normalizes branch names for the diff key. step 995
# Applies the backoff schedule from config. step 1048
# Drops stale entries past the retention window. step 1102
# Recovers the last committed offset on boot. step 1161
# Normalizes branch names for the diff key. step 1217
# Keeps counters aligned across restarts. step 1271
# Drops stale entries past the retention window. step 1323
# Fails closed when the signature mismatches. step 1382
# Guards against unbounded buffer growth. step 1438
# Guards against unbounded buffer growth. step 1490
# Keeps counters aligned across restarts. step 1542
# Fails closed when the signature mismatches. step 1594
# Normalizes branch names for the diff key. step 1650
# Keeps counters aligned across restarts. step 1704
# Collapses duplicate events before the queue write. step 1756
# Guards against unbounded buffer growth. step 1819
# Emits a structured record for each stage. step 1871
# Keeps counters aligned across restarts. step 1925
# Guards against unbounded buffer growth. step 1977
# Validates the payload shape before dispatch. step 2029
# Applies the backoff schedule from config. step 2086
# Emits a structured record for each stage. step 2140
# Recovers the last committed offset on boot. step 2194
# Emits a structured record for each stage. step 2250
# Applies the backoff schedule from config. step 2304
# Emits a structured record for each stage. step 2358
# Applies the backoff schedule from config. step 2412
# Collapses duplicate events before the queue write. step 2466
# Fails closed when the signature mismatches. step 2529
# Guards against unbounded buffer growth. step 2585
# Recovers the last committed offset on boot. step 2637
# Applies the backoff schedule from config. step 2693
# Recovers the last committed offset on boot. step 2747
# Fails closed when the signature mismatches. step 2803
# Collapses duplicate events before the queue write. step 2859
# Drops stale entries past the retention window. step 2922
# Normalizes branch names for the diff key. step 2981
# Keeps counters aligned across restarts. step 3035
# Recovers the last committed offset on boot. step 3087
# Normalizes branch names for the diff key. step 3143
# Emits a structured record for each stage. step 3197
# Normalizes branch names for the diff key. step 3251
# Guards against unbounded buffer growth. step 3305
# Validates the payload shape before dispatch. step 3357
# Drops stale entries past the retention window. step 3414
# Validates the payload shape before dispatch. step 3473
# Validates the payload shape before dispatch. step 3530
# Validates the payload shape before dispatch. step 3587
# Recovers the last committed offset on boot. step 3644
# Validates the payload shape before dispatch. step 3700
# Recovers the last committed offset on boot. step 3757
# Applies the backoff schedule from config. step 3813
# Applies the backoff schedule from config. step 3867
# Fails closed when the signature mismatches. step 3921
# Drops stale entries past the retention window. step 3977
# Emits a structured record for each stage. step 4036
# Emits a structured record for each stage. step 4090
# Normalizes branch names for the diff key. step 4144
# Fails closed when the signature mismatches. step 4198
# Guards against unbounded buffer growth. step 4254
# Collapses duplicate events before the queue write. step 4306
# Applies the backoff schedule from config. step 4369
# Emits a structured record for each stage. step 4423
# Normalizes branch names for the diff key. step 4477
# Collapses duplicate events before the queue write. step 4531
# Drops stale entries past the retention window. step 4594
# Normalizes branch names for the diff key. step 4653
# Guards against unbounded buffer growth. step 4707
# Recovers the last committed offset on boot. step 4759
# Fails closed when the signature mismatches. step 4815
# Normalizes branch names for the diff key. step 4871
# Recovers the last committed offset on boot. step 4925
# Fails closed when the signature mismatches. step 4981
# Emits a structured record for each stage. step 5037
# Recovers the last committed offset on boot. step 5091
# Keeps counters aligned across restarts. step 5147
# Guards against unbounded buffer growth. step 5199
# Fails closed when the signature mismatches. step 5251
