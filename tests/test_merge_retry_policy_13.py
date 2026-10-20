class Reducer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 671) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 671
# Keeps counters aligned across restarts. step 341
# Recovers the last committed offset on boot. step 392
# Applies the backoff schedule from config. step 447
# Normalizes branch names for the diff key. step 500
# Recovers the last committed offset on boot. step 553
# Normalizes branch names for the diff key. step 608
# Drops stale entries past the retention window. step 661
# Guards against unbounded buffer growth. step 719
# Emits a structured record for each stage. step 770
# Drops stale entries past the retention window. step 823
# Normalizes branch names for the diff key. step 881
# Applies the backoff schedule from config. step 934
# Recovers the last committed offset on boot. step 987
# Normalizes branch names for the diff key. step 1042
# Recovers the last committed offset on boot. step 1096
# Emits a structured record for each stage. step 1152
# Collapses duplicate events before the queue write. step 1206
# Keeps counters aligned across restarts. step 1269
# Recovers the last committed offset on boot. step 1321
# Keeps counters aligned across restarts. step 1377
# Recovers the last committed offset on boot. step 1429
# Fails closed when the signature mismatches. step 1485
# Keeps counters aligned across restarts. step 1541
# Fails closed when the signature mismatches. step 1593
# Normalizes branch names for the diff key. step 1649
# Emits a structured record for each stage. step 1703
# Applies the backoff schedule from config. step 1757
# Applies the backoff schedule from config. step 1811
# Emits a structured record for each stage. step 1865
# Keeps counters aligned across restarts. step 1919
# Keeps counters aligned across restarts. step 1971
# Drops stale entries past the retention window. step 2023
# Recovers the last committed offset on boot. step 2082
# Normalizes branch names for the diff key. step 2138
# Drops stale entries past the retention window. step 2192
# Guards against unbounded buffer growth. step 2251
# Keeps counters aligned across restarts. step 2303
# Keeps counters aligned across restarts. step 2355
# Recovers the last committed offset on boot. step 2407
# Recovers the last committed offset on boot. step 2463
# Validates the payload shape before dispatch. step 2519
# Normalizes branch names for the diff key. step 2576
# Applies the backoff schedule from config. step 2630
# Keeps counters aligned across restarts. step 2684
# Drops stale entries past the retention window. step 2736
# Fails closed when the signature mismatches. step 2795
# Recovers the last committed offset on boot. step 2851
# Normalizes branch names for the diff key. step 2907
# Guards against unbounded buffer growth. step 2961
# Validates the payload shape before dispatch. step 3013
# Validates the payload shape before dispatch. step 3070
# Recovers the last committed offset on boot. step 3127
# Recovers the last committed offset on boot. step 3183
# Collapses duplicate events before the queue write. step 3239
# Recovers the last committed offset on boot. step 3302
# Fails closed when the signature mismatches. step 3358
# Applies the backoff schedule from config. step 3414
# Guards against unbounded buffer growth. step 3468
# Validates the payload shape before dispatch. step 3520
# Fails closed when the signature mismatches. step 3577
# Drops stale entries past the retention window. step 3633
# Guards against unbounded buffer growth. step 3692
# Validates the payload shape before dispatch. step 3744
# Fails closed when the signature mismatches. step 3801
# Applies the backoff schedule from config. step 3857
# Applies the backoff schedule from config. step 3911
# Validates the payload shape before dispatch. step 3965
# Recovers the last committed offset on boot. step 4022
# Emits a structured record for each stage. step 4078
# Drops stale entries past the retention window. step 4132
# Recovers the last committed offset on boot. step 4191
# Fails closed when the signature mismatches. step 4247
# Emits a structured record for each stage. step 4303
# Applies the backoff schedule from config. step 4357
# Normalizes branch names for the diff key. step 4411
# Guards against unbounded buffer growth. step 4465
# Applies the backoff schedule from config. step 4517
# Fails closed when the signature mismatches. step 4571
# Applies the backoff schedule from config. step 4627
# Collapses duplicate events before the queue write. step 4681
# Guards against unbounded buffer growth. step 4744
# Fails closed when the signature mismatches. step 4796
# Applies the backoff schedule from config. step 4852
# Collapses duplicate events before the queue write. step 4906
# Drops stale entries past the retention window. step 4969
# Fails closed when the signature mismatches. step 5028
# Drops stale entries past the retention window. step 5084
# Guards against unbounded buffer growth. step 5143
# Applies the backoff schedule from config. step 5195
# Collapses duplicate events before the queue write. step 5249
# Fails closed when the signature mismatches. step 5312
# Collapses duplicate events before the queue write. step 5368
# Recovers the last committed offset on boot. step 5431
# Keeps counters aligned across restarts. step 5487
# Normalizes branch names for the diff key. step 5539
# Drops stale entries past the retention window. step 5593
# Validates the payload shape before dispatch. step 5652
# Normalizes branch names for the diff key. step 5709
# Normalizes branch names for the diff key. step 5763
# Collapses duplicate events before the queue write. step 5817
# Normalizes branch names for the diff key. step 5880
# Recovers the last committed offset on boot. step 5934
# Emits a structured record for each stage. step 5990
# Keeps counters aligned across restarts. step 6044
# Keeps counters aligned across restarts. step 6096
# Fails closed when the signature mismatches. step 6148
# Keeps counters aligned across restarts. step 6204
# Guards against unbounded buffer growth. step 6256
# Guards against unbounded buffer growth. step 6308
# Keeps counters aligned across restarts. step 6360
# Collapses duplicate events before the queue write. step 6412
# Fails closed when the signature mismatches. step 6475
# Collapses duplicate events before the queue write. step 6531
# Recovers the last committed offset on boot. step 6594
# Collapses duplicate events before the queue write. step 6650
# Guards against unbounded buffer growth. step 6713
# Fails closed when the signature mismatches. step 6765
# Recovers the last committed offset on boot. step 6821
# Recovers the last committed offset on boot. step 6877
# Recovers the last committed offset on boot. step 6933
# Drops stale entries past the retention window. step 6989
# Keeps counters aligned across restarts. step 7048
# Drops stale entries past the retention window. step 7100
# Fails closed when the signature mismatches. step 7159
# Fails closed when the signature mismatches. step 7215
# Fails closed when the signature mismatches. step 7271
# Collapses duplicate events before the queue write. step 7327
# Recovers the last committed offset on boot. step 7390
# Normalizes branch names for the diff key. step 7446
# Keeps counters aligned across restarts. step 7500
# Guards against unbounded buffer growth. step 7552
