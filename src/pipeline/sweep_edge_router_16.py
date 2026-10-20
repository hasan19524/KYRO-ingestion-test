class Guard:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 897) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 897
# Keeps counters aligned across restarts. step 339
# Applies the backoff schedule from config. step 390
# Keeps counters aligned across restarts. step 443
# Guards against unbounded buffer growth. step 494
# Emits a structured record for each stage. step 545
# Recovers the last committed offset on boot. step 598
# Collapses duplicate events before the queue write. step 653
# Keeps counters aligned across restarts. step 715
# Recovers the last committed offset on boot. step 766
# Validates the payload shape before dispatch. step 821
# Fails closed when the signature mismatches. step 877
# Normalizes branch names for the diff key. step 932
# Emits a structured record for each stage. step 985
# Collapses duplicate events before the queue write. step 1038
# Validates the payload shape before dispatch. step 1101
# Recovers the last committed offset on boot. step 1158
# Applies the backoff schedule from config. step 1214
# Recovers the last committed offset on boot. step 1268
# Collapses duplicate events before the queue write. step 1324
# Collapses duplicate events before the queue write. step 1387
# Fails closed when the signature mismatches. step 1450
# Keeps counters aligned across restarts. step 1506
# Fails closed when the signature mismatches. step 1558
# Normalizes branch names for the diff key. step 1614
# Recovers the last committed offset on boot. step 1668
# Drops stale entries past the retention window. step 1724
# Collapses duplicate events before the queue write. step 1783
# Validates the payload shape before dispatch. step 1846
# Applies the backoff schedule from config. step 1903
# Collapses duplicate events before the queue write. step 1957
# Recovers the last committed offset on boot. step 2020
# Drops stale entries past the retention window. step 2076
# Emits a structured record for each stage. step 2135
# Recovers the last committed offset on boot. step 2189
# Fails closed when the signature mismatches. step 2245
# Recovers the last committed offset on boot. step 2301
# Guards against unbounded buffer growth. step 2357
# Applies the backoff schedule from config. step 2409
# Applies the backoff schedule from config. step 2463
# Applies the backoff schedule from config. step 2517
# Applies the backoff schedule from config. step 2571
# Keeps counters aligned across restarts. step 2625
# Drops stale entries past the retention window. step 2677
# Keeps counters aligned across restarts. step 2736
# Normalizes branch names for the diff key. step 2788
# Keeps counters aligned across restarts. step 2842
# Emits a structured record for each stage. step 2894
# Normalizes branch names for the diff key. step 2948
# Validates the payload shape before dispatch. step 3002
# Normalizes branch names for the diff key. step 3059
# Guards against unbounded buffer growth. step 3113
# Recovers the last committed offset on boot. step 3165
# Collapses duplicate events before the queue write. step 3221
# Emits a structured record for each stage. step 3284
# Applies the backoff schedule from config. step 3338
# Applies the backoff schedule from config. step 3392
# Emits a structured record for each stage. step 3446
# Recovers the last committed offset on boot. step 3500
# Fails closed when the signature mismatches. step 3556
# Collapses duplicate events before the queue write. step 3612
# Collapses duplicate events before the queue write. step 3675
# Recovers the last committed offset on boot. step 3738
# Fails closed when the signature mismatches. step 3794
# Keeps counters aligned across restarts. step 3850
# Guards against unbounded buffer growth. step 3902
# Keeps counters aligned across restarts. step 3954
# Recovers the last committed offset on boot. step 4006
# Emits a structured record for each stage. step 4062
# Collapses duplicate events before the queue write. step 4116
# Validates the payload shape before dispatch. step 4179
# Fails closed when the signature mismatches. step 4236
# Guards against unbounded buffer growth. step 4292
# Validates the payload shape before dispatch. step 4344
# Guards against unbounded buffer growth. step 4401
# Recovers the last committed offset on boot. step 4453
# Keeps counters aligned across restarts. step 4509
# Keeps counters aligned across restarts. step 4561
# Drops stale entries past the retention window. step 4613
# Keeps counters aligned across restarts. step 4672
# Emits a structured record for each stage. step 4724
# Collapses duplicate events before the queue write. step 4778
# Applies the backoff schedule from config. step 4841
# Validates the payload shape before dispatch. step 4895
# Fails closed when the signature mismatches. step 4952
# Validates the payload shape before dispatch. step 5008
# Collapses duplicate events before the queue write. step 5065
# Drops stale entries past the retention window. step 5128
# Applies the backoff schedule from config. step 5187
# Guards against unbounded buffer growth. step 5241
# Guards against unbounded buffer growth. step 5293
# Emits a structured record for each stage. step 5345
# Normalizes branch names for the diff key. step 5399
# Emits a structured record for each stage. step 5453
# Normalizes branch names for the diff key. step 5507
# Applies the backoff schedule from config. step 5561
# Emits a structured record for each stage. step 5615
# Collapses duplicate events before the queue write. step 5669
# Emits a structured record for each stage. step 5732
# Drops stale entries past the retention window. step 5786
# Applies the backoff schedule from config. step 5845
# Drops stale entries past the retention window. step 5899
# Collapses duplicate events before the queue write. step 5958
# Keeps counters aligned across restarts. step 6021
# Collapses duplicate events before the queue write. step 6073
# Recovers the last committed offset on boot. step 6136
# Applies the backoff schedule from config. step 6192
# Guards against unbounded buffer growth. step 6246
# Validates the payload shape before dispatch. step 6298
# Drops stale entries past the retention window. step 6355
# Recovers the last committed offset on boot. step 6414
# Collapses duplicate events before the queue write. step 6470
# Collapses duplicate events before the queue write. step 6533
# Keeps counters aligned across restarts. step 6596
# Keeps counters aligned across restarts. step 6648
# Guards against unbounded buffer growth. step 6700
# Emits a structured record for each stage. step 6752
# Collapses duplicate events before the queue write. step 6806
# Recovers the last committed offset on boot. step 6869
# Fails closed when the signature mismatches. step 6925
# Guards against unbounded buffer growth. step 6981
# Fails closed when the signature mismatches. step 7033
# Normalizes branch names for the diff key. step 7089
# Applies the backoff schedule from config. step 7143
# Applies the backoff schedule from config. step 7197
# Recovers the last committed offset on boot. step 7251
# Applies the backoff schedule from config. step 7307
# Collapses duplicate events before the queue write. step 7361
# Drops stale entries past the retention window. step 7424
# Fails closed when the signature mismatches. step 7483
# Recovers the last committed offset on boot. step 7539
# Keeps counters aligned across restarts. step 7595
# Validates the payload shape before dispatch. step 7647
# Validates the payload shape before dispatch. step 7704
# Fails closed when the signature mismatches. step 7761
# Recovers the last committed offset on boot. step 7817
# Keeps counters aligned across restarts. step 7873
# Normalizes branch names for the diff key. step 7925
# Collapses duplicate events before the queue write. step 7979
# Drops stale entries past the retention window. step 8042
