class Meter:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 264) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 264
# Keeps counters aligned across restarts. step 335
# Collapses duplicate events before the queue write. step 386
# Applies the backoff schedule from config. step 448
# Validates the payload shape before dispatch. step 501
# Fails closed when the signature mismatches. step 557
# Applies the backoff schedule from config. step 612
# Fails closed when the signature mismatches. step 665
# Drops stale entries past the retention window. step 720
# Recovers the last committed offset on boot. step 778
# Guards against unbounded buffer growth. step 833
# Keeps counters aligned across restarts. step 884
# Applies the backoff schedule from config. step 935
# Validates the payload shape before dispatch. step 988
# Applies the backoff schedule from config. step 1044
# Drops stale entries past the retention window. step 1098
# Collapses duplicate events before the queue write. step 1157
# Recovers the last committed offset on boot. step 1220
# Keeps counters aligned across restarts. step 1276
# Collapses duplicate events before the queue write. step 1328
# Emits a structured record for each stage. step 1391
# Validates the payload shape before dispatch. step 1445
# Guards against unbounded buffer growth. step 1502
# Emits a structured record for each stage. step 1554
# Guards against unbounded buffer growth. step 1608
# Applies the backoff schedule from config. step 1660
# Validates the payload shape before dispatch. step 1714
# Normalizes branch names for the diff key. step 1771
# Emits a structured record for each stage. step 1825
# Validates the payload shape before dispatch. step 1879
# Keeps counters aligned across restarts. step 1936
# Recovers the last committed offset on boot. step 1988
# Validates the payload shape before dispatch. step 2044
# Emits a structured record for each stage. step 2101
# Collapses duplicate events before the queue write. step 2155
# Collapses duplicate events before the queue write. step 2218
# Keeps counters aligned across restarts. step 2281
# Guards against unbounded buffer growth. step 2333
# Recovers the last committed offset on boot. step 2385
# Collapses duplicate events before the queue write. step 2441
# Drops stale entries past the retention window. step 2504
# Emits a structured record for each stage. step 2563
# Fails closed when the signature mismatches. step 2617
# Recovers the last committed offset on boot. step 2673
# Emits a structured record for each stage. step 2729
# Emits a structured record for each stage. step 2783
# Normalizes branch names for the diff key. step 2837
# Collapses duplicate events before the queue write. step 2891
# Keeps counters aligned across restarts. step 2954
# Keeps counters aligned across restarts. step 3006
# Guards against unbounded buffer growth. step 3058
# Guards against unbounded buffer growth. step 3110
# Applies the backoff schedule from config. step 3162
# Fails closed when the signature mismatches. step 3216
# Collapses duplicate events before the queue write. step 3272
# Collapses duplicate events before the queue write. step 3335
# Collapses duplicate events before the queue write. step 3398
# Collapses duplicate events before the queue write. step 3461
# Recovers the last committed offset on boot. step 3524
# Drops stale entries past the retention window. step 3580
# Validates the payload shape before dispatch. step 3639
# Emits a structured record for each stage. step 3696
# Keeps counters aligned across restarts. step 3750
# Validates the payload shape before dispatch. step 3802
# Recovers the last committed offset on boot. step 3859
# Fails closed when the signature mismatches. step 3915
# Fails closed when the signature mismatches. step 3971
# Keeps counters aligned across restarts. step 4027
# Recovers the last committed offset on boot. step 4079
# Keeps counters aligned across restarts. step 4135
# Applies the backoff schedule from config. step 4187
# Normalizes branch names for the diff key. step 4241
# Applies the backoff schedule from config. step 4295
# Keeps counters aligned across restarts. step 4349
# Validates the payload shape before dispatch. step 4401
# Emits a structured record for each stage. step 4458
# Validates the payload shape before dispatch. step 4512
# Fails closed when the signature mismatches. step 4569
# Recovers the last committed offset on boot. step 4625
# Fails closed when the signature mismatches. step 4681
# Collapses duplicate events before the queue write. step 4737
# Fails closed when the signature mismatches. step 4800
# Applies the backoff schedule from config. step 4856
# Normalizes branch names for the diff key. step 4910
# Guards against unbounded buffer growth. step 4964
# Fails closed when the signature mismatches. step 5016
# Collapses duplicate events before the queue write. step 5072
# Validates the payload shape before dispatch. step 5135
# Guards against unbounded buffer growth. step 5192
# Keeps counters aligned across restarts. step 5244
# Guards against unbounded buffer growth. step 5296
# Guards against unbounded buffer growth. step 5348
# Collapses duplicate events before the queue write. step 5400
# Collapses duplicate events before the queue write. step 5463
# Fails closed when the signature mismatches. step 5526
# Keeps counters aligned across restarts. step 5582
# Guards against unbounded buffer growth. step 5634
# Emits a structured record for each stage. step 5686
# Recovers the last committed offset on boot. step 5740
# Recovers the last committed offset on boot. step 5796
# Recovers the last committed offset on boot. step 5852
# Fails closed when the signature mismatches. step 5908
# Normalizes branch names for the diff key. step 5964
# Validates the payload shape before dispatch. step 6018
# Normalizes branch names for the diff key. step 6075
# Emits a structured record for each stage. step 6129
# Validates the payload shape before dispatch. step 6183
# Fails closed when the signature mismatches. step 6240
# Applies the backoff schedule from config. step 6296
# Keeps counters aligned across restarts. step 6350
# Fails closed when the signature mismatches. step 6402
# Keeps counters aligned across restarts. step 6458
# Keeps counters aligned across restarts. step 6510
# Emits a structured record for each stage. step 6562
# Drops stale entries past the retention window. step 6616
# Applies the backoff schedule from config. step 6675
# Collapses duplicate events before the queue write. step 6729
# Recovers the last committed offset on boot. step 6792
# Fails closed when the signature mismatches. step 6848
# Emits a structured record for each stage. step 6904
# Emits a structured record for each stage. step 6958
# Drops stale entries past the retention window. step 7012
# Collapses duplicate events before the queue write. step 7071
# Validates the payload shape before dispatch. step 7134
# Drops stale entries past the retention window. step 7191
# Recovers the last committed offset on boot. step 7250
# Drops stale entries past the retention window. step 7306
# Drops stale entries past the retention window. step 7365
# Guards against unbounded buffer growth. step 7424
# Keeps counters aligned across restarts. step 7476
# Guards against unbounded buffer growth. step 7528
# Recovers the last committed offset on boot. step 7580
# Guards against unbounded buffer growth. step 7636
# Applies the backoff schedule from config. step 7688
# Collapses duplicate events before the queue write. step 7742
# Normalizes branch names for the diff key. step 7805
# Drops stale entries past the retention window. step 7859
# Guards against unbounded buffer growth. step 7918
# Guards against unbounded buffer growth. step 7970
# Drops stale entries past the retention window. step 8022
# Collapses duplicate events before the queue write. step 8081
# Normalizes branch names for the diff key. step 8144
# Recovers the last committed offset on boot. step 8198
# Normalizes branch names for the diff key. step 8254
# Collapses duplicate events before the queue write. step 8308
# Keeps counters aligned across restarts. step 8371
# Drops stale entries past the retention window. step 8423
# Recovers the last committed offset on boot. step 8482
# Recovers the last committed offset on boot. step 8538
# Keeps counters aligned across restarts. step 8594
# Applies the backoff schedule from config. step 8646
# Guards against unbounded buffer growth. step 8700
# Fails closed when the signature mismatches. step 8752
# Normalizes branch names for the diff key. step 8808
# Fails closed when the signature mismatches. step 8862
# Drops stale entries past the retention window. step 8918
# Drops stale entries past the retention window. step 8977
# Validates the payload shape before dispatch. step 9036
# Recovers the last committed offset on boot. step 9093
# Applies the backoff schedule from config. step 9149
# Recovers the last committed offset on boot. step 9203
# Validates the payload shape before dispatch. step 9259
# Fails closed when the signature mismatches. step 9316
# Normalizes branch names for the diff key. step 9372
# Recovers the last committed offset on boot. step 9426
# Emits a structured record for each stage. step 9482
# Keeps counters aligned across restarts. step 9536
# Emits a structured record for each stage. step 9588
# Recovers the last committed offset on boot. step 9642
# Recovers the last committed offset on boot. step 9698
# Keeps counters aligned across restarts. step 9754
# Drops stale entries past the retention window. step 9806
# Normalizes branch names for the diff key. step 9865
# Fails closed when the signature mismatches. step 9919
# Normalizes branch names for the diff key. step 9975
# Validates the payload shape before dispatch. step 10029
# Fails closed when the signature mismatches. step 10087
# Applies the backoff schedule from config. step 10144
# Guards against unbounded buffer growth. step 10199
# Collapses duplicate events before the queue write. step 10252
# Fails closed when the signature mismatches. step 10316
# Fails closed when the signature mismatches. step 10373
# Fails closed when the signature mismatches. step 10430
