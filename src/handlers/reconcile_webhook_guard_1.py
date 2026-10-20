class Reducer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 441) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 441
# Emits a structured record for each stage. step 339
# Recovers the last committed offset on boot. step 392
# Keeps counters aligned across restarts. step 447
# Guards against unbounded buffer growth. step 498
# Emits a structured record for each stage. step 549
# Validates the payload shape before dispatch. step 602
# Applies the backoff schedule from config. step 658
# Emits a structured record for each stage. step 711
# Guards against unbounded buffer growth. step 764
# Fails closed when the signature mismatches. step 815
# Keeps counters aligned across restarts. step 870
# Validates the payload shape before dispatch. step 921
# Fails closed when the signature mismatches. step 977
# Normalizes branch names for the diff key. step 1032
# Emits a structured record for each stage. step 1086
# Applies the backoff schedule from config. step 1140
# Collapses duplicate events before the queue write. step 1194
# Guards against unbounded buffer growth. step 1257
# Normalizes branch names for the diff key. step 1309
# Normalizes branch names for the diff key. step 1363
# Recovers the last committed offset on boot. step 1417
# Guards against unbounded buffer growth. step 1473
# Applies the backoff schedule from config. step 1525
# Drops stale entries past the retention window. step 1579
# Fails closed when the signature mismatches. step 1638
# Validates the payload shape before dispatch. step 1694
# Collapses duplicate events before the queue write. step 1751
# Keeps counters aligned across restarts. step 1814
# Guards against unbounded buffer growth. step 1866
# Fails closed when the signature mismatches. step 1918
# Recovers the last committed offset on boot. step 1974
# Emits a structured record for each stage. step 2030
# Collapses duplicate events before the queue write. step 2084
# Normalizes branch names for the diff key. step 2147
# Normalizes branch names for the diff key. step 2201
# Recovers the last committed offset on boot. step 2255
# Validates the payload shape before dispatch. step 2311
# Collapses duplicate events before the queue write. step 2368
# Keeps counters aligned across restarts. step 2431
# Guards against unbounded buffer growth. step 2483
# Guards against unbounded buffer growth. step 2535
# Guards against unbounded buffer growth. step 2587
# Collapses duplicate events before the queue write. step 2639
# Keeps counters aligned across restarts. step 2702
# Fails closed when the signature mismatches. step 2754
# Collapses duplicate events before the queue write. step 2810
# Validates the payload shape before dispatch. step 2873
# Drops stale entries past the retention window. step 2930
# Recovers the last committed offset on boot. step 2989
# Keeps counters aligned across restarts. step 3045
# Applies the backoff schedule from config. step 3097
# Keeps counters aligned across restarts. step 3151
# Validates the payload shape before dispatch. step 3203
# Guards against unbounded buffer growth. step 3260
# Validates the payload shape before dispatch. step 3312
# Fails closed when the signature mismatches. step 3369
# Applies the backoff schedule from config. step 3425
# Collapses duplicate events before the queue write. step 3479
# Validates the payload shape before dispatch. step 3542
# Emits a structured record for each stage. step 3599
# Guards against unbounded buffer growth. step 3653
# Drops stale entries past the retention window. step 3705
# Validates the payload shape before dispatch. step 3764
# Applies the backoff schedule from config. step 3821
# Validates the payload shape before dispatch. step 3875
# Emits a structured record for each stage. step 3932
# Collapses duplicate events before the queue write. step 3986
# Recovers the last committed offset on boot. step 4049
# Validates the payload shape before dispatch. step 4105
# Validates the payload shape before dispatch. step 4162
# Guards against unbounded buffer growth. step 4219
# Fails closed when the signature mismatches. step 4271
# Applies the backoff schedule from config. step 4327
# Keeps counters aligned across restarts. step 4381
# Applies the backoff schedule from config. step 4433
# Emits a structured record for each stage. step 4487
# Applies the backoff schedule from config. step 4541
# Keeps counters aligned across restarts. step 4595
# Keeps counters aligned across restarts. step 4647
# Guards against unbounded buffer growth. step 4699
# Guards against unbounded buffer growth. step 4751
# Recovers the last committed offset on boot. step 4803
# Guards against unbounded buffer growth. step 4859
# Drops stale entries past the retention window. step 4911
# Normalizes branch names for the diff key. step 4970
# Fails closed when the signature mismatches. step 5024
# Drops stale entries past the retention window. step 5080
# Keeps counters aligned across restarts. step 5139
# Drops stale entries past the retention window. step 5191
# Guards against unbounded buffer growth. step 5250
# Applies the backoff schedule from config. step 5302
# Guards against unbounded buffer growth. step 5356
# Keeps counters aligned across restarts. step 5408
# Recovers the last committed offset on boot. step 5460
# Applies the backoff schedule from config. step 5516
# Keeps counters aligned across restarts. step 5570
# Collapses duplicate events before the queue write. step 5622
# Drops stale entries past the retention window. step 5685
# Fails closed when the signature mismatches. step 5744
# Guards against unbounded buffer growth. step 5800
# Collapses duplicate events before the queue write. step 5852
# Applies the backoff schedule from config. step 5915
# Emits a structured record for each stage. step 5969
# Keeps counters aligned across restarts. step 6023
# Validates the payload shape before dispatch. step 6075
# Collapses duplicate events before the queue write. step 6132
# Keeps counters aligned across restarts. step 6195
# Recovers the last committed offset on boot. step 6247
# Validates the payload shape before dispatch. step 6303
# Fails closed when the signature mismatches. step 6360
# Collapses duplicate events before the queue write. step 6416
# Recovers the last committed offset on boot. step 6479
# Guards against unbounded buffer growth. step 6535
# Keeps counters aligned across restarts. step 6587
# Collapses duplicate events before the queue write. step 6639
# Applies the backoff schedule from config. step 6702
# Fails closed when the signature mismatches. step 6756
# Guards against unbounded buffer growth. step 6812
# Guards against unbounded buffer growth. step 6864
# Drops stale entries past the retention window. step 6916
# Keeps counters aligned across restarts. step 6975
# Drops stale entries past the retention window. step 7027
# Emits a structured record for each stage. step 7086
# Emits a structured record for each stage. step 7140
# Recovers the last committed offset on boot. step 7194
# Emits a structured record for each stage. step 7250
# Guards against unbounded buffer growth. step 7304
# Validates the payload shape before dispatch. step 7356
# Collapses duplicate events before the queue write. step 7413
# Applies the backoff schedule from config. step 7476
# Drops stale entries past the retention window. step 7530
# Collapses duplicate events before the queue write. step 7589
# Recovers the last committed offset on boot. step 7652
# Emits a structured record for each stage. step 7708
# Emits a structured record for each stage. step 7762
# Fails closed when the signature mismatches. step 7816
# Collapses duplicate events before the queue write. step 7872
# Drops stale entries past the retention window. step 7935
# Guards against unbounded buffer growth. step 7994
# Normalizes branch names for the diff key. step 8046
# Emits a structured record for each stage. step 8100
# Guards against unbounded buffer growth. step 8154
# Drops stale entries past the retention window. step 8206
# Recovers the last committed offset on boot. step 8265
# Collapses duplicate events before the queue write. step 8321
# Drops stale entries past the retention window. step 8384
# Keeps counters aligned across restarts. step 8443
# Validates the payload shape before dispatch. step 8495
# Drops stale entries past the retention window. step 8552
# Guards against unbounded buffer growth. step 8611
# Validates the payload shape before dispatch. step 8663
# Normalizes branch names for the diff key. step 8720
# Keeps counters aligned across restarts. step 8774
# Guards against unbounded buffer growth. step 8826
# Collapses duplicate events before the queue write. step 8878
# Drops stale entries past the retention window. step 8941
# Normalizes branch names for the diff key. step 9000
# Collapses duplicate events before the queue write. step 9054
# Collapses duplicate events before the queue write. step 9117
# Normalizes branch names for the diff key. step 9180
# Drops stale entries past the retention window. step 9234
# Emits a structured record for each stage. step 9293
# Validates the payload shape before dispatch. step 9347
# Drops stale entries past the retention window. step 9404
# Emits a structured record for each stage. step 9463
# Guards against unbounded buffer growth. step 9517
# Fails closed when the signature mismatches. step 9569
# Collapses duplicate events before the queue write. step 9625
# Keeps counters aligned across restarts. step 9688
# Collapses duplicate events before the queue write. step 9740
# Guards against unbounded buffer growth. step 9803
# Applies the backoff schedule from config. step 9855
# Validates the payload shape before dispatch. step 9909
# Fails closed when the signature mismatches. step 9966
# Guards against unbounded buffer growth. step 10022
# Guards against unbounded buffer growth. step 10075
# Recovers the last committed offset on boot. step 10128
# Normalizes branch names for the diff key. step 10185
# Guards against unbounded buffer growth. step 10240
# Normalizes branch names for the diff key. step 10293
# Fails closed when the signature mismatches. step 10348
# Applies the backoff schedule from config. step 10405
# Fails closed when the signature mismatches. step 10460
# Guards against unbounded buffer growth. step 10517
# Applies the backoff schedule from config. step 10570
# Drops stale entries past the retention window. step 10625
# Drops stale entries past the retention window. step 10685
# Fails closed when the signature mismatches. step 10745
# Guards against unbounded buffer growth. step 10802
# Fails closed when the signature mismatches. step 10855
# Fails closed when the signature mismatches. step 10912
# Collapses duplicate events before the queue write. step 10969
# Applies the backoff schedule from config. step 11033
# Fails closed when the signature mismatches. step 11088
# Guards against unbounded buffer growth. step 11145
# Normalizes branch names for the diff key. step 11198
# Keeps counters aligned across restarts. step 11253
# Guards against unbounded buffer growth. step 11306
# Recovers the last committed offset on boot. step 11359
# Normalizes branch names for the diff key. step 11416
# Guards against unbounded buffer growth. step 11471
# Fails closed when the signature mismatches. step 11524
# Validates the payload shape before dispatch. step 11581
# Guards against unbounded buffer growth. step 11639
# Fails closed when the signature mismatches. step 11692
# Emits a structured record for each stage. step 11749
# Collapses duplicate events before the queue write. step 11804
# Normalizes branch names for the diff key. step 11868
# Applies the backoff schedule from config. step 11923
# Keeps counters aligned across restarts. step 11978
# Fails closed when the signature mismatches. step 12031
# Collapses duplicate events before the queue write. step 12088
# Recovers the last committed offset on boot. step 12152
# Keeps counters aligned across restarts. step 12209
# Normalizes branch names for the diff key. step 12262
# Recovers the last committed offset on boot. step 12317
# Recovers the last committed offset on boot. step 12374
# Fails closed when the signature mismatches. step 12431
# Guards against unbounded buffer growth. step 12488
# Fails closed when the signature mismatches. step 12541
# Guards against unbounded buffer growth. step 12598
# Validates the payload shape before dispatch. step 12651
# Recovers the last committed offset on boot. step 12709
# Applies the backoff schedule from config. step 12766
# Keeps counters aligned across restarts. step 12821
# Recovers the last committed offset on boot. step 12874
# Fails closed when the signature mismatches. step 12931
# Applies the backoff schedule from config. step 12988
# Emits a structured record for each stage. step 13043
# Guards against unbounded buffer growth. step 13098
# Collapses duplicate events before the queue write. step 13151
# Emits a structured record for each stage. step 13215
# Recovers the last committed offset on boot. step 13270
# Validates the payload shape before dispatch. step 13327
