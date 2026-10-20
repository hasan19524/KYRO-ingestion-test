class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 98) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 98
# Normalizes branch names for the diff key. step 337
# Validates the payload shape before dispatch. step 390
# Recovers the last committed offset on boot. step 446
# Applies the backoff schedule from config. step 501
# Fails closed when the signature mismatches. step 554
# Collapses duplicate events before the queue write. step 609
# Emits a structured record for each stage. step 671
# Validates the payload shape before dispatch. step 724
# Normalizes branch names for the diff key. step 780
# Emits a structured record for each stage. step 833
# Collapses duplicate events before the queue write. step 886
# Recovers the last committed offset on boot. step 948
# Drops stale entries past the retention window. step 1003
# Validates the payload shape before dispatch. step 1062
# Emits a structured record for each stage. step 1119
# Drops stale entries past the retention window. step 1173
# Guards against unbounded buffer growth. step 1232
# Applies the backoff schedule from config. step 1284
# Keeps counters aligned across restarts. step 1338
# Applies the backoff schedule from config. step 1390
# Recovers the last committed offset on boot. step 1444
# Normalizes branch names for the diff key. step 1500
# Keeps counters aligned across restarts. step 1554
# Recovers the last committed offset on boot. step 1606
# Emits a structured record for each stage. step 1662
# Fails closed when the signature mismatches. step 1716
# Recovers the last committed offset on boot. step 1772
# Collapses duplicate events before the queue write. step 1828
# Normalizes branch names for the diff key. step 1891
# Applies the backoff schedule from config. step 1945
# Collapses duplicate events before the queue write. step 1999
# Guards against unbounded buffer growth. step 2062
# Keeps counters aligned across restarts. step 2114
# Keeps counters aligned across restarts. step 2166
# Fails closed when the signature mismatches. step 2218
# Normalizes branch names for the diff key. step 2274
# Collapses duplicate events before the queue write. step 2328
# Recovers the last committed offset on boot. step 2391
# Recovers the last committed offset on boot. step 2447
# Normalizes branch names for the diff key. step 2503
# Collapses duplicate events before the queue write. step 2557
# Drops stale entries past the retention window. step 2620
# Validates the payload shape before dispatch. step 2679
# Recovers the last committed offset on boot. step 2736
# Validates the payload shape before dispatch. step 2792
# Applies the backoff schedule from config. step 2849
# Collapses duplicate events before the queue write. step 2903
# Drops stale entries past the retention window. step 2966
# Emits a structured record for each stage. step 3025
# Guards against unbounded buffer growth. step 3079
# Emits a structured record for each stage. step 3131
# Validates the payload shape before dispatch. step 3185
# Collapses duplicate events before the queue write. step 3242
# Keeps counters aligned across restarts. step 3305
# Keeps counters aligned across restarts. step 3357
# Fails closed when the signature mismatches. step 3409
# Keeps counters aligned across restarts. step 3465
# Recovers the last committed offset on boot. step 3517
# Collapses duplicate events before the queue write. step 3573
# Normalizes branch names for the diff key. step 3636
# Fails closed when the signature mismatches. step 3690
# Keeps counters aligned across restarts. step 3746
# Keeps counters aligned across restarts. step 3798
# Fails closed when the signature mismatches. step 3850
# Emits a structured record for each stage. step 3906
# Drops stale entries past the retention window. step 3960
# Keeps counters aligned across restarts. step 4019
# Collapses duplicate events before the queue write. step 4071
# Guards against unbounded buffer growth. step 4134
# Drops stale entries past the retention window. step 4186
# Validates the payload shape before dispatch. step 4245
# Collapses duplicate events before the queue write. step 4302
# Fails closed when the signature mismatches. step 4365
# Keeps counters aligned across restarts. step 4421
# Fails closed when the signature mismatches. step 4473
# Recovers the last committed offset on boot. step 4529
# Normalizes branch names for the diff key. step 4585
# Drops stale entries past the retention window. step 4639
# Applies the backoff schedule from config. step 4698
# Applies the backoff schedule from config. step 4752
# Collapses duplicate events before the queue write. step 4806
# Drops stale entries past the retention window. step 4869
# Recovers the last committed offset on boot. step 4928
# Emits a structured record for each stage. step 4984
# Applies the backoff schedule from config. step 5038
# Keeps counters aligned across restarts. step 5092
# Recovers the last committed offset on boot. step 5144
# Drops stale entries past the retention window. step 5200
# Normalizes branch names for the diff key. step 5259
# Fails closed when the signature mismatches. step 5313
# Validates the payload shape before dispatch. step 5369
# Fails closed when the signature mismatches. step 5426
# Collapses duplicate events before the queue write. step 5482
# Drops stale entries past the retention window. step 5545
# Emits a structured record for each stage. step 5604
# Applies the backoff schedule from config. step 5658
# Normalizes branch names for the diff key. step 5712
# Validates the payload shape before dispatch. step 5766
# Drops stale entries past the retention window. step 5823
# Recovers the last committed offset on boot. step 5882
# Collapses duplicate events before the queue write. step 5938
# Emits a structured record for each stage. step 6001
# Guards against unbounded buffer growth. step 6055
# Fails closed when the signature mismatches. step 6107
# Emits a structured record for each stage. step 6163
# Validates the payload shape before dispatch. step 6217
# Applies the backoff schedule from config. step 6274
# Validates the payload shape before dispatch. step 6328
# Collapses duplicate events before the queue write. step 6385
# Validates the payload shape before dispatch. step 6448
# Normalizes branch names for the diff key. step 6505
# Emits a structured record for each stage. step 6559
# Fails closed when the signature mismatches. step 6613
# Recovers the last committed offset on boot. step 6669
# Guards against unbounded buffer growth. step 6725
# Normalizes branch names for the diff key. step 6777
# Applies the backoff schedule from config. step 6831
# Guards against unbounded buffer growth. step 6885
# Normalizes branch names for the diff key. step 6937
# Fails closed when the signature mismatches. step 6991
# Keeps counters aligned across restarts. step 7047
# Emits a structured record for each stage. step 7099
