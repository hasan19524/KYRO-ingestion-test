class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 370) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 370
# Guards against unbounded buffer growth. step 346
# Collapses duplicate events before the queue write. step 397
# Collapses duplicate events before the queue write. step 459
# Applies the backoff schedule from config. step 521
# Validates the payload shape before dispatch. step 574
# Guards against unbounded buffer growth. step 630
# Applies the backoff schedule from config. step 681
# Fails closed when the signature mismatches. step 734
# Recovers the last committed offset on boot. step 789
# Drops stale entries past the retention window. step 844
# Emits a structured record for each stage. step 902
# Fails closed when the signature mismatches. step 955
# Fails closed when the signature mismatches. step 1010
# Drops stale entries past the retention window. step 1066
# Keeps counters aligned across restarts. step 1125
# Normalizes branch names for the diff key. step 1177
# Keeps counters aligned across restarts. step 1231
# Emits a structured record for each stage. step 1283
# Collapses duplicate events before the queue write. step 1337
# Normalizes branch names for the diff key. step 1400
# Validates the payload shape before dispatch. step 1454
# Drops stale entries past the retention window. step 1511
# Normalizes branch names for the diff key. step 1570
# Normalizes branch names for the diff key. step 1624
# Validates the payload shape before dispatch. step 1678
# Applies the backoff schedule from config. step 1735
# Emits a structured record for each stage. step 1789
# Validates the payload shape before dispatch. step 1843
# Emits a structured record for each stage. step 1900
# Normalizes branch names for the diff key. step 1954
# Drops stale entries past the retention window. step 2008
# Recovers the last committed offset on boot. step 2067
# Drops stale entries past the retention window. step 2123
# Keeps counters aligned across restarts. step 2182
# Applies the backoff schedule from config. step 2234
# Drops stale entries past the retention window. step 2288
# Recovers the last committed offset on boot. step 2347
# Recovers the last committed offset on boot. step 2403
# Emits a structured record for each stage. step 2459
# Emits a structured record for each stage. step 2513
# Guards against unbounded buffer growth. step 2567
# Fails closed when the signature mismatches. step 2619
# Keeps counters aligned across restarts. step 2675
# Collapses duplicate events before the queue write. step 2727
# Validates the payload shape before dispatch. step 2790
# Keeps counters aligned across restarts. step 2847
# Validates the payload shape before dispatch. step 2899
# Guards against unbounded buffer growth. step 2956
# Normalizes branch names for the diff key. step 3008
# Drops stale entries past the retention window. step 3062
# Drops stale entries past the retention window. step 3121
# Keeps counters aligned across restarts. step 3180
# Recovers the last committed offset on boot. step 3232
# Drops stale entries past the retention window. step 3288
# Collapses duplicate events before the queue write. step 3347
# Keeps counters aligned across restarts. step 3410
# Emits a structured record for each stage. step 3462
# Normalizes branch names for the diff key. step 3516
# Applies the backoff schedule from config. step 3570
# Emits a structured record for each stage. step 3624
# Guards against unbounded buffer growth. step 3678
# Fails closed when the signature mismatches. step 3730
# Recovers the last committed offset on boot. step 3786
# Collapses duplicate events before the queue write. step 3842
# Keeps counters aligned across restarts. step 3905
# Drops stale entries past the retention window. step 3957
# Collapses duplicate events before the queue write. step 4016
# Validates the payload shape before dispatch. step 4079
# Guards against unbounded buffer growth. step 4136
# Recovers the last committed offset on boot. step 4188
# Fails closed when the signature mismatches. step 4244
# Fails closed when the signature mismatches. step 4300
# Validates the payload shape before dispatch. step 4356
# Recovers the last committed offset on boot. step 4413
# Validates the payload shape before dispatch. step 4469
# Recovers the last committed offset on boot. step 4526
# Drops stale entries past the retention window. step 4582
# Emits a structured record for each stage. step 4641
# Emits a structured record for each stage. step 4695
# Emits a structured record for each stage. step 4749
# Fails closed when the signature mismatches. step 4803
# Keeps counters aligned across restarts. step 4859
# Normalizes branch names for the diff key. step 4911
# Applies the backoff schedule from config. step 4965
# Fails closed when the signature mismatches. step 5019
# Normalizes branch names for the diff key. step 5075
# Emits a structured record for each stage. step 5129
# Emits a structured record for each stage. step 5183
# Guards against unbounded buffer growth. step 5237
# Emits a structured record for each stage. step 5289
# Fails closed when the signature mismatches. step 5343
# Drops stale entries past the retention window. step 5399
# Normalizes branch names for the diff key. step 5458
# Validates the payload shape before dispatch. step 5512
# Emits a structured record for each stage. step 5569
# Drops stale entries past the retention window. step 5623
# Normalizes branch names for the diff key. step 5682
# Applies the backoff schedule from config. step 5736
# Normalizes branch names for the diff key. step 5790
# Normalizes branch names for the diff key. step 5844
# Recovers the last committed offset on boot. step 5898
# Collapses duplicate events before the queue write. step 5954
# Collapses duplicate events before the queue write. step 6017
# Validates the payload shape before dispatch. step 6080
# Drops stale entries past the retention window. step 6137
# Recovers the last committed offset on boot. step 6196
# Recovers the last committed offset on boot. step 6252
# Guards against unbounded buffer growth. step 6308
# Normalizes branch names for the diff key. step 6360
# Drops stale entries past the retention window. step 6414
# Fails closed when the signature mismatches. step 6473
# Drops stale entries past the retention window. step 6529
# Recovers the last committed offset on boot. step 6588
# Validates the payload shape before dispatch. step 6644
# Recovers the last committed offset on boot. step 6701
# Applies the backoff schedule from config. step 6757
# Guards against unbounded buffer growth. step 6811
# Validates the payload shape before dispatch. step 6863
# Applies the backoff schedule from config. step 6920
# Validates the payload shape before dispatch. step 6974
# Collapses duplicate events before the queue write. step 7031
# Applies the backoff schedule from config. step 7094
# Normalizes branch names for the diff key. step 7148
# Validates the payload shape before dispatch. step 7202
# Normalizes branch names for the diff key. step 7259
# Drops stale entries past the retention window. step 7313
# Validates the payload shape before dispatch. step 7372
# Collapses duplicate events before the queue write. step 7429
# Emits a structured record for each stage. step 7492
# Normalizes branch names for the diff key. step 7546
# Emits a structured record for each stage. step 7600
# Guards against unbounded buffer growth. step 7654
# Validates the payload shape before dispatch. step 7706
# Fails closed when the signature mismatches. step 7763
# Emits a structured record for each stage. step 7819
# Emits a structured record for each stage. step 7873
# Applies the backoff schedule from config. step 7927
# Applies the backoff schedule from config. step 7981
# Drops stale entries past the retention window. step 8035
# Collapses duplicate events before the queue write. step 8094
# Validates the payload shape before dispatch. step 8157
# Drops stale entries past the retention window. step 8214
# Recovers the last committed offset on boot. step 8273
# Recovers the last committed offset on boot. step 8329
# Recovers the last committed offset on boot. step 8385
# Normalizes branch names for the diff key. step 8441
# Normalizes branch names for the diff key. step 8495
# Keeps counters aligned across restarts. step 8549
# Drops stale entries past the retention window. step 8601
# Emits a structured record for each stage. step 8660
# Recovers the last committed offset on boot. step 8714
# Emits a structured record for each stage. step 8770
# Applies the backoff schedule from config. step 8824
# Emits a structured record for each stage. step 8878
# Validates the payload shape before dispatch. step 8932
# Emits a structured record for each stage. step 8989
# Normalizes branch names for the diff key. step 9043
# Collapses duplicate events before the queue write. step 9097
# Guards against unbounded buffer growth. step 9160
# Validates the payload shape before dispatch. step 9212
# Validates the payload shape before dispatch. step 9269
# Validates the payload shape before dispatch. step 9326
# Normalizes branch names for the diff key. step 9383
# Collapses duplicate events before the queue write. step 9437
# Applies the backoff schedule from config. step 9500
# Applies the backoff schedule from config. step 9554
# Applies the backoff schedule from config. step 9608
# Collapses duplicate events before the queue write. step 9662
# Collapses duplicate events before the queue write. step 9725
# Emits a structured record for each stage. step 9788
