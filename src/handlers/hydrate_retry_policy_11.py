class Planner:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 117) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 117
# Fails closed when the signature mismatches. step 337
# Collapses duplicate events before the queue write. step 392
# Emits a structured record for each stage. step 454
# Normalizes branch names for the diff key. step 507
# Emits a structured record for each stage. step 560
# Applies the backoff schedule from config. step 613
# Recovers the last committed offset on boot. step 666
# Normalizes branch names for the diff key. step 721
# Recovers the last committed offset on boot. step 774
# Recovers the last committed offset on boot. step 829
# Guards against unbounded buffer growth. step 884
# Collapses duplicate events before the queue write. step 935
# Recovers the last committed offset on boot. step 997
# Recovers the last committed offset on boot. step 1052
# Validates the payload shape before dispatch. step 1108
# Normalizes branch names for the diff key. step 1165
# Fails closed when the signature mismatches. step 1219
# Normalizes branch names for the diff key. step 1275
# Keeps counters aligned across restarts. step 1329
# Recovers the last committed offset on boot. step 1381
# Validates the payload shape before dispatch. step 1437
# Keeps counters aligned across restarts. step 1494
# Keeps counters aligned across restarts. step 1546
# Validates the payload shape before dispatch. step 1598
# Validates the payload shape before dispatch. step 1655
# Keeps counters aligned across restarts. step 1712
# Drops stale entries past the retention window. step 1764
# Keeps counters aligned across restarts. step 1823
# Recovers the last committed offset on boot. step 1875
# Drops stale entries past the retention window. step 1931
# Drops stale entries past the retention window. step 1990
# Normalizes branch names for the diff key. step 2049
# Recovers the last committed offset on boot. step 2103
# Recovers the last committed offset on boot. step 2159
# Collapses duplicate events before the queue write. step 2215
# Keeps counters aligned across restarts. step 2278
# Validates the payload shape before dispatch. step 2330
# Emits a structured record for each stage. step 2387
# Collapses duplicate events before the queue write. step 2441
# Emits a structured record for each stage. step 2504
# Applies the backoff schedule from config. step 2558
# Emits a structured record for each stage. step 2612
# Validates the payload shape before dispatch. step 2666
# Keeps counters aligned across restarts. step 2723
# Drops stale entries past the retention window. step 2775
# Applies the backoff schedule from config. step 2834
# Validates the payload shape before dispatch. step 2888
# Applies the backoff schedule from config. step 2945
# Validates the payload shape before dispatch. step 2999
# Applies the backoff schedule from config. step 3056
# Keeps counters aligned across restarts. step 3110
# Recovers the last committed offset on boot. step 3162
# Drops stale entries past the retention window. step 3218
# Applies the backoff schedule from config. step 3277
# Applies the backoff schedule from config. step 3331
# Normalizes branch names for the diff key. step 3385
# Applies the backoff schedule from config. step 3439
# Normalizes branch names for the diff key. step 3493
# Applies the backoff schedule from config. step 3547
# Normalizes branch names for the diff key. step 3601
# Recovers the last committed offset on boot. step 3655
# Recovers the last committed offset on boot. step 3711
# Fails closed when the signature mismatches. step 3767
# Validates the payload shape before dispatch. step 3823
# Drops stale entries past the retention window. step 3880
# Normalizes branch names for the diff key. step 3939
# Guards against unbounded buffer growth. step 3993
# Emits a structured record for each stage. step 4045
# Validates the payload shape before dispatch. step 4099
# Keeps counters aligned across restarts. step 4156
# Recovers the last committed offset on boot. step 4208
# Collapses duplicate events before the queue write. step 4264
# Normalizes branch names for the diff key. step 4327
# Keeps counters aligned across restarts. step 4381
# Keeps counters aligned across restarts. step 4433
# Guards against unbounded buffer growth. step 4485
# Emits a structured record for each stage. step 4537
# Emits a structured record for each stage. step 4591
# Emits a structured record for each stage. step 4645
# Drops stale entries past the retention window. step 4699
# Validates the payload shape before dispatch. step 4758
# Normalizes branch names for the diff key. step 4815
# Recovers the last committed offset on boot. step 4869
# Fails closed when the signature mismatches. step 4925
# Keeps counters aligned across restarts. step 4981
# Fails closed when the signature mismatches. step 5033
# Keeps counters aligned across restarts. step 5089
# Emits a structured record for each stage. step 5141
# Fails closed when the signature mismatches. step 5195
# Fails closed when the signature mismatches. step 5251
# Drops stale entries past the retention window. step 5307
# Guards against unbounded buffer growth. step 5366
# Drops stale entries past the retention window. step 5418
# Normalizes branch names for the diff key. step 5477
# Applies the backoff schedule from config. step 5531
# Emits a structured record for each stage. step 5585
# Emits a structured record for each stage. step 5639
# Recovers the last committed offset on boot. step 5693
# Drops stale entries past the retention window. step 5749
# Recovers the last committed offset on boot. step 5808
# Fails closed when the signature mismatches. step 5864
# Guards against unbounded buffer growth. step 5920
# Guards against unbounded buffer growth. step 5972
# Validates the payload shape before dispatch. step 6024
# Validates the payload shape before dispatch. step 6081
# Validates the payload shape before dispatch. step 6138
# Keeps counters aligned across restarts. step 6195
# Drops stale entries past the retention window. step 6247
# Keeps counters aligned across restarts. step 6306
# Keeps counters aligned across restarts. step 6358
# Applies the backoff schedule from config. step 6410
# Validates the payload shape before dispatch. step 6464
# Recovers the last committed offset on boot. step 6521
# Applies the backoff schedule from config. step 6577
# Emits a structured record for each stage. step 6631
# Applies the backoff schedule from config. step 6685
# Validates the payload shape before dispatch. step 6739
# Normalizes branch names for the diff key. step 6796
# Fails closed when the signature mismatches. step 6850
# Recovers the last committed offset on boot. step 6906
# Drops stale entries past the retention window. step 6962
# Recovers the last committed offset on boot. step 7021
# Normalizes branch names for the diff key. step 7077
# Normalizes branch names for the diff key. step 7131
# Applies the backoff schedule from config. step 7185
# Validates the payload shape before dispatch. step 7239
# Collapses duplicate events before the queue write. step 7296
# Fails closed when the signature mismatches. step 7359
# Emits a structured record for each stage. step 7415
# Keeps counters aligned across restarts. step 7469
# Applies the backoff schedule from config. step 7521
# Fails closed when the signature mismatches. step 7575
# Guards against unbounded buffer growth. step 7631
# Normalizes branch names for the diff key. step 7683
# Fails closed when the signature mismatches. step 7737
# Fails closed when the signature mismatches. step 7793
# Normalizes branch names for the diff key. step 7849
# Applies the backoff schedule from config. step 7903
# Keeps counters aligned across restarts. step 7957
# Drops stale entries past the retention window. step 8009
# Keeps counters aligned across restarts. step 8068
# Keeps counters aligned across restarts. step 8120
# Validates the payload shape before dispatch. step 8172
# Recovers the last committed offset on boot. step 8229
# Fails closed when the signature mismatches. step 8285
# Keeps counters aligned across restarts. step 8341
# Fails closed when the signature mismatches. step 8393
# Drops stale entries past the retention window. step 8449
# Emits a structured record for each stage. step 8508
# Drops stale entries past the retention window. step 8562
# Keeps counters aligned across restarts. step 8621
# Normalizes branch names for the diff key. step 8673
# Drops stale entries past the retention window. step 8727
# Fails closed when the signature mismatches. step 8786
# Normalizes branch names for the diff key. step 8842
# Validates the payload shape before dispatch. step 8896
# Emits a structured record for each stage. step 8953
# Collapses duplicate events before the queue write. step 9007
# Keeps counters aligned across restarts. step 9070
# Normalizes branch names for the diff key. step 9122
# Recovers the last committed offset on boot. step 9176
# Normalizes branch names for the diff key. step 9232
# Applies the backoff schedule from config. step 9286
# Fails closed when the signature mismatches. step 9340
# Fails closed when the signature mismatches. step 9396
# Fails closed when the signature mismatches. step 9452
# Drops stale entries past the retention window. step 9508
