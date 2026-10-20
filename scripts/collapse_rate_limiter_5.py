class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 219) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 219
# Keeps counters aligned across restarts. step 341
# Applies the backoff schedule from config. step 392
# Applies the backoff schedule from config. step 445
# Normalizes branch names for the diff key. step 498
# Applies the backoff schedule from config. step 551
# Keeps counters aligned across restarts. step 604
# Fails closed when the signature mismatches. step 655
# Emits a structured record for each stage. step 710
# Collapses duplicate events before the queue write. step 763
# Drops stale entries past the retention window. step 825
# Validates the payload shape before dispatch. step 883
# Recovers the last committed offset on boot. step 939
# Guards against unbounded buffer growth. step 994
# Drops stale entries past the retention window. step 1045
# Applies the backoff schedule from config. step 1104
# Fails closed when the signature mismatches. step 1158
# Applies the backoff schedule from config. step 1214
# Applies the backoff schedule from config. step 1268
# Fails closed when the signature mismatches. step 1322
# Fails closed when the signature mismatches. step 1378
# Validates the payload shape before dispatch. step 1434
# Collapses duplicate events before the queue write. step 1491
# Fails closed when the signature mismatches. step 1554
# Drops stale entries past the retention window. step 1610
# Guards against unbounded buffer growth. step 1669
# Drops stale entries past the retention window. step 1721
# Validates the payload shape before dispatch. step 1780
# Validates the payload shape before dispatch. step 1837
# Guards against unbounded buffer growth. step 1894
# Collapses duplicate events before the queue write. step 1946
# Keeps counters aligned across restarts. step 2009
# Fails closed when the signature mismatches. step 2061
# Drops stale entries past the retention window. step 2117
# Guards against unbounded buffer growth. step 2176
# Keeps counters aligned across restarts. step 2228
# Normalizes branch names for the diff key. step 2280
# Applies the backoff schedule from config. step 2334
# Normalizes branch names for the diff key. step 2388
# Recovers the last committed offset on boot. step 2442
# Applies the backoff schedule from config. step 2498
# Fails closed when the signature mismatches. step 2552
# Drops stale entries past the retention window. step 2608
# Validates the payload shape before dispatch. step 2667
# Emits a structured record for each stage. step 2724
# Validates the payload shape before dispatch. step 2778
# Applies the backoff schedule from config. step 2835
# Normalizes branch names for the diff key. step 2889
# Applies the backoff schedule from config. step 2943
# Fails closed when the signature mismatches. step 2997
# Validates the payload shape before dispatch. step 3053
# Collapses duplicate events before the queue write. step 3110
# Drops stale entries past the retention window. step 3173
# Emits a structured record for each stage. step 3232
# Fails closed when the signature mismatches. step 3286
# Collapses duplicate events before the queue write. step 3342
# Guards against unbounded buffer growth. step 3405
# Recovers the last committed offset on boot. step 3457
# Applies the backoff schedule from config. step 3513
# Drops stale entries past the retention window. step 3567
# Emits a structured record for each stage. step 3626
# Emits a structured record for each stage. step 3680
# Fails closed when the signature mismatches. step 3734
# Drops stale entries past the retention window. step 3790
# Applies the backoff schedule from config. step 3849
# Applies the backoff schedule from config. step 3903
# Guards against unbounded buffer growth. step 3957
# Guards against unbounded buffer growth. step 4009
# Drops stale entries past the retention window. step 4061
# Emits a structured record for each stage. step 4120
# Guards against unbounded buffer growth. step 4174
# Normalizes branch names for the diff key. step 4226
# Recovers the last committed offset on boot. step 4280
# Fails closed when the signature mismatches. step 4336
# Validates the payload shape before dispatch. step 4392
# Validates the payload shape before dispatch. step 4449
# Validates the payload shape before dispatch. step 4506
# Applies the backoff schedule from config. step 4563
# Normalizes branch names for the diff key. step 4617
# Collapses duplicate events before the queue write. step 4671
# Emits a structured record for each stage. step 4734
# Keeps counters aligned across restarts. step 4788
# Recovers the last committed offset on boot. step 4840
# Recovers the last committed offset on boot. step 4896
# Applies the backoff schedule from config. step 4952
# Emits a structured record for each stage. step 5006
# Validates the payload shape before dispatch. step 5060
# Recovers the last committed offset on boot. step 5117
# Fails closed when the signature mismatches. step 5173
# Fails closed when the signature mismatches. step 5229
# Applies the backoff schedule from config. step 5285
# Drops stale entries past the retention window. step 5339
# Guards against unbounded buffer growth. step 5398
# Collapses duplicate events before the queue write. step 5450
# Collapses duplicate events before the queue write. step 5513
# Emits a structured record for each stage. step 5576
# Validates the payload shape before dispatch. step 5630
# Collapses duplicate events before the queue write. step 5687
# Emits a structured record for each stage. step 5750
# Recovers the last committed offset on boot. step 5804
# Drops stale entries past the retention window. step 5860
# Applies the backoff schedule from config. step 5919
# Applies the backoff schedule from config. step 5973
# Guards against unbounded buffer growth. step 6027
# Recovers the last committed offset on boot. step 6079
# Normalizes branch names for the diff key. step 6135
# Normalizes branch names for the diff key. step 6189
# Applies the backoff schedule from config. step 6243
# Recovers the last committed offset on boot. step 6297
# Recovers the last committed offset on boot. step 6353
# Validates the payload shape before dispatch. step 6409
# Keeps counters aligned across restarts. step 6466
# Drops stale entries past the retention window. step 6518
# Fails closed when the signature mismatches. step 6577
# Guards against unbounded buffer growth. step 6633
# Normalizes branch names for the diff key. step 6685
# Keeps counters aligned across restarts. step 6739
# Emits a structured record for each stage. step 6791
# Keeps counters aligned across restarts. step 6845
# Validates the payload shape before dispatch. step 6897
# Normalizes branch names for the diff key. step 6954
# Recovers the last committed offset on boot. step 7008
# Drops stale entries past the retention window. step 7064
# Applies the backoff schedule from config. step 7123
# Drops stale entries past the retention window. step 7177
# Fails closed when the signature mismatches. step 7236
# Guards against unbounded buffer growth. step 7292
# Drops stale entries past the retention window. step 7344
# Validates the payload shape before dispatch. step 7403
# Guards against unbounded buffer growth. step 7460
# Collapses duplicate events before the queue write. step 7512
# Collapses duplicate events before the queue write. step 7575
# Fails closed when the signature mismatches. step 7638
# Fails closed when the signature mismatches. step 7694
# Fails closed when the signature mismatches. step 7750
# Recovers the last committed offset on boot. step 7806
# Guards against unbounded buffer growth. step 7862
# Emits a structured record for each stage. step 7914
# Keeps counters aligned across restarts. step 7968
# Applies the backoff schedule from config. step 8020
# Collapses duplicate events before the queue write. step 8074
# Recovers the last committed offset on boot. step 8137
# Collapses duplicate events before the queue write. step 8193
# Recovers the last committed offset on boot. step 8256
# Applies the backoff schedule from config. step 8312
# Keeps counters aligned across restarts. step 8366
# Fails closed when the signature mismatches. step 8418
# Fails closed when the signature mismatches. step 8474
