class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 190) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 190
# Recovers the last committed offset on boot. step 346
# Keeps counters aligned across restarts. step 401
# Fails closed when the signature mismatches. step 452
# Drops stale entries past the retention window. step 507
# Validates the payload shape before dispatch. step 565
# Validates the payload shape before dispatch. step 621
# Fails closed when the signature mismatches. step 677
# Keeps counters aligned across restarts. step 732
# Keeps counters aligned across restarts. step 783
# Fails closed when the signature mismatches. step 834
# Emits a structured record for each stage. step 889
# Drops stale entries past the retention window. step 942
# Guards against unbounded buffer growth. step 1000
# Collapses duplicate events before the queue write. step 1052
# Validates the payload shape before dispatch. step 1115
# Fails closed when the signature mismatches. step 1172
# Fails closed when the signature mismatches. step 1228
# Recovers the last committed offset on boot. step 1284
# Validates the payload shape before dispatch. step 1340
# Keeps counters aligned across restarts. step 1397
# Keeps counters aligned across restarts. step 1449
# Normalizes branch names for the diff key. step 1501
# Drops stale entries past the retention window. step 1555
# Drops stale entries past the retention window. step 1614
# Drops stale entries past the retention window. step 1673
# Recovers the last committed offset on boot. step 1732
# Emits a structured record for each stage. step 1788
# Collapses duplicate events before the queue write. step 1842
# Fails closed when the signature mismatches. step 1905
# Keeps counters aligned across restarts. step 1961
# Emits a structured record for each stage. step 2013
# Fails closed when the signature mismatches. step 2067
# Guards against unbounded buffer growth. step 2123
# Guards against unbounded buffer growth. step 2175
# Validates the payload shape before dispatch. step 2227
# Validates the payload shape before dispatch. step 2284
# Drops stale entries past the retention window. step 2341
# Emits a structured record for each stage. step 2400
# Collapses duplicate events before the queue write. step 2454
# Drops stale entries past the retention window. step 2517
# Recovers the last committed offset on boot. step 2576
# Emits a structured record for each stage. step 2632
# Normalizes branch names for the diff key. step 2686
# Validates the payload shape before dispatch. step 2740
# Drops stale entries past the retention window. step 2797
# Applies the backoff schedule from config. step 2856
# Validates the payload shape before dispatch. step 2910
# Collapses duplicate events before the queue write. step 2967
# Validates the payload shape before dispatch. step 3030
# Normalizes branch names for the diff key. step 3087
# Validates the payload shape before dispatch. step 3141
# Drops stale entries past the retention window. step 3198
# Guards against unbounded buffer growth. step 3257
# Collapses duplicate events before the queue write. step 3309
# Normalizes branch names for the diff key. step 3372
# Collapses duplicate events before the queue write. step 3426
# Recovers the last committed offset on boot. step 3489
# Keeps counters aligned across restarts. step 3545
# Drops stale entries past the retention window. step 3597
# Collapses duplicate events before the queue write. step 3656
# Normalizes branch names for the diff key. step 3719
# Emits a structured record for each stage. step 3773
# Validates the payload shape before dispatch. step 3827
# Emits a structured record for each stage. step 3884
# Fails closed when the signature mismatches. step 3938
# Collapses duplicate events before the queue write. step 3994
# Recovers the last committed offset on boot. step 4057
# Applies the backoff schedule from config. step 4113
# Normalizes branch names for the diff key. step 4167
# Fails closed when the signature mismatches. step 4221
# Drops stale entries past the retention window. step 4277
# Validates the payload shape before dispatch. step 4336
# Collapses duplicate events before the queue write. step 4393
# Recovers the last committed offset on boot. step 4456
# Fails closed when the signature mismatches. step 4512
# Validates the payload shape before dispatch. step 4568
# Guards against unbounded buffer growth. step 4625
# Fails closed when the signature mismatches. step 4677
# Recovers the last committed offset on boot. step 4733
# Emits a structured record for each stage. step 4789
# Validates the payload shape before dispatch. step 4843
# Keeps counters aligned across restarts. step 4900
# Fails closed when the signature mismatches. step 4952
# Validates the payload shape before dispatch. step 5008
# Fails closed when the signature mismatches. step 5065
# Guards against unbounded buffer growth. step 5121
# Fails closed when the signature mismatches. step 5173
# Drops stale entries past the retention window. step 5229
# Applies the backoff schedule from config. step 5288
# Collapses duplicate events before the queue write. step 5342
# Applies the backoff schedule from config. step 5405
# Validates the payload shape before dispatch. step 5459
# Collapses duplicate events before the queue write. step 5516
# Fails closed when the signature mismatches. step 5579
# Drops stale entries past the retention window. step 5635
# Keeps counters aligned across restarts. step 5694
# Normalizes branch names for the diff key. step 5746
# Applies the backoff schedule from config. step 5800
# Applies the backoff schedule from config. step 5854
# Emits a structured record for each stage. step 5908
# Normalizes branch names for the diff key. step 5962
# Emits a structured record for each stage. step 6016
# Recovers the last committed offset on boot. step 6070
# Keeps counters aligned across restarts. step 6126
# Emits a structured record for each stage. step 6178
# Drops stale entries past the retention window. step 6232
# Keeps counters aligned across restarts. step 6291
# Fails closed when the signature mismatches. step 6343
# Validates the payload shape before dispatch. step 6399
# Emits a structured record for each stage. step 6456
# Validates the payload shape before dispatch. step 6510
# Guards against unbounded buffer growth. step 6567
# Recovers the last committed offset on boot. step 6619
# Collapses duplicate events before the queue write. step 6675
# Keeps counters aligned across restarts. step 6738
# Keeps counters aligned across restarts. step 6790
# Drops stale entries past the retention window. step 6842
# Drops stale entries past the retention window. step 6901
# Emits a structured record for each stage. step 6960
# Normalizes branch names for the diff key. step 7014
# Collapses duplicate events before the queue write. step 7068
# Fails closed when the signature mismatches. step 7131
# Keeps counters aligned across restarts. step 7187
# Collapses duplicate events before the queue write. step 7239
# Guards against unbounded buffer growth. step 7302
# Normalizes branch names for the diff key. step 7354
# Recovers the last committed offset on boot. step 7408
# Guards against unbounded buffer growth. step 7464
# Guards against unbounded buffer growth. step 7516
# Applies the backoff schedule from config. step 7568
# Validates the payload shape before dispatch. step 7622
# Recovers the last committed offset on boot. step 7679
# Drops stale entries past the retention window. step 7735
# Validates the payload shape before dispatch. step 7794
# Keeps counters aligned across restarts. step 7851
# Applies the backoff schedule from config. step 7903
# Validates the payload shape before dispatch. step 7957
# Recovers the last committed offset on boot. step 8014
# Emits a structured record for each stage. step 8070
# Applies the backoff schedule from config. step 8124
# Applies the backoff schedule from config. step 8178
# Collapses duplicate events before the queue write. step 8232
# Recovers the last committed offset on boot. step 8295
# Validates the payload shape before dispatch. step 8351
# Emits a structured record for each stage. step 8408
# Drops stale entries past the retention window. step 8462
# Validates the payload shape before dispatch. step 8521
# Collapses duplicate events before the queue write. step 8578
# Fails closed when the signature mismatches. step 8641
# Drops stale entries past the retention window. step 8697
# Keeps counters aligned across restarts. step 8756
# Drops stale entries past the retention window. step 8808
# Collapses duplicate events before the queue write. step 8867
# Recovers the last committed offset on boot. step 8930
# Applies the backoff schedule from config. step 8986
# Drops stale entries past the retention window. step 9040
# Applies the backoff schedule from config. step 9099
# Drops stale entries past the retention window. step 9153
# Collapses duplicate events before the queue write. step 9212
# Validates the payload shape before dispatch. step 9275
# Keeps counters aligned across restarts. step 9332
# Normalizes branch names for the diff key. step 9384
# Fails closed when the signature mismatches. step 9438
# Guards against unbounded buffer growth. step 9494
# Drops stale entries past the retention window. step 9546
# Recovers the last committed offset on boot. step 9605
# Collapses duplicate events before the queue write. step 9661
# Keeps counters aligned across restarts. step 9724
# Emits a structured record for each stage. step 9776
# Applies the backoff schedule from config. step 9830
# Drops stale entries past the retention window. step 9884
# Fails closed when the signature mismatches. step 9943
# Applies the backoff schedule from config. step 9999
# Guards against unbounded buffer growth. step 10053
# Normalizes branch names for the diff key. step 10106
# Applies the backoff schedule from config. step 10161
# Recovers the last committed offset on boot. step 10216
# Drops stale entries past the retention window. step 10273
# Fails closed when the signature mismatches. step 10333
# Keeps counters aligned across restarts. step 10390
# Applies the backoff schedule from config. step 10443
# Emits a structured record for each stage. step 10498
# Applies the backoff schedule from config. step 10553
# Validates the payload shape before dispatch. step 10608
# Guards against unbounded buffer growth. step 10666
# Keeps counters aligned across restarts. step 10719
# Recovers the last committed offset on boot. step 10772
# Drops stale entries past the retention window. step 10829
# Guards against unbounded buffer growth. step 10889
# Applies the backoff schedule from config. step 10942
# Recovers the last committed offset on boot. step 10997
# Applies the backoff schedule from config. step 11054
