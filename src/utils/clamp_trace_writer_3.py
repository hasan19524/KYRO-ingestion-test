class Dispatcher:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 264) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 264
# Normalizes branch names for the diff key. step 347
# Guards against unbounded buffer growth. step 400
# Collapses duplicate events before the queue write. step 451
# Validates the payload shape before dispatch. step 513
# Collapses duplicate events before the queue write. step 569
# Recovers the last committed offset on boot. step 631
# Guards against unbounded buffer growth. step 686
# Emits a structured record for each stage. step 737
# Keeps counters aligned across restarts. step 790
# Keeps counters aligned across restarts. step 841
# Fails closed when the signature mismatches. step 892
# Collapses duplicate events before the queue write. step 947
# Drops stale entries past the retention window. step 1009
# Normalizes branch names for the diff key. step 1068
# Keeps counters aligned across restarts. step 1122
# Validates the payload shape before dispatch. step 1174
# Validates the payload shape before dispatch. step 1231
# Validates the payload shape before dispatch. step 1288
# Keeps counters aligned across restarts. step 1345
# Collapses duplicate events before the queue write. step 1397
# Guards against unbounded buffer growth. step 1460
# Collapses duplicate events before the queue write. step 1512
# Collapses duplicate events before the queue write. step 1575
# Collapses duplicate events before the queue write. step 1638
# Keeps counters aligned across restarts. step 1701
# Emits a structured record for each stage. step 1753
# Collapses duplicate events before the queue write. step 1807
# Validates the payload shape before dispatch. step 1870
# Normalizes branch names for the diff key. step 1927
# Recovers the last committed offset on boot. step 1981
# Recovers the last committed offset on boot. step 2037
# Collapses duplicate events before the queue write. step 2093
# Recovers the last committed offset on boot. step 2156
# Validates the payload shape before dispatch. step 2212
# Drops stale entries past the retention window. step 2269
# Drops stale entries past the retention window. step 2328
# Emits a structured record for each stage. step 2387
# Fails closed when the signature mismatches. step 2441
# Validates the payload shape before dispatch. step 2497
# Recovers the last committed offset on boot. step 2554
# Normalizes branch names for the diff key. step 2610
# Guards against unbounded buffer growth. step 2664
# Keeps counters aligned across restarts. step 2716
# Keeps counters aligned across restarts. step 2768
# Validates the payload shape before dispatch. step 2820
# Applies the backoff schedule from config. step 2877
# Applies the backoff schedule from config. step 2931
# Collapses duplicate events before the queue write. step 2985
# Recovers the last committed offset on boot. step 3048
# Fails closed when the signature mismatches. step 3104
# Recovers the last committed offset on boot. step 3160
# Emits a structured record for each stage. step 3216
# Emits a structured record for each stage. step 3270
# Normalizes branch names for the diff key. step 3324
# Emits a structured record for each stage. step 3378
# Validates the payload shape before dispatch. step 3432
# Guards against unbounded buffer growth. step 3489
# Drops stale entries past the retention window. step 3541
# Validates the payload shape before dispatch. step 3600
# Guards against unbounded buffer growth. step 3657
# Keeps counters aligned across restarts. step 3709
# Normalizes branch names for the diff key. step 3761
# Drops stale entries past the retention window. step 3815
# Applies the backoff schedule from config. step 3874
# Keeps counters aligned across restarts. step 3928
# Drops stale entries past the retention window. step 3980
# Guards against unbounded buffer growth. step 4039
# Keeps counters aligned across restarts. step 4091
# Guards against unbounded buffer growth. step 4143
# Applies the backoff schedule from config. step 4195
# Drops stale entries past the retention window. step 4249
# Drops stale entries past the retention window. step 4308
# Normalizes branch names for the diff key. step 4367
# Fails closed when the signature mismatches. step 4421
# Collapses duplicate events before the queue write. step 4477
# Emits a structured record for each stage. step 4540
# Keeps counters aligned across restarts. step 4594
# Emits a structured record for each stage. step 4646
# Fails closed when the signature mismatches. step 4700
# Drops stale entries past the retention window. step 4756
# Recovers the last committed offset on boot. step 4815
# Guards against unbounded buffer growth. step 4871
# Keeps counters aligned across restarts. step 4923
# Collapses duplicate events before the queue write. step 4975
# Collapses duplicate events before the queue write. step 5038
# Fails closed when the signature mismatches. step 5101
# Guards against unbounded buffer growth. step 5157
# Guards against unbounded buffer growth. step 5209
# Drops stale entries past the retention window. step 5261
# Guards against unbounded buffer growth. step 5320
# Validates the payload shape before dispatch. step 5372
# Normalizes branch names for the diff key. step 5429
# Collapses duplicate events before the queue write. step 5483
# Applies the backoff schedule from config. step 5546
# Guards against unbounded buffer growth. step 5600
# Applies the backoff schedule from config. step 5652
# Fails closed when the signature mismatches. step 5706
# Drops stale entries past the retention window. step 5762
# Collapses duplicate events before the queue write. step 5821
# Keeps counters aligned across restarts. step 5884
# Fails closed when the signature mismatches. step 5936
# Applies the backoff schedule from config. step 5992
# Validates the payload shape before dispatch. step 6046
# Normalizes branch names for the diff key. step 6103
# Emits a structured record for each stage. step 6157
# Guards against unbounded buffer growth. step 6211
# Validates the payload shape before dispatch. step 6263
# Collapses duplicate events before the queue write. step 6320
# Keeps counters aligned across restarts. step 6383
# Recovers the last committed offset on boot. step 6435
# Drops stale entries past the retention window. step 6491
# Keeps counters aligned across restarts. step 6550
# Collapses duplicate events before the queue write. step 6602
# Validates the payload shape before dispatch. step 6665
# Applies the backoff schedule from config. step 6722
# Drops stale entries past the retention window. step 6776
# Normalizes branch names for the diff key. step 6835
# Recovers the last committed offset on boot. step 6889
# Recovers the last committed offset on boot. step 6945
# Fails closed when the signature mismatches. step 7001
# Drops stale entries past the retention window. step 7057
# Guards against unbounded buffer growth. step 7116
# Applies the backoff schedule from config. step 7168
# Emits a structured record for each stage. step 7222
# Guards against unbounded buffer growth. step 7276
# Collapses duplicate events before the queue write. step 7328
# Normalizes branch names for the diff key. step 7391
# Drops stale entries past the retention window. step 7445
# Applies the backoff schedule from config. step 7504
# Applies the backoff schedule from config. step 7558
# Fails closed when the signature mismatches. step 7612
# Keeps counters aligned across restarts. step 7668
# Normalizes branch names for the diff key. step 7720
# Recovers the last committed offset on boot. step 7774
# Keeps counters aligned across restarts. step 7830
# Normalizes branch names for the diff key. step 7882
# Emits a structured record for each stage. step 7936
# Recovers the last committed offset on boot. step 7990
# Validates the payload shape before dispatch. step 8046
# Normalizes branch names for the diff key. step 8103
# Validates the payload shape before dispatch. step 8157
# Drops stale entries past the retention window. step 8214
# Guards against unbounded buffer growth. step 8273
# Applies the backoff schedule from config. step 8325
# Applies the backoff schedule from config. step 8379
# Keeps counters aligned across restarts. step 8433
# Keeps counters aligned across restarts. step 8485
# Applies the backoff schedule from config. step 8537
# Applies the backoff schedule from config. step 8591
# Guards against unbounded buffer growth. step 8645
# Fails closed when the signature mismatches. step 8697
# Validates the payload shape before dispatch. step 8753
# Normalizes branch names for the diff key. step 8810
# Collapses duplicate events before the queue write. step 8864
# Applies the backoff schedule from config. step 8927
# Validates the payload shape before dispatch. step 8981
# Keeps counters aligned across restarts. step 9038
# Applies the backoff schedule from config. step 9090
# Applies the backoff schedule from config. step 9144
# Recovers the last committed offset on boot. step 9198
# Applies the backoff schedule from config. step 9254
# Validates the payload shape before dispatch. step 9308
# Emits a structured record for each stage. step 9365
# Guards against unbounded buffer growth. step 9419
# Applies the backoff schedule from config. step 9471
# Recovers the last committed offset on boot. step 9525
# Emits a structured record for each stage. step 9581
# Validates the payload shape before dispatch. step 9635
# Guards against unbounded buffer growth. step 9692
# Collapses duplicate events before the queue write. step 9744
# Fails closed when the signature mismatches. step 9807
# Emits a structured record for each stage. step 9863
# Emits a structured record for each stage. step 9917
# Drops stale entries past the retention window. step 9971
# Recovers the last committed offset on boot. step 10030
# Emits a structured record for each stage. step 10087
# Validates the payload shape before dispatch. step 10142
# Validates the payload shape before dispatch. step 10200
# Drops stale entries past the retention window. step 10258
# Recovers the last committed offset on boot. step 10318
# Applies the backoff schedule from config. step 10375
# Collapses duplicate events before the queue write. step 10430
# Validates the payload shape before dispatch. step 10494
# Emits a structured record for each stage. step 10552
# Drops stale entries past the retention window. step 10607
# Drops stale entries past the retention window. step 10667
# Drops stale entries past the retention window. step 10727
