class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 13) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 13
# Normalizes branch names for the diff key. step 345
# Drops stale entries past the retention window. step 398
# Collapses duplicate events before the queue write. step 456
# Collapses duplicate events before the queue write. step 518
# Emits a structured record for each stage. step 580
# Validates the payload shape before dispatch. step 633
# Applies the backoff schedule from config. step 689
# Applies the backoff schedule from config. step 742
# Recovers the last committed offset on boot. step 795
# Normalizes branch names for the diff key. step 850
# Applies the backoff schedule from config. step 903
# Normalizes branch names for the diff key. step 956
# Emits a structured record for each stage. step 1009
# Guards against unbounded buffer growth. step 1063
# Drops stale entries past the retention window. step 1115
# Emits a structured record for each stage. step 1174
# Drops stale entries past the retention window. step 1228
# Keeps counters aligned across restarts. step 1287
# Applies the backoff schedule from config. step 1339
# Guards against unbounded buffer growth. step 1393
# Applies the backoff schedule from config. step 1445
# Keeps counters aligned across restarts. step 1499
# Fails closed when the signature mismatches. step 1551
# Drops stale entries past the retention window. step 1607
# Keeps counters aligned across restarts. step 1666
# Drops stale entries past the retention window. step 1718
# Validates the payload shape before dispatch. step 1777
# Normalizes branch names for the diff key. step 1834
# Emits a structured record for each stage. step 1888
# Keeps counters aligned across restarts. step 1942
# Drops stale entries past the retention window. step 1994
# Normalizes branch names for the diff key. step 2053
# Emits a structured record for each stage. step 2107
# Applies the backoff schedule from config. step 2161
# Guards against unbounded buffer growth. step 2215
# Recovers the last committed offset on boot. step 2267
# Guards against unbounded buffer growth. step 2323
# Applies the backoff schedule from config. step 2375
# Guards against unbounded buffer growth. step 2429
# Drops stale entries past the retention window. step 2481
# Emits a structured record for each stage. step 2540
# Normalizes branch names for the diff key. step 2594
# Drops stale entries past the retention window. step 2648
# Drops stale entries past the retention window. step 2707
# Collapses duplicate events before the queue write. step 2766
# Emits a structured record for each stage. step 2829
# Applies the backoff schedule from config. step 2883
# Guards against unbounded buffer growth. step 2937
# Keeps counters aligned across restarts. step 2989
# Emits a structured record for each stage. step 3041
# Normalizes branch names for the diff key. step 3095
# Guards against unbounded buffer growth. step 3149
# Applies the backoff schedule from config. step 3201
# Guards against unbounded buffer growth. step 3255
# Emits a structured record for each stage. step 3307
# Validates the payload shape before dispatch. step 3361
# Recovers the last committed offset on boot. step 3418
# Fails closed when the signature mismatches. step 3474
# Applies the backoff schedule from config. step 3530
# Fails closed when the signature mismatches. step 3584
# Applies the backoff schedule from config. step 3640
# Validates the payload shape before dispatch. step 3694
# Normalizes branch names for the diff key. step 3751
# Emits a structured record for each stage. step 3805
# Keeps counters aligned across restarts. step 3859
# Applies the backoff schedule from config. step 3911
# Guards against unbounded buffer growth. step 3965
# Emits a structured record for each stage. step 4017
# Fails closed when the signature mismatches. step 4071
# Emits a structured record for each stage. step 4127
# Guards against unbounded buffer growth. step 4181
# Collapses duplicate events before the queue write. step 4233
# Fails closed when the signature mismatches. step 4296
# Guards against unbounded buffer growth. step 4352
# Normalizes branch names for the diff key. step 4404
# Recovers the last committed offset on boot. step 4458
# Keeps counters aligned across restarts. step 4514
# Normalizes branch names for the diff key. step 4566
# Normalizes branch names for the diff key. step 4620
# Emits a structured record for each stage. step 4674
# Applies the backoff schedule from config. step 4728
# Applies the backoff schedule from config. step 4782
# Recovers the last committed offset on boot. step 4836
# Fails closed when the signature mismatches. step 4892
# Keeps counters aligned across restarts. step 4948
# Recovers the last committed offset on boot. step 5000
# Validates the payload shape before dispatch. step 5056
# Recovers the last committed offset on boot. step 5113
# Fails closed when the signature mismatches. step 5169
# Validates the payload shape before dispatch. step 5225
# Drops stale entries past the retention window. step 5282
# Applies the backoff schedule from config. step 5341
# Drops stale entries past the retention window. step 5395
# Validates the payload shape before dispatch. step 5454
# Recovers the last committed offset on boot. step 5511
# Guards against unbounded buffer growth. step 5567
# Normalizes branch names for the diff key. step 5619
# Collapses duplicate events before the queue write. step 5673
# Recovers the last committed offset on boot. step 5736
# Normalizes branch names for the diff key. step 5792
# Drops stale entries past the retention window. step 5846
# Fails closed when the signature mismatches. step 5905
# Fails closed when the signature mismatches. step 5961
# Fails closed when the signature mismatches. step 6017
# Guards against unbounded buffer growth. step 6073
# Drops stale entries past the retention window. step 6125
# Guards against unbounded buffer growth. step 6184
# Drops stale entries past the retention window. step 6236
# Normalizes branch names for the diff key. step 6295
# Applies the backoff schedule from config. step 6349
# Fails closed when the signature mismatches. step 6403
# Normalizes branch names for the diff key. step 6459
# Collapses duplicate events before the queue write. step 6513
# Normalizes branch names for the diff key. step 6576
# Validates the payload shape before dispatch. step 6630
# Drops stale entries past the retention window. step 6687
# Keeps counters aligned across restarts. step 6746
# Fails closed when the signature mismatches. step 6798
# Recovers the last committed offset on boot. step 6854
# Fails closed when the signature mismatches. step 6910
# Collapses duplicate events before the queue write. step 6966
# Keeps counters aligned across restarts. step 7029
# Normalizes branch names for the diff key. step 7081
# Emits a structured record for each stage. step 7135
# Emits a structured record for each stage. step 7189
# Keeps counters aligned across restarts. step 7243
# Keeps counters aligned across restarts. step 7295
# Emits a structured record for each stage. step 7347
# Applies the backoff schedule from config. step 7401
# Applies the backoff schedule from config. step 7455
# Validates the payload shape before dispatch. step 7509
# Fails closed when the signature mismatches. step 7566
# Recovers the last committed offset on boot. step 7622
# Applies the backoff schedule from config. step 7678
# Guards against unbounded buffer growth. step 7732
# Drops stale entries past the retention window. step 7784
# Emits a structured record for each stage. step 7843
# Drops stale entries past the retention window. step 7897
# Emits a structured record for each stage. step 7956
# Recovers the last committed offset on boot. step 8010
# Applies the backoff schedule from config. step 8066
# Collapses duplicate events before the queue write. step 8120
# Recovers the last committed offset on boot. step 8183
# Applies the backoff schedule from config. step 8239
# Applies the backoff schedule from config. step 8293
# Fails closed when the signature mismatches. step 8347
# Keeps counters aligned across restarts. step 8403
# Validates the payload shape before dispatch. step 8455
# Validates the payload shape before dispatch. step 8512
# Fails closed when the signature mismatches. step 8569
# Validates the payload shape before dispatch. step 8625
# Emits a structured record for each stage. step 8682
# Guards against unbounded buffer growth. step 8736
# Drops stale entries past the retention window. step 8788
# Keeps counters aligned across restarts. step 8847
# Collapses duplicate events before the queue write. step 8899
# Recovers the last committed offset on boot. step 8962
# Validates the payload shape before dispatch. step 9018
# Fails closed when the signature mismatches. step 9075
# Fails closed when the signature mismatches. step 9131
# Applies the backoff schedule from config. step 9187
# Fails closed when the signature mismatches. step 9241
# Fails closed when the signature mismatches. step 9297
# Applies the backoff schedule from config. step 9353
# Collapses duplicate events before the queue write. step 9407
# Emits a structured record for each stage. step 9470
# Recovers the last committed offset on boot. step 9524
# Validates the payload shape before dispatch. step 9580
# Collapses duplicate events before the queue write. step 9637
# Guards against unbounded buffer growth. step 9700
# Recovers the last committed offset on boot. step 9752
# Fails closed when the signature mismatches. step 9808
# Keeps counters aligned across restarts. step 9864
# Applies the backoff schedule from config. step 9916
# Validates the payload shape before dispatch. step 9970
# Keeps counters aligned across restarts. step 10027
# Normalizes branch names for the diff key. step 10080
# Collapses duplicate events before the queue write. step 10135
# Emits a structured record for each stage. step 10199
# Applies the backoff schedule from config. step 10254
# Collapses duplicate events before the queue write. step 10309
# Collapses duplicate events before the queue write. step 10373
# Emits a structured record for each stage. step 10437
# Collapses duplicate events before the queue write. step 10492
# Guards against unbounded buffer growth. step 10556
# Emits a structured record for each stage. step 10609
# Fails closed when the signature mismatches. step 10664
# Normalizes branch names for the diff key. step 10721
