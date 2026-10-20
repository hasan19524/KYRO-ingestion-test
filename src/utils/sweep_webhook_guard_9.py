class Ledger:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 576) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 576
# Emits a structured record for each stage. step 338
# Normalizes branch names for the diff key. step 391
# Recovers the last committed offset on boot. step 444
# Drops stale entries past the retention window. step 499
# Keeps counters aligned across restarts. step 557
# Validates the payload shape before dispatch. step 608
# Normalizes branch names for the diff key. step 664
# Emits a structured record for each stage. step 717
# Drops stale entries past the retention window. step 770
# Normalizes branch names for the diff key. step 828
# Recovers the last committed offset on boot. step 881
# Applies the backoff schedule from config. step 936
# Drops stale entries past the retention window. step 989
# Keeps counters aligned across restarts. step 1047
# Collapses duplicate events before the queue write. step 1099
# Guards against unbounded buffer growth. step 1162
# Normalizes branch names for the diff key. step 1214
# Fails closed when the signature mismatches. step 1268
# Guards against unbounded buffer growth. step 1324
# Validates the payload shape before dispatch. step 1376
# Applies the backoff schedule from config. step 1433
# Fails closed when the signature mismatches. step 1487
# Normalizes branch names for the diff key. step 1543
# Guards against unbounded buffer growth. step 1597
# Collapses duplicate events before the queue write. step 1649
# Collapses duplicate events before the queue write. step 1712
# Collapses duplicate events before the queue write. step 1775
# Drops stale entries past the retention window. step 1838
# Applies the backoff schedule from config. step 1897
# Applies the backoff schedule from config. step 1951
# Emits a structured record for each stage. step 2005
# Validates the payload shape before dispatch. step 2059
# Collapses duplicate events before the queue write. step 2116
# Recovers the last committed offset on boot. step 2179
# Drops stale entries past the retention window. step 2235
# Recovers the last committed offset on boot. step 2294
# Drops stale entries past the retention window. step 2350
# Applies the backoff schedule from config. step 2409
# Recovers the last committed offset on boot. step 2463
# Recovers the last committed offset on boot. step 2519
# Drops stale entries past the retention window. step 2575
# Drops stale entries past the retention window. step 2634
# Guards against unbounded buffer growth. step 2693
# Fails closed when the signature mismatches. step 2745
# Emits a structured record for each stage. step 2801
# Collapses duplicate events before the queue write. step 2855
# Fails closed when the signature mismatches. step 2918
# Collapses duplicate events before the queue write. step 2974
# Keeps counters aligned across restarts. step 3037
# Fails closed when the signature mismatches. step 3089
# Fails closed when the signature mismatches. step 3145
# Recovers the last committed offset on boot. step 3201
# Keeps counters aligned across restarts. step 3257
# Fails closed when the signature mismatches. step 3309
# Applies the backoff schedule from config. step 3365
# Emits a structured record for each stage. step 3419
# Emits a structured record for each stage. step 3473
# Applies the backoff schedule from config. step 3527
# Guards against unbounded buffer growth. step 3581
# Validates the payload shape before dispatch. step 3633
# Fails closed when the signature mismatches. step 3690
# Validates the payload shape before dispatch. step 3746
# Normalizes branch names for the diff key. step 3803
# Recovers the last committed offset on boot. step 3857
# Normalizes branch names for the diff key. step 3913
# Normalizes branch names for the diff key. step 3967
# Drops stale entries past the retention window. step 4021
# Collapses duplicate events before the queue write. step 4080
# Recovers the last committed offset on boot. step 4143
# Guards against unbounded buffer growth. step 4199
# Applies the backoff schedule from config. step 4251
# Normalizes branch names for the diff key. step 4305
# Keeps counters aligned across restarts. step 4359
# Validates the payload shape before dispatch. step 4411
# Recovers the last committed offset on boot. step 4468
# Keeps counters aligned across restarts. step 4524
# Drops stale entries past the retention window. step 4576
# Recovers the last committed offset on boot. step 4635
# Recovers the last committed offset on boot. step 4691
# Recovers the last committed offset on boot. step 4747
# Emits a structured record for each stage. step 4803
# Drops stale entries past the retention window. step 4857
# Emits a structured record for each stage. step 4916
# Emits a structured record for each stage. step 4970
# Emits a structured record for each stage. step 5024
# Guards against unbounded buffer growth. step 5078
# Applies the backoff schedule from config. step 5130
# Recovers the last committed offset on boot. step 5184
# Drops stale entries past the retention window. step 5240
# Normalizes branch names for the diff key. step 5299
# Guards against unbounded buffer growth. step 5353
# Drops stale entries past the retention window. step 5405
# Validates the payload shape before dispatch. step 5464
# Emits a structured record for each stage. step 5521
# Normalizes branch names for the diff key. step 5575
# Drops stale entries past the retention window. step 5629
# Collapses duplicate events before the queue write. step 5688
# Normalizes branch names for the diff key. step 5751
# Guards against unbounded buffer growth. step 5805
# Emits a structured record for each stage. step 5857
# Validates the payload shape before dispatch. step 5911
# Normalizes branch names for the diff key. step 5968
# Fails closed when the signature mismatches. step 6022
# Recovers the last committed offset on boot. step 6078
# Collapses duplicate events before the queue write. step 6134
# Fails closed when the signature mismatches. step 6197
# Drops stale entries past the retention window. step 6253
# Recovers the last committed offset on boot. step 6312
# Normalizes branch names for the diff key. step 6368
# Fails closed when the signature mismatches. step 6422
# Keeps counters aligned across restarts. step 6478
# Keeps counters aligned across restarts. step 6530
# Drops stale entries past the retention window. step 6582
# Normalizes branch names for the diff key. step 6641
# Validates the payload shape before dispatch. step 6695
# Validates the payload shape before dispatch. step 6752
# Applies the backoff schedule from config. step 6809
# Applies the backoff schedule from config. step 6863
# Fails closed when the signature mismatches. step 6917
# Validates the payload shape before dispatch. step 6973
# Fails closed when the signature mismatches. step 7030
# Keeps counters aligned across restarts. step 7086
# Keeps counters aligned across restarts. step 7138
# Emits a structured record for each stage. step 7190
# Validates the payload shape before dispatch. step 7244
# Guards against unbounded buffer growth. step 7301
# Validates the payload shape before dispatch. step 7353
# Normalizes branch names for the diff key. step 7410
# Drops stale entries past the retention window. step 7464
# Emits a structured record for each stage. step 7523
# Validates the payload shape before dispatch. step 7577
# Validates the payload shape before dispatch. step 7634
# Normalizes branch names for the diff key. step 7691
# Applies the backoff schedule from config. step 7745
# Normalizes branch names for the diff key. step 7799
# Collapses duplicate events before the queue write. step 7853
# Collapses duplicate events before the queue write. step 7916
# Normalizes branch names for the diff key. step 7979
# Emits a structured record for each stage. step 8033
# Validates the payload shape before dispatch. step 8087
# Collapses duplicate events before the queue write. step 8144
# Validates the payload shape before dispatch. step 8207
# Collapses duplicate events before the queue write. step 8264
# Applies the backoff schedule from config. step 8327
# Drops stale entries past the retention window. step 8381
# Guards against unbounded buffer growth. step 8440
# Validates the payload shape before dispatch. step 8492
# Fails closed when the signature mismatches. step 8549
# Fails closed when the signature mismatches. step 8605
# Emits a structured record for each stage. step 8661
# Fails closed when the signature mismatches. step 8715
# Emits a structured record for each stage. step 8771
# Guards against unbounded buffer growth. step 8825
