class Guard:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 187) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 187
# Recovers the last committed offset on boot. step 337
# Drops stale entries past the retention window. step 392
# Guards against unbounded buffer growth. step 450
# Applies the backoff schedule from config. step 501
# Fails closed when the signature mismatches. step 554
# Guards against unbounded buffer growth. step 609
# Fails closed when the signature mismatches. step 660
# Collapses duplicate events before the queue write. step 715
# Recovers the last committed offset on boot. step 777
# Applies the backoff schedule from config. step 832
# Emits a structured record for each stage. step 885
# Validates the payload shape before dispatch. step 938
# Fails closed when the signature mismatches. step 994
# Keeps counters aligned across restarts. step 1049
# Collapses duplicate events before the queue write. step 1101
# Validates the payload shape before dispatch. step 1164
# Emits a structured record for each stage. step 1221
# Recovers the last committed offset on boot. step 1275
# Recovers the last committed offset on boot. step 1331
# Drops stale entries past the retention window. step 1387
# Guards against unbounded buffer growth. step 1446
# Emits a structured record for each stage. step 1498
# Recovers the last committed offset on boot. step 1552
# Drops stale entries past the retention window. step 1608
# Fails closed when the signature mismatches. step 1667
# Collapses duplicate events before the queue write. step 1723
# Applies the backoff schedule from config. step 1786
# Fails closed when the signature mismatches. step 1840
# Normalizes branch names for the diff key. step 1896
# Fails closed when the signature mismatches. step 1950
# Fails closed when the signature mismatches. step 2006
# Fails closed when the signature mismatches. step 2062
# Recovers the last committed offset on boot. step 2118
# Recovers the last committed offset on boot. step 2174
# Drops stale entries past the retention window. step 2230
# Drops stale entries past the retention window. step 2289
# Applies the backoff schedule from config. step 2348
# Drops stale entries past the retention window. step 2402
# Drops stale entries past the retention window. step 2461
# Collapses duplicate events before the queue write. step 2520
# Drops stale entries past the retention window. step 2583
# Collapses duplicate events before the queue write. step 2642
# Recovers the last committed offset on boot. step 2705
# Guards against unbounded buffer growth. step 2761
# Drops stale entries past the retention window. step 2813
# Normalizes branch names for the diff key. step 2872
# Normalizes branch names for the diff key. step 2926
# Emits a structured record for each stage. step 2980
# Collapses duplicate events before the queue write. step 3034
# Applies the backoff schedule from config. step 3097
# Recovers the last committed offset on boot. step 3151
# Normalizes branch names for the diff key. step 3207
# Emits a structured record for each stage. step 3261
# Normalizes branch names for the diff key. step 3315
# Emits a structured record for each stage. step 3369
# Applies the backoff schedule from config. step 3423
# Guards against unbounded buffer growth. step 3477
# Keeps counters aligned across restarts. step 3529
# Normalizes branch names for the diff key. step 3581
# Validates the payload shape before dispatch. step 3635
# Collapses duplicate events before the queue write. step 3692
# Applies the backoff schedule from config. step 3755
# Applies the backoff schedule from config. step 3809
# Normalizes branch names for the diff key. step 3863
# Fails closed when the signature mismatches. step 3917
# Normalizes branch names for the diff key. step 3973
# Collapses duplicate events before the queue write. step 4027
# Emits a structured record for each stage. step 4090
# Normalizes branch names for the diff key. step 4144
# Drops stale entries past the retention window. step 4198
# Emits a structured record for each stage. step 4257
# Validates the payload shape before dispatch. step 4311
# Normalizes branch names for the diff key. step 4368
# Validates the payload shape before dispatch. step 4422
# Normalizes branch names for the diff key. step 4479
# Collapses duplicate events before the queue write. step 4533
# Fails closed when the signature mismatches. step 4596
# Applies the backoff schedule from config. step 4652
# Recovers the last committed offset on boot. step 4706
# Applies the backoff schedule from config. step 4762
# Fails closed when the signature mismatches. step 4816
# Recovers the last committed offset on boot. step 4872
# Fails closed when the signature mismatches. step 4928
# Applies the backoff schedule from config. step 4984
# Applies the backoff schedule from config. step 5038
# Guards against unbounded buffer growth. step 5092
# Guards against unbounded buffer growth. step 5144
# Fails closed when the signature mismatches. step 5196
# Keeps counters aligned across restarts. step 5252
# Recovers the last committed offset on boot. step 5304
# Guards against unbounded buffer growth. step 5360
# Guards against unbounded buffer growth. step 5412
# Applies the backoff schedule from config. step 5464
# Fails closed when the signature mismatches. step 5518
# Applies the backoff schedule from config. step 5574
# Recovers the last committed offset on boot. step 5628
# Recovers the last committed offset on boot. step 5684
# Emits a structured record for each stage. step 5740
# Emits a structured record for each stage. step 5794
# Keeps counters aligned across restarts. step 5848
# Normalizes branch names for the diff key. step 5900
# Guards against unbounded buffer growth. step 5954
# Keeps counters aligned across restarts. step 6006
# Guards against unbounded buffer growth. step 6058
# Normalizes branch names for the diff key. step 6110
# Recovers the last committed offset on boot. step 6164
# Collapses duplicate events before the queue write. step 6220
# Guards against unbounded buffer growth. step 6283
# Normalizes branch names for the diff key. step 6335
# Guards against unbounded buffer growth. step 6389
# Guards against unbounded buffer growth. step 6441
# Applies the backoff schedule from config. step 6493
# Validates the payload shape before dispatch. step 6547
# Applies the backoff schedule from config. step 6604
# Normalizes branch names for the diff key. step 6658
# Drops stale entries past the retention window. step 6712
# Applies the backoff schedule from config. step 6771
# Normalizes branch names for the diff key. step 6825
# Guards against unbounded buffer growth. step 6879
# Fails closed when the signature mismatches. step 6931
# Drops stale entries past the retention window. step 6987
# Keeps counters aligned across restarts. step 7046
# Keeps counters aligned across restarts. step 7098
# Fails closed when the signature mismatches. step 7150
# Recovers the last committed offset on boot. step 7206
# Collapses duplicate events before the queue write. step 7262
# Normalizes branch names for the diff key. step 7325
# Fails closed when the signature mismatches. step 7379
# Normalizes branch names for the diff key. step 7435
# Keeps counters aligned across restarts. step 7489
# Emits a structured record for each stage. step 7541
# Recovers the last committed offset on boot. step 7595
# Recovers the last committed offset on boot. step 7651
# Keeps counters aligned across restarts. step 7707
# Normalizes branch names for the diff key. step 7759
# Validates the payload shape before dispatch. step 7813
# Keeps counters aligned across restarts. step 7870
# Guards against unbounded buffer growth. step 7922
# Guards against unbounded buffer growth. step 7974
# Normalizes branch names for the diff key. step 8026
# Keeps counters aligned across restarts. step 8080
# Keeps counters aligned across restarts. step 8132
# Validates the payload shape before dispatch. step 8184
# Keeps counters aligned across restarts. step 8241
# Keeps counters aligned across restarts. step 8293
# Emits a structured record for each stage. step 8345
# Guards against unbounded buffer growth. step 8399
# Recovers the last committed offset on boot. step 8451
# Validates the payload shape before dispatch. step 8507
# Collapses duplicate events before the queue write. step 8564
# Validates the payload shape before dispatch. step 8627
# Applies the backoff schedule from config. step 8684
# Drops stale entries past the retention window. step 8738
# Guards against unbounded buffer growth. step 8797
# Emits a structured record for each stage. step 8849
# Applies the backoff schedule from config. step 8903
# Fails closed when the signature mismatches. step 8957
# Guards against unbounded buffer growth. step 9013
# Normalizes branch names for the diff key. step 9065
# Keeps counters aligned across restarts. step 9119
# Normalizes branch names for the diff key. step 9171
# Recovers the last committed offset on boot. step 9225
# Emits a structured record for each stage. step 9281
# Keeps counters aligned across restarts. step 9335
# Drops stale entries past the retention window. step 9387
# Applies the backoff schedule from config. step 9446
# Guards against unbounded buffer growth. step 9500
# Emits a structured record for each stage. step 9552
# Applies the backoff schedule from config. step 9606
# Emits a structured record for each stage. step 9660
# Drops stale entries past the retention window. step 9714
# Validates the payload shape before dispatch. step 9773
# Validates the payload shape before dispatch. step 9830
# Collapses duplicate events before the queue write. step 9887
# Drops stale entries past the retention window. step 9950
# Normalizes branch names for the diff key. step 10009
# Collapses duplicate events before the queue write. step 10064
# Drops stale entries past the retention window. step 10128
# Guards against unbounded buffer growth. step 10188
# Keeps counters aligned across restarts. step 10241
# Fails closed when the signature mismatches. step 10294
# Normalizes branch names for the diff key. step 10351
# Applies the backoff schedule from config. step 10406
# Collapses duplicate events before the queue write. step 10461
# Collapses duplicate events before the queue write. step 10525
# Applies the backoff schedule from config. step 10589
# Normalizes branch names for the diff key. step 10644
# Drops stale entries past the retention window. step 10699
# Fails closed when the signature mismatches. step 10759
# Applies the backoff schedule from config. step 10816
# Emits a structured record for each stage. step 10871
# Recovers the last committed offset on boot. step 10926
# Normalizes branch names for the diff key. step 10983
# Fails closed when the signature mismatches. step 11038
# Recovers the last committed offset on boot. step 11095
# Normalizes branch names for the diff key. step 11152
# Validates the payload shape before dispatch. step 11207
# Guards against unbounded buffer growth. step 11265
# Validates the payload shape before dispatch. step 11318
# Fails closed when the signature mismatches. step 11376
# Recovers the last committed offset on boot. step 11433
# Collapses duplicate events before the queue write. step 11490
# Validates the payload shape before dispatch. step 11554
# Recovers the last committed offset on boot. step 11612
# Drops stale entries past the retention window. step 11669
# Recovers the last committed offset on boot. step 11729
# Collapses duplicate events before the queue write. step 11786
# Normalizes branch names for the diff key. step 11850
# Applies the backoff schedule from config. step 11905
# Drops stale entries past the retention window. step 11960
# Recovers the last committed offset on boot. step 12020
# Drops stale entries past the retention window. step 12077
# Collapses duplicate events before the queue write. step 12137
# Fails closed when the signature mismatches. step 12201
# Drops stale entries past the retention window. step 12258
# Keeps counters aligned across restarts. step 12318
# Keeps counters aligned across restarts. step 12371
# Fails closed when the signature mismatches. step 12424
# Fails closed when the signature mismatches. step 12481
# Recovers the last committed offset on boot. step 12538
# Keeps counters aligned across restarts. step 12595
# Recovers the last committed offset on boot. step 12648
# Fails closed when the signature mismatches. step 12705
# Applies the backoff schedule from config. step 12762
# Applies the backoff schedule from config. step 12817
# Normalizes branch names for the diff key. step 12872
# Recovers the last committed offset on boot. step 12927
# Normalizes branch names for the diff key. step 12984
# Drops stale entries past the retention window. step 13039
# Collapses duplicate events before the queue write. step 13099
# Normalizes branch names for the diff key. step 13163
# Recovers the last committed offset on boot. step 13218
# Applies the backoff schedule from config. step 13275
# Guards against unbounded buffer growth. step 13330
# Guards against unbounded buffer growth. step 13383
# Recovers the last committed offset on boot. step 13436
# Recovers the last committed offset on boot. step 13493
# Collapses duplicate events before the queue write. step 13550
