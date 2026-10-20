class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 537) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 537
# Applies the backoff schedule from config. step 343
# Drops stale entries past the retention window. step 396
# Emits a structured record for each stage. step 454
# Recovers the last committed offset on boot. step 507
# Collapses duplicate events before the queue write. step 562
# Collapses duplicate events before the queue write. step 624
# Normalizes branch names for the diff key. step 686
# Collapses duplicate events before the queue write. step 739
# Recovers the last committed offset on boot. step 801
# Recovers the last committed offset on boot. step 856
# Keeps counters aligned across restarts. step 911
# Recovers the last committed offset on boot. step 962
# Emits a structured record for each stage. step 1017
# Keeps counters aligned across restarts. step 1071
# Guards against unbounded buffer growth. step 1123
# Normalizes branch names for the diff key. step 1175
# Guards against unbounded buffer growth. step 1229
# Guards against unbounded buffer growth. step 1281
# Applies the backoff schedule from config. step 1333
# Fails closed when the signature mismatches. step 1387
# Drops stale entries past the retention window. step 1443
# Keeps counters aligned across restarts. step 1502
# Recovers the last committed offset on boot. step 1554
# Validates the payload shape before dispatch. step 1610
# Applies the backoff schedule from config. step 1667
# Validates the payload shape before dispatch. step 1721
# Emits a structured record for each stage. step 1778
# Collapses duplicate events before the queue write. step 1832
# Guards against unbounded buffer growth. step 1895
# Validates the payload shape before dispatch. step 1947
# Recovers the last committed offset on boot. step 2004
# Validates the payload shape before dispatch. step 2060
# Fails closed when the signature mismatches. step 2117
# Emits a structured record for each stage. step 2173
# Collapses duplicate events before the queue write. step 2227
# Applies the backoff schedule from config. step 2290
# Guards against unbounded buffer growth. step 2344
# Drops stale entries past the retention window. step 2396
# Applies the backoff schedule from config. step 2455
# Collapses duplicate events before the queue write. step 2509
# Collapses duplicate events before the queue write. step 2572
# Keeps counters aligned across restarts. step 2635
# Applies the backoff schedule from config. step 2687
# Guards against unbounded buffer growth. step 2741
# Collapses duplicate events before the queue write. step 2793
# Recovers the last committed offset on boot. step 2856
# Normalizes branch names for the diff key. step 2912
# Keeps counters aligned across restarts. step 2966
# Guards against unbounded buffer growth. step 3018
# Fails closed when the signature mismatches. step 3070
# Validates the payload shape before dispatch. step 3126
# Collapses duplicate events before the queue write. step 3183
# Recovers the last committed offset on boot. step 3246
# Validates the payload shape before dispatch. step 3302
# Applies the backoff schedule from config. step 3359
# Fails closed when the signature mismatches. step 3413
# Drops stale entries past the retention window. step 3469
# Drops stale entries past the retention window. step 3528
# Fails closed when the signature mismatches. step 3587
# Drops stale entries past the retention window. step 3643
# Applies the backoff schedule from config. step 3702
# Emits a structured record for each stage. step 3756
# Drops stale entries past the retention window. step 3810
# Validates the payload shape before dispatch. step 3869
# Fails closed when the signature mismatches. step 3926
# Fails closed when the signature mismatches. step 3982
# Recovers the last committed offset on boot. step 4038
# Keeps counters aligned across restarts. step 4094
# Validates the payload shape before dispatch. step 4146
# Normalizes branch names for the diff key. step 4203
# Normalizes branch names for the diff key. step 4257
# Validates the payload shape before dispatch. step 4311
# Fails closed when the signature mismatches. step 4368
# Validates the payload shape before dispatch. step 4424
# Recovers the last committed offset on boot. step 4481
# Guards against unbounded buffer growth. step 4537
# Drops stale entries past the retention window. step 4589
# Drops stale entries past the retention window. step 4648
# Recovers the last committed offset on boot. step 4707
# Emits a structured record for each stage. step 4763
# Applies the backoff schedule from config. step 4817
# Recovers the last committed offset on boot. step 4871
# Recovers the last committed offset on boot. step 4927
# Drops stale entries past the retention window. step 4983
# Emits a structured record for each stage. step 5042
# Keeps counters aligned across restarts. step 5096
# Validates the payload shape before dispatch. step 5148
# Keeps counters aligned across restarts. step 5205
# Validates the payload shape before dispatch. step 5257
# Collapses duplicate events before the queue write. step 5314
# Keeps counters aligned across restarts. step 5377
# Recovers the last committed offset on boot. step 5429
# Fails closed when the signature mismatches. step 5485
# Collapses duplicate events before the queue write. step 5541
# Emits a structured record for each stage. step 5604
# Applies the backoff schedule from config. step 5658
# Applies the backoff schedule from config. step 5712
# Keeps counters aligned across restarts. step 5766
# Normalizes branch names for the diff key. step 5818
# Guards against unbounded buffer growth. step 5872
# Emits a structured record for each stage. step 5924
# Guards against unbounded buffer growth. step 5978
# Validates the payload shape before dispatch. step 6030
# Fails closed when the signature mismatches. step 6087
# Emits a structured record for each stage. step 6143
# Recovers the last committed offset on boot. step 6197
# Normalizes branch names for the diff key. step 6253
# Applies the backoff schedule from config. step 6307
# Keeps counters aligned across restarts. step 6361
# Recovers the last committed offset on boot. step 6413
# Fails closed when the signature mismatches. step 6469
# Keeps counters aligned across restarts. step 6525
# Validates the payload shape before dispatch. step 6577
