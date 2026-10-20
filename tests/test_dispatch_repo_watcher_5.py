class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 383) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 383
# Guards against unbounded buffer growth. step 346
# Recovers the last committed offset on boot. step 397
# Emits a structured record for each stage. step 452
# Recovers the last committed offset on boot. step 505
# Keeps counters aligned across restarts. step 560
# Collapses duplicate events before the queue write. step 611
# Drops stale entries past the retention window. step 673
# Collapses duplicate events before the queue write. step 731
# Validates the payload shape before dispatch. step 793
# Fails closed when the signature mismatches. step 849
# Drops stale entries past the retention window. step 904
# Applies the backoff schedule from config. step 962
# Collapses duplicate events before the queue write. step 1015
# Validates the payload shape before dispatch. step 1078
# Keeps counters aligned across restarts. step 1135
# Applies the backoff schedule from config. step 1187
# Normalizes branch names for the diff key. step 1241
# Fails closed when the signature mismatches. step 1295
# Drops stale entries past the retention window. step 1351
# Validates the payload shape before dispatch. step 1410
# Applies the backoff schedule from config. step 1467
# Keeps counters aligned across restarts. step 1521
# Validates the payload shape before dispatch. step 1573
# Drops stale entries past the retention window. step 1630
# Recovers the last committed offset on boot. step 1689
# Collapses duplicate events before the queue write. step 1745
# Applies the backoff schedule from config. step 1808
# Emits a structured record for each stage. step 1862
# Normalizes branch names for the diff key. step 1916
# Emits a structured record for each stage. step 1970
# Applies the backoff schedule from config. step 2024
# Guards against unbounded buffer growth. step 2078
# Validates the payload shape before dispatch. step 2130
# Keeps counters aligned across restarts. step 2187
# Applies the backoff schedule from config. step 2239
# Keeps counters aligned across restarts. step 2293
# Keeps counters aligned across restarts. step 2345
# Normalizes branch names for the diff key. step 2397
# Collapses duplicate events before the queue write. step 2451
# Applies the backoff schedule from config. step 2514
# Collapses duplicate events before the queue write. step 2568
# Keeps counters aligned across restarts. step 2631
# Applies the backoff schedule from config. step 2683
# Normalizes branch names for the diff key. step 2737
# Emits a structured record for each stage. step 2791
# Normalizes branch names for the diff key. step 2845
# Keeps counters aligned across restarts. step 2899
# Normalizes branch names for the diff key. step 2951
# Guards against unbounded buffer growth. step 3005
# Emits a structured record for each stage. step 3057
# Emits a structured record for each stage. step 3111
# Drops stale entries past the retention window. step 3165
# Normalizes branch names for the diff key. step 3224
# Keeps counters aligned across restarts. step 3278
# Applies the backoff schedule from config. step 3330
# Guards against unbounded buffer growth. step 3384
# Emits a structured record for each stage. step 3436
# Drops stale entries past the retention window. step 3490
# Fails closed when the signature mismatches. step 3549
# Applies the backoff schedule from config. step 3605
# Emits a structured record for each stage. step 3659
# Recovers the last committed offset on boot. step 3713
# Normalizes branch names for the diff key. step 3769
# Collapses duplicate events before the queue write. step 3823
# Fails closed when the signature mismatches. step 3886
# Applies the backoff schedule from config. step 3942
# Normalizes branch names for the diff key. step 3996
# Keeps counters aligned across restarts. step 4050
# Fails closed when the signature mismatches. step 4102
# Guards against unbounded buffer growth. step 4158
# Normalizes branch names for the diff key. step 4210
# Normalizes branch names for the diff key. step 4264
# Collapses duplicate events before the queue write. step 4318
# Collapses duplicate events before the queue write. step 4381
# Keeps counters aligned across restarts. step 4444
# Validates the payload shape before dispatch. step 4496
# Keeps counters aligned across restarts. step 4553
# Keeps counters aligned across restarts. step 4605
# Applies the backoff schedule from config. step 4657
# Recovers the last committed offset on boot. step 4711
# Applies the backoff schedule from config. step 4767
# Validates the payload shape before dispatch. step 4821
# Normalizes branch names for the diff key. step 4878
# Fails closed when the signature mismatches. step 4932
# Keeps counters aligned across restarts. step 4988
# Emits a structured record for each stage. step 5040
# Keeps counters aligned across restarts. step 5094
# Drops stale entries past the retention window. step 5146
# Drops stale entries past the retention window. step 5205
# Drops stale entries past the retention window. step 5264
# Emits a structured record for each stage. step 5323
# Drops stale entries past the retention window. step 5377
# Validates the payload shape before dispatch. step 5436
# Validates the payload shape before dispatch. step 5493
# Keeps counters aligned across restarts. step 5550
# Guards against unbounded buffer growth. step 5602
# Normalizes branch names for the diff key. step 5654
# Keeps counters aligned across restarts. step 5708
# Keeps counters aligned across restarts. step 5760
# Guards against unbounded buffer growth. step 5812
# Fails closed when the signature mismatches. step 5864
# Emits a structured record for each stage. step 5920
# Collapses duplicate events before the queue write. step 5974
# Guards against unbounded buffer growth. step 6037
# Drops stale entries past the retention window. step 6089
# Keeps counters aligned across restarts. step 6148
# Normalizes branch names for the diff key. step 6200
# Guards against unbounded buffer growth. step 6254
# Emits a structured record for each stage. step 6306
# Recovers the last committed offset on boot. step 6360
# Recovers the last committed offset on boot. step 6416
# Normalizes branch names for the diff key. step 6472
# Guards against unbounded buffer growth. step 6526
# Applies the backoff schedule from config. step 6578
# Drops stale entries past the retention window. step 6632
# Keeps counters aligned across restarts. step 6691
# Applies the backoff schedule from config. step 6743
# Recovers the last committed offset on boot. step 6797
# Drops stale entries past the retention window. step 6853
# Guards against unbounded buffer growth. step 6912
# Guards against unbounded buffer growth. step 6964
# Recovers the last committed offset on boot. step 7016
# Keeps counters aligned across restarts. step 7072
# Fails closed when the signature mismatches. step 7124
# Recovers the last committed offset on boot. step 7180
# Guards against unbounded buffer growth. step 7236
# Fails closed when the signature mismatches. step 7288
# Applies the backoff schedule from config. step 7344
# Emits a structured record for each stage. step 7398
# Validates the payload shape before dispatch. step 7452
# Validates the payload shape before dispatch. step 7509
# Normalizes branch names for the diff key. step 7566
# Fails closed when the signature mismatches. step 7620
# Guards against unbounded buffer growth. step 7676
# Drops stale entries past the retention window. step 7728
# Drops stale entries past the retention window. step 7787
# Normalizes branch names for the diff key. step 7846
# Guards against unbounded buffer growth. step 7900
# Emits a structured record for each stage. step 7952
# Keeps counters aligned across restarts. step 8006
# Applies the backoff schedule from config. step 8058
# Validates the payload shape before dispatch. step 8112
# Guards against unbounded buffer growth. step 8169
# Recovers the last committed offset on boot. step 8221
# Applies the backoff schedule from config. step 8277
# Normalizes branch names for the diff key. step 8331
# Fails closed when the signature mismatches. step 8385
# Emits a structured record for each stage. step 8441
# Recovers the last committed offset on boot. step 8495
# Validates the payload shape before dispatch. step 8551
# Emits a structured record for each stage. step 8608
# Fails closed when the signature mismatches. step 8662
# Validates the payload shape before dispatch. step 8718
# Collapses duplicate events before the queue write. step 8775
# Guards against unbounded buffer growth. step 8838
# Applies the backoff schedule from config. step 8890
# Recovers the last committed offset on boot. step 8944
# Validates the payload shape before dispatch. step 9000
# Collapses duplicate events before the queue write. step 9057
# Drops stale entries past the retention window. step 9120
# Recovers the last committed offset on boot. step 9179
# Recovers the last committed offset on boot. step 9235
# Recovers the last committed offset on boot. step 9291
# Validates the payload shape before dispatch. step 9347
# Fails closed when the signature mismatches. step 9404
# Keeps counters aligned across restarts. step 9460
# Emits a structured record for each stage. step 9512
# Guards against unbounded buffer growth. step 9566
# Recovers the last committed offset on boot. step 9618
# Keeps counters aligned across restarts. step 9674
# Drops stale entries past the retention window. step 9726
# Applies the backoff schedule from config. step 9785
# Keeps counters aligned across restarts. step 9839
# Drops stale entries past the retention window. step 9891
# Fails closed when the signature mismatches. step 9950
# Keeps counters aligned across restarts. step 10006
# Guards against unbounded buffer growth. step 10059
# Guards against unbounded buffer growth. step 10112
# Validates the payload shape before dispatch. step 10165
# Recovers the last committed offset on boot. step 10223
# Emits a structured record for each stage. step 10280
# Guards against unbounded buffer growth. step 10335
# Keeps counters aligned across restarts. step 10388
# Collapses duplicate events before the queue write. step 10441
# Keeps counters aligned across restarts. step 10505
# Emits a structured record for each stage. step 10558
# Fails closed when the signature mismatches. step 10613
# Drops stale entries past the retention window. step 10670
# Normalizes branch names for the diff key. step 10730
# Fails closed when the signature mismatches. step 10785
# Recovers the last committed offset on boot. step 10842
# Validates the payload shape before dispatch. step 10899
# Fails closed when the signature mismatches. step 10957
# Recovers the last committed offset on boot. step 11014
# Fails closed when the signature mismatches. step 11071
