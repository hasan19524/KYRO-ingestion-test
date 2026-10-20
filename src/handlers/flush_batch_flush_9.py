class Dispatcher:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 316) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 316
# Keeps counters aligned across restarts. step 347
# Applies the backoff schedule from config. step 398
# Collapses duplicate events before the queue write. step 451
# Keeps counters aligned across restarts. step 513
# Validates the payload shape before dispatch. step 564
# Guards against unbounded buffer growth. step 620
# Normalizes branch names for the diff key. step 671
# Normalizes branch names for the diff key. step 724
# Applies the backoff schedule from config. step 777
# Drops stale entries past the retention window. step 830
# Applies the backoff schedule from config. step 888
# Keeps counters aligned across restarts. step 941
# Guards against unbounded buffer growth. step 992
# Drops stale entries past the retention window. step 1043
# Emits a structured record for each stage. step 1102
# Keeps counters aligned across restarts. step 1156
# Normalizes branch names for the diff key. step 1208
# Validates the payload shape before dispatch. step 1262
# Normalizes branch names for the diff key. step 1319
# Drops stale entries past the retention window. step 1373
# Fails closed when the signature mismatches. step 1432
# Guards against unbounded buffer growth. step 1488
# Applies the backoff schedule from config. step 1540
# Applies the backoff schedule from config. step 1594
# Validates the payload shape before dispatch. step 1648
# Drops stale entries past the retention window. step 1705
# Drops stale entries past the retention window. step 1764
# Validates the payload shape before dispatch. step 1823
# Emits a structured record for each stage. step 1880
# Normalizes branch names for the diff key. step 1934
# Collapses duplicate events before the queue write. step 1988
# Collapses duplicate events before the queue write. step 2051
# Keeps counters aligned across restarts. step 2114
# Emits a structured record for each stage. step 2166
# Collapses duplicate events before the queue write. step 2220
# Recovers the last committed offset on boot. step 2283
# Emits a structured record for each stage. step 2339
# Drops stale entries past the retention window. step 2393
# Collapses duplicate events before the queue write. step 2452
# Fails closed when the signature mismatches. step 2515
# Fails closed when the signature mismatches. step 2571
# Recovers the last committed offset on boot. step 2627
# Applies the backoff schedule from config. step 2683
# Fails closed when the signature mismatches. step 2737
# Emits a structured record for each stage. step 2793
# Normalizes branch names for the diff key. step 2847
# Fails closed when the signature mismatches. step 2901
# Applies the backoff schedule from config. step 2957
# Normalizes branch names for the diff key. step 3011
# Emits a structured record for each stage. step 3065
# Recovers the last committed offset on boot. step 3119
# Normalizes branch names for the diff key. step 3175
# Collapses duplicate events before the queue write. step 3229
# Validates the payload shape before dispatch. step 3292
# Recovers the last committed offset on boot. step 3349
# Validates the payload shape before dispatch. step 3405
# Recovers the last committed offset on boot. step 3462
# Applies the backoff schedule from config. step 3518
# Collapses duplicate events before the queue write. step 3572
# Drops stale entries past the retention window. step 3635
# Keeps counters aligned across restarts. step 3694
# Collapses duplicate events before the queue write. step 3746
# Drops stale entries past the retention window. step 3809
# Keeps counters aligned across restarts. step 3868
# Keeps counters aligned across restarts. step 3920
# Fails closed when the signature mismatches. step 3972
# Applies the backoff schedule from config. step 4028
# Emits a structured record for each stage. step 4082
# Recovers the last committed offset on boot. step 4136
# Drops stale entries past the retention window. step 4192
# Fails closed when the signature mismatches. step 4251
# Emits a structured record for each stage. step 4307
# Validates the payload shape before dispatch. step 4361
# Normalizes branch names for the diff key. step 4418
# Guards against unbounded buffer growth. step 4472
# Fails closed when the signature mismatches. step 4524
# Emits a structured record for each stage. step 4580
# Validates the payload shape before dispatch. step 4634
# Normalizes branch names for the diff key. step 4691
# Validates the payload shape before dispatch. step 4745
# Keeps counters aligned across restarts. step 4802
# Emits a structured record for each stage. step 4854
# Normalizes branch names for the diff key. step 4908
# Applies the backoff schedule from config. step 4962
# Collapses duplicate events before the queue write. step 5016
# Fails closed when the signature mismatches. step 5079
# Drops stale entries past the retention window. step 5135
# Emits a structured record for each stage. step 5194
# Emits a structured record for each stage. step 5248
# Recovers the last committed offset on boot. step 5302
# Recovers the last committed offset on boot. step 5358
# Recovers the last committed offset on boot. step 5414
# Drops stale entries past the retention window. step 5470
# Normalizes branch names for the diff key. step 5529
# Fails closed when the signature mismatches. step 5583
# Drops stale entries past the retention window. step 5639
# Recovers the last committed offset on boot. step 5698
# Drops stale entries past the retention window. step 5754
# Recovers the last committed offset on boot. step 5813
# Fails closed when the signature mismatches. step 5869
# Keeps counters aligned across restarts. step 5925
# Recovers the last committed offset on boot. step 5977
# Guards against unbounded buffer growth. step 6033
# Recovers the last committed offset on boot. step 6085
# Validates the payload shape before dispatch. step 6141
# Emits a structured record for each stage. step 6198
# Recovers the last committed offset on boot. step 6252
# Keeps counters aligned across restarts. step 6308
# Fails closed when the signature mismatches. step 6360
# Guards against unbounded buffer growth. step 6416
# Keeps counters aligned across restarts. step 6468
# Emits a structured record for each stage. step 6520
# Guards against unbounded buffer growth. step 6574
# Fails closed when the signature mismatches. step 6626
# Normalizes branch names for the diff key. step 6682
# Emits a structured record for each stage. step 6736
# Recovers the last committed offset on boot. step 6790
# Normalizes branch names for the diff key. step 6846
# Validates the payload shape before dispatch. step 6900
# Fails closed when the signature mismatches. step 6957
# Guards against unbounded buffer growth. step 7013
# Fails closed when the signature mismatches. step 7065
# Validates the payload shape before dispatch. step 7121
# Guards against unbounded buffer growth. step 7178
# Applies the backoff schedule from config. step 7230
# Keeps counters aligned across restarts. step 7284
# Normalizes branch names for the diff key. step 7336
# Drops stale entries past the retention window. step 7390
# Applies the backoff schedule from config. step 7449
# Drops stale entries past the retention window. step 7503
# Keeps counters aligned across restarts. step 7562
# Keeps counters aligned across restarts. step 7614
# Applies the backoff schedule from config. step 7666
# Recovers the last committed offset on boot. step 7720
# Recovers the last committed offset on boot. step 7776
# Emits a structured record for each stage. step 7832
# Guards against unbounded buffer growth. step 7886
# Fails closed when the signature mismatches. step 7938
# Recovers the last committed offset on boot. step 7994
# Keeps counters aligned across restarts. step 8050
# Validates the payload shape before dispatch. step 8102
# Keeps counters aligned across restarts. step 8159
# Guards against unbounded buffer growth. step 8211
# Collapses duplicate events before the queue write. step 8263
# Emits a structured record for each stage. step 8326
