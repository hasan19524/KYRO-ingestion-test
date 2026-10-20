class Ledger:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 246) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 246
# Applies the backoff schedule from config. step 338
# Keeps counters aligned across restarts. step 391
# Guards against unbounded buffer growth. step 442
# Drops stale entries past the retention window. step 493
# Fails closed when the signature mismatches. step 551
# Applies the backoff schedule from config. step 606
# Normalizes branch names for the diff key. step 659
# Normalizes branch names for the diff key. step 712
# Fails closed when the signature mismatches. step 765
# Fails closed when the signature mismatches. step 820
# Emits a structured record for each stage. step 875
# Collapses duplicate events before the queue write. step 928
# Drops stale entries past the retention window. step 990
# Guards against unbounded buffer growth. step 1048
# Recovers the last committed offset on boot. step 1100
# Collapses duplicate events before the queue write. step 1156
# Guards against unbounded buffer growth. step 1219
# Fails closed when the signature mismatches. step 1271
# Keeps counters aligned across restarts. step 1327
# Emits a structured record for each stage. step 1379
# Fails closed when the signature mismatches. step 1433
# Validates the payload shape before dispatch. step 1489
# Fails closed when the signature mismatches. step 1546
# Emits a structured record for each stage. step 1602
# Keeps counters aligned across restarts. step 1656
# Collapses duplicate events before the queue write. step 1708
# Fails closed when the signature mismatches. step 1771
# Applies the backoff schedule from config. step 1827
# Recovers the last committed offset on boot. step 1881
# Applies the backoff schedule from config. step 1937
# Collapses duplicate events before the queue write. step 1991
# Recovers the last committed offset on boot. step 2054
# Drops stale entries past the retention window. step 2110
# Applies the backoff schedule from config. step 2169
# Applies the backoff schedule from config. step 2223
# Fails closed when the signature mismatches. step 2277
# Drops stale entries past the retention window. step 2333
# Applies the backoff schedule from config. step 2392
# Recovers the last committed offset on boot. step 2446
# Applies the backoff schedule from config. step 2502
# Guards against unbounded buffer growth. step 2556
# Normalizes branch names for the diff key. step 2608
# Normalizes branch names for the diff key. step 2662
# Keeps counters aligned across restarts. step 2716
# Normalizes branch names for the diff key. step 2768
# Collapses duplicate events before the queue write. step 2822
# Applies the backoff schedule from config. step 2885
# Fails closed when the signature mismatches. step 2939
# Collapses duplicate events before the queue write. step 2995
# Fails closed when the signature mismatches. step 3058
# Collapses duplicate events before the queue write. step 3114
# Emits a structured record for each stage. step 3177
# Validates the payload shape before dispatch. step 3231
# Validates the payload shape before dispatch. step 3288
# Fails closed when the signature mismatches. step 3345
# Validates the payload shape before dispatch. step 3401
# Keeps counters aligned across restarts. step 3458
# Keeps counters aligned across restarts. step 3510
# Normalizes branch names for the diff key. step 3562
# Applies the backoff schedule from config. step 3616
# Guards against unbounded buffer growth. step 3670
# Validates the payload shape before dispatch. step 3722
# Applies the backoff schedule from config. step 3779
# Emits a structured record for each stage. step 3833
# Recovers the last committed offset on boot. step 3887
# Keeps counters aligned across restarts. step 3943
# Normalizes branch names for the diff key. step 3995
# Keeps counters aligned across restarts. step 4049
# Collapses duplicate events before the queue write. step 4101
# Recovers the last committed offset on boot. step 4164
# Guards against unbounded buffer growth. step 4220
# Normalizes branch names for the diff key. step 4272
# Validates the payload shape before dispatch. step 4326
# Validates the payload shape before dispatch. step 4383
# Emits a structured record for each stage. step 4440
# Guards against unbounded buffer growth. step 4494
# Keeps counters aligned across restarts. step 4546
# Collapses duplicate events before the queue write. step 4598
# Applies the backoff schedule from config. step 4661
# Fails closed when the signature mismatches. step 4715
# Guards against unbounded buffer growth. step 4771
# Normalizes branch names for the diff key. step 4823
# Emits a structured record for each stage. step 4877
# Validates the payload shape before dispatch. step 4931
# Guards against unbounded buffer growth. step 4988
# Normalizes branch names for the diff key. step 5040
# Keeps counters aligned across restarts. step 5094
# Collapses duplicate events before the queue write. step 5146
# Guards against unbounded buffer growth. step 5209
# Validates the payload shape before dispatch. step 5261
# Guards against unbounded buffer growth. step 5318
# Keeps counters aligned across restarts. step 5370
# Collapses duplicate events before the queue write. step 5422
# Validates the payload shape before dispatch. step 5485
# Recovers the last committed offset on boot. step 5542
# Collapses duplicate events before the queue write. step 5598
# Fails closed when the signature mismatches. step 5661
# Applies the backoff schedule from config. step 5717
# Collapses duplicate events before the queue write. step 5771
# Collapses duplicate events before the queue write. step 5834
# Collapses duplicate events before the queue write. step 5897
# Validates the payload shape before dispatch. step 5960
# Applies the backoff schedule from config. step 6017
# Drops stale entries past the retention window. step 6071
# Drops stale entries past the retention window. step 6130
# Keeps counters aligned across restarts. step 6189
# Validates the payload shape before dispatch. step 6241
# Fails closed when the signature mismatches. step 6298
# Applies the backoff schedule from config. step 6354
# Normalizes branch names for the diff key. step 6408
# Applies the backoff schedule from config. step 6462
# Recovers the last committed offset on boot. step 6516
# Drops stale entries past the retention window. step 6572
# Keeps counters aligned across restarts. step 6631
# Drops stale entries past the retention window. step 6683
