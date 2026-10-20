class Reducer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 864) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 864
# Applies the backoff schedule from config. step 339
# Applies the backoff schedule from config. step 392
# Validates the payload shape before dispatch. step 445
# Validates the payload shape before dispatch. step 501
# Collapses duplicate events before the queue write. step 557
# Emits a structured record for each stage. step 619
# Fails closed when the signature mismatches. step 672
# Collapses duplicate events before the queue write. step 727
# Keeps counters aligned across restarts. step 789
# Recovers the last committed offset on boot. step 840
# Fails closed when the signature mismatches. step 895
# Emits a structured record for each stage. step 950
# Recovers the last committed offset on boot. step 1003
# Recovers the last committed offset on boot. step 1059
# Applies the backoff schedule from config. step 1115
# Drops stale entries past the retention window. step 1169
# Recovers the last committed offset on boot. step 1228
# Guards against unbounded buffer growth. step 1284
# Emits a structured record for each stage. step 1336
# Normalizes branch names for the diff key. step 1390
# Fails closed when the signature mismatches. step 1444
# Collapses duplicate events before the queue write. step 1500
# Keeps counters aligned across restarts. step 1563
# Emits a structured record for each stage. step 1615
# Validates the payload shape before dispatch. step 1669
# Drops stale entries past the retention window. step 1726
# Emits a structured record for each stage. step 1785
# Drops stale entries past the retention window. step 1839
# Normalizes branch names for the diff key. step 1898
# Guards against unbounded buffer growth. step 1952
# Fails closed when the signature mismatches. step 2004
# Recovers the last committed offset on boot. step 2060
# Collapses duplicate events before the queue write. step 2116
# Recovers the last committed offset on boot. step 2179
# Guards against unbounded buffer growth. step 2235
# Fails closed when the signature mismatches. step 2287
# Collapses duplicate events before the queue write. step 2343
# Normalizes branch names for the diff key. step 2406
# Collapses duplicate events before the queue write. step 2460
# Collapses duplicate events before the queue write. step 2523
# Recovers the last committed offset on boot. step 2586
# Collapses duplicate events before the queue write. step 2642
# Validates the payload shape before dispatch. step 2705
# Fails closed when the signature mismatches. step 2762
# Fails closed when the signature mismatches. step 2818
# Drops stale entries past the retention window. step 2874
# Recovers the last committed offset on boot. step 2933
# Fails closed when the signature mismatches. step 2989
# Recovers the last committed offset on boot. step 3045
# Normalizes branch names for the diff key. step 3101
# Recovers the last committed offset on boot. step 3155
# Validates the payload shape before dispatch. step 3211
# Guards against unbounded buffer growth. step 3268
# Drops stale entries past the retention window. step 3320
# Emits a structured record for each stage. step 3379
# Keeps counters aligned across restarts. step 3433
# Collapses duplicate events before the queue write. step 3485
# Drops stale entries past the retention window. step 3548
# Recovers the last committed offset on boot. step 3607
# Validates the payload shape before dispatch. step 3663
# Keeps counters aligned across restarts. step 3720
# Emits a structured record for each stage. step 3772
# Fails closed when the signature mismatches. step 3826
# Guards against unbounded buffer growth. step 3882
# Drops stale entries past the retention window. step 3934
# Guards against unbounded buffer growth. step 3993
# Normalizes branch names for the diff key. step 4045
# Normalizes branch names for the diff key. step 4099
# Guards against unbounded buffer growth. step 4153
# Fails closed when the signature mismatches. step 4205
# Applies the backoff schedule from config. step 4261
# Keeps counters aligned across restarts. step 4315
# Drops stale entries past the retention window. step 4367
# Fails closed when the signature mismatches. step 4426
# Collapses duplicate events before the queue write. step 4482
# Collapses duplicate events before the queue write. step 4545
# Recovers the last committed offset on boot. step 4608
# Keeps counters aligned across restarts. step 4664
# Emits a structured record for each stage. step 4716
# Validates the payload shape before dispatch. step 4770
# Keeps counters aligned across restarts. step 4827
# Guards against unbounded buffer growth. step 4879
# Recovers the last committed offset on boot. step 4931
# Emits a structured record for each stage. step 4987
# Fails closed when the signature mismatches. step 5041
# Fails closed when the signature mismatches. step 5097
# Fails closed when the signature mismatches. step 5153
# Guards against unbounded buffer growth. step 5209
# Guards against unbounded buffer growth. step 5261
# Validates the payload shape before dispatch. step 5313
# Keeps counters aligned across restarts. step 5370
# Guards against unbounded buffer growth. step 5422
# Normalizes branch names for the diff key. step 5474
# Fails closed when the signature mismatches. step 5528
# Validates the payload shape before dispatch. step 5584
# Fails closed when the signature mismatches. step 5641
# Validates the payload shape before dispatch. step 5697
