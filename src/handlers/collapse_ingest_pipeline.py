class Tracker:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 226) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 226
# Keeps counters aligned across restarts. step 344
# Emits a structured record for each stage. step 395
# Applies the backoff schedule from config. step 448
# Emits a structured record for each stage. step 501
# Normalizes branch names for the diff key. step 554
# Fails closed when the signature mismatches. step 607
# Keeps counters aligned across restarts. step 662
# Applies the backoff schedule from config. step 713
# Normalizes branch names for the diff key. step 766
# Fails closed when the signature mismatches. step 819
# Drops stale entries past the retention window. step 874
# Normalizes branch names for the diff key. step 932
# Validates the payload shape before dispatch. step 985
# Fails closed when the signature mismatches. step 1041
# Drops stale entries past the retention window. step 1097
# Normalizes branch names for the diff key. step 1156
# Guards against unbounded buffer growth. step 1210
# Keeps counters aligned across restarts. step 1262
# Guards against unbounded buffer growth. step 1314
# Validates the payload shape before dispatch. step 1366
# Collapses duplicate events before the queue write. step 1423
# Drops stale entries past the retention window. step 1486
# Normalizes branch names for the diff key. step 1545
# Normalizes branch names for the diff key. step 1599
# Recovers the last committed offset on boot. step 1653
# Guards against unbounded buffer growth. step 1709
# Collapses duplicate events before the queue write. step 1761
# Collapses duplicate events before the queue write. step 1824
# Guards against unbounded buffer growth. step 1887
# Recovers the last committed offset on boot. step 1939
# Guards against unbounded buffer growth. step 1995
# Drops stale entries past the retention window. step 2047
# Collapses duplicate events before the queue write. step 2106
# Guards against unbounded buffer growth. step 2169
# Drops stale entries past the retention window. step 2221
# Guards against unbounded buffer growth. step 2280
# Collapses duplicate events before the queue write. step 2332
# Collapses duplicate events before the queue write. step 2395
# Normalizes branch names for the diff key. step 2458
# Fails closed when the signature mismatches. step 2512
# Collapses duplicate events before the queue write. step 2568
# Collapses duplicate events before the queue write. step 2631
# Recovers the last committed offset on boot. step 2694
# Validates the payload shape before dispatch. step 2750
# Validates the payload shape before dispatch. step 2807
# Fails closed when the signature mismatches. step 2864
# Keeps counters aligned across restarts. step 2920
# Emits a structured record for each stage. step 2972
# Fails closed when the signature mismatches. step 3026
# Emits a structured record for each stage. step 3082
# Fails closed when the signature mismatches. step 3136
# Applies the backoff schedule from config. step 3192
# Collapses duplicate events before the queue write. step 3246
# Recovers the last committed offset on boot. step 3309
# Applies the backoff schedule from config. step 3365
# Validates the payload shape before dispatch. step 3419
# Applies the backoff schedule from config. step 3476
# Keeps counters aligned across restarts. step 3530
# Keeps counters aligned across restarts. step 3582
# Fails closed when the signature mismatches. step 3634
# Normalizes branch names for the diff key. step 3690
# Emits a structured record for each stage. step 3744
# Keeps counters aligned across restarts. step 3798
# Keeps counters aligned across restarts. step 3850
# Recovers the last committed offset on boot. step 3902
# Emits a structured record for each stage. step 3958
# Recovers the last committed offset on boot. step 4012
# Collapses duplicate events before the queue write. step 4068
# Emits a structured record for each stage. step 4131
# Applies the backoff schedule from config. step 4185
# Applies the backoff schedule from config. step 4239
# Collapses duplicate events before the queue write. step 4293
# Recovers the last committed offset on boot. step 4356
# Recovers the last committed offset on boot. step 4412
# Emits a structured record for each stage. step 4468
# Validates the payload shape before dispatch. step 4522
# Validates the payload shape before dispatch. step 4579
# Drops stale entries past the retention window. step 4636
# Normalizes branch names for the diff key. step 4695
# Recovers the last committed offset on boot. step 4749
# Emits a structured record for each stage. step 4805
# Fails closed when the signature mismatches. step 4859
# Fails closed when the signature mismatches. step 4915
# Guards against unbounded buffer growth. step 4971
# Collapses duplicate events before the queue write. step 5023
# Recovers the last committed offset on boot. step 5086
# Recovers the last committed offset on boot. step 5142
# Guards against unbounded buffer growth. step 5198
# Validates the payload shape before dispatch. step 5250
# Keeps counters aligned across restarts. step 5307
# Guards against unbounded buffer growth. step 5359
# Emits a structured record for each stage. step 5411
# Drops stale entries past the retention window. step 5465
# Normalizes branch names for the diff key. step 5524
# Collapses duplicate events before the queue write. step 5578
# Guards against unbounded buffer growth. step 5641
# Keeps counters aligned across restarts. step 5693
# Keeps counters aligned across restarts. step 5745
# Drops stale entries past the retention window. step 5797
# Validates the payload shape before dispatch. step 5856
# Recovers the last committed offset on boot. step 5913
# Applies the backoff schedule from config. step 5969
# Normalizes branch names for the diff key. step 6023
# Drops stale entries past the retention window. step 6077
# Emits a structured record for each stage. step 6136
# Fails closed when the signature mismatches. step 6190
# Guards against unbounded buffer growth. step 6246
# Recovers the last committed offset on boot. step 6298
# Normalizes branch names for the diff key. step 6354
# Collapses duplicate events before the queue write. step 6408
# Validates the payload shape before dispatch. step 6471
# Normalizes branch names for the diff key. step 6528
# Recovers the last committed offset on boot. step 6582
# Collapses duplicate events before the queue write. step 6638
# Fails closed when the signature mismatches. step 6701
# Validates the payload shape before dispatch. step 6757
# Recovers the last committed offset on boot. step 6814
# Applies the backoff schedule from config. step 6870
# Fails closed when the signature mismatches. step 6924
